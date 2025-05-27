---
title: "Using Scala in a Go-First Company"
day: day3
stage: stage2
time: 17:00 - 17:40
speaker: Christian Hollinger
---

We introduced a very specialized Scala 3 project - a high-volume, real-time streaming pipeline for complex traffic data - at a company that does (practically) everything in go. Why would we do that? And would we do it again?

In the overall Data Engineering world, go has very little foothold; Python has been king in this space for many years now, and using Python for a project like this seemed like the obvious choice. In fact, I've been told that Scala is a dead language for data engineering several times!

In this talk, I'll go over the details of **why we chose Scala 3 instead of go, Python, or Java**. We'll cover things like

- How good abstraction is the difference between "software" and "scripts" (and how Scala has many mechanisms for this)
- Why schema evolution is a hard problem and how Scala's type system helps us to tackle this
- How type classes allow for more generic (and well tested) data pipelines

And, perhaps more importantly: **How we ensure the project remains maintainable for people who aren't Scala experts**. We'll touch on writing maintainable, pragmatic Scala code, integrating Scala into go-focused developer tooling (CLI tools, CI/CD, testing, observability & more), as well as the long-term impact on hiring and tech debt.

And, of course, answer the question: Would we make that choice again?
