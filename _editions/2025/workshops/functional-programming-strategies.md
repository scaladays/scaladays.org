---
workshop-id: strategies
title: Functional Programming Strategies
trainer: noel
level: Intermediate
order: 2
room: BC 229
---

### Abstract

This workshop presents a toolkit of concepts and coding practices, which I call programming strategies, developed through my fifteen years of Scala experience. The workshop approaches programming primarily through a functional programming lens, emphasizing designs that enhance reasoning and composition, while leveraging Scala's object-oriented features where appropriate.

The workshop has two primary goals:

1. To develop a coherent framework of program design concepts and the connections between them. For example, we'll see classic functional programming (FP) and object-oriented (OO) approaches, the tradeoffs of each, and how they are connected by a concept known as duality.

2. To show how we translate these concepts into Scala code, providing a systematic and repeatable way for implementing designs in software. For example, we'll see how we can translate an abstract API into either FP or OO style code, depending on which is most appropriate for the situation.

This workshop is about the big picture; it is focused on the design or architecture of code, and the implementation of these designs. So, for example, we won't talk about details such as how you might connect to a database in Scala, but discussing the overall design and implementation of a library for database interaction is definitely on topic. It's for people who see software libraries as force multipliers, and who want to build libraries that are more productive, flexible, and enjoyable to use.


### Target Audience

Developers who want to make themselves or their team more productive by building powerful abstractions, and developers who want a deep understanding of the concepts behind Scala and how to use them effectively.


### Prerequisites
You should have a solid grasp of Scala, though not necessarily the more esoteric areas like the details of how givens / implicits work. This workshop will use Scala 3, though almost everything can be translated to Scala 2 with a little effort.


### Requirements
Laptop with Scala and development environment installed.


### Agenda

#### Foundations
- Reasoning and composition as guiding principles for program design
- Data (FP) and codata (OO) as fundamental approaches for representing program structures. Duality as the relationship between data and codata. Advantages and disadvantages of data and codata.
- Interpreters as the fundamental approach to handling effects while retaining reasoning and composition. Interpreters using data.

#### Strategies for Composition
- Monads as capturing sequential composition. The Monad type class, and its implementation in Cats. Standard monads such as Reader and State.
- Applicatives as capturing parallel composition. The Applicative and Semigroupal type classes, and their implementation in Cats. Common uses of applicatives.

#### Strategies for Interpreters
- Codata interpreters. Terminal case study.
- Advanced data interpreters. Optimisation and stack machines. Regular expressions case study.
- Tagless final. Basic structure. Improvement using Scala features. Algebraic UI case study.

