+++
title = "Bayes vs machine learning "
date = "2023-01-15T15:22:01Z"
author = "ssamot"
tags = ["AI", ""]
description = "..via regularisers"
+++

The classic exposition of current trends in AI is captured nicely here: http://www.incompleteideas.net/IncIdeas/BitterLesson.html

Summing up, 

> One thing that should be learned from the bitter lesson is the great power of general purpose methods, of methods that continue to scale with increased computation even as the available computation becomes very great. The two methods that seem to scale arbitrarily in this way are search and learning.

> The second general point to be learned from the bitter lesson is that the actual contents of minds are tremendously, irredeemably complex; we should stop trying to find simple ways to think about the contents of minds, such as simple ways to think about space, objects, multiple agents, or symmetries. All these are part of the arbitrary, intrinsically-complex, outside world. They are not what should be built in, as their complexity is endless; instead we should build in only the meta-methods that can find and capture this arbitrary complexity. Essential to these methods is that they can find good approximations, but the search for them should be by our methods, not by us. We want AI agents that can discover like we can, not which contain what we have discovered. Building in our discoveries only makes it harder to see how the discovering process can be done.

As a research programme, this roughly translates to "discover methods that scale with more data and someone will eventually find the computation needed to train them in bigger machines". I might be stating the obvious, but the biases of such methods matter. We are throwing tons of data to machines, for decreasing returns, and my suspicion is that we might not be solving the regularisation problem properly. 