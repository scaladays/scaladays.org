---
title: "Full-stack scala"
day: TODO
stage: TODO
time: TODO
speaker: Jonas Chapuis
---

Scala 3 is a fantastic language. While it may not be mainstream, it’s a hidden gem for full-stack development. At exomap.io, we’re building a geospatial SaaS platform entirely in Scala. This talk is a tour of that codebase and the stack that makes it work:

* Front-end: Laminar’s functional reactive model makes building responsive UIs a joy. Its expressiveness makes rigid state containers and component hierarchies feel obsolete. Combined with Tailwind and Vite's Scala.js integration, we get fast visual iteration.
* HTTP & API: Tapir makes APIs nearly invisible—just plain case classes and functions. By defining endpoints in a shared project, the client and server stay perfectly in sync. This is where using one language really pays off in terms of productivity.
* Back-end: Cats Effect, Http4s, and Tapir keep things tight yet capable. Middleware gives us logging and monitoring out of the box. With FS2 and Doobie, we stream data directly from the database and cancel long-running requests cleanly, all the way down to the DB layer.
* Infrastructure: Finally, Besom and Pulumi let us close the loop—writing infrastructure as code, in Scala. Domains, certificates, networks, load balancers, databases, containers—you name it, we configure it with full expressive power and strong typing.

Scala’s type system and expressiveness are liberating. They let us build and maintain complex systems solo or in small teams—without sacrificing correctness or velocity.
    