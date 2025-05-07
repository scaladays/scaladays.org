---
title: Crossing the Boundaries of Stateful Streaming and Actors Using Serverless Portals
day: day3
stage: stage3
time: 15:30 - 16:15
##image:img/assets/madrid/talks/SpeakerCard-JonasSpenger-1920x1080.png
speaker: Jonas Spenger
---

We present the Portals Project, our envisioned future of dataflow streaming systems with native support for serverless computing. Dataflow streaming has been widely adopted, via systems like Spark and Flink, due to its capability to process large amounts of data in real-time. However, writing certain applications in the dataflow streaming model can be difficult.

Portals is a completely new programming model that introduces novel abstractions, called Atomic Streams and Portals, that simplify building applications where multiple dataflow streaming pipelines need to communicate with each other. At the same time, Atomic Streams ensure that exactly-once processing is guaranteed end-to-end, even across multiple stateful dataflow pipelines. These additions enable writing new applications that were impossible to express previously in the dataflow streaming model: microservices such as shopping carts; iterative programming models such as the actor model or the bulk synchronous parallel (BSP) model, and streaming analytics applications.

This talk will provide an overview of the Portals model, demo several examples, including a fault-tolerant actor model, and present the open-source implementation and project, inviting contributions from the Scala community.
