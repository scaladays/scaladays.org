---
title: "Keynote: Where Are We With Scala's Capabilities?"
day: day1
stage: room1
time: 17:00 - 18:00
speaker: Martin Odersky
---

The object capability model has been established since the 1960s. It is probably the most obvious and clean way to protect trusted from untrusted components in a complex system. Capabilities are a unifying concept for many aspects of programming, including permissions, effects, and resources. They can be the missing link that can make combinations of functional and imperative programming safe.

So why are object capabilities not used everywhere? I argue it's because they currently lack in both convenience and safety: Convenience: Passing all capabilities along long call chains to code that needs them can quickly get tedious. Safety: Access restrictions such as limited lifetimes or sharing are traditionally encoded using runtime mechanisms with the possibility of runtime failures.

At EPFL we have been working on overcoming these two impediments. Convenience: capabilities can be passed as implicit parameters in using clauses, and capability passing can be completely abstracted over using context functions. Safety: We have extended the type system to track capabilities in types. Specifically, we track which capabilities are closed over in a lambda or object. We are now two years into a project to make these ideas usable on a large scale. I will report on the state of capability checking today: the usage experience with these concepts, what measures we took to make the notations more ergonomic, and what our plans for the future are.
