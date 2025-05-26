---
title: "Building a Modern LSP in Scala 3"
day: TODO
stage: TODO
time: TODO
speaker: David Salathé
---

# Smart Data Lake Builder: Empowering Developers with an LSP written in Scala 3
 
## Proposal Overview
 
ELCA's Smart Data Lake Builder is an open-source Automation Tool to build modern Data Pipelines, written in Scala and leveraging Apache Spark. The presentation focuses on a custom Language Server Protocol implementation built with Scala 3.
 
## Technical Highlights
 
- **Scala 3 Implementation**: Utilizing advanced language features including intersection and union types, extension methods exports and givens
- **Custom LSP Features**: Sophisticated hovering capabilities and context-aware auto-completion
- **Highly Customized Integration**: Tailored to the specificity of Smart Data Lake Builder's design, auto-completion shows suggestions from the current object context as well as the user defined components.
- **AI-Augmented Capabilities**: Intelligent code suggestions powered by Large Language Models that understand the data pipeline context, optimized for low-latency scenarios 

## Key Challenges Overcome
 
- **Debugging Techniques**: Developing specialized approaches for debugging LSP interactions
- **AI-Augmented Completions With Low-Latency**:  Developing coherent AI suggestions with custom context and designing a high performant concurrent system for the best developer experience.
 
## Future Directions
 
- **Adding AI use cases** We're currently improving AI-assisted features for additional use cases
- **Partial Multi-file Context Awareness**: Building cross-file reference resolution to understand relationships between pipeline components
 
## Value for Attendees
 
This session will demonstrate how Scala 3's modern capabilities can be leveraged to create powerful developer tooling. Attendees will gain insights into:

1. Building custom LSP implementations with Scala 3
2. Enhancing developer experience for domain-specific languages
3. Integrating AI capabilities into developer tooling

## About ELCA
 
ELCA is committed to advancing open-source technologies and contributing to the Scala ecosystem. Our team brings extensive experience in both data engineering and language tooling development.

## Resources
Code is publicly available at: https://github.com/smart-data-lake/sdl-lsp
    