+++
title = "Labour theory of value through the lens of reinforcement learning"
date = "2022-06-13T07:09:59+01:00"
author = "ssamot"
tags = ["Socialism", "Artificial Intelligence"]
description = "Slavery in the high seas..."
math = true
+++

One of the popular online debates has been on the usefulness of the labour theory of value (LTV). I'll attempt to give LTV a reinforcement learning (RL) spin (that's how I understand it anyway) which should hopefully clarify things a bit. I'll also abuse notation.

Imagine a scenario where an agent (an abstraction of a capitalist, firm, upper management etc) has access to the following at every time step $t$:

* $o_t$ --> an observation the agent receives containing information about the *world* at time $t$
* $a_t$ --> an action the agent does in time $t$, in this case choosing a *concept*, the amount/type of *labour* to use and the appropriate *resources*.  
* $R_t$ --> profit at time $t$
* $B$ --> a belief function that maps from observations to internal states


The (exchange) value is a hypothetical average of reward, referred to as the Q-value in RL:

$$Q^\pi(B(world)|concept, labour, resources) = E_\pi [R_t | (world, a_t = concept,labour, resources\]$$

A *policy* is what the agent decides to do and is defined as:
$$\pi(B(world)|concept, labour, resources)$$

The agent will have to calibrate its beliefs to help it in its quest for long term reward (which is different than trying to understand the true state of the world, and has implications on consciousness -- see [here](https://www.theguardian.com/science/2021/aug/21/neuroscientist-anil-seth-we-risk-not-understanding-the-central-mystery-of-life) for my MSc supervisor's views), as well as discover the relevant concepts, find labour and grab resources. More precisely, the agent follows a process trying to do this:

$$\pi^* = \argmax_{B, concept, labour, resource}Q^\pi$$

The whole process seems to be producing commodities, but it it doesn't strictly have to. Assuming that the observable outcome of the process is a commodity it might be better to split things into multiple steps (instead of one) following a causal chain of concept --> (labour, resources) --> reward, but the above approximation of value as $Q^\pi$ and $\pi$ should be sufficient for now.

The agent samples the environment, receives observations, takes actions and tastes rewards. The state of the world has to be inferred through beliefs (it is never observed by anyone). The *concept* cannot be observed either. The value cannot be observed, all an individual agent perceives is profit.  Note that an agent can lose money creating valuable commodities and make money creating commodities with zero or negative value. An agent can keep the process going for a long time if they can operate on negative profits. Because value is a long-term concept, one can also extract short term profits and destroy value completely - an elite university selling degrees would be an example of this.

A third party can use observable quantities such as prices, socially necessary labour time, wages, commodities (i.e. manifestations of concepts) and other byproducts of the process and infer value (this is often called "off-policy RL"), approximately.  Could the agent have made all its profits without labour and resources? Absolutely not, but nobody is disputing this. Could the agent have extracted profit without a concept and a profit-maximising execution? I doubt anyone would dispute that either.

So where is all the confusion coming from? It comes from implicit definitions about justice. More specifically, one can easily discern two camps:  


(a) The agent is worth ever penny

The agent deserves all reward. Any reasonable subjectivist would tell you that, yes, labour and resources are in the mix, but even if the agent pays labour peanuts and pocket all profit, that's fine they came up with the concept and executed the policy. It's the moral thing to do. Labour in the above formulation does not even have agency, it resembles a pool of extremely configurable robots. It deserves nothing outside the value-capture process (i.e. the agent's policy).

(b) The agent is stealing everything

A socialist would tell you that (paraphrasing Marx' [Critique of the Gotha Programme](https://www.marxists.org/archive/marx/works/1875/gotha/)) all wealth comes from labour and nature; the fact that an agent found itself in a position to play wizard does not mean they should be earning anything more than what they would have been paid from their own socially necessary labour time. In this view, the concept and policy are worth nothing. They are obvious, social constructs, the agent somehow inherited them; the only reason the agent is an agent in the first place is because of primitive accumulation and/or blind luck. The difference between the profit of the agent and the profit that goes to labour in the form of wages is theft. Doing the off-policy RL trick would tell you (more or less) how much the agent is stealing from labour.    

Most post-1990s subjects fall into camp (a). They see economy as concepts and policy (i.e. what to make and how to make it), and all value derives from them. It is really hard to take position (b) seriously, as a naive causal reading (which most humans do by default) is that labour and nature *cause* value, absent of a concept and a policy, and this is evidently not true. What position (b) is really saying is that more or less anyone can be an agent, the problem is not that hard, it's just that the vast majority of people will never have the opportunity. If you sample a single labourer, you can turn them into CEO pretty quickly.
Socialists would put together various programmes forward to address the issue (planning, coops), but none has been that convincing so far, and solutions deserver another post. Overall, capturing value directly is not easy (we are probably not after exchange value either, it's use values we are after), and the proxy a society uses for value would change it drastically.
