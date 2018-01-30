# Day 2

## Do random notes exist in Nature

- - Randomness $\not=$ total unpredictability; we can quantify what's unpredictable
  - Stochastic = random, vs Deterministic
- Experiment
  - Def: Actions which have a set of results
  - can't predict result prior to performing the experiment to some defree of certainty
  - $\Omega$ is the sample space constiting of all possible outcomes
    - $\Omega = \{H,T\}$ for a coin toss
    - $\Omega = \{1,2,3,4,5,6\}$ for the roll of a dice
  - $E$  (event) is any subset of $\Omega$
    - $E = \{H\}$ or $E = \{T\}$ for the roll of a coin
  - Consider events $E,F$
    - New event $E \cup F$, all outcomes in either $E$ or $F$ (Boolean `OR` operation)
    - $E\cap F$ is all in both $E$ and $F$ (Boolean `AND`)
    - $E^\complement$ is if and only if $E$ does not occur (logical `NOT`)
      - $\Omega^\complement = 0$ since it has all possible events
  - $P(E)$ is the probability that $E$ will happen
    - Three conditions for it to be true:
      - $0 \leq P(E) \leq 1$
      - $P(\Omega) = 1$
      - $P(\cup^\infty_n E_n) = \sum_n^\infty P(E_n)$ for any disjoint (mutually exclusive) events $E_n$
        - $P(E) + P(E^\complement) = 1$
        - $P(E^\complement) = 1 - P(E)$

# Day 3

Countable additivity requires that if $A,B$ are disjoint then $P(A \cup B) = P(A) + P(B)$, and 

- $A \cup B \equiv AB$
- $A \cap B \equiv \varnothing$

Ohterwise, Look up "Inclusion/Exclusion rule for $n$ events"

- Conditional Probability

  - $P(E | F)$ = Probability of $E$ given $F$
  - $F \subset \Omega$ is an event, $E$ is an event conditional upon $F$
  - Suppose we toss two fair dice. If the first dice is 4, what is the probability that the sum is 6?
    - Since only one of $\{1,2,3,4,5,6\} + 4 = 6$, $P(6|4) = 1/6$ 
  - $$P(E|F) = \frac{P(EF)}{P(F)} \implies P(EF) = P(E|F)\cdot P(F)$$ (called the multiplication rule)
    - $P(E|E) = 1$
    - When $E,F$ are mutually exclusive, $P(EF) = 0 \implies P(E | F) = 0$

- Independent events

  - If $E,F$ don't depend on one another, then $P(E|F) = P(E), \quad P(F|E) = P(F)$,
  - By the multiplication rule, $P(EF) = P(E)\cdot P(F)$

- Bayes' Theorem

  - $$P(F | E) = \frac{P(E|F)\cdot P(F)}{P(E)}$$
  - $P(F|E)$ = posterior probability
  - $P(E|F)$ = Likelihood
  - $P(F)$ = Prior probability
  - $P(E)$ = Marginal likelihood, model evidence (not as important)
  - posterior prob. $\propto$ likelihood $\times$ prior probability
    - We can normalize the posterior probability after the fact based on this

- Law of total probability

  - Let $B_1,\dots,B_k$ be a partition of $\Omega$ (partition = disjoint, union of all is $\Omega$), and $A$ be a subset of $\Omega$. Then $P(A) = P(A\cap B_1) + \cdots + P(A \cap B_k) = \sum_i P(A \cap B_i)$
  - Since $P(A \cap B_i) = P(A|B_i)P(B_i)$, we can say that $P(A) = \sum_i P(A|B_i)P(B_i)$
  - Using Bayes' Theorem: $P(B_j | A) = P(A|B_j)P(B_j) / P(A)$
  - We can rewrite as $P(A|B_j)P(B_j) / (\sum_{i=0}^n P(A|B_i)\cdot P(B_i))$

- Random Variables

  - Variable whose value results from the measurement of a quantity which is subject to random variation
  - Number of photons in a spectral band, the sum of the roll of two dice, etc
  - Data are realizations of random variables
  - Random var is $X$, particular realization is $x$ 
  - Discrete Random Variables

  ​