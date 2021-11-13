import json as js
from Calls import Calls
import argparse as arg
from Building import Building


# calls = Calls('Calls_a.csv')
# for row in calls.calls:
#     print("Time: " + row[1] + ", Src: " + row[2] + ", Des: " + row[3])
#
# print(calls.number_of_calls())
# print(calls.each_call_time(0))
#
# with open('B1.json', 'r') as f:
#     data = f.read()
# obj = js.loads(data)
# for x in obj:
#     print(x)
# print(obj)
# gg = Building('B1.json')
# print(gg.NumbersOfElevators())
#
# for x in gg.elev:
#     print(x._speed)
# elev = []

csv = Calls('Calls_a.csv')
for row in csv.calls:
    print("Time: " + row[1] + ", Src: " + row[2] + ", Des: " + row[3])
json = Building('B1.json')
for row in json.elev:
    print(row)

for x in json.elev:
    print(x.to_string())

# c = input()
# csv = Calls(c)
# for row in csv.calls:
#     print("Time: " + row[1] + ", Src: " + row[2] + ", Des: " + row[3])

def main():
    json_file, csv_file, log_file = input().split()
    # reader_file = arg.ArgumentParser(description='ULTIMATE')
    # reader_file.add_argument('json')
    # reader_file.add_argument('csv')
    # reader_file.add_argument('log')
    # file = reader_file.parse_args()
    json = Building(json_file)
    csv = Calls(csv_file)
    for row in csv.calls:
        print("Time: " + row[1] + ", Src: " + row[2] + ", Des: " + row[3])
    # calls.update_output(file.LOG)

    # print (calls.calls)


# with open('B1.json', 'r') as f:
#     data = f.read()
#     for row in data['_elevators']:
#         elev.append(row)

# for x in elev:
#     print("ID :" + x[0] + ""+x[1]+x[2]+x[3]+x[4]+x[5])


# list_elevator = obj['_elevators']
# list_size = len(list_elevator)
# building = Building(str(obj['_minFloor']), str(obj['_maxFloor']), list_elevator)

# print(building)


# def allocate_elevator(time, src, dst, direction):
#     for

def add_to_elev(list1, list2, list3, src, dst, time):
    return 0
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
# function add_to_elev(list,list,list, src\dst , time ):->returns time of last index in time
#   here we add in the right place the src and dst in all the 3 lists and add all the times.
#   look at java code very similar
