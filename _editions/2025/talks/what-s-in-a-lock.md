---
title: "What's in a lock?"
day: TODO
stage: TODO
time: TODO
speaker: Daniel Urban
---

A detailed look at concurrent programming through a deep dive into locks: what are they; how to implement them (probably don't); how to use them (maybe don't).
- Table stakes: mutual exclusion
  - What does it mean?
  - Why is it useful?
- What happens when acquiring a lock succeeds?
  - We have exclusive access... to what?
  - Make sure we release it!
  - Memory visibility effects
- What to do, when we can't take a lock?
  - We must wait... but how?
  - Just... retry (spinning)
  - Suspend... but what? (Thread? Fiber? Others?)
- Who's next?
  - Okay, we've acquired a lock, did whatever we wanted to, and... what now?
  - Release the lock (very important!)
  - Notify the next one... but who is that? (fairness)
- Do we really need locks?
  - No.
  - Okay, maybe _sometimes_ we do, but: a short look at lock-free programming.
    