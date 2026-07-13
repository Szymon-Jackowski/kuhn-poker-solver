# Kuhn Poker CFR Solver

## Files

`poker.py` handles the game rules - terminal states, payoffs, and legal actions.

`DecisionNode.py` implements regret matching and keeps track of the average strategy for each decision point.

`solver.py` is the core of the project: a recursive function that walks the game tree, computing values and updating regrets.

`train.py` runs the solver repeatedly over randomly dealt hands so the strategy can converge over time.

`validate.py` checks the trained strategy against the known, exact Nash equilibrium formulas.

`visualize.py` plots how the strategy converges over the course of training.

`convergence0.png` through `convergence9.png` show the evolution of the estimated alpha value during each of the 10 independent training runs.

## A quirk of Kuhn Poker: there isn't one single equilibrium

Kuhn Poker doesn't have a single Nash equilibrium - it has infinitely many, forming a family parameterized by a value called alpha (α), which ranges from 0 to 1/3. Alpha is defined as the probability that Player 1 bluffs (bets) when holding a Jack, on the very first action of the game. Once alpha is picked, every other probability in the equilibrium strategy follows from it - for example, Player 1 should bet with a King with probability 3α.

This means two independently trained solvers can converge to different, equally correct strategies, as long as they're internally consistent with the same alpha.

## Validation

`validate.py` estimates alpha from the trained strategy, then checks 11 other decision points against the exact formulas from Kuhn's original 1950 solution, using a tolerance of 0.1. All 11 checks pass.

## Convergence

I ran 10 independent training sessions, one million iterations each, and plotted how alpha evolved over the course of each one (see convergence0.png through convergence9.png). Every run converged to a different value of alpha, which is expected given that there's a whole family of valid equilibria. All of them stayed within the theoretical range of 0 to 1/3 for the vast majority of training. Early on, with very little data, the curves are noisy and occasionally spike above 1/3 briefly - that's just small-sample variance, not a bug. They settle down and stay under the bound as training progresses.

## Running it

```bash
python3 train.py      # train and print the final strategy
python3 validate.py   # train and check it against the known equilibrium
python3 visualize.py  # run 10 training sessions and plot convergence
```

## References

Kuhn, H. W. (1950). A simplified two-person poker.

Zinkevich, M., Johanson, M., Bowling, M., & Piccione, C. (2007). Regret Minimization in Games with Incomplete Information.