from concurrent.futures import ThreadPoolExecutor
import numpy as np
import matplotlib.pyplot as plt
from tabulate import tabulate
import os


class DiceSimulation:
    def __init__(self, rolls=100000, bottom_range=1, top_range=6):
        self.rolls = rolls
        self.sum_counts = {sum_: 0 for sum_ in range(bottom_range, top_range)}

    def simulate_roll(self, n):
        rolls = np.random.randint(1, 7, size=(n, 2))
        sums = np.sum(rolls, axis=1)
        return sums

    def simulate_rolls(self):
        chunk_size = self.rolls // (os.cpu_count() or 1)
        with ThreadPoolExecutor() as executor:
            futures = [
                executor.submit(self.simulate_roll, chunk_size)
                for _ in range(os.cpu_count() or 1)
            ]
            for future in futures:
                result = future.result()
                unique, counts = np.unique(result, return_counts=True)
                for sum_, count in zip(unique, counts):
                    if sum_ in self.sum_counts:
                        self.sum_counts[sum_] += count

    def visualize_results(self):
        sums = list(self.sum_counts.keys())
        probabilities = [self.sum_counts[sum_] / self.rolls * 100 for sum_ in sums]
        plt.bar(sums, probabilities, tick_label=sums)
        plt.xlabel("Sum")
        plt.ylabel("Probability (%)")
        plt.title("Dice Roll Simulation Probabilities")
        plt.show()

    def visualize_results_with_scatter(self):
        angles = np.linspace(0, 2 * np.pi, len(self.sum_counts), endpoint=False)
        probabilities = np.array(
            [self.sum_counts[sum_] / self.rolls * 100 for sum_ in self.sum_counts]
        )

        radii = probabilities / probabilities.max() * 10

        fig, ax = plt.subplots(subplot_kw={"projection": "polar"})
        ax.scatter(angles, radii, c=radii, cmap="hsv", alpha=0.75)

        ax.set_yticklabels([])
        ax.set_xticks(angles)
        ax.set_xticklabels([str(sum_) for sum_ in self.sum_counts])

        plt.title("Dice Roll Probabilities Scatter Visualization")
        plt.show()


def main(rolls):
    simulation = DiceSimulation(rolls=rolls, bottom_range=2, top_range=13)
    simulation.simulate_rolls()

    data_comparison = [
        [
            sum_,
            f"{1/36*100*min(sum_-1, 13-sum_):.2f}% (1/36)",
            f"{simulation.sum_counts[sum_]/simulation.rolls*100:.2f}%",
        ]
        for sum_ in range(2, 13)
    ]

    print(
        tabulate(
            data_comparison,
            headers=["Sum", "Theoretical Probability", "Monte Carlo Probability"],
            tablefmt="pipe",
        )
    )

    num_threads = os.cpu_count() or 1
    print(f"\nTotal rolls: {rolls}, Number of threads used: {num_threads}\n")

    simulation.visualize_results()
    simulation.visualize_results_with_scatter()


if __name__ == "__main__":
    main(rolls=1000000)
