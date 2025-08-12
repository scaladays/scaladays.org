---
workshop-id: ddd
title: Domain Driven Design in Scala 3
trainer: david
level: Beginner 
order: 4
---

### Abstract

One of the shortcomings of Domain Driven Design (DDD) is that it can be a lengthy process to define the bounded contexts
(BCs) properly, and subsequently to transcribe the BCs into a code and to introduce them in your codebase. 

This workshop aims to demonstrate how to minimize this inconvenience by relying on:
- The robustness of DDD in Scala
- The fast iteration loop provided by scripting in Scala-CLI
- The ease of transforming a Proof of Concept (PoC) into a Minimum Viable Product (MVP) with the current Scala tooling
 
You will learn:
- What the building blocks of DDD and Scala 3 are
- Which production-tested libraries help us do DDD in Scala 3
- How to go from a design to a safe and convenient code in a matter of hours

By the end of the workshop, you will have a full stack app with DDD implementations, ready for review.


### Target Audience 

If you are a Full-Stack Developer, a Software Engineer, a Data Engineer, a Migration Architect or a programming aficionado
who would like to acquire, upgrade or master your skills in DDD, this workshop is for you.

### Prerequisites

Prior knowledge of Scala is not necessary, although it is a plus – regardless of the flavour of Scala you code in. 

Basic understanding of functional programming concepts like map, flapMap, error handling, type classes, etc. is required.

### Requirements

Have installed on your computer:
- Scala-CLI
- IDE:
  - IntelliJ Idea with Scala plugin
  - VS Code with Metals
  - Or any other IDE that supports Scala

### Agenda

#### Use Case: Spanish ID validator
- Business needs
- Front-end or back-end validation?
- Task requirements

#### Why DDD? Domain Driven Design premises
- Benefits of making illegal states unrepresentable
- Who are the domain experts?
- What is the ubiquitous language?
- What is a model?
- What is a bounded context?
- Quiz
- Bonus: DDD in the time of LLMs

#### Hands-on with Scala-CLI - PoC
- Identifying the nouns, behaviours, rules and invariants
- Codifying invariants
- Codifying the rules
- Testing the behaviour

#### Domain types
- Business Domain
- Types of Subdomains
- Comparing Subdomains
- Bounded Context vs Subdomains
- Quiz

#### Trade-offs
- Software complexity vs Domain accuracy
- Engineering expertise vs Business needs

#### Hands-on Full-stack App with Mill
- Basic Implementation - MVP
- Parse, don't validate - Error handling
- Scala 3 libraries to the rescue

#### DDD building blocks
- Value Objects
- Entities
- Aggregates
- Domain Events
- Domain Services
- Quiz

#### Hands-on Spanish ID as a Value Object
- Metaprogramming in Scala 3
- Compile-time validation
- Advance usage of Scala 3 libraries

#### Conclusion
- Trade-offs revisited
    - Software complexity vs Domain accuracy
    - Engineering expertise vs Business needs
- Benefits & Limitations
- Engineering staffing challenges
