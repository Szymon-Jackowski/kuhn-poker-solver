from solver import DecisionTree, solver
import random

alpha_history_for_visualisation = []

def train(iterations):
    for i in range(iterations):
        cards = ["Jack", "Queen", "King"]
        first_card = cards[random.randint(0,2)]
        cards.pop(cards.index(first_card))
        second_card=cards[random.randint(0,1)]
        solver([first_card, second_card], "", [1.0, 1.0])
        if i%1000==0 and "Jack" in DecisionTree:
            alpha = DecisionTree["Jack"].compute_average_strategy()["bet"]
            alpha_history_for_visualisation.append(alpha)

if __name__=="__main__":
    train(100000)
    for node in DecisionTree:
        print(node, DecisionTree[node].compute_average_strategy())
        