---
title: "Just Import 'N' Go: Spec-first APIs without codegen"
day: TODO
stage: TODO
time: TODO
speaker: Tomas Mikula
---

Imagine having native support for OpenAPI and/or other API specification languages _built into_ your programming language. By merely importing a specification document, we would obtain a typed interface to a remote service, ready to be used, without the accidental complexity of dealing with HTTP or (de)serialization.

Sounds both exciting and scary, right? (Anyone remember xml literals?) I'd rather have a programming language powerful enough to support the above experience _as a library._ The good news is, Scala is already capable of that today, via its compile-time metaprogramming functionality.

In this talk, I'm going to present [JING](https://github.com/TomasMikula/jing), a new library for spec-first OpenAPI endpoints without codegen.

 - In the first, beginner friendly part, I will show how JING dramatically lowers the barrier to spec-first development against Web APIs and how it facilitates explorative, type-driven programming without unnecessary complexity.
 - Then, I will give a brief peek under the hood and talk about implementation techniques and design decisions.
 - Finally, I'm going to ponder other areas where the JING approach can be applied to unlock a simpler, more productive future.
    