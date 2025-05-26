---
title: "From Imports to Targets: Bazel on Autopilot with Scala Gazelle"
day: TODO
stage: TODO
time: TODO
speaker: Wojciech Mazur
---

Bazel gives you reproducible, incremental builds at scale—yet many teams still spend hours gardening hand‑written BUILD files. What if your code maintained those files for you?

Enter Scala Gazelle. This open‑source Bazel extension scans the import statements already living in your .scala files, resolves them to Maven coordinates or in‑repo targets, and auto‑generates perfectly scoped BUILD rules—then keeps them synchronized every time you hit save. Goodbye boilerplate, goodbye drift, hello faster CI and happier developers.

Here’s what we’ll cover together: Lightning tour of Bazel — why it excels at large‑scale builds and how Scala fits into the picture Gazelle in action — a hands‑on introduction to the import‑powered BUILD‑file generator Language meets tooling — how specific Scala features shape, challenge, and enhance build automation
    