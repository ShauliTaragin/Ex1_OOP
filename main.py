import copy
import sys
from Calls import Calls
import argparse as arg
from Building import Building
from Elevator import Elevator


def update_times(ele: Elevator, index):  # Update time get elevator and index
    for i in range(len(ele.time)):
        if len(ele.time) == 1:  # we check if the list is size 1
            if ele.floors[i] != 0:
                elements = abs(ele.floors[i]) / ele.speed + (  # we calculate the abs value from the current floor to
                    # zero with the all elements and we insert the new time in the right index
                        ele._openTime + ele._closeTime + ele._startTime + ele._stopTime)
                new_time = elements + ele.time[i]
                ele.time[i] = new_time
        elif i == index:  # we check if the i equals to the index we want to.
            elements = (abs(ele.floors[i - 1] - ele.floors[i]) / ele.speed) + (
                # we calculate the abs value from the current floor to
                # zero with the all elements and we insert the new time in the right index
                    ele._openTime + ele._closeTime + ele._startTime + ele._stopTime)
            new_time = elements + ele.time[i - 1]
            ele.time[i] = new_time
        elif i > index:  # we going to update all times after we go the right index
            elements = (abs(ele.floors[i - 1] - ele.floors[i]) / ele.speed) + (
                    ele._openTime + ele._closeTime + ele._startTime + ele._stopTime)
            new_t = elements + ele.time[i - 1]
            ele.time[i] = new_t


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
                    new_time = elev.time[
                                   i - 1] + elev.startTime + elev._closeTime + elev._stopTime + elev._openTime + abs(
                        elev.floors[i - 1] - elev.floors[i]) / elev._speed
                    if new_time > t:
                        elev.time.insert(i, t)
                        elev.floors.insert(i, src_or_dst)
                        update_times(elev, i)
                        return i


def allocate_elev(time_of_call, src, dst,
                  building: Building) -> int:  # will return the n umber of elevator which to locate the current call
    min_time = sys.maxsize * 2 + 1  # this is the max number in python
    min_elev = 0  # this is arbitrary and will change of course
    for i in building.elev:
        copy_elev = copy.deepcopy(i)
        # to see the elev before changes and know how much the changes affected me
        src_inserted = add_to_elev(copy_elev, src, time_of_call)  # add to elev src
        estimated_time_src_to_dst = copy_elev.time[
                                        src_inserted] + copy_elev._startTime + copy_elev._closeTime + copy_elev._stopTime + copy_elev._openTime + abs(
            src - dst) / copy_elev.speed
        dst_inserted = add_to_elev(copy_elev, dst, estimated_time_src_to_dst)  # add to elev dst
        # the way we calculate which elevator is the most efficient to take this call is seeing which elevator was
        # most affected by adding this new call
        time_diff = copy_elev.time[src_inserted] - time_of_call
        time_diff += copy_elev.time[dst_inserted] - estimated_time_src_to_dst
        if len(copy_elev.time) > 1:
            copy_elev.time.pop(src_inserted)
            copy_elev.time.pop(dst_inserted - 1)
        for j in range(len(copy_elev.time)):
            time_diff += copy_elev.time[j] - i.time[j]
        if time_diff < min_time:
            min_time = time_diff
            min_elev = copy_elev._id
    best_elev = building.elev[min_elev]  # getting the best elevator
    src_inserted = add_to_elev(best_elev, src, time_of_call)
    estimated_time_src_to_dst = time_of_call + best_elev._startTime + best_elev._closeTime + best_elev._stopTime + best_elev._openTime + abs(
        src - dst) / best_elev.speed
    add_to_elev(best_elev, dst, estimated_time_src_to_dst)  # add to elev dst
    best_elev.time
    return min_elev
