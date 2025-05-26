---
title: "Compiling Scala without the JVM"
day: TODO
stage: TODO
time: TODO
speaker: Jamie Thompson
---

This talk describes the journey to answering the question "can we build a Scala compiler that doesn't run on JVM?" It describes the parts that rely on JVM features, and explores the minimum language feature set that can be supported without them. Then we explore the possible paths forward to adding them back in for a Scala.js or Scala Native built compiler.

If I am extra diligent then maybe a practical result will come out! (with benchmarks) Practical questions do remain such as possibly embedding either the tasty-interpreter or sjsir-interpreter for macros with a minimal set of bridges to call back into uninterpreted code.
    