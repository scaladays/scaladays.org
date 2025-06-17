---
title: "Domain modeling for event-sourced data"
day: day2
stage: stage4
time: 16:10 - 16:50
speaker: César Enrique Ramírez
---

In complex systems, separating read and write models can unlock flexibility, scalability, and adaptability and it also comes with other nice side effects: ease of schema evolution, flexibility of access patterns.

In this talk, we’ll explore how to model the read side of event-sourced systems using Scala, leveraging its type system and functional capabilities to create expressive and resilient models over non-SQL event stores.

We'll cover:

- Modeling read and write concerns separately for clarity and maintainability
- Strategies for schema evolution in long-lived event systems
- Common access patterns and performance considerations
- Why Scala is well-suited for defining domain-specific languages (DSLs) for safe and composable access to read data

Along the way, we’ll discuss real-world problems and how this approach can reduce coupling, improve correctness, and enable agile evolution of both domain and infrastructure.
