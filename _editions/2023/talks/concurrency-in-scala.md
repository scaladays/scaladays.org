---
title: Concurrency in Scala and on the JVM
day: day2
stage: stage1
time: 14:30 - 15:15
##image:img/assets/madrid/talks/SpeakerCard-AdamWarski-1920x1080.png
speaker: Adam Warski
---

Concurrent programming is one of the areas where Scala shines. Due to its flexibility in defining new abstractions, we can enjoy concurrency toolkits that provide declarative concurrency APIs. They often eliminate the causes of race conditions or deadlocks at their source.

Despite concurrency being Scala's specialization, or probably because of that fact, the landscape of concurrency libraries and frameworks is dynamic. There are a couple of approaches that have been gaining popularity: starting with Akka, through Monix, cats-effect, ZIO, joined recently by a new contender: libraries based on JVM's Loom project.

Let's characterize the various approaches to concurrency, revealing their strong and weak sides so that you can pick whatever suits your project best. We'll consider safety, developer experience, readability, interaction with effect systems, type-level guarantees, and more!
