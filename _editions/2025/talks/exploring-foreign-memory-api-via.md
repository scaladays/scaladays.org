---
title: "Exploring foreign memory API via DataFrames"
day: TODO
stage: TODO
time: TODO
speaker: Jamie Thompson
---

The FF&M API is quite rigid - relying upon specific patterns such as static final fields and "signature polymorphic" methods to be optimised at runtime - hence making it hard to use. One use case that can hide that complexity is a "computation engine" abstraction over the top such as data frame, which transforms high level query expressions into optimised code. So in this talk perhaps we can implement the "guts" with this new API and compare the performance/usability (e.g. the 1 billion row challenge).
    