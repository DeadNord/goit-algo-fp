from tabulate import tabulate


class FoodSelection:
    def __init__(self, items):
        self.items = items

    def greedy_algorithm(self, budget):
        sorted_items = sorted(
            self.items.items(),
            key=lambda x: x[1]["calories"] / x[1]["cost"],
            reverse=True,
        )
        selected_items = []
        total_cost = 0
        total_calories = 0

        for item in sorted_items:
            name, data = item
            if total_cost + data["cost"] <= budget:
                selected_items.append(name)
                total_cost += data["cost"]
                total_calories += data["calories"]

        return selected_items, total_cost, total_calories

    def dynamic_programming(self, budget):
        dp = [[0 for _ in range(budget + 1)] for _ in range(len(self.items) + 1)]
        item_list = list(self.items.keys())
        for i in range(1, len(self.items) + 1):
            for w in range(1, budget + 1):
                cost = self.items[item_list[i - 1]]["cost"]
                calories = self.items[item_list[i - 1]]["calories"]
                if cost <= w:
                    dp[i][w] = max(dp[i - 1][w], dp[i - 1][w - cost] + calories)
                else:
                    dp[i][w] = dp[i - 1][w]

        selected_items = []
        w = budget
        total_cost = 0
        for i in range(len(self.items), 0, -1):
            if dp[i][w] != dp[i - 1][w]:
                selected_items.append(item_list[i - 1])
                w -= self.items[item_list[i - 1]]["cost"]
                total_cost += self.items[item_list[i - 1]]["cost"]

        return selected_items[::-1], total_cost, dp[-1][-1]


def main():
    items = {
        "pizza": {"cost": 50, "calories": 300},
        "hamburger": {"cost": 40, "calories": 250},
        "hot-dog": {"cost": 30, "calories": 200},
        "pepsi": {"cost": 10, "calories": 100},
        "cola": {"cost": 15, "calories": 220},
        "potato": {"cost": 25, "calories": 350},
    }
    budget = 100

    food_selection = FoodSelection(items)

    greedy_result, greedy_cost, greedy_calories = food_selection.greedy_algorithm(
        budget
    )
    dynamic_result, dynamic_cost, dynamic_calories = food_selection.dynamic_programming(
        budget
    )

    results_data = {
        "Algorithm": ["Greedy", "Dynamic Programming"],
        "Selected Items": [", ".join(greedy_result), ", ".join(dynamic_result)],
        "Total Cost": [greedy_cost, dynamic_cost],
        "Total Calories": [greedy_calories, dynamic_calories],
    }

    table = tabulate(results_data, headers="keys", tablefmt="pipe")
    print(table)


if __name__ == "__main__":
    main()
