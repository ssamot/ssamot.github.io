+++
title = "Alpha Go Zero and sample efficiency"
date = "2024-10-02T12:49:53+01:00"
author = "ssamot"
tags = ["AI"]
description = "Too much data, too little thinking"
+++

I am having a re-read of the original alpha-go zero paper here: https://www.nature.com/articles/nature24270


> Over the course of training, 4.9 million games of self-play were generated, using 1,600 simulations for each MCTS, which corresponds to approximately 0.4s thinking time per move. Parameters were updated from 700,000 mini-batches of 2,048 positions. The neural network contained 20 residual blocks (see Methods for further details)

The amount of compute used seems on the low side (even if you account for the fact that this is a "nested" algorithm, with simulations within simulations) compared to the monstrosities we use for LLMs -- and that's 7 years ago! Still, sample efficiency would need to be improved massively before RL becomes relevant to situations where the model is not available or cannot be learned, and my suspicion is that this is not an RL problem, but a supervised learning problem. 
