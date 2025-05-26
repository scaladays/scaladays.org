---
title: "Routing Http Requests with Scala 3"
day: TODO
stage: TODO
time: TODO
speaker: Noel Welsh
---

Request routing is the problem of choosing a function to invoke based on a HTTP request. All but the simplest web frameworks include routing, but that doesn't mean that routing isn't an interesting problem. I set out to design a request routing library that was all of:

- compositional;
- type safe;
- reversible, meaning clients can be constructed from a route; and
- a delight to use, with great error messages.

Doing requires some interesting design decisions. We'll discuss FP versus OO representations,
finite state machine builders (which are a lot simpler than this name implies!), using Scala 3's tuple types for greater type safety and convenience, and designing for dot-driven development. Along the way I'll discuss other routing libraries that made different decisions, to help illustrate the design space and the tradeoffs that can be made.

Did I succeed? Well, you can decide. Either way, I think the journey is interesting and you should learn something you can apply to your own coding.
    