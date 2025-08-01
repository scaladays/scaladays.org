---
title: "Akka Unplugged - the anti-patterns that kill performance (and how to fix them)"
day: day2
stage: stage2
time: 14:30 - 15:10
speaker: Lukasz Marchewka
---

# The mistakes you don't have to make

Akka is simultaneously one of Scala's most powerful and most misunderstood technologies. Its flexibility becomes a double-edged sword - enabling developers to solve hard problems easily while also tempting them to build overcomplicated architectures that become slow, buggy, and unmaintainable. This presentation explores the most common Akka anti-patterns encountered across dozens of real-world projects, providing practical solutions to transform struggling systems into high-performance applications.

Drawing on extensive consulting experience, this talk reveals and examines the mistakes that plague Akka implementations, and demonstrates how to fix them without incurring expensive rewrites. From misused HTTP endpoints to poorly designed actor hierarchies, from persistence pitfalls to clustering complications, we'll dissect the patterns that lead to failure and provide actionable strategies for success.

# The developer's field guide

This presentation examines real-world Akka anti-patterns and their solutions, focusing on the most common architectural mistakes that developers make when building systems with Akka HTTP, Akka Actors, Akka Persistence, and Akka Clustering. Through solid examples and live demonstrations, attendees will learn to identify these patterns in their own codebases and apply proven remediation strategies.

Teams applying these anti-pattern fixes typically achieve significant improvements faster development, reduced memory consumption, eliminated system crashes, less buggy systems, and improved maintainability. More importantly, these improvements are achieved through better utilization of existing Akka capabilities rather than expensive infrastructure additions or complete rewrites.

The key success factors include recognizing that Akka's power requires disciplined application, focusing on proven patterns rather than clever solutions, and leveraging the framework's strengths while respecting its design principles.

# TL;DR

This talk reveals the performance killers lurking in real-world Akka systems and guides how to address them quickly. Instead of costly rewrites, you'll learn to spot and solve common design problems across HTTP, actors, persistence, and clustering using what Akka already gives you. The focused approach delivers major wins in speed, memory usage, stability, and maintainability by sticking to proven patterns that work with Akka's strengths, not against them.
