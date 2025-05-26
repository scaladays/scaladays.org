---
title: "Say goodbye to implicits - contextual abstractions in Scala 3"
day: TODO
stage: TODO
time: TODO
speaker: Magda Stożek
---

Have you ever been confused by implicits in Scala? I most certainly have. I struggled to understand them at the beginning of my Scala journey, and to this day I trip over them regularly. It doesn't help that one keyword can be used for many different things  - defining Implicit parameters, implicit conversions, or type class instances. And sometimes it's so frustrating when your code doesn't compile because you can't remember the magical implicit import incantation that is needed (the problem also known as "why does it work fine in that other file, but not here?!"). 
Scala 3 addresses a lot of the tricky bits in the language to make it clearer and easier to use, and luckily, implicits have also undergone a redesign. Well, to be precise... they're gone. But in their place, we're getting language constructs that do one thing and do it well. Please join me in welcoming the new keywords: "given" and "using", as well as context functions and extension methods. They're the new kids on the block to define our contextual abstractions, and they're here to make our code more expressive and easier to understand. Let's see them in action.
    