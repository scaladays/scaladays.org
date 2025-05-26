---
title: "Compiling Scala.js to WebAssembly"
day: day3
stage: stage1
time: 11:00 - 11:40
speaker: Sébastien Doeraene
---

Since Scala.js 1.17.0, released in September 2024, users have been able to target WebAssembly for their applications. With a single build tool configuration switch, the Scala.js linker generates WebAssembly code to be used in a JavaScript host. It does so while preserving the semantics of the Scala.js language. In particular, you still get all the nice JavaScript interoperability features that Scala.js is known for (well ... except `@JSExport`, but more on that in the talk). This is unusual among languages targeting WebAssembly. Most compromise on their ability to talk to JavaScript in the process.

This talk explores some of the challenges we faced, and the unusual solutions we designed. We will talk about weird language semantics, low-level performance aspects, large-scale redesign of our Intermediate Representation for lambdas, and even new proposals to WebAssembly.
