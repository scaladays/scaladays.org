---
title: "MeshCI: defining and running workflows in Scala"
day: TODO
stage: TODO
time: TODO
speaker: Jakob Odersky
---

Automated workflows, such as continuous integration (CI) pipelines, deployment scripts, or cron jobs, are an essential part of any modern software project. There are a plethora of solutions for running these, ranging from classic Jenkins, to more modern solutions such as GitHub actions. These workflows save a lot of time and offer peace of mind. For example by automatically compiling and running tests on pull requests, or releasing new versions on merges. Yet when it comes to actually writing and maintaining them, the experience is often less than ideal: requiring the use of ad-hoc domain-specific languages, bash-in-YAML, or monolithic build scripts. Furthermore, it’s often difficult to run these workflows locally on a developer’s machine, leading to platform lock-in, and making the experience even more error-prone and frustrating.

It doesn’t have to be that way however! At their core, workflows are quite simple data structures: directed acyclic graphs (DAGs) of tasks. In this talk, I’ll introduce MeshCI, a workflow orchestration system that, based on this insight, makes writing workflows easy. It uses plain direct-style Scala to define graphs of tasks. These tasks can then be run anywhere, for example on existing systems such as GitHub action runners. MeshCI is local-first: you can test whether your flows work properly before deploying them. Since workflows are just regular Scala files, you get all the usual benefits of type safety, re-usable abstractions and simply the ability to use a language you already know.

The talk will be in two parts:

- I’ll first give an overview of how the system works as a whole, how and where Scala is used (there’s some ScalaJS in there too)
- then, I’ll dive into details of how Scala 3’s metaprogramming and contextual abstractions are used to derive a task graph structure from plain Scala files, which are used to represent the actual workflows

    