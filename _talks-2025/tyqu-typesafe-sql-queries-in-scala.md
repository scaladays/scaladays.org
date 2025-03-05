---
title: "Tyqu: Typesafe SQL Queries in Scala"
day: day3
stage: stage1
time: 15:30 - 16:15
#image:img/assets/madrid/talks/SpeakerCard-MartinKucera-1920x1080.png
speaker: Martin Kučera
---

Language-Integrated Queries (LINQ) is a popular language extension in the .NET framework which allows to generate and execute database queries. It embeds the queries within application code, providing a convenient and type safe API. In other languages including Scala, people have been striving for a similar solution for many years, but it has proven difficult to implement without modifying the language itself.

Tyqu is a LINQ-like Scala library for generating and executing SQL queries against a relational database with the guarantee of type safety for both the generated queries as well as the retrieved data. It enables users to write queries in a familiar functional style operating on nested data, which are automatically translated to relational queries. Tyqu makes heavy use of the latest Scala 3 features such as match types, type-level operations, and a new meta-programming framework. Thanks to that, it provides a more convenient interface, requiring less boilerplate code compared to other popular libraries such as Slick or Quill.

Thanks to a unique mix of compile-time checks and runtime code generation, we have managed to keep Tyqu farily simple and lightweight. To guarantee type safety, all necessary information about a query is represented within its data type. Thus, data accesses are checked statically by the Scala compiler even though the queries themselves are not generated yet. Moreover, we benefit from full code editor support, including suggestions for column names, even when selecting complex named expressions.

In this talk we will introduce the library's API, including a live demo. Afterwards, we will discuss some of the internal architecture and the challenges that we have encountered while designing it.
