---
title: Introduction to Smithy/Smithy4s
day: day2
stage: stage2
time: 11:15 - 12:00
#image:img/assets/madrid/talks/SpeakerCard-OlivierMelois-1920x1080.png
speaker: Olivier Mélois
speaker2:
---

AWS (Amazon Web Services), one of the biggest cloud providers, provides hundreds of services, and offers SDKs in multiple languages to interact with these services. These public-facing services are backed by tens of thousands of services internal to the AWS platform. In order to streamline the development process of such a behemoth, AWS relies on code-generation. 

Smithy is the culmination of ~14 years of iterations in the field of code-generation. It is an elegant declarative language that enables defining data types, operations and services in a clear and concise manner. The unique aspect of Smithy is that protocol concerns (transport, serialisation) are abstracted away in an extensible annotation-based mechanism. This means that Smithy can be used to describe things like rest/json services, but a virtually infinite amount of other things. 

Smithy4s is a Scala code-generator that feeds off Smithy files. It is unique in that it retains the protocol-agnostic nature of Smithy :the code-generator is not biased towards any protocol or serialisation mechanism. Users can generate Scala code from Smithy to get case classes and interfaces, that can be wired in runtime-interpreters in an opt-in fashion, to derive http services, or CLIs, or even pure-Scala AWS SDKs. Smithy4s is used for streamlining the development of REST/json applications at DisneyStreaming, but offers a strong basis for building bespoke SDKs for remote interactions. 

This talk will serve as an introduction to the Smithy IDL, and a demo of what is possible with Smithy4s
