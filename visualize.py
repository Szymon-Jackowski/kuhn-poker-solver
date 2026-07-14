import matplotlib.pyplot as plt
import os
from matplotlib.ticker import FuncFormatter
from train import train, alpha_history_for_visualisation
from solver import DecisionTree


if __name__ == "__main__":
    os.makedirs("charts", exist_ok=True)
    for file_number in range(10):
        DecisionTree.clear()
        alpha_history_for_visualisation.clear()
        train(1000000)
        iterations = [point[0] for point in alpha_history_for_visualisation]
        alphas = [point[1] for point in alpha_history_for_visualisation]
        plt.figure()
        plt.plot(iterations, alphas)
        plt.xlabel("Training iteration")
        plt.ylabel("Estimated alpha (Jack bet probability)")
        plt.title("Convergence of alpha during training")
        plt.axhline(y=1/3, color='r', linestyle='--', label='Theoretical max (1/3)')
        plt.gca().xaxis.set_major_formatter(FuncFormatter(lambda x, _: f'{int(x/1000)}k'))
        plt.legend()
        plt.savefig("charts/convergence" + str(file_number) + ".png")
        plt.close()