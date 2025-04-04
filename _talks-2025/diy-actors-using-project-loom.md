---
title: DIY Actors using Project Loom
day: day2
stage: stage3
time: 15:30 - 16:15
#image:img/assets/madrid/talks/SpeakerCard-MushtaqAhmed-1920x1080.png
speaker: Mushtaq Ahmed
speaker2:
---

After the recent changes in Akka license, Scala developers are looking for an alternatives, especially for the `akka-actors` module. Actors allow race-free handling of mutable state without resorting to threads and locks. Key features of an actor that enables this use case are:
1. Sequential processing of messages within an actor: this can be done using *Executors.newSingleThreadExecutor*
2. Ability to spawn large number of actors on top of a handful JVM threads: this can be done using virtual-threads from Loom.

Combining these two, we will show how to do the following:
- Implement a simple ActorRef (send and ask) and Actor (receive) api
- Handle Future callbacks from inside an actor without race conditions
- Use the same principles for local state management within non-actor Scala classes
- Port a few akka-actor examples and compare both approaches

akka-actors provides a lot more features like supervision, fault tolerance and so on. But, those features may not be essential for your app. If so, following the pattern we described will simplify your code without having to deal with the licensing dilemma.
