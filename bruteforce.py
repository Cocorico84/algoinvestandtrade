import itertools
from utils import read_csv, timer


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


def filtered_wallet(data: list):
    filter_wallets = []
    for combination in get_all_combinations(data):
        if get_total(combination) <= 500:
            filter_wallets.append(combination)
    return filter_wallets


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
                "profit": round(get_profit(wallet), 2),
                "total": get_total(wallet),
                "wallet": wallet
            }
        )

    return sorted(profit_wallet, key=lambda x: x["profit"], reverse=True)[0]


if __name__ == "__main__":
    data = read_csv("bruteforce_data.csv", float_numbers=False)
    print(get_best_wallet(data))
