from utils import read_csv

data = read_csv("bruteforce_data.csv")

for row in data:
    row["money"] = row["price"] * row["profit"] / 100

clean_data = sorted(data, key=lambda x: x["money"], reverse=True)

wallet = []
total = 0
profit = 0
while total <= 500:
    for row in clean_data:
        if row["price"] + total > 500:
            break
        else:
            wallet.append(row["name"])
            total += row["price"]
            profit += row["money"]
    break

print(total, profit)
print(wallet)
# action_20', 'action_6', 'action_4', 'action_5', 'action_12', 'action_10'
