---
title: Load Testing Made Easy with Gatling
day: day3
stage: stage2
time: 14:30 - 15:15
#image:img/assets/madrid/talks/SpeakerCard-RafalPiotrowski-1920x1080.png
speaker: Rafał Piotrowski
speaker2:
---

In this talk I want to show how to check if your API can handle high load. I will show how to simulate a complex scenario with ramp up number of users, constant traffic for certain amount of time and ramp down number of users. All of that using using Scala 3, Gatling and testing GraphQL API.

Load testing looks like a very complex and hard thing to do. I want to show that using right tools, it can be done quite easy. Having example [GraphQL API](https://graphql.org/){:target="_blank" rel="noopener noreferrer"}, I will use generators from [Scalacheck](https://scalacheck.org/){:target="_blank" rel="noopener noreferrer"} to make random valid [GraphQL](https://graphql.org/){:target="_blank" rel="noopener noreferrer"} queries, use them in load testing scenario made with [Gatling](https://gatling.io/){:target="_blank" rel="noopener noreferrer"}. Scenario will contain ramp up number of users, constant high traffic for certain amount of time and ramp down number of users. All that in a very simple manner and using Scala 3.
