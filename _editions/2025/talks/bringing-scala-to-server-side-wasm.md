---
title: "Bringing Scala to Server-Side Wasm with WASI & Component Model"
day: TODO
stage: TODO
time: TODO
speaker: Rikito Taniguchi
---

WebAssembly (Wasm) is a binary instruction format originally designed for web browsers. In recent years, its security and speed have led to its adoption beyond the browser, such as in cloud edge computing.

[Scala.js 1.17.0](https://www.scala-js.org/news/2024/09/28/announcing-scalajs-1.17.0/) introduced support for compiling to Wasm with JavaScript embedding. Building on this, we are now working to extend Wasm support to non-web environments using [WASI](https://github.com/WebAssembly/WASI).

This talk will cover how we get Scala Wasm to run outside the browser, key technologies like the [Component Model](https://github.com/WebAssembly/component-model) - which provides a standard for interoperability between languages - and the current state of the Scala-to-Wasm compiler, highlighting its potential and limitations.
    