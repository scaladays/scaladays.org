---
title: "Yo Dawg, Heard You Want To FlatMap Your Direct-Style"
day: day2
stage: stage4
time: 11:00 - 11:40
speaker: Riccardo Cardin
---

The direct style in Scala 3, influenced by languages like Kotlin and Rust, simplifies functional programming by eliminating for-comprehension syntax on higher-kinded types. It offers an imperative approach supported by context functions.

While many Scala developers support it, others prefer the traditional functional styles used in libraries like Cats Effect and ZIO, which manage effects differently. The potential of combining Algebraic Effects and Handlers with Scala 3's direct style opens new possibilities for exploring different programming paradigms and libraries.

During the talk, we’ll build a small effect system using solely Scala 3 context functions step by step. With some enhancements to the common approach, we’ll discover that adding for-comprehension capabilities to such a system is possible. We'll end up with a system that can express the same program using either direct style syntax or monad style.
