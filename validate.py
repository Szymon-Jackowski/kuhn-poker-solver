from train import train
from solver import decision_tree

TOLERANCE = 0.1

def check(name, actual, expected):
    diff = abs(actual - expected)
    status = "PASS" if diff < TOLERANCE else "FAIL"
    print(f"[{status}] {name}: actual={actual:.4f}, expected={expected:.4f}, diff={diff:.4f}")
    return status == "PASS"

def validate():
    alpha = decision_tree["Jack"].compute_average_strategy()["bet"]
    print(f"Estimated alpha: {alpha:.4f} (theoretical range: [0, 0.333])\n")
    results = []

    results.append(check("King bet (start)", decision_tree["King"].compute_average_strategy()["bet"], 3*alpha))
    results.append(check("Queen bet (start)", decision_tree["Queen"].compute_average_strategy()["bet"], 0))

    results.append(check("Jack call (check-bet)", decision_tree["Jackcheck-bet"].compute_average_strategy()["call"], 0))
    results.append(check("Queen call (check-bet)", decision_tree["Queencheck-bet"].compute_average_strategy()["call"], 1/3 + alpha))
    results.append(check("King call (check-bet)", decision_tree["Kingcheck-bet"].compute_average_strategy()["call"], 1))

    results.append(check("Jack bet (after check)", decision_tree["Jackcheck"].compute_average_strategy()["bet"], 1/3))
    results.append(check("Queen bet (after check)", decision_tree["Queencheck"].compute_average_strategy()["bet"], 0))
    results.append(check("King bet (after check)", decision_tree["Kingcheck"].compute_average_strategy()["bet"], 1))

    results.append(check("Jack call (after bet)", decision_tree["Jackbet"].compute_average_strategy()["call"], 0))
    results.append(check("Queen call (after bet)", decision_tree["Queenbet"].compute_average_strategy()["call"], 1/3))
    results.append(check("King call (after bet)", decision_tree["Kingbet"].compute_average_strategy()["call"], 1))

    passed = sum(results)
    total = len(results)
    print(f"\n{passed}/{total} checks passed")

if __name__ == "__main__":
    train(100000)
    validate()