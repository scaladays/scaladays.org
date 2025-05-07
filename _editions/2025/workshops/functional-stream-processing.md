---
workshop-id: processing
title: Functional Stream Processing
trainer: zainab
level: All 
order: 1
---

### Abstract

This workshop is a practical deep-dive into building reliable incremental processes with Scala 3 and fs2.

Modern business applications are moving towards incremental processing. We design realtime data pipelines, event-driven architectures, reactive systems, and use stream-based I/O with databases, files and websockets. Just as functional programming has transformed the way we build applications, functional stream processing has enabled us to write simple, safe, scalable incremental processes.

In this workshop, you'll use functional streams to explore the challenges of incremental processing. By the end, you'll be able to recognize when a problem needs an incremental solution, ask the right questions about it, choose the right tools to solve it, and avoid pitfalls in memory and concurrency.

Equipped with functional streams in fs2, you'll discover that designing incremental processes can be easy, enjoyable, and deeply empowering.


### Target Audience

- Scala developers at all levels (junior, mid-level and senior) and data engineers
- Anyone who wants to develop practical skills in stream processing: understand what it is, how to use it and where to apply it.
- Developers working on incremental pipelines or event driven architectures 
- Technical decision makers who wish to know the differences between streaming technologies, such as fs2, reactive streams, Flink and Kafka


### Prerequisites

You'll benefit from having some functional Scala knowledge already (Scala 2 or 3), such as working with map and flatMap on lists. Absolutely no knowledge of stream processing or fs2 is needed.


### Requirements

You’ll need a laptop with an IDE setup for basic Scala projects.


### Agenda

##### Part 1: Introduction
- *What is functional stream processing?:* We’ll explore areas where stream processing is typically used, and compare it to conventional processing.
- *Designing incremental pipelines:* We’ll learn how to chain operations to compose larger pipelines.
- *Reasoning about stream processing:* We’ll learn to think of streams as iterative programs, develop a mental model of their execution, and use that to predict their output.
- *Combining and splitting streams:* We’ll explore the different methods of combining functional streams and explore what it means to split them.

##### Part 2: Handling Side Effects
- *Working with cats-effect IO:* We’ll take a brief tour of cats-effect IO and its suspension of side effects.
- *Working with effectful streams:* We’ll see how IO lets us write many more practical stream programs.
- *Error propagation, recovery and retries:* We’ll learn how to recover from errors in an incremental process.
- *Bracketing with streams:* We’ll learn how to encode traditional try-catch-finally logic in an incremental process.
- *Performance optimization:* We’ll see how to detect performance problems in streams and address them with chunking.

##### Part 3: Concurrent Systems
- *Concurrency and parallelism:* We’ll learn how to use streams to write safe, simple concurrent processes.
- *Managing concurrent state:* We’ll learn how to cleanly share state across concurrent streams.

##### Part 4: Streams at Scale
- *Scaling challenges in event-driven systems:* We’ll explore the impact of load in incremental pipelines and the phenomena of backpressure.
- *Designing simple, reliable systems with functional streams:* We’ll analyse the differences between pull and push systems, and of functional streams and reactive systems, and see how functional streams greatly simplify system design.
- *Handling backpressure with queues:* We’ll use different types of queues to ensure predictable behaviour under load.
- *Interoperating with the imperative world:* We’ll explore methods for dealing with push systems, callbacks and other runtimes. 

##### Part 5: Application
We’ll use everything we’ve learned to create an interactive game. We’ll write an event-based stream for receiving user input, have a publisher-subscriber model for handling input and updating game state, and a separate concurrent render loop for displaying state to the screen. We’ll then enhance it with error handling, metrics, and logging, as we would any production-ready application.

