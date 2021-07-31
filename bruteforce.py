import itertools
from utils import read_csv, timer

data = read_csv("bruteforce_data.csv")

def get_total(data: list) -> int:
    total = 0
    for action in data:
        total += action["price"]
    return total


def flatten_list(unflatten_list):
    return [item for sublist in unflatten_list for item in sublist]


def get_all_combinations(action_names: list) -> list:
    wallets = []
    for i in range(len(data)):
        wallets.append(list(itertools.combinations(list(action_names), i)))
    return flatten_list(wallets)



# print(len(get_all_combinations())) # 1048575

def filtered_wallet(data: list):
    filter_wallets = []
    for combination in get_all_combinations(data):
        if get_total(combination) <= 500:
            filter_wallets.append(combination)
    return filter_wallets

# print(len(filtered_wallet())) # 813347

def get_profit(data: list) -> int:
    total = 0
    for action in data:
        total += action["price"] * (action["profit"] / 100)
    return total

@timer
def get_best_wallet(data: list) -> dict:
    profit_wallet = []
    for wallet in filtered_wallet(data):
        profit_wallet.append(
            {
                "profit": get_profit(wallet),
                "total": get_total(wallet),
                "wallet": wallet
            }
        )

    return sorted(profit_wallet, key=lambda x: x["profit"], reverse=True)[0]


print(get_best_wallet(data))
# {'profit': 99.08000000000001, 'total': 498, 'wallet': ('action_4', 'action_5', 'action_6', 'action_8', 'action_10', 'action_11', 'action_13', 'action_18', 'action_19', 'action_20')}
