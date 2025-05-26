---
title: "Vibe-coding Scala awesomeness!"
day: TODO
stage: TODO
time: TODO
speaker: Rory Graves
---

LLMs are changing the world.   They have reached the point where they can actually write code.

Tools such as Claude code, aider, and cursor have shown that LLMs can be a valuable companion, not just in implementing small methods, but can now look at wider codebases and make multi-file changes, explain code and help in wider project design.

If you have tried vibe-coding, letting an LLM take the lead in building software you will quickly discover two things.  Firstly LLMs can be scarily good, building out an entire feature of suggesting a novel design.  And secondly, sometimes it just generates nonsense, calling functions that don't exist,  creating uncompilable broken code that it cant fix.

LLM coding tools work by running in a loop, taking actions such as reading, writing or running code.  They must find the write piece of code to edit, understand the structure to work out what to change and correctly apply changes.

LLMs are all about context, giving them the right help and information at the right time is key.  Currently, because a lot of AI has been done in Python it is the target programming language of choice.  However Python is terrible for this,  you write arbitrary things and run it and maybe it works, a spelling mistake is only found if that line of code is run.... Library often don't even tell you what types they are expecting.

So what do you need:

- Succint
- Typesafe
- With a rich ecosystem
- Fast
- self documenting
- Ideally one that has been around  long enough that LLMs recognise it.

Remind you of any language you know?  
Whilst not a popular target (YET) Scala is the answer.

Scala’s succinct structured style allows us to provide the LLM with meaningful code outlines and hints about what is needed easily - helping to produce the right code.

The rich set of existing libraries and a world of examples means it can already generate good Scala code. 
A structured library allows us to provide the LLM with consist code outlines, helping it find the right code, and produce the correct calls.

Fast clean compilation allows us to provide immediate feedback, shortening the cycle to working code. 

Scala provides the ecosystem and guardrails that GenAI coding needs to really sing. 

This talk will cover three aspects, firstly what an LLM needs to build great code well, secondly practical advice on guiding tools such as Claude-code to speed up your own development.  Lastly we will explore how we can leverage Scala’s strengths to improve the code-gen tooling to make Scala-vibing a true pleasure.
    