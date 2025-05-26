---
title: "Macro-Free Type-Safe Database Queries in Scala"
day: TODO
stage: TODO
time: TODO
speaker: Anna Herlihy
---

In Scala, writing correct and composable database queries requires navigating a crowded design space: solutions range from powerful but opaque libraries that rely on advanced language features like macros and higher-kinded types, to lightweight, flexible, yet error-prone string-based approaches.

The ultimate goal is a query system that combines compile-time type safety, flexibility, and seamless integration into Scala’s syntax and tooling - without confusing error messages, a steep learning curve, or a large and complex code base.

This talk presents TyQL, a new type-safe database query library for Scala 3 that avoids macros and higher-kinded types by leveraging Scala’s new Named Tuples feature to model data and enforce correctness at compile-time. TyQL offers a LINQ-style query interface using idiomatic Scala syntax, with support for both core and advanced database features. It provides clear error messages, IDE integration, and dialect-aware type-checking.

We will explore TyQL’s core design, demonstrate how Named Tuples enable expressive, intuitive yet type-safe embedded queries, and demo real-world examples. Attendees will come away with a clear understanding of both how to use TyQL in practice and how it works under the hood.
    