---
title: Polymorphic Function Types in Scala 3
day: day3
stage: stage1
time: 10:15 - 11:00
#image:img/assets/madrid/talks/SpeakerCard-GuillaumeMartres-1920x1080.png
speaker: Guillaume Martres
speaker2:
---

"Methods in Scala are not first-class values: they cannot be passed around, only called. This is not a fundamental limitation since it's always possible to wrap a method in a class and create an instance of this class (the wrapped method is usually called ""apply"" since Scala will automatically rewrite calls like ""f(x)"" to ""f.apply(x)"" if necessary). But requiring users to create a new class for every kind of method they wish to wrap in a value would be inconvenient and hard to abstract over, so the language comes built-in with `scala.FunctionN` classes that each contain an `apply` method with `N` parameters, combined with some syntactic sugar and special typing rules this lets us conveniently represent functions.

However, Scala methods support a rich set of features that are not expressible with the traditional `FunctionN` classes: they can have type parameters, dependent parameters, contextual parameters, etc. Thankfully, most of these limitations have now been lifted in Scala 3, in each case the trick was to find a type to abstract over these functions.[^1] [^2] [^3]

In this talk we will take a deep dive into polymorphic function types which let us define functions with type parameters.

We will show how to use them, what they're good for, how they interact with other language features and how they're implemented.

We will also discuss recent improvements made in the compiler to make them more pleasant to use, and possible future improvements.

[^1]: [https://docs.scala-lang.org/scala3/reference/new-types/polymorphic-function-types.html](https://docs.scala-lang.org/scala3/reference/new-types/polymorphic-function-types.html){:target="_blank" rel="noopener noreferrer"}
[^2]: [https://docs.scala-lang.org/scala3/reference/new-types/dependent-function-types.html](https://docs.scala-lang.org/scala3/reference/new-types/dependent-function-types.html){:target="_blank" rel="noopener noreferrer"}
[^3]: [https://docs.scala-lang.org/scala3/reference/contextual/context-functions.html](https://docs.scala-lang.org/scala3/reference/contextual/context-functions.html){:target="_blank" rel="noopener noreferrer"}
