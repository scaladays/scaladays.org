---
title: Implementing a Macro
day: day3
stage: stage2
time: 11:15 - 12:00
#image:img/assets/madrid/talks/SpeakerCard-NicolasStucki-1920x1080.png
speaker: Nicolas Stucki
speaker2:
---

In this talk, we will walk through the implementation of a macro, exploring the metaprogramming API and how to use it. It will cover inline macros, the use of quotes to construct and pattern-match on expressions, and the use of reflection to enhance the expressiveness of the macro.

The code we will explore will contain string interpolator macros to construct and deconstruct a JSON object representation. The macro will leverage the Selectable trait in combination with refinement types to encode the object schema.
