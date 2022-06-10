+++
title = "Goodhart’s Law and AI "
date = "2022-06-10T14:18:52+01:00"
author = "ssamot"
tags = ["Artificial Intelligence"]
description = "There are no objectives..."
+++

OpenAI has a blog post [here](https://openai.com/blog/measuring-goodharts-law) -- from the article:

> Goodhart’s law famously says: “When a measure becomes a target, it ceases to be a good measure.” Although originally from economics, it’s something we have to grapple with at OpenAI when figuring out how to optimize objectives that are difficult or costly to measure. It’s often necessary to introduce some proxy objective that’s easier or cheaper to measure, but when we do this, we need to be careful not to optimize it too much.

In my experience, the problem is not that that proxy objectives are easier to measure (hence we need to align the proxy and true objectives), it's that the "real" objective in societal issues is almost never available, apart from very controlled settings. This creates massive distortions; the real reward is unknowable and needs to be discovered iteratively, which will inevitably lead to "over-optimisation". When the detrimental effects of optimising for a proxy objective become apparent, it's already too late as power relationships have already been established, and they all have incentives to point towards the broken proxy objective, inevitably leading to conflict.  
