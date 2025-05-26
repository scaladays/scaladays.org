---
title: "Exploring Cats Effect’s New Integrated I/O Runtime: Async I/O with io_uring"
day: TODO
stage: TODO
time: TODO
speaker: Antonio Jimenez
---

This presentation explores the new Cats Effect I/O integrated runtime and how it leverages kernel interfaces like `io_uring` to achieve dramatic performance gains.

We will dive into the foundations of this approach: blocking I/O, syscalls, event loops, and polling systems. From there, we will take a closer look at how `io_uring` works and how it integrates with the Cats Effect runtime. We will walk through the implementation and explore how this design differs from traditional I/O. Finally, we will look at some benchmarks that demonstrate the performance benefits of this new approach.

    