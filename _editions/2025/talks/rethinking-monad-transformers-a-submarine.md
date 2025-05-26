---
title: "Rethinking Monad Transformers: A Submarine way for Error Handling"
day: TODO
stage: TODO
time: TODO
speaker: Thanh Le
---

Error handling is a crucial aspect of software development, yet achieving a balance between simplicity, precision, and static type checking remains a challenge. Often, developers face trade-offs between code ergonomics, performance, and precise error control.

In this talk, we present an innovative approach (referred as the "submarine") to seamlessly integrate arbitrary error types into the main `Throwable` channel within an effect context. This technique offers functionality akin to `try/catch` blocks, but with the flexibility to handle custom error types within a monadic context. By leveraging implicit capabilities for introduction and elimination, this method provides a robust error handling mechanism.

This approach is particularly effective in Scala 3, thanks to the advanced features of context functions and the inline mechanism. We will delve into the underlying problem, explore the proposed solution, and highlight the Scala 3-specific features and techniques employed in the implementation.
    