---
title: Improve your Tests with Property State-Machine Tests
day: day2
stage: stage2
time: 15:30 - 16:15
#image:img/assets/madrid/talks/SpeakerCard-FedeFernandez-1920x1080.png
speaker: Fede Fernández
speaker2:
---

Do you want to improve your testing skills and know other techniques that will enhance your knowledge about critical pieces of your system? In this talk, I'll show how to leverage property-based testing to effectively and efficiently test crucial parts of your system using state machine testing.

This talk will provide an overview of property-based testing and its application to state machines in Scala. It will discuss how to use property-based testing to validate state machine traces and how these activities can bring other benefits than code coverage.

The audience will learn the basics of property state-machine testing, a technique extending regular state-machine testing to ensure that the system evolves as expected. By testing the system over a complete trace of execution, we can discover problems only apparent after several steps ‚Äì for example, a complete purchase flow using a shopping cart. Examples and code samples will be used to demonstrate the concepts discussed.

Our chosen approach takes a black-box view of the system where developers only interact with it using events and commands and only ""see"" the obtained responses. This gives room for changing the internals of our system-under-test while ensuring that the available public behavior remains within the desired bounds. This approach can produce better results and benefits than the white-box approach available in Scalacheck and Hedgehog.
