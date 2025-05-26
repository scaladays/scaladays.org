---
title: "Scala-JS runs a Model for Exploring Climate Choices & Feedbacks -  Scala3 -> both Dynamic Web-app (JS / WASM) and Scientific Analyses (Native / JVM)"
day: TODO
stage: TODO
time: TODO
speaker: Ben Matthews (Dr)
---

This talk will show how an interactive web model for exploring future global climate pathways / scenarios has been developed using Scala3/.js, demonstrating how this is robust, efficient and scalable for complex scientific applications. 

The initial idea was to help stakeholders (includes you!) explore the relative sensitivity to diverse climate policy options and scientific uncertainties. You can adjust hundreds of parameters, and see a dynamic response on dozens of connected plots (interactive svgs).  People learn best by experiment, and movement (instant response by client-side calculation) adds a dimension to visualisation.    

The model,  “Scalable World Interactive Model” (SWIM), is available online, you can try it at 
[swim.benmatthews.eu](https://swim.benmatthews.eu)    
There you see the JS web app, but it also runs as a JVM desktop app, as WASM (you can also test on website), and most recently in Scala-Native. You can see the science code simply by clicking on the 'cogs' representing science modules. 

This is not a small project, now with ±30k lines Scala3 code, with ~50 interlinked science modules, from demographics economy energy, through biogeochemical cycles to atmospheric forcing and sea-level rise, over a time-horizon 1700-2300, with ~250 parameters and ~160 plots, and data for ~250 countries.  It’s a complex, delicate calculation, yet it works fast and robustly,  all client-side (so far -  may evolve), in your web-browser. This is *not* yet-another data / scenario visualiser - the input data is only historical, the future calculates on demand, according to your choices. 

While this Scala version is still evolving,  SWIM has a long history, beginning as a java applet, ("Java Climate Model") in year 2000. Since then it was applied for both education and research in several universities and countries, and presented at many scientific and policy conferences.   
We found that a model designed to be fast and flexible for interactivity, is also suitable for probabilistic analyses, integrating over thousands of model variants. Indeed, JCM was used for the first ever probabilistic studies of emissions pathways consistent with diverse climate stabilisation goals, which had some influence on the history of  IPCC scenarios and UNFCCC objectives. 

But this talk is not much about the climate science (that’s another conference), as how the code structure works - such as how the “cogs” representing science modules interact, to recalculate efficiently only the parts of the system that change as the user adjusts parameters, and are needed for dynamically-responding plots, created on the fly, and also adapting to diverse page-layouts.  

The story of the evolution of the code (some of which over 20 yrs old ...), including challenges overcome during transition from java, may help inspire others make this leap. Scala3 attracted me, particularly as it revives the potential of "write once run anywhere", especially since java in browsers died. So the cross-platform structure of this model will be explained, and we can compare run times and check accuracy (hint - it just works...) between JS, WASM, Native and JVM. 

 In the context of real-world scientific code, applications of enums and other structures for small irregular in-code data (essential for transparency) will also be discussed, including current limitations and aspiration for multi-level enums, and a workaround via Scala3 macros.
 
SWIM can also suggest new interpretations of the term “scalable”:    
The model eventually aspires to enable the user to zoom in and out over space (global <=> regional), time (with more detail near-present than distant past/future), sectors (of society), and complexity level (varying for beginner and expert users, or faster and slower analyses). 

Potentially as resolution increases, requiring larger datasets, modules might seamlessly shift to calculate server-side,  depending on relative web and browser speed. 
With scala there is no limit to complexity, so it is envisaged to develop further dimensions, for example, a specific focus on future human migration, in response to both climate impacts and other driving factors. With this in mind, the world region structure is evolving from 250 to 1000 regions.   As we can't study everything at once, so it helps to separate some 'cogs' such as the demographic modules as a separate web-app for more detail, with the aim to eventually reconnect the feedbacks.    

So, Scala3(.js) proves very good for such scientific applications, our challenge now is that too few people are aware of this. Python now rules in science, yet Scala3 now looks quite similar and much more robust and efficient for complex projects. 

The great thing about developing the science code in SWIM, is that once it compiles mostly it just works, and the main test is visually inspecting the circle of plots and checking dynamic interactions.  

Showing the code linked directly from the cogs on the web-app, may help new students to discover Scala, illustrating it is neat but not . Potentially, we might even let them experiment adjusting it in real time online ( although that awaits finer control of the JS-linker module splitting, to allow for hot-reloading of science modules without reloading the data ).

Demonstrating that the model also works in WASM and Native, can help people who are concerned, how might this interlink with other models and tools written in other languages. 
 
So we will conclude by discussing how this tool (inter alia) might help to promote Scala in science and education. Ultimately, the future is still run by people (we hope...), we need more to interact with us.    
    