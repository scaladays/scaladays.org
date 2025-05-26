---
title: "gRPC APIs for Autonomous Driving from Design to Implementation in Scala"
day: TODO
stage: TODO
time: TODO
speaker: Bendix Sältz
---

## Introduction

Everyone uses APIs all the time. Some of us integrate with existing APIs. Some of us need to create and implement new APIs for the services we're working on. This talk follows the story of creating new APIs for integrating autonomous mobility as a service into existing mobile applications. This has been a two year cross-team effort, impacting half of the company and requiring lots of coordination across distributed product development teams.

## Outline

Starting with the motivation to build public-facing APIs, we discuss the pros and cons of gRPC vs. REST (or rather _JSON over HTTP/1_).
Next, we delve into the API design process, taking inspiration from domain-driven design, to collaboratively decide for easy interfaces, foster inclusivity and create a mutual understanding.
API governance plays an important role in insuring consistency of the interface's naming, behavior and documentation.
We look at the implementation in Scala (_of course_) and face hurdles with AWS load balancers and gRPC streaming.

## Talk's Topic

Experience report, talking about industrial adoption of Scala backing public APIs of the mobility tech provider MOIA.
    