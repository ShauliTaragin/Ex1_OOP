import json as js


class Elevator:
    def __init__(self, _id, _speed, _minFloor, _maxFloor, _closeTime, _openTime, _startTime, _stopTime):
        self._id = _id
        self._speed = _speed
        self._minFloor = _minFloor
        self._maxFloor = _maxFloor
        self._closeTime = _closeTime
        self._openTime = _openTime
        self._startTime = _startTime
        self._stopTime = _stopTime
        self.time = []
        self.floors = []


        # + self._speed + self._minFloor + self._maxFloor + self._closeTime + self._openTime + self._startTime + self._stopTime

    def add_time(self, t, index: int):
        self.time.insert(index, t)

    def add_floor(self, f, index: int):
        self.time.insert(index, f)


    def to_string(self):
        return "ID: " + self._id.__str__() + "\n" + "Time: " + self.time.__str__() + "\n" + "Floors: " + self.floors.__str__() + "\n" + "Direction: " + self.direction.__str__()

    @property
    def speed(self):
        return self._speed

    @property
    def startTime(self):
        return self._startTime

