---
title: "Are You Tall Enough for This Ride? Real-world Challenges in Code Generation"
day: day2
stage: stage2
time: 16:10 - 16:50
speaker: Michał Pawlik & Jakob Koslowski
---

He just released a patch release in smithy4s. Little did he know, a “simple bugfix” would turn into a compilation error for several dozen developers, faster than he could say "binary compatibility."

Our tale of woe begins with an innocent, one-line change to companion objects, continues through the inevitable GitHub issues from confused users, and culminates in a classic engineer's dilemma: break backward compatibility or keep the bugs? (spoiler: we chose the secret option C).

Through this real-world disaster-turned-teaching-moment, we'll navigate the double-edged sword of code generation - powerful enough to create cross-language platforms with ease, yet temperamental enough to bring down your API with a single diff. We'll demonstrate how a cleverly concealed macro saved our users from frustration while preserving our bugfix integrity.

Come for the horror story of wicked workarounds, stay for the practical strategies on taming generated code with scalameta, snapshot tests, and knowing when you're "tall enough" for the codegen rollercoaster. Because sometimes in Scala, the real bugs were the friends we made along the way.

