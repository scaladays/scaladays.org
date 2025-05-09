---
workshop-id: ddd
title: Domain Driven Design in Scala 3
trainer: david
level: Beginner 
order: 4
---

### Abstract

One of the shortcomings of Domain Driven Design (DDD) is that it can be a lengthy process to define the bounded contexts (BCs) properly, and subsequently to transcribe the BCs into a code and to introduce them in your codebase. 

This workshop aims to demonstrate how to minimize this inconvenience by relying on:
- The robustness of DDD in Scala
- The fast iteration loop provided by scripting in Scala-CLI
- The ease of transforming a Proof of Concept (PoC) into a Minimum Viable Product (MVP) with the current Scala tooling
 
You will learn:
- What the building blocks of Scala 3 are
- Which production-tested libraries are built on top of it
- How to go from a design to a safe and convenient code in a matter of hours

By the end of the workshop, you will have a full stack app with DDD implementations, ready for review.


### Target Audience 

If you are a Full-Stack Developer, a Software Engineer, a Data Engineer, a Migration Architect or a programming aficionado who would like to acquire, upgrade or master your skills in DDD, this workshop is for you. 


### Prerequisites

Prior knowledge of Scala is not necessary, although it is a plus – regardless of the flavour of Scala you code in. 

Basic understanding of functional programming concepts like map, flapmap, error handling, type classes, etc. is required. 


### Requirements

Have installed on your computer:
- Scala-CLI
- IDE:
  - IntelliJ Idea with Scala plugin
  - VS Code with Metals
  - Or any other IDE that supports Scala


### Agenda

#### Part 1: Introductions
- Premise of DDD
- Benefits of making illegal values irrepresentable 
- Advantage of DDD in the age of LLMs
- Introduction of a use case: Spanish IDs validator
- Trade-offs:
  - Application complexity vs domain accuracy
  - Front-end vs back-end validation
  - Team’s expertise vs business needs

#### Part 2: Building Blocks of Scala
- Algebraic Data types and Enums
- Classes
- Value classes
- Type aliases
- Overview of metaprogramming
- Inline
- Opaque types
- Union types
- Intersection types

#### Part 3: What can be Built on Top of Them?
- Combining the blocks
- Vanilla DDD
- Type level DDD

#### Part 4: Full Stack Application
- Description of the front end
- Description of the back end 
- Running all the implementations

#### Part 5: Conclusion
- Recap of Scala DDD
  - Benefits
  - Limitations
  - Error handling
  - Entry barriers for engineers
- Trade-offs revisited
  - Application Complexity vs Domain Accuracy 
  - Front-end vs back-end validation 
  - Team expertise vs business needs


