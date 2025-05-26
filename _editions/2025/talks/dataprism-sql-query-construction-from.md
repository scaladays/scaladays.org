---
title: "DataPrism: SQL query construction from typeclasses and Higher Kinded Data"
day: TODO
stage: TODO
time: TODO
speaker: Kathryn Frid
---

DataPrism is a SQL query construction library with a unique spin, being built on higher kinded data and typeclasses close to `Functor`, `Apply`, `Traverse` and so on. Specifically, it uses typeclasses for one kind higher found in [perspective](https://github.com/Katrix/perspective). 

In DataPrism, a lot of data is contained in data types having higher kinded typeclasses like `ApplyK` and `TraverseK`. Combining two values then (maybe because of a join for example), is as simple as recording the join in the query, and producing a product of the values using `ApplyK`. At the same time, type safety is retained all the way through.

Of course, as DataPrism just requires the right typeclasses, you can use more than just normal higher kinded data with DataPrism. What for example, would `Option[DbValue[Int]]` mean?

Along the way, I will also go over tradeoffs and smaller design ideas I had which either improves usability or simplifies the design of the library. Maybe some of these ideas can also be used elsewhere?
    