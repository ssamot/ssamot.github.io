+++
title = "Measures tend to become targets"
date = "2022-05-15T09:34:45+01:00"
author = "ssamot"
tags = ["Measures", "Reinforcement Learning"]
description = "The minute you measure something, you alter it"
+++

Most complaints about gaming a system can be traced back to [Goodhart's law](https://en.wikipedia.org/wiki/Goodhart's_law), i.e. "when a measure becomes a target, it ceases to be a good measure". In the most trivial of scenarios, let us imagine that an oversight institution is created to measure the quality of teaching, and they come up with a measure of "average GPA", which takes the mean of all student GPAs at a certain school. The minute this is measured and compiled in a table, someone will start ranking schools according to average GPA. School principals and education boards will see this and start competing on average GPAs, thus creating a target. Now, political pressures is going to be applied to the oversight institute to come up with a target that favours certain schools (e.g. combining average GPA with teaching hours) and from that point onwards its games and meta-games around fictional targets.

In an RL setting, you can measure things that help you form state (rather then rewards/targets) -- think pixel values vs score in a game. There are certain game states that carry high reward; the only reason you would measure state is to do actions that would take you to high reward states. It would be really bizarre for an institution to be created that would measure things without wanting to change them. In this sense, all measures form targets; acting and sensing are interlinked in ways that current RL or optimisation does not clearly capture, as they usually come in after a problem has been formulated, i.e. after the measurement process has taken place. 
