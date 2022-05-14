+++
title = "Adversus ludii, adversus ludos"
date = "2022-05-14T16:15:06+01:00"
author = "ssamot"
tags = ["Games", "AI"]
description = "How I lost my faith"
+++

## Quick self-bio
I entered AI through games; I've started my PhD thinking roughly that if we manage to solve poker (or more generally, games of imperfection and/or incompleteness), we will manage to more or less solve the problem of AI; solving the problem of AI meant solving the problem of labour. Nobody would have to work, because machines would do all -- just need to solve "the problem of games" and all we would end up doing is playing games.

I was wrong on all accounts, but in this piece we will focus on games.

## Core game AI
I practically owe the Game AI community a career. It's made up by really nice people, that do really cool research. But somewhere towards the end of my PhD I've lost my faith in games as a medium to achieve AI, and almost 8 years later I don't know what I believe anymore. I consider "core game AI" to be trying to beat certain games, which has been done successfully, but has not lead to AI.


1. **Games *are* models**: ...but I am doing model free RL I hear you say; well yeah, but you have an environment you can sample millions of times per second and reset it upon request. The distinction between model-free vs model based in this context is largely semantics (i.e. if you spend time learning "the model of model", either as some kind of regulariser or to help predict states faster).

1. **Games promote undergeneralisation**:  The obsession with solving specific games by super-human teams (some of the best RLers in the world work in these problems), combined with almost infinite compute time has created a situation where implicit hyper-parameter tuning is a real problem. Try changing MCTS exploration strengths, the NN architecture or anything else that can be tuned and see these systems fail. This is a problem for ML in general, but games were supposed to be a way out of it.  

1. **"All models are wrong some models are useful":** The Von Neumann aphorism makes you question why are games useful in the general sense.  The existence of a model (even in its PCG version) allows you to learn and "generalise" in ways that are completely predictable. Nothing in the real world is, which is why we have no shoe making robots, no garment making robots, no robot butlers and no self-driving cars. Games have irrelevant physics and we have no clue how to model the physics of the real world close enough to get these robotic butlers.

## Side game AI

Not everyone was/is trying to find ways to beat games, and quite a few people were/are exploring aligned topics, often in dedicated conferences/journals. Two of them are:

1. **Computational creativity:** DALLE-2 is the posterchild of this line of research. These modern systems allow for a degree of compositionality that is impressive, and I am sure people will find ways of making use of it beyond gimmicks (by, for example, further enriching PCG capabilities). Can they help with solving real problems, even spaces they were meant to operate in (e.g. advertising)?. I doubt it, but happy to be proven wrong.

1. **Player modelling:** I started writing this blog post as a response to [Julian's post](https://modl.ai/learning-ai-from-players/). I obviously agree with much of his (excellent) commentary, but I am not convinced at all that player modelling will take us anywhere. Games have very clear reward structures (hence not much to discover via IRL) and player actions are limited to whatever the game designers wanted them to do (so the openness is questionable). More importantly, in quite a few games the state of the world is not something that would make sense to a real-world agent, unless that agent carries with it real-world knowledge of games, i.e. you don't kill monsters and get drops. It's an interesting problem if you want to do the usual predictions that data science teams do (i.e. improve churn), but I can't see the link with AI.


## Hints of neo-platonism
Yeah, I stole the title from Irenaeus, that Greek bishop of Lyon. I really can't draw direct analogies with a heresiological text, but there is something in common between certain tenets of neo-platonic and/or gnostic thought that Irenaeus is attacking and game AI research. Both assume you can "solve" the world through mental abstractions. This line of thinking, in its extreme version, would posit that the virtual world inside the computer is as real as the world outside it. In the more grounded form, the argument would be that there is at least some relevance between the real world and the virtual world of equations that lives inside the machine, with data being the glue. It is the primary reason as to why we claimed games are useful for AI (not just fun). All these look like excuses to me now; we are actively looking to have fun and try to justify it with "one day all this research will lead to something great". It might (as any exploratory research programme would), but somehow I doubt it is going to be through our current expectations. 
