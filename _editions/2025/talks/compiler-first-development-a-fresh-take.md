---
title: "Compiler-First Development: A Fresh Take on Scala in IntelliJ"
day: TODO
stage: TODO
time: TODO
speaker: Jędrzej Rochala
---

This talk will describe an idea / PoC (potentially something that will be already be released on Scala Days date) that overrides Scala Plugin features with custom providers driven by Scala Presentation Compiler. This approach ensures the correctness of your completions, hovers. It also works with plugins / macros without any hacking and will also result in truthful responses. I also believe and have working demos in which this approach has faster response times.

This is all possible because of some tricks and reuse of the IntelliJ plugin work, such as BSP connection and compiler diagnostics.
This new approach is not a whole new implementation created from the ground up, but rather a replacement of common IDE features.
It also won't affect java interoperability that is already implemented in IntelliJ and still retains all clever lints implemented by Scala Plugin such as `1.filter(_ == 1).headOption` can simplified by `1.find(_ == 1)`. 
    