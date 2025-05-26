---
title: "Safe Coding with LLMs: Verifiable Scala Silver Bullet ?"
day: TODO
stage: TODO
time: TODO
speaker: Andrei Kucharavy
---

Code generation is one of the most promising applications of large language models (LLMs), offering substantial productivity boosts for developers. However, this benefit is tempered by serious concerns surrounding the correctness and security of the generated code—especially in mission-critical systems where vulnerable or unsafe code can have dire consequences. Fortunately, such systems are often built using strongly typed languages, which support static verification techniques to ensure the absence of bugs, race conditions, or non-termination. Among verifiable, strongly typed languages, Scala is the prime candidate for successful LLM generation, given extensive public codebases and code documentation, and this project investigates if SotA LLMs can generate certifiably safe code in Scala. We focus on the Stainless verification framework, assuming use by an experienced but new to Scala developer. Hence, the LLMs are prompted to generate both the implementation of a function from its description and the formal specification needed for such verification. Our results reveal that this task is far from trivial. Models often produce code with syntax errors and actively interfere with verification by inserting constructs like @extern to bypass verification while ensuring the absence of formal verification errors. Before the conference, we plan to refine prompting strategies, explore a wider range of models, and investigate Scala’s rich type system to support static safety guarantees. Our goal is to assess the limits and potential of current LLMs in generating code that isn’t just functional—but provably correct and secure.
    