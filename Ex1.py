from Calls import Calls
import argparse as arg
import main
from Building import Building

if __name__ == '__main__':
    reader_file = arg.ArgumentParser(description='Algo')
    reader_file.add_argument('json')
    reader_file.add_argument('csv')
    reader_file.add_argument('log')
    file = reader_file.parse_args()
    building1 = Building(file.json)
    csv = Calls(file.csv)
    n = 0
    for row in csv.calls:
        Calls.set_target(csv, n, main.allocate_elev(float(row[1]), int(row[2]), int(row[3]), building1))
        n += 1
    if file.log[len(file.log) - 4:] != ".csv":
        csv.csv_w(file.log + ".csv")
    else:
        csv.csv_w(file.log)