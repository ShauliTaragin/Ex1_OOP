import csv
import math


class Calls:
    def __init__(self, df):
        self.calls = []
        self.csv_r(df)

    def __str__(self):
        return self.df

    def allocate_elevator(time, num_elev):  # this functions
        return time

    # we want a list of calls for each elevator. need to decide how to represent the calls
    # we will have a main function which will calculate how to allocate each elevator
    # have a function which will change the calls in the csv according to what the main function allocated
    # function that calculate the time of each elev. (maybe calling from main function)

    def csv_r(self, df):
        calls = []
        with open(df) as f:
            csv_r = csv.reader(f)
            for row in csv_r:
                calls.append(row)
        self.calls = calls

    def number_of_calls(self):
        return len(self.calls)

    def each_call_time(self, index):
        if index < 0 or index > self.number_of_calls() or index + 1 > self.number_of_calls():
            return "ERROR INVALID INDEX"
        else:
            return abs((float(self.calls[index + 1][1])) - (float(self.calls[index][1])))

    def set_target(self, index, target):
        self.calls[index][5] = target

    def csv_w(self, filename):
        with open(filename, 'w', newline='') as f:
            writer = csv.writer(f)
            writer.writerows(self.calls)
