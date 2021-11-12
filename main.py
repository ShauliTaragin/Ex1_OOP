# This is a sample Python script.

# Press Shift+F10 to execute it or replace it with your code.
# Press Double Shift to search everywhere for classes, files, tool windows, actions, and settings.
import json as js
import pandas as pd
import csv

from Calls import Calls
from Elevator import Elevator

#df = pd.read_csv (r'Calls_a.csv')
calls = Calls('Calls_a.csv')
for row in calls.calls:
    print("Time: "+row[1]+", Src: "+row[2]+", Des: "+row[3])

print(calls.number_of_calls())
print(calls.each_call_time(0))


from Building import Building

with open('B5.json', 'r') as f:
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

# main function AllocateElev(time_of_call , src, dst , type: i.e 1 for up -1 for down):
#   loop over lists of all elevators
#       for each elevator:
#       create 3 copy lists for the lists of that elevator
#           search where time_of_call is less then time in time list e.g time_of_call -> 23.9240 time->[1.42342,12.23,24.55,55.00] time_of_call will check 3rd index
#           for that place in time list check if src/dst is between the floor we are checking to the next floor e.g between floor in index 3 to floor in index 4
#           and check if type of direction in index 4 is same as as type of call.
#           if the 3 conditions we stated are satisfied we add them to the elev's copy lists.->function add to list
#               is time for this elev the smallest?
#   after we check all elevators the one with smallest time is the one we the new call to.
#
#
#
#function add_to_elev(list,list,list, src\dst , time ):->returns time of last index in time
#   here we add in the right place the src and dst in all the 3 lists and add all the times.
#   look at java code very similar

