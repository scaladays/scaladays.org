---
title: "Simple and safe serialization/pickling of closures in Scala 3"
day: day2
stage: stage4
time: 10:10 - 10:50
speaker: Jonas Spenger
---

More and more use cases in parallel and distributed programming are testing the limits of closures. Serializing/pickling closures/functions is incredibly powerful, but full of issues. Using the JVM’s built-in serializer may result in strange outcomes and runtime-errors during deserialization. For example, one may *accidentally* serialize the JUnit testing framework when serializing a lambda in a test case by capturing the outer testing class. Other existing libraries come with their own imperfections.

This talk introduces the Spores3 library, which makes serializing closures simple and safe in Scala 3. It builds on the long-running Spores project. And now, after a complete rewrite, features an improved interface and rigorous compile-time checks. A spore can be packed to a serialized representation, and unpacked to get its value. Further, the serialized spore can be partially applied to another serialized spore, used, for example, internally in the type-class derivation of spore serializers. Compile-time checks ensure that there are no runtime errors when serializing/deserializing a spore.

This talk will discuss challenges of serializing closures for distributed and durable systems. It will highlight by example some of the shortcomings of existing approaches. It will introduce the core interface and design of Spores3. Further, it will show by example how a distributed and durable futures library can be implemented with Spores3, in which the execution state consisting of all futures is durably persisted to disk and crash-resistant. The talk will conclude with an outlook of future developments of Spores3 and its use cases.
