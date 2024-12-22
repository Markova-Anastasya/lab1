import csv
import json

INPUT_FILENAME = "input.csv"
OUTPUT_FILENAME = "output.json"


def task() -> None:
    with open(INPUT_FILENAME, newline='') as csvfile_:
        reader_ = csv.DictReader(csvfile_)
        data_ = [line for line in reader_]

    with open(OUTPUT_FILENAME, 'w') as jsonfile_:
        json.dump(data_, jsonfile_, indent=4)


if __name__ == '__main__':
    task()

    with open(OUTPUT_FILENAME) as output_f:
        for line in output_f:
            print(line, end="")
