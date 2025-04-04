---
title: When is an ADT not an ADT?
day: day2
stage: stage2
time: 12:15 - 13:00
#image:img/assets/madrid/talks/SpeakerCard-NicolasRinaudo-1920x1080.png
speaker: Nicolas Rinaudo
speaker2:
---

Modeling data types is a critical aspect of programming: coming up with the right data representation can mean the difference between clear, efficient code, and an unholy mess of spaghetti code with tons of forgotten edge cases.

At the same time, there's a fundamental tension between what's commonly known as ""the OOP approach"" and ""the FP approach"", where the former introduces a tight coupling between data and behaviors, and the latter does the exact opposite.

In this talk, we explore both by attempting to represent and interpret a (very simple) programming language using ""the OOP approach,"" observing the pain points, and seeing what different set of properties we get by fixing them. By the time we're done, we'll have explored a large chunk of the design space, and learned lessons on the various tradeoffs one makes by choosing one approach over the other.
Importantly, we try to stay away from oversimplifications such as _FP good, OO bad_. We hope to demonstrate that both approaches are interesting and valid, and choosing one should be a matter of context rather than religious belief.
