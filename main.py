# This is a sample Python script.

# Press Shift+F10 to execute it or replace it with your code.
# Press Double Shift to search everywhere for classes, files, tool windows, actions, and settings.
import json as js

with open('D:\\B5.json', 'r') as f:
    data = f.read()

# parse file
obj = js.loads(data)
print("MIN FLOOR", str(obj['_minFloor']))
print("MAX FLOOR", str(obj['_maxFloor']))
list = obj['_elevators']
list_size = len(list)
for i in range(list_size):
    print("ID:", list[i].get("_id"))
    print("SPEED:", list[i].get("_speed"))
    print("MIN FLOOR", list[i].get("_minFloor"))
    print("MAX FLOOR", list[i].get("_maxFloor"))
    print("CLOSE TIME", list[i].get("_closeTime"))
    print("OPEN TIME", list[i].get("_openTime"))
    print("START TIME", list[i].get("_startTime"))
    print("STOP TIME", list[i].get("_stopTime"))


def print_hi(name):
    # Use a breakpoint in the code line below to debug your script.
    print(f'Hi, {name}')  # Press Ctrl+F8 to toggle the breakpoint.


# Press the green button in the gutter to run the script.
if __name__ == '__main__':
    print_hi('PyCharm')

# See PyCharm help at https://www.jetbrains.com/help/pycharm/
