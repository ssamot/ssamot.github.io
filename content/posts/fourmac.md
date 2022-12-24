+++
title = "4 Maccabees and reinforcement learning"
date = "2022-12-23T21:57:24Z"
author = "ssamot"
tags = ["Planning"]
description = "..."
+++

A little known book of Christian apocrypha, which I do not think is considered canonical by any church, is 4 Maccabees. The book reads like a proto-account of martyrdom, with its central theme being a treatise on how "logic" or "rationality" overcomes all passions. The author of the text claims that prime among the passions are pleasure and pain: 

> (4 Macc 13:20) The two most comprehensive types of the passions are pleasure and pain, and each of these is by nature concerned with both body and soul

He then goes to show how what he terms "logic" overcomes the passions. As with the rest of the Maccabee books, its main rhetorical device is Israelite resistance to Antiochus Epiphanes, a Seleucid king. In 4 Macc, Antiochus tries to feed pork to Eleazar, a local Israelite elder. Eleazar flat out refuses, and is tortured to death. Following his death, seven brothers are brought forward and asked to eat pork (no need to turn Greek says Antiochus, just eat a bit of pork). They all refuse and are put to death one by one, in the most gory ways possible, while their mother watches. She then commits suicide by tossing herself into the flames. There is no explicit claim as to what reward the brothers claim by their self-sacrifice, other than that they will be with the prophets and God. 

As agents, it looks like the brothers and the elder are acting irrationally. They have such a strong preference for not eating pork, and thus not violating the Law, that no amount of pain or any promise of pleasure can make them forfeit it. I *guess* succumbing to Antiochus would be the equivalent of losing ones soul, living a life alienated by your own identity, but it says little about total reward. 

It is not trivial to incorporate such behaviour in RL agents. Somehow V(s,horrible death) > V(s,pork). This can be made possible either be assuming some form of extreme afterlife reward (which does not seem to be in the text), or that eating pork changes the meaning/reward of all future external states. In this sense, eating pork is a special reward-modulating action, which changes the pleasure of everything that is to happen. This goes against the spirit of RL/game theory -- the rewards are not defined by the agent, but by the environment. As an example, an agent is not allowed to change the winning state for chess. If that was the case, then both black and white agents could agree that they both win and finish the game after the first move. It also points out to a strategy of fanaticism for winning in real-world conflict. Unlike chess, where the rewards are fixed but it is hard to get in terms of how strategy, rewards are easy to get intellectually but hard to get morally. 


