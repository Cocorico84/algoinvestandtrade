import itertools
from datetime import datetime

ACTIONS = {
    "action_1": (20, 5),
    "action_2": (30, 10),
    "action_3": (50, 15),
    "action_4": (70, 20),
    "action_5": (60, 17),
    "action_6": (80, 25),
    "action_7": (22, 7),
    "action_8": (26, 11),
    "action_9": (48, 13),
    "action_10": (34, 27),
    "action_11": (42, 17),
    "action_12": (110, 9),
    "action_13": (38, 23),
    "action_14": (14, 1),
    "action_15": (18, 3),
    "action_16": (8, 8),
    "action_17": (4, 12),
    "action_18": (10, 14),
    "action_19": (24, 21),
    "action_20": (114, 18),
}


def get_total(actions: list) -> int:
    total = 0
    for action in actions:
        total += ACTIONS[action][0]
    return total


def flatten_list(unflatten_list):
    return [item for sublist in unflatten_list for item in sublist]


def get_all_combinations() -> list:
    wallets = []
    for i in range(len(ACTIONS)):
        wallets.append(list(itertools.combinations(list(ACTIONS.keys()), i)))
    return flatten_list(wallets)


# print(len(get_all_combinations())) # 1048575

def filtered_wallet():
    filter_wallets = []
    for combination in get_all_combinations():
        if get_total(combination) <= 500:
            filter_wallets.append(combination)
    return filter_wallets


# print(len(filtered_wallet())) # 813347

def get_profit(actions: list) -> int:
    total = 0
    for action in actions:
        total += ACTIONS[action][0] * (ACTIONS[action][1] / 100)
    return total


def get_best_wallet() -> dict:
    profit_wallet = []
    for wallet in filtered_wallet():
        profit_wallet.append(
            {
                "profit": get_profit(wallet),
                "total": get_total(wallet),
                "wallet": wallet
            }
        )

    return sorted(profit_wallet, key=lambda x: x["profit"], reverse=True)[0]

# start_time = datetime.now()
print(get_best_wallet())
# end_time = datetime.now()
# print(end_time-start_time)

