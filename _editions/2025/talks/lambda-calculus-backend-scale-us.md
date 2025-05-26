---
title: "Lambda Calculus Backend: Scale Us to Blockchain with Scalus"
day: TODO
stage: TODO
time: TODO
speaker: Alexander Nemish
---

Scala was built to scale across diverse domains, and Scalus extends this reach to blockchain smart contracts by compiling to Untyped Plutus Core. This presentation shows how we've developed a compiler backend that transforms Scala's expressive constructs into pure lambda calculus for Cardano blockchain execution. I'll demonstrate the technical architecture that makes this possible, including compiler plugins that intercept Scala's typed trees and metaprogramming techniques that generate optimized intermediate code. You'll see how we represent algebraic data types using Scott encoding, implement pattern matching through function application, and handle Scala's complex features within lambda calculus constraints. The talk includes live demonstrations of the transformation pipeline, showing real Scala code compiled to UPLC and executed on-chain. I'll share performance benchmarks comparing Scalus-generated smart contracts with those written in dedicated languages, highlighting both the advantages and current limitations. This approach enables Scala developers to leverage existing skills instead of learning specialized blockchain languages, truly delivering on Scala's promise as a scalable language.
    