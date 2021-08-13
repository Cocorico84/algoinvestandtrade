import csv
from datetime import datetime


def read_csv(csv_file, float_numbers: bool):
    with open(csv_file, newline='') as f:
        reader = csv.DictReader(f)
        data = []
        for row in reader:
            if '-' not in row["price"] and float(row["price"]) > 0:
                if float_numbers:
                    row["price"] = int(float(row["price"]) * 100)
                    row["profit"] = int(float(row["profit"]) * 100)
                else:
                    row["price"] = float(row["price"])
                    row["profit"] = float(row["profit"])
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
