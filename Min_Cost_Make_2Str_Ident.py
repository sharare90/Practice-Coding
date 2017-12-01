# geeksforgeeks.org: Minimum cost to make two strings identical by deleting the digits
# Code: Sharare Zehtabian


def get_min_cost(a, b):
    cost_a = 0
    cost_b = 0
    min_cost = [[0 for i in range(len(a) + 1)] for j in range(len(b) + 1)]
    for i in a:
        cost_a = cost_a + int(i)
    for j in b:
        cost_b = cost_b + int(j)
    for i in range(len(a) + 1):
        for j in range(len(b) + 1):
            if i == 0 or j == 0:
                min_cost[i][j] = 0
            elif int(a[i - 1]) == int(b[j - 1]):
                min_cost[i][j] = (min_cost[i - 1][j - 1] + int(a[i - 1]) + int(b[j - 1]))
            else:
                min_cost[i][j] = (max(min_cost[i - 1][j], min_cost[i][j - 1]))

    return cost_a + cost_b - min_cost[len(a)][len(b)]


if __name__ == "__main__":
    print(get_min_cost("3759", "9350"))
