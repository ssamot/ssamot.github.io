+++
title = "The renegade Kautsky III"
date = "2022-06-05T21:16:24+01:00"
author = "ssamot"
tags = ["Socialism", "Religion"]
description = "Patience is a virtue"
math = true
+++

Rodney Stark in his book [The Rise of Christianity](https://en.wikipedia.org/wiki/The_Rise_of_Christianity), attempts to estimate the number of Christians per year, and comes up with a some figures that point to exponential growth. Bart Ehrman in the [Triumph of Christianity](https://www.bartehrman.com/the-triumph-of-christianity/) disputes the numbers a bit, but again comes up with exponential growth figures. Incidently, Kautsky in his [Foundations of Christianity](https://www.marxists.org/archive/kautsky/1908/christ/) discusses numbers, but mostly to claim that the Acts are exaggerating (i.e. the numbers are wrong :P).
<!--
{{< table title=" 1. Stark's calculations" id="1" >}}

|   year |  Number of Christians   |    Percent of Population |
|-------:|:------------------------|-------------------------:|
|     40 | 1,000                   |                   0.0017 |
|     50 | 1,400                   |                   0.0023 |
|    100 | 7,530                   |                   0.0126 |
|    150 | 40,496                  |                   0.07   |
|    200 | 217,795                 |                   0.36   |
|    250 | 1,171,356               |                   1.9    |
|    300 | 6,229,832               |                  10.5    |
|    350 | 33,882,008              |                  56.5    |

{{< /table >}}

{{< table title=" 1. Ehrman's calculations" id="1" >}}

|   year |   Number of Christians   |  Minimum Number of Christians   |  Maximum Number of Christians   |
|-------:|:-------------------------|:--------------------------------|:--------------------------------|
|     30 | 20                       | 20                              | 20                              |
|     60 | 1,280                    | 1,000                           | 1,500                           |
|    100 | 8,389                    | 7,000                           | 10,000                          |
|    150 | 36,000                   | 30,000                          | 40,000                          |
|    200 | 157,000                  | 140,000                         | 170,000                         |
|    250 | 676,000                  | 600,000                         | 700,000                         |
|    300 | 2,923,000                | 2,500,000                       | 3,500,000                       |
|    312 | 3,857,000                | 3,500,000                       | 4,000,000                       |
|    400 | 29,478,000               | 25,000,000                      | 35,000,000                      |


{{< /table >}} -->

Looking at the estimates, it seems that Christians needed 300 years (more or less) to start dominating. The core idea is that slow exponential growth can lead to a takeover if it can be maintained. We can infer the growth rates if we use Stark's and Ehrman's estimates and fit an exponential growth curve (though we strictly do not need to, the authors have done a great analysis already). I am doing this [here](/code/christian_growth.py) using [CMA-ES](https://cma-es.github.io/) (a very well known evolutionary strategy), but the same thing can be achieved using any form of gradient descent. More formally, this equation below describes the curve: $f(x, a, r) = a (1-r)^x$, where

- $a$ is the initial population
- $r$ is the growth rate
- $x$ is the current time step (the year starting from 40 in our case)

<!-- The corresponding code is:

{{< highlight python "title="title in double quotes"" >}}

def growth(a, r, X):
    return a * np.power(1 + r, X)

{{< / highlight >}}


The code below does the optimisation -- fits the curve in the data


{{< highlight python "title="title in double quotes"" >}}



optimizer = cma.CMAEvolutionStrategy(x0=np.zeros(2), sigma0=1.3,
                                        inopts={"popsize":10,
                                                "bounds": [[0,0], [None,None]],
                                                "verbose":-100
                                                }
                                        )
   with trange(n) as t:
       for i in t:
           solutions = []
           asked = optimizer.ask()
           for a,r in asked:
               y_hat = model(y[0], r, x - initial_year)
               error = mean_absolute_error(y,y_hat)
               solutions.append(error)

           t.set_description('Iter %i, loss %.3f, perc loss %.4f' % (i, error,r))
           optimizer.tell(asked, solutions)
   best = y[0], optimizer.best.x[1]
   return best

{{< / highlight >}} -->

We get Figure 1 and Figure 2 for Stark's and Ehrman's estimates respectively. The growth rate needed (something like 3%-4% a year, see Figure 1 and 2 for the exact numbers) is modest, but not small, and probably requires active proselyting. It also needs structures of support for new believers so as not to haemorrhage converts. In practice this means active institutions where people meet, discuss, play and lead their lives; these institutions are to provide an alternative to the existing order of things and get people to invest their time in them (so as to create a sense of identity).


{{< figure src="/code/Stark_cgrowth.png" caption="Figure 1. Exponential growth for Stark's estimates" class="floatleftsplit"   >}}

{{< figure src="/code/Ehrman_cgrowth.png" caption="Figure 2. Exponential growth for Ehrman's estimates -- note the lack of exact fit" class="floatrightsplit"   >}}

This is very much a [strategy of patience](https://brill.com/view/title/33937?language=en) approach, and might require some metaphysical beliefs; if year 0 is now, it is unlikely for things to turn around fast enough. It looks like that without a socialist existence and no socialist praxis, we are just isolated nodes with some bizarre beliefs and at best all we can be is liberals. So, how do we go about creating these institutions? Well, we need to get inspired by the [Erfurt spirit](/posts/kauts/) and replicate its ambitions.  

{{< figure src="https://thebricktestament.com/acts_of_the_apostles/accept_communism_or_die/ac05_03-04.jpg" caption="Ananias, just before being struck by God for not giving his whole fortune to early Christians -- Peter is not impressed. Image from the exceptional Brick Bible https://thebricktestament.com/acts_of_the_apostles/accept_communism_or_die/ac05_03-04.html"  >}}



- [Stark's estimates](/code/Stark.csv)
- [Ehrman's estimates](/code/Ehrman.csv)
- [Hacky code for the above post](/code/christian_growth.py)
