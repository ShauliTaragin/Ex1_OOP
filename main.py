import copy
import json as js
import sys

from Calls import Calls
import argparse as arg
import math
from Building import Building
from Elevator import Elevator


def update_times(ele: Elevator, index):
    for i in range(len(ele.time)):
        if len(ele.time) == 1:
            if ele.floors[i] != 0:
                elements = abs(ele.floors[i]) / ele.speed + (
                        ele._openTime + ele._closeTime + ele._startTime + ele._stopTime)
                new_time = elements + ele.time[i]
                ele.time[i] = new_time
        elif i == index:
            elements = (abs(ele.floors[i - 1] - ele.floors[i]) / ele.speed) + (
                    ele._openTime + ele._closeTime + ele._startTime + ele._stopTime)
            new_time = elements + ele.time[i - 1]
            ele.time[i] = new_time
        elif i > index:
            elements = (abs(ele.floors[i - 1] - ele.floors[i]) / ele.speed) + (
                    ele._openTime + ele._closeTime + ele._startTime + ele._stopTime)
            new_t = elements + ele.time[i - 1]
            ele.time[i] = new_t


def direct(src, dst):
    if (int(dst) - int(src)) > 0:
        return 1
    else:
        return -1


def add_to_elev(elev: Elevator, src_or_dst, t):  # notice type here is if up to me will
    if len(elev.time) == 0:
        elev.time.append(t)
        elev.floors.append(src_or_dst)
        update_times(elev, 0)
        return 0
    elif len(elev.time) == 1:
        elev.time.append(t)
        elev.floors.append(src_or_dst)
        update_times(elev, 1)
        return 1
    else:
        for i in range(len(elev.time)):  # maybe need to start for loop from i=2
            if i == len(elev.time) - 1:  # case for if we need to add the call to the last index in are list
                elev.time.append(t)
                elev.floors.append(src_or_dst)
                update_times(elev, i + 1)
                return i + 1
            if t < elev.time[i]:
                if (elev.floors[i - 1] > src_or_dst > elev.floors[i]) or (
                        elev.floors[i - 1] < src_or_dst < elev.floors[i]):
                    new_time = elev.time[i - 1] + elev.startTime + elev._closeTime + elev._stopTime + elev._openTime + abs(
                        elev.floors[i - 1] - elev.floors[i]) / elev._speed
                    if new_time > t:
                        elev.time.insert(i, t)
                        elev.floors.insert(i, src_or_dst)
                        update_times(elev, i)
                        return i

        # need case for if it will be inserted at the end


def allocate_elev(time_of_call, src, dst,
                  building: Building) -> int:  # will return the n umber of elevator which to locate the current call
    min_time = sys.maxsize * 2 + 1  # this is the max number in python
    min_elev = 0  # this is arbitrary and will change of course
    for i in building.elev:
        copy_elev = copy.deepcopy(i)
        copy_of_cop_elev = copy.deepcopy(
            copy_elev)  # to see the elev before changes and know how much the changes affected me
        add_to_elev(copy_elev, src, time_of_call)  # add to elev src
        estimated_time_src_to_dst = time_of_call + copy_elev._startTime + copy_elev._closeTime + copy_elev._stopTime + copy_elev._openTime + abs(
            src - dst) / copy_elev.speed
        add_to_elev(copy_elev, dst, estimated_time_src_to_dst)  # add to elev dst
        # the way we calculate which elevator is the most efficient to take this call is seeing which elevator was most affected by adding this new call
        if len(copy_of_cop_elev.time) == 0:
            copy_of_cop_elev.time.append(0)
        time_diff = copy_elev.time[-1] - copy_of_cop_elev.time[-1]
        if time_diff < min_time:
            min_time = time_diff
            min_elev = copy_elev._id
    best_elev = building.elev[min_elev]  # getting the best elevator
    add_to_elev(best_elev, src, time_of_call)
    estimated_time_src_to_dst = time_of_call + best_elev._startTime + best_elev._closeTime + best_elev._stopTime + best_elev._openTime + abs(
        src - dst) / best_elev.speed
    add_to_elev(best_elev, dst, estimated_time_src_to_dst)  # add to elev dst
    return min_elev
    # here we need to write to the output file the updated elevator allocated to the call


if __name__ == '__main__':

    reader_file = arg.ArgumentParser(description='ULTIMATE')
    reader_file.add_argument('json')
    reader_file.add_argument('csv')
    reader_file.add_argument('log')
    file = reader_file.parse_args()
    building1 = Building(file.json)
    csv = Calls(file.csv)
    #log = Calls(file.log)
    n = 0
    for row in csv.calls:
        Calls.set_target(csv, n, allocate_elev(float(row[1]), int(row[2]), int(row[3]), building1))
        n+=1
    csv.csv_w()





# main function AllocateElev(time_of_call , src, dst , type: i.e 1 for up -1 for down):
#   loop over lists of all elevators
#       for each elevator:
#       create 3 copy lists for the lists of that elevator
#           search where time_of_call is less then time in time list e.g time_of_call -> 23.9240 time->[1.42342,12.23,24.55,55.00] time_of_call will check 3rd index
#           for that place in time list check if type is same as the direct list in third index and if floor in that index is bigger/smaller depending if its up or down e.g between floor in index 3 to floor in index 4
#           and check with index 2 if we add the time for the stop we will be able to stop there i.e the time . if conditions dont satisfy we move to the next time
#           if the 3 conditions we stated are satisfied we add them to the elev's copy lists.->function add to list
#               is time for this elev the smallest?
#   after we check all elevators the one with smallest time is the one we the new call to.
#
#
# function add_to_elev(elev, src\dst , time ):->returns time of last index in time then we check difference to previous last time
#   here we add in the right place the src and dst in all the 3 lists and add all the times.
#   look at java code very similar
