---
title: "ZIO from a Data Scientist’s Perspective: For Those Who Don’t Speak Category Theory"
day: TODO
stage: TODO
time: TODO
speaker: kostas passadis
---

ZIO has a reputation for being powerful — but intimidating, especially for those who don’t come from a functional programming background. In this talk, I explore the ZIO ecosystem through the lens of a machine learning and data science practitioner who doesn’t speak in morphisms or monads — and doesn’t need to.

Why not just stick with Python? Because putting Python ML models into production can be notoriously painful. Scala, by contrast, was designed for building robust systems — and ZIO fully leverages that power.

We’ll walk through how ZIO simplifies production-grade ML workflows by:

- Clearly expressing failure modes and dependencies with its type system.
- Assembling models and pipelines using dependency injection (`ZLayer`).
- Effortlessly parallelizing training via its powerful concurrency model.
- Processing large or real-time datasets using `ZIO Streams`.
- Serving trained models efficiently with `ZIO HTTP`.

By the end, you’ll see why ZIO isn’t “too academic.” On the contrary — it’s one of the most **practical** tools available to a working data scientist.

Here’s a glimpse of what that looks like: a Simulated Annealing optimizer built entirely with ZIO, demonstrating modularity, composability, and testability via layers.


    abstract class Problem[A] {
        def evaluate(candidate: A): UIO[Double]
        def generate(): UIO[A]
        // Provide a default implementation for generate which simply echoes back the candidate solution.
        def generate(candidate: A): UIO[A] = ZIO.succeed(candidate)
    }

    type Path = Seq[Int]
    type Graph = Array[Array[Double]]

    class TSP(val graph: Graph) extends Problem[Path] {
        override def evaluate(path: Path): UIO[Double] = {
            def calculate(p: Path, cost: Double): UIO[Double] = for {
                c <- ZIO.attempt(graph(p(0))(p(1))).foldZIO(
                    _ => ZIO.succeed(cost),
                    extra => calculate(p.tail, cost + extra)
                )
            } yield c
            calculate(path, 0.0)
        }

        override def generate(): UIO[Path] = ZIO.succeed(Seq(0, 1, 2, 3, 4))

        override def generate(path: Path): UIO[Path] = ZIO.attempt {
            val source = path.head
            val dest = path.last
            val hops = path.tail.dropRight(1)
            source +: scala.util.Random.shuffle(hops) :+ dest
        }.catchAll(_ => ZIO.succeed(path))
    }

    object TSP {
        def make(graph: Graph): UIO[TSP] = ZIO.succeed(new TSP(graph))
        def live(graph: Graph): ZLayer[Any, Nothing, TSP] = ZLayer.fromZIO(make(graph))
    }

    trait HyperParameter[A] {
        val value: A
        val name: String
    }

    object HyperParameterSeq {
        def live(hp: HyperParameter[_]*): ZLayer[Any, Nothing, Seq[HyperParameter[_]]] =
            ZLayer.fromFunction(() => hp.toSeq)
    }

    object HyperParameters {
        def live: ZLayer[Seq[HyperParameter[_]], Nothing, HyperParameters] = {
            val hyperparams = for {
                params <- ZIO.service[Seq[HyperParameter[_]]]
                continuous = params.collect { case p: RealHyperparameter => p }
                discrete = params.collect { case p: DiscreteHyperparameter => p }
            } yield HyperParameters(continuous, discrete)

            ZLayer.fromZIO(hyperparams)
        }
    }

    trait Solver[A] {
        val problem: Problem[A]
        def step(candidate: A, epoch: Int): ZIO[Any, Nothing, A]
        def optimize(epochs: Int): ZIO[Any, Nothing, A]
    }

    trait CoolingSchedule {
        val t0: Double
        def getTemperature(iter: Int): UIO[Double]
    }

    class SimulatedAnnealing[A](override val problem: Problem[A], schedule: CoolingSchedule, nIter: Int)
        extends Solver[A] { ... }

    object SimulatedAnnealing {
        def live[A: Tag](nIter: Int): ZIO[Problem[A] with CoolingSchedule, Nothing, SimulatedAnnealing[A]] = for {
            problem <- ZIO.service[Problem[A]]
            schedule <- ZIO.service[CoolingSchedule]
        } yield new SimulatedAnnealing[A](problem, schedule, nIter)
    }

    val solution = for {
        s <- SimulatedAnnealing.live
        path <- s.optimize(10)
    } yield path

    val runnable = solution.provide(
        TSP.live(graph),
        HyperParameterSeq.live(RealHyperparameter(1.0, "alpha"), RealHyperparameter(100.0, "t0")),
        HyperParameters.live,
        LinearInverseCooling.live
    )

    run(runnable)




    