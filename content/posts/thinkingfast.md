+++
title = "Thinking fast and slow"
date = "2023-07-01T20:49:38+01:00"
author = "ssamot"
tags = ["AI"]
description = "Contexts?"
+++

So in [Thinking, Fast and Slow](https://www.goodreads.com/en/book/show/11468377), two modes of thinking are proposed: 

1. A fast mode of thinking, akin to having learned Q-values and executing them, i.e. have more or less developed a really good reflex on what to do in every situation. 
2. A slow and deliberate mode of thinking, where one refines his knowledge by thinking more (i.e doing some kind of model-based RL in their heads). 

At the very least this is the RL-like interpretation I've heard people commonly discuss, e.g. see here: [Thinking fast and slow with deep learning and tree search](https://proceedings.neurips.cc/paper/2017/hash/d8e1344e27a5b08cdfd5d027d9b8d6de-Abstract.html). I am pretty confident that some kind of heuristic is involved (maybe in the form of reward shaping) that makes most games trivial. Every game has one, and it operates outside the rules of the game through analogies, on some other symbolic space that makes sense only to humans. One can think of this as some sort of hidden context which, if revealed, makes the game trivial. Maybe LLMs can provide this context? 