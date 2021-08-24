from utils import read_csv, timer
import argparse

parser = argparse.ArgumentParser()
parser.add_argument("-d", "--dataset", type=str, required=True, action="store")
parser.add_argument("-t", "--type", type=str, required=True, action="store")
args = parser.parse_args()

@timer
def optimized():
    wallet = []
    total = 0
    profit = 0
    while total <= 50000:
        for row in clean_data:
            if row["price"] + total > 50000:
                continue
            else:
                wallet.append(row["name"])
                total += row["price"]
                profit += row["money"]
        break
    return {
        "total": round(total/100, 2),
        "profit": round(profit / 1000000, 2),
        "wallet": wallet
    }


@timer
def knapsack(capacity, wt, val, n):
    matrix = [[0 for x in range(capacity + 1)] for x in range(n + 1)]

    for i in range(n + 1):
        for w in range(capacity + 1):
            if i == 0 or w == 0:
                matrix[i][w] = 0
            elif wt[i - 1][0] <= w:
                matrix[i][w] = max(val[i - 1] + matrix[i - 1][[w - wt[i - 1][0]][0]], matrix[i - 1][w])
            else:
                matrix[i][w] = matrix[i - 1][w]

    res = matrix[n][capacity]
    total = 0
    wallet = []

    w = capacity
    for i in range(n, 0, -1):
        if res <= 0:
            break
        if res == matrix[i - 1][w]:
            continue
        else:
            res = res - val[i - 1]
            w = w - wt[i - 1][0]
            wallet.append(wt[i - 1][1])

    for i in clean_data:
        if i["name"] in wallet:
            total += i["price"] / 100

    return round(matrix[n][capacity] / 1000000, 2), round(total, 2), wallet


if __name__ == "__main__":
    data = read_csv(f"datasets/dataset{args.dataset}_Python+P7.csv", float_numbers=True)

    for row in data:
        row["money"] = round((row["price"] * row["profit"] / 100) * 100)

    clean_data = sorted(data, key=lambda x: x["money"], reverse=True)

    if args.type == "greedy":
        print(optimized())
    elif args.type == "knapsack":
        val = [row["money"] for row in data]
        wt = [(row["price"], row["name"]) for row in data]
        capacity = 50000
        n = len(val)
        print(knapsack(capacity, wt, val, n))
    else:
        print("I don't know this algorithm!")
