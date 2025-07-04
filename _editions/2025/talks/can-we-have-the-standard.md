---
title: "Can we have the Standard Library for Macros?"
day: day3
stage: stage1
time: 11:00 - 11:40
speaker: Mateusz Kubuszok
---

Do you like it when compiler generates the boring code for you? *Fast, mundane, boring-but-error-prone code?* Do you need to implement such a code generator yourself? Have you found out that *Shapeless*/*Mirrors* bend your brain a bit too much?

Congratulations! You might have a valid use case for writing a macro! Plain-old code with some plain old, `val`s, `def`s and `if`-`else`s. So, we're opening up an IDE, looking at the API and... oh, no. It's so low-level. And **error prone**. And everyone needs to copy-paste the same utilities... which are handling like 50% of the cases, and for the remaining 50% politely asking you to *rewrite your code to something actually supported*.

Oh, and if your users are both on Scala 2 and Scala 3 you have to write everything twice. You'd better have some tests written to keep them aligned!

At this point, you might reconsider using macros: maybe generate some files as managed source, or get back to Shapeless/Mirrors, or just write the boring and error-prone code by hand?

But it doesn't have to be this way. We can have a ***standard library* for macros** that makes simple things simple, and hard things (at least) possible. And we can design it in such a way, that most of the code could be *shared between Scala 2 and 3*.

And this talk will show you how.
