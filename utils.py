import csv
from datetime import datetime


def read_csv(csv_file):
    with open(csv_file, newline='') as f:
        reader = csv.DictReader(f)
        data = []
        for row in reader:
            row["price"] = int(row["price"])
            row["profit"] = int(row["profit"])
            data.append(row)

    return data


def timer(func):
    def wrapper(*args, **kwargs):
        start_time = datetime.now()
        func(*args, **kwargs)
        end_time = datetime.now()
        print(end_time - start_time)
        return func(*args)
    return wrapper