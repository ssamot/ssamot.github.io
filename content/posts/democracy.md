+++
title = "Democracy and reinforcement learning"
date = "2022-08-14T16:25:13+01:00"
author = "ssamot"
tags = ["AI", "Democracy"]
description = "...are intertwined"
+++

In the age-old battle between representative vs direct democracy, two systems stand out. In representative democracy, it seems [range voting](https://rangevoting.org/WarrenSmithPages/homepage/rangevote.pdf), where each candidate is given a score from 0 to 99 by each voter, has certain desirable properties. In (direct) democracy, the way Aristotle describes it in [Politics](http://classics.mit.edu/Aristotle/politics.html), no elections take place but a group of qualified candidates (which can presumably be the whole population) is subsampled randomly. The argument for random subsampling is that people tend to vote for wealthy and famous individuals, so getting someone to represent the "common man" requires just picking someone in random and giving them an admin post.

Why institute these mechanisms in the first place? The idea is that as a society, we should have a way to express our preferences, the "genuine" will of the people. Both systems look flawed to me, as they allow for malicious players to dominate without much difficulty. In the representative democracy case this can be achieved by using excessive propaganda, in the direct democracy case by taking over the institutions that make up the state; individuals of strong ability and will have an incentive to move to institutional (but unelected) positions and gain power there. This in turn would require some kind of ostracism (a form of negative voting) to get rid of them, which which might prove undesirable.

There is somewhere a full research programme ready to be launched on how collective decisions can be made that do not overly favour certain individuals. Potentially a good starting point could be [Greenwald, Amy, Keith Hall, and Martin Zinkevich. "Correlated Q-Learning." (2005)](ftp://ftp.cs.brown.edu/pub/techreports/05/cs05-08.pdf). They define four types of equilibria a system can stabilise in:

> 1. utilitarian: maximize the sum of all agents’ rewards
> 2. egalitarian: maximize the minimum of all agents’ rewards
> 3. plutocratic: maximize the maximum of all agents’ rewards
> 4. dictatorial: maximize the maximum of any individual agent’s rewards

A good voting system should allow for a mix of egalitarian and utilitarian equilibria, and thus push society forward collectively. You could potentially set this up as a full simulation where different voting schemes come into play, with propaganda also playing a prominent role, and try to find out how coalition formations would play out as the system moves from one set of equlibria to another.

 <!-- There is a really good discussion [here](https://www.rangevoting.org/OmoUtil.html) that links societal utility to rather interesting results in economics and [AI](https://selfawaresystems.files.wordpress.com/2008/01/nature_of_self_improving_ai.pdf). -->
