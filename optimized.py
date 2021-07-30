import csv

with open("bruteforce_data.csv", newline='') as f:
    reader = csv.DictReader(f)
    data = []
    for row in reader:
        row["cost"] = int(row["cost"])
        row["profit"] = int(row["profit"])
        data.append(row)


action_names = [row["actions"] for row in data]

for row in data:
    row["money"] = row["cost"] * row["profit"] / 100

clean_data = sorted(data, key=lambda x: x["money"], reverse=True)

wallet = []
total = 0
profit = 0
while total <= 500:
    for row in clean_data:
        if row["cost"] + total > 500:
            break
        else:
            wallet.append(row["actions"])
            total += row["cost"]
            profit += row["money"]
    break

print(total, profit)
print(wallet)
# action_20', 'action_6', 'action_4', 'action_5', 'action_12', 'action_10'
