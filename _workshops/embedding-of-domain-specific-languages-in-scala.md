---
workshop-id: embedding
title: Embedding of Domain-Specific Languages in Scala
trainer: juanma
level: Intermediate 
order: 1
---

### Description

This course takes advantage of functional programming techniques in the design of domain-specific languages. In particular, it shows how to exploit GADTs and tagless-final type classes in the specification of the syntax, type system and semantics of embedded DSLs in Scala. Several examples of untyped and typed DSLs will be described, but the course will focus on the design of one or two DSLs identified beforehand. Some examples of languages that could be considered for the course are the following ones:

- An embedding in Scala of the Haskell Diagrams DSL
- An embedding in Scala of the Jq language
- A DSL for writing type-safe Column expressions in Spark etc.

Although optimization techniques, higher-order DSLs, Quoted DSLs, and other advanced techniques on DSL design are out of the scope of this course, it covers enough material to be able to put into production well-founded, modular and most efficient embedded DSLs.

At the end of the course you should be able to:
- Understand how to approach the design of a Scala-embedded DSL in a principled way
- Understand tagless-final and GADT-based techniques for designing DSLs
- Put into practice functional abstractions in the design of DSLs, the main goal of functional programming!


{: .mt-4}
### Prerequisites

This is an **intermediate** level course. In particular, it assumes familiarity with Scala and basic functional programming techniques: algebraic data types, higher-order functions and type classes. Nevertheless, a lightning introduction to these techniques will be provided at the beginning of the course.

{: .mt-4 .mb-4}
### Content

##### Module 1. Syntax
- Deep and surface syntax: tagless-final and ADTs
- DSL development (I)

##### Module 2. Type systems
- Typed vs. untyped DSLs: Generalised ADTs and tagless-final (with type constructors)
- DSL development (II)

##### Module 3. Semantics
- Standard semantics (testing)
- Non-standard semantics (production)
- DSL development (III)

##### Methodology
- The three core modules of the course will be explained through <TBD> sessions of <TBD> hours each.
- Each session will be mainly devoted to the implementation of some concerns of the chosen DSLs; preliminary material on the major concepts of DSL design involved in the examples will be presented first.
- The material for the course primarily consists of notebooks that will be made available via Github. Mostly, sessions will be carried out through live coding practices using templates of these notebooks.
- After each session, assignments will be proposed which aim at completing or extending the ongoing DSLs. They will be reviewed on a case-by-case basis via pull requests. Alternatively, guidance will be provided on the development of a DSL chosen by the attendee.
