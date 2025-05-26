---
title: "Designing with Duality"
day: TODO
stage: TODO
time: TODO
speaker: Noel Welsh
---

How can we systematically design software? One way is to use dualities. Dualities, such as the duality between functional programming (FP) and object-oriented programming (OO), are bidirectional program transformations. By applying a duality we can transform, say, code in a FP style, into code in an OO style and vice versa. This sounds quite esoteric, but turns out to have very practical applications. I'll show how dualities can be applied to an code, yielding a range of implementations with different properties. This allows us to pick the implementation that best suits our needs, and makes creating software less a matter of inspiration and more the application of a consistent and repeatable process.

A duality is a transformation between mathematical structures. Programming language researchers have long known about several dualities in programming, such as the duality being between FP and OO, and the duality between functions calls and function returns. They allow us to take one conceptual model and realize it in different ways by applying dualities. This is particularly powerful in a language like Scala that mixes together several programming paradigms, and thus offers the programmer a lot of choice in their implementation approach. Interpreters are at the core of many functional programming libraries, and therefore interpreter performance is a core concern in FP. To showcase the practicality of dualities I'll take a basic interpreter loop and systematically transform it into much more efficient version.

    