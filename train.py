from solver import decision_tree, solver
import random

alpha_history_for_visualization = []

def train(iterations):
    '''
    iterations: number of training iterations to run

    Runs the solver repeatedly on randomly dealt hands so decision_tree accumulates
    regret and converges toward a Nash equilibrium strategy over time.
    '''
    for i in range(iterations):
        cards = ["Jack", "Queen", "King"]
        first_card = cards[random.randint(0,2)]
        cards.pop(cards.index(first_card))
        second_card=cards[random.randint(0,1)]
        solver([first_card, second_card], "", [1.0, 1.0])
        if i % 1000 == 0:
            node = decision_tree.get("Jack")
            if node is not None:
                alpha = node.compute_average_strategy()["bet"]
                alpha_history_for_visualization.append((i, alpha))

if __name__=="__main__":
    train(100000)
    for node in decision_tree:
        print(node, decision_tree[node].compute_average_strategy())
        