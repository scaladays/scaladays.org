---
title: "Tagless Final for Humans"
day: TODO
stage: TODO
time: TODO
speaker: Noel Welsh
---

Tagless final can be either an amazing tool that allows for incredibly expressive code, or a colossal pain in the butt. So how do we make it more the former and less the latter? In this talk I'll describe when tagless final is appropriate, and Scala programming techniques that can make the notational overhead disappear.

Tagless Final is common in the Scala world, but does it really justify the resulting code complexity? I've spent a decade writing a library using tagless final, so I can't claim I don't like the technique. At the same time I've worked on many codes bases where I felt it added a lot of complexity for little value.

In this talk I'll look at the different uses to which tagless final is put to, and see what we can learn about when it is useful and when it just gets in the way. Then, when we decide it is useful, I'll show how we can use subtyping, extension methods, and path-dependent types to allow the end user to write tagless final code that feels a natural as writing code without it, and won't have people shouting "What the F[_]?!" 

    