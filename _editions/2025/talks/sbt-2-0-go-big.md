---
title: "sbt 2.0: go big"
day: TODO
stage: TODO
time: TODO
speaker: Eugene Yokota
---

This is going to be a debut talk of sbt 2.0, a Scala 3 rewrite of sbt, which I have been working on for the last few years (in my free time) with the help of Scala Center and other volunteers. Given that sbt 1.x already exists, and it's the most widely-used build tool in Scala, we wanted to take big bold steps forward.

Set aside the fact that the macro system is rewritten to use Scala 3 macros, build.sbt semantics is simplified; it incorporates Bazel-compatible remote cache system, allowing you to share the build artifacts across the machine. In this talk, I'll go over the features of sbt 2.0 that are available in beta, and share the vision forward.
    