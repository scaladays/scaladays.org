---
title: Simple and Speedy UIs in Scala 3
day: day2
stage: stage1
time: 12:15 - 13:00
#image:img/assets/madrid/talks/SpeakerCard-NoelWelsh-1920x1080.png
speaker: Noel Welsh
speaker2:
---

The typical Scala developer is probably a backend developer, and most backend developers shy away from user interface work. This is, I think, a mistake. Backend systems almost always have non-technical internal users. Giving them a user interface means they can solve their own problems, which is a win for them and a win for the backend team that wants to focus on the code.

User interfaces are often seen as a sizable project, and for this reason rarely make it off the backlog. I don't think this should be the case. I've been working on a Scala 3 library that makes building a user interface the work of a few hours instead of a few weeks. The library is targetted at internal interfaces, where minimal customization is acceptable. The core of the system is a combinator library for expressing user interfaces. This is a very typical functional programming pattern, but implemented with a Scala 3 twist. In my system the language of user interface descriptions can be extended, as can the generators that produce the interface. Thus my system solves the so-called ""expression problem"", and it does so in a novel way using union types. For maximum development speed, generic derivation can be used to almost instantaneously construct forms, while allowing incremental customization if the defaults are found lacking. This layered design allows a spectrum of development styles, from fully automatic generation to full customization, and truly shows that Scala 3 is a scalable language.

My talk will motivate the problem using several real examples, and then dive into the design and implementation of the library. The talk will focus on the general patterns of the design, and the Scala 3 specific features that are used in the implementation. I'll conclude with a brief comparison to alternative systems.
