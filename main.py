# This is a sample Python script.

# Press Shift+F10 to execute it or replace it with your code.
# Press Double Shift to search everywhere for classes, files, tool windows, actions, and settings.
import json as js
import pandas as pd
import csv

from Ex1_OOP.Calls import Calls
from Ex1_OOP.Elevator import Elevator

#df = pd.read_csv (r'Calls_a.csv')
calls = Calls('Calls_a.csv')
for row in calls.calls:
    print("Time: "+row[1]+", Src: "+row[2]+", Des: "+row[3])

print(calls.number_of_calls())
print(calls.each_call_time(0))


from Building import Building

with open('B1.json', 'r') as f:
    data = f.read()
# parse file
obj = js.loads(data)
# print("MIN FLOOR", str(obj['_minFloor']))
# print("MAX FLOOR", str(obj['_maxFloor']))
list_elevator = obj['_elevators']
list_size = len(list_elevator)
building = Building(str(obj['_minFloor']), str(obj['_maxFloor']), list_elevator)
# for i in range(list_size):
#     print("ID:", list[i].get("_id"))
#     print("SPEED:", list[i].get("_speed"))
#     print("MIN FLOOR", list[i].get("_minFloor"))
#     print("MAX FLOOR", list[i].get("_maxFloor"))
#     print("CLOSE TIME", list[i].get("_closeTime"))
#     print("OPEN TIME", list[i].get("_openTime"))
#     print("START TIME", list[i].get("_startTime"))
#     print("STOP TIME", list[i].get("_stopTime"))
print(building)

def print_hi(name):
    # Use a breakpoint in the code line below to debug your script.
    print(f'Hi, {name}')  # Press Ctrl+F8 to toggle the breakpoint.
    print("hello world")

# Press the green button in the gutter to run the script.
if __name__ == '__main__':
    print_hi('PyCharm')

# See PyCharm help at https://www.jetbrains.com/help/pycharm/
