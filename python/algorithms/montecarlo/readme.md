**From [this PDF about algorithms](http://www.uta.edu/faculty/rcli/TopTen/topten.pdf):**

1946: John von Neumann, Stan Ulam, and Nick Metropolis, all at the Los Alamos Scientific Laboratory, cook up the Metropolis algorithm, also known as the Monte Carlo method. The Metropolis algorithm aims to obtain approximate solutions to numerical problems with unmanageably many degrees of freedom and to combinatorial problems of factorial size, by mimicking a random process. Given the digital computer’s reputation for deterministic calculation, it’s fitting that one of its earliest applications was the generation of random numbers.

**From [this post with an introductory example in Python](http://niallohiggins.com/2007/07/05/monte-carlo-simulation-in-python-1/)**

"Monte Carlo methods" is a term covering pretty much any use of pseudo-randomness to help solve any kind of problem. Apparently, Monte Carlo is an old name for what is now commonly known as a roulette wheel, hence the relation to randomness. One of the fascinating examples of a Monte Carlo simulator described in Fooled by Randomness is the use of pseudo-random numbers to calculate an approximation of the value of Pi. Imagine a dart board inside of a square. If you throw darts, in a random fashion, at the square, counting the number of darts which land on the dart board versus the number which land on the square, you can approximate Pi with some simple arithmetic. 

**[This post here](http://www.vertex42.com/ExcelArticles/mc/MonteCarloSimulation.html) explains some details.**

Monte Carlo simulation is a method for iteratively evaluating a deterministic model using sets of random numbers as inputs. This method is often used when the model is complex, nonlinear, or involves more than just a couple uncertain parameters. A simulation can typically involve over 10,000 evaluations of the model, a task which in the past was only practical using super computers. 

Monte Carlo simulation is categorized as a sampling method because the inputs are randomly generated from probability distributions to simulate the process of sampling from an actual population. So, we try to choose a distribution for the inputs that most closely matches data we already have, or best represents our current state of knowledge. The data generated from the simulation can be represented as probability distributions (or histograms) or converted to error bars, reliability predictions, tolerance zones, and confidence intervals.

*For the last example in the article, they suggest these steps. Probably they are useful in other cases too:*

+ Step 1: Create a parametric model, y = f(x1, x2, ..., xq).

+ Step 2: Generate a set of random inputs, xi1, xi2, ..., xiq.

+ Step 3: Evaluate the model and store the results as yi.

+ Step 4: Repeat steps 2 and 3 for i = 1 to n.

+ Step 5: Analyze the results using histograms, summary statistics, confidence intervals, etc.

**Montecarlo relies heavily on probability, so it's concepts are necessary.**

[From here](http://math.elon.edu/statistics112/prob_dist.html): A random variable is a variable (typically represented by x) that has a single numerical value that is determined by chance. A probability distribution is a graph, table, or formula that gives the probability for each value of the random variable. If x is a random variable then denote by P(x) to be the probability that x occurs. It must be the case that the sum of all the probabilities is 1.

A *binomial probability distribution* is useful when dealing with two outcomes. Here is the definition of a binomial distribution. A binomial probability distribution occurs when the following requirements are met.

+ The procedure has a fixed number of trials. 
+ The trials must be independent.
+ Each trial must have all outcomes that fall into two categories. 
+ The probabilities must remain constant for each trial. 

The article also has a part on *Mean and Standard Deviation for Binomial Probability Distribution*

[From here](http://math.elon.edu/statistics112/norm_dist.html): A random variable is said to have a normal distribution if it has a probability distribution that is symmetric and bell-shaped. There two VERY important things to mention here. First, the total area under the curve is 1. The second is area will be used to measure probabilities. A normal distribution is intimately connected to Z-scores.

The article then goes to talk about Z-scores. Since markdown doesn't have formulas, let's bring in the example:

> The heights of men have a bell-shaped distribution with a mean of 69.0 inches and a standard deviation of 2.8 inches. What percentage of men have heights between 65.4 inches and 72.3 inches? **Solution:** The Z-score associated with 65.4 is (65.4 - 69.0)/2.8 = -1.29. For 72.3, the Z-score is 1.18 (why?) Since the respective Z-scores are -1.29 and 1.18, the area under the bell-shaped curve is 78.25%. *The idea of Z-scores is very valuble for understanding what you are calculating when finding probabilities.*
