import json as js

from Elevator import Elevator


class Building:
    def __init__(self, file):
        with open(file, 'r') as f:
            data = js.load(f)
        self._minFloor = data['_minFloor']
        self._maxFloor = data['_maxFloor']
        self.elev = []
        for line in data['_elevators']:
            self.elev.append(Elevator(line['_id'], line['_speed'], line['_minFloor'], line['_maxFloor'], line['_closeTime'],
                                  line['_openTime'], line['_startTime'], line['_stopTime']))
        f.close()

    # def __str__(self):
    #     str = "Min floor is:  " + self._minFloor + "\n" + "Max floor is:  " + self._maxFloor + "\n" + "The elevators are:  " + self._elevators.__str__()
    #     return str

    def number_of_elevators(self):
        count = 0
        for i in self.elev:
            count = count + 1
        return count

    def json_reader(self, file):
        elevs = []
        with open(file, 'r') as f:
            data = js.load(f)
            for line in data['_elevators']:
                elevs.append(Elevator(line['_id'], line['_speed'], line['_minFloor'], line['_maxFloor'], line['_closeTime'], line['_openTime'], line['_startTime'], line['_stopTime']))
            self.elev = elevs
        f.close()
