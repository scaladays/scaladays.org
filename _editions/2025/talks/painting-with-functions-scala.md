---
title: "Painting with functions - Scala on GPUs"
day: day3
stage: stage3
time: 10:10 - 10:50
speaker: Szymon Rodziewicz
---

Ways to run functional code on GPUs are scarce. Moreover, the most common approaches to GPU programming suffer from a lack of support for multiple platforms and very steep learning curves. To address those problems, I am working on a Cyfra DSL and a compiler. With them, you can write Scala code that compiles to SPIR-V and seamlessly runs on a GPU with minimal set-up on a Vulkan runtime, on virtually any system and hardware.

During this talk, I will present the Cyfra library. We will use it to render a 3D scene using ray tracing and ray marching by writing the whole renderer purely in Scala. I will also show how it can be used to make animations and offload compute to GPUs for more business-centered applications.
