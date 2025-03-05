---
title: Explaining Different Coroutine Flavours using Scala Native
day: day2
stage: stage1
time: 17:45 - 18:30
#image:img/assets/madrid/talks/SpeakerCard-WojciechMazur-1920x1080.png
speaker: Wojciech Mazur
speaker2:
---

Multiple modern languages are already using or introducing some kind of coroutines. Stackless coroutines are one of the main features of Kotlin, however, their different, stackfull, variant is powering the project Loom and the Java Virtual Threads. Coroutines are so trendy, that even C++ received support for them! It looks like everyone wants to use them! But, do you know how they work? What are their limitations? 

In this talk, I will explain to you everything you need to know to get a better understatement of this powerful feature. What's more, we'll try to see how we can add them to Scala Native runtime. We'll take a quick look at how the LLVM backend can transform our regular functions into well-optimized continuations, and how we might do the same using AST transformations in the Scala compiler. We'll also acknowledge how operating systems can let us create user-scheduled threads, also known as green threads.
