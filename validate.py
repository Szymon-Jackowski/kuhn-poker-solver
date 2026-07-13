from train import train
from solver import DecisionTree

TOLERANCE = 0.1

def check(name, actual, expected):
    diff = abs(actual - expected)
    status = "PASS" if diff < TOLERANCE else "FAIL"
    print(f"[{status}] {name}: actual={actual:.4f}, expected={expected:.4f}, diff={diff:.4f}")
    return status == "PASS"

def validate():
    alpha = DecisionTree["Jack"].compute_average_strategy()["bet"]
    print(f"Estimated alpha: {alpha:.4f} (theoretical range: [0, 0.333])\n")
    results = []

    results.append(check("King bet (start)", DecisionTree["King"].compute_average_strategy()["bet"], 3*alpha))
    results.append(check("Queen bet (start)", DecisionTree["Queen"].compute_average_strategy()["bet"], 0))

    results.append(check("Jack call (check-bet)", DecisionTree["Jackcheck-bet"].compute_average_strategy()["call"], 0))
    results.append(check("Queen call (check-bet)", DecisionTree["Queencheck-bet"].compute_average_strategy()["call"], 1/3 + alpha))
    results.append(check("King call (check-bet)", DecisionTree["Kingcheck-bet"].compute_average_strategy()["call"], 1))

    results.append(check("Jack bet (after check)", DecisionTree["Jackcheck"].compute_average_strategy()["bet"], 1/3))
    results.append(check("Queen bet (after check)", DecisionTree["Queencheck"].compute_average_strategy()["bet"], 0))
    results.append(check("King bet (after check)", DecisionTree["Kingcheck"].compute_average_strategy()["bet"], 1))

    results.append(check("Jack call (after bet)", DecisionTree["Jackbet"].compute_average_strategy()["call"], 0))
    results.append(check("Queen call (after bet)", DecisionTree["Queenbet"].compute_average_strategy()["call"], 1/3))
    results.append(check("King call (after bet)", DecisionTree["Kingbet"].compute_average_strategy()["call"], 1))

    passed = sum(results)
    total = len(results)
    print(f"\n{passed}/{total} checks passed")

if __name__ == "__main__":
    train(100000)
    validate()