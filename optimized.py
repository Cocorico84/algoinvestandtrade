from utils import read_csv, timer

data = read_csv("bruteforce_data.csv")

for row in data:
    row["money"] = row["price"] * row["profit"] / 100

clean_data = sorted(data, key=lambda x: x["money"], reverse=True)

@timer
def optimized():
    wallet = []
    total = 0
    profit = 0
    while total <= 500:
        for row in clean_data:
            if row["price"] + total > 500:
                continue
            else:
                wallet.append(row["name"])
                total += row["price"]
                profit += row["money"]
        break
    return {
        "total": total,
        "profit": profit,
        "wallet": wallet
    }

# print(optimized())

# {'total': 500, 'profit': 89.48000000000002, 'wallet': ['action_20', 'action_6', 'action_4', 'action_5', 'action_12', 'action_10', 'action_19', 'action_16']}


