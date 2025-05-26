---
title: "The first steps towards practical capture checking "
day: TODO
stage: TODO
time: TODO
speaker: Cao Nguyen Pham

---

Capture Checking is the next significant feature of Scala, promising a safe and scalable paradigm to write effectful programs using capabilities. Over the past few years, its development has been rapidly progressing, on both theoretical foundations and implementation within the Scala 3 compiler. However, our goal for capture checking has always been to support the entirety of Scala, including all its features and libraries. For this talk, we want to show you the first step towards practical capture checking. Beyond the feature specification and theory, we shall introduce a fully capture-checked version of the Scala API, as well as a capture-checked version of Gears - an experimental asynchronous programming library utilizing capabilities as effect boundaries. We will discuss the process of gradually introducing CC to an existing library, the changes needed, and how to guide your library users into safer patterns using capture annotations. Finally, with the libraries upgraded, we shall see how to implement a small-to-medium-sized project using capabilities-as-effects, and see how CC helps you catch mistakes during the implementation.
    