import matplotlib.pyplot as plt
from train import train, alpha_history_for_visualisation

if __name__ == "__main__":
    train(1000000)

    iterations = [i * 1000 for i in range(len(alpha_history_for_visualisation))]

    plt.plot(iterations, alpha_history_for_visualisation)
    plt.xlabel("Training iteration")
    plt.ylabel("Estimated alpha (Jack bet probability)")
    plt.title("Convergence of alpha during training")
    plt.axhline(y=1/3, color='r', linestyle='--', label='Theoretical max (1/3)')
    plt.legend()
    plt.savefig("convergence.png")
    plt.show()