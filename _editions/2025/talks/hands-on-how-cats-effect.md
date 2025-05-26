---
title: "Hands On: How Cats Effect Reimplemented Async I/O on JVM and Native"
day: TODO
stage: TODO
time: TODO
speaker: Daniel Spiewak
---

Over the past few years, the Cats Effect project has been rebuilding the core of its scheduler worker loop with the long-term goal of fully subsuming all I/O and timer-related event dispatch. Put more simply, this moves Cats Effect out of the category of a "Future replacement" and into the far more ambitious category of "Netty replacement". Regardless of whether you think this is a good idea or not (reasonable people can disagree!), *how* it works is really very fun and interesting. In this talk, we will skip the slides and go straight to the code, diving into how the CE integrated runtime handles multithreaded compute, timers, and extensible asynchronous I/O across the JVM and Native backends.
    