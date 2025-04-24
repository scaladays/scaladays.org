---
title: Diamond Architecture on Scala 3
day: day3
stage: stage3
time: 14:30 - 15:15
#image:img/assets/madrid/talks/SpeakerCard-DavidMendez-1920x1080.png
speaker: David Amancio Gil Méndez
speaker2:
---

Managing large codebases is a difficult challenge, as code organization can become unwieldy, leading to high cognitive overhead and reduced productivity. Scala offers some architectural choices of its own flavor but here the focus is on one that is language agnostic: The Diamond Architecture. It addresses the problem by using some key object-oriented programming (OOP) techniques, such as abstraction and polymorphism that make code organisation more manageable. 

OOP techniques have proven effective in managing large codebases, particularly in the context of distributed systems like Apache Spark and Apache Kafka. These systems have to deal with a high degree of complexity and heterogeneity, making it crucial to organize code in a way that makes it easy to reason about and modify. The Diamond Architecture extends these OOP techniques by introducing a modular approach to code organisation that can be used across different types of systems.

Scala 3 provides a powerful set of new features that make it even easier to implement the Diamond Architecture. By leveraging these new language features, I will show how developers can build large-scale Scala 3 applications that are more maintainable and easier to reason about. Some code snippets will include a comparison with Scala 2 code or other language.The presentation will go in depth covering why, when and where to use extension methods, using clauses, given instances, conversion type-classes, union, Intersection and structural types.
