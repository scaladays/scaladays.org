---
title: 'X-Ray your Build: Build Events, Build Scans, and Caching Explained'
day: day2
stage: stage2
time: 16:45 - 17:30
#image:img/assets/madrid/talks/SpeakerCard-Iulian.Mirco-1920x1080.png
speaker: Iulian Dragos
speaker2: Mirco Dotta
---

A frequent complaint about Scala is build times: Scala builds are slow, and the immediate reaction is to blame the compiler. While indeed the Scala compiler is slower than the Java one, it's not always the only culprit.

Developer productivity is seriously impacted by build performance, but what is happening during a Scala build? Most engineers have a high-level understanding of what a build does: compile some sources, compress them into a jar, run some tests. Some may mention dependency resolution, or generating sources. But how do all these tasks get executed, and which ones have a real impact on your build? What do you do if the CI fails, but everything passes locally?

In this talk we will describe how Sbt is different from other build tools and show what actionable insights can be gained by exposing and exploring build events. We will look at raw build events, and leverage freeGradle Enterprise build scans to understand and visualize the build.

Build caching, be it local or remote, is another technique to speed up builds by avoiding work altogether: when inputs are the same, we can reuse a previous build result. This applies to everything that acts as a pure function, and it often works well for compile tasks, but also tests. Most build tools offer some level of caching, and Sbt has its own variation. We will look at ways to leverage build caching in Sbt, and what can be learned from the experience of Gradle Enterprise, and how the GE build cache compares to the built-in solution.

Keeping it all in check requires a great deal of attention and hard to acquire know-how. It's a continuous and never ending effort, demanding our most precious and scarce asset: time. We'll wrap up by showing how Gradle Enterprise tackles this issue, and how the Scala community can benefit from it.
