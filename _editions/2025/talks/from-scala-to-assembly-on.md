---
title: "from Scala to assembly (on JVM)"
day: TODO
stage: TODO
time: TODO
speaker: Jarek Ratajski
---

"When it comes to performance, many developers take certain statements (myths) for granted, which are not always valid, no longer valid, or were never valid to begin with. Performance and benchmarking have always been challenging topics, especially in languages like Scala, where there are many layers between the code and the machine, making any analysis seem futile.
Nevertheless, we will attempt to dive into this issue and examine a few interesting Scala code snippets down to the 'bare metal.' We will utilize recent JVM versions, including Graal, and some useful tools such as JITWatch, javap, GC logs, JMH, and performance counters.

We will show that simple statements such as fp code is slow, or that one can simple read bytecode  to understand performance are false, as the reality is far more complex.

The next time someone makes a claim about performance, you can measure and verify it."
    