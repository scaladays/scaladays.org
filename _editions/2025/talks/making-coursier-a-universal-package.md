---
title: "Making coursier a universal package manager"
day: TODO
stage: TODO
time: TODO
speaker: Alexandre Archambault
---

This talk will discuss nascent support for new package management systems in [coursier](https://github.com/coursier/coursier), such as [docker](https://www.docker.com), [npm](https://www.npmjs.com), or [pip](https://github.com/pypa/pip).

While Scala has been supporting or interfacing with non-JVM ecosystems ([JS](https://github.com/scala-js/scala-js), [Python](https://github.com/scalapy/scalapy), [native](https://github.com/scala-native/scala-native), …), the tooling around these integrations doesn't provide as good a user experience as on the JVM. Support for new packaging systems in coursier could help bridge that gap.

By adapting these packaging systems to the cache system of coursier, we get back the same speed and reproducibility than on the JVM, while the use of Scala allows for a tighter integration in the Scala tooling, and a better user experience with no more external dependencies and a cache living in a single location on disk.
    