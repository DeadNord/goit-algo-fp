## Task 7

# Conclusions from the Monte Carlo simulation

## Objective of the Study

The aim of this study is to determine the probabilities of obtaining each possible sum when rolling two dice. To achieve this goal, a Monte Carlo simulation was used.

## Research Methodology

The dice rolling simulation was conducted using software written in the Python programming language. [Number of] rolls were simulated, with each roll calculating the sum of the numbers that appeared on the two dice.

## Simulation Results

The simulation results showed the following probabilities for obtaining sums from 2 to 12:

| Sum | Monte Carlo Probability |
| --: | :---------------------- |
|   2 | 2.76%                   |
|   3 | 5.52%                   |
|   4 | 8.31%                   |
|   5 | 11.14%                  |
|   6 | 13.89%                  |
|   7 | 16.68%                  |
|   8 | 13.93%                  |
|   9 | 11.14%                  |
|  10 | 8.31%                   |
|  11 | 5.51%                   |
|  12 | 2.80%                   |

Total rolls: 1,000,000, Number of threads used: 16

## Theoretical Calculations

According to the theoretical calculations, the probabilities of obtaining each possible sum are as follows:

| Sum | Theoretical Probability |
| --: | :---------------------- |
|   2 | 2.78% (1/36)            |
|   3 | 5.56% (1/36)            |
|   4 | 8.33% (1/36)            |
|   5 | 11.11% (1/36)           |
|   6 | 13.89% (1/36)           |
|   7 | 16.67% (1/36)           |
|   8 | 13.89% (1/36)           |
|   9 | 11.11% (1/36)           |
|  10 | 8.33% (1/36)            |
|  11 | 5.56% (1/36)            |
|  12 | 2.78% (1/36)            |

## Comparison of Results

Comparing the results obtained through the Monte Carlo method with the theoretical calculations showed that:

| Sum | Theoretical Probability | Monte Carlo Probability |
| --: | :---------------------- | :---------------------- |
|   2 | 2.78% (1/36)            | 2.76%                   |
|   3 | 5.56% (1/36)            | 5.52%                   |
|   4 | 8.33% (1/36)            | 8.31%                   |
|   5 | 11.11% (1/36)           | 11.14%                  |
|   6 | 13.89% (1/36)           | 13.89%                  |
|   7 | 16.67% (1/36)           | 16.68%                  |
|   8 | 13.89% (1/36)           | 13.93%                  |
|   9 | 11.11% (1/36)           | 11.14%                  |
|  10 | 8.33% (1/36)            | 8.31%                   |
|  11 | 5.56% (1/36)            | 5.51%                   |
|  12 | 2.78% (1/36)            | 2.80%                   |

## Conclusions

Based on the conducted study, it can be concluded that the Monte Carlo method is an effective tool for approximating probabilities in tasks similar to dice rolling. The results obtained through simulation largely coincide with the theoretical calculations, demonstrating the high accuracy of the Monte Carlo method for this type of task.
