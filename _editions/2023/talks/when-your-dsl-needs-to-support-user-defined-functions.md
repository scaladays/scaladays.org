---
title: When your DSL Needs to Support User-Defined Functions
day: day3
stage: stage3
time: 10:15 - 11:00
#image:img/assets/madrid/talks/SpeakerCard-TomasMikula-1920x1080.png
speaker: Tomas Mikula
speaker2:
---

Scala's flexible syntax makes it a powerful host for embedding domain-specific languages (DSLs). As authors of a DSL, we define data structures to represent domain objects and we provide, quite easily, nice syntax to construct them. However, things get complicated once the domain objects, constructed by the users, include some form of functions. Provided there are good reasons to not have Scala functions inside our domain objects, we now need a data structure for representing functions and an ergonomic syntax for defining them. Needless to say, we would like to offload the bulk of typechecking our DSL programs to the Scala compiler.

In this talk, I will present a technique for implementing DSLs which support user-defined domain functions.
 
Firstly, domain functions will be represented as _abstract arrows._ Even though the primitive arrows will necessarily be specific to each particular domain, the operations for gluing simpler arrows into more complex ones are quite generic. For example, operations like sequential composition, parallel composition, branching, recursion will find their use in many domains.

Secondly, we will give the users of our DSL a familiar _lambda syntax_ for defining domain functions. In practice, the user writes an anonymous Scala function on placeholder expressions. These expressions are parameterized by the types of the domain, so typechecking is delegated to the Scala compiler. We then translate the Scala function to a point-free (i.e. variable-free) composition of arrows of our domain. As the translation operates only on the generic glue code, we don't have to reimplement it for every DSL. Instead, we will use a library solution from the [Libretto](https://github.com/TomasMikula/libretto/){:target="_blank" rel="noopener noreferrer"} project.
 
As a result, DSL implementors get a clean, point-free representation suitable for consumption by programs, whereas DSL users get to write domain functions using a familiar lambda notation.
 
Although the technique is applicable in languages other than Scala, I will highlight how some _specifically Scala_ features make the result especially pleasant.
