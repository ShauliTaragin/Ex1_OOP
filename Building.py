class Building:
    def __init__(self , _minFloor, _maxFloor , _elevators : list):
        self._minFloor = _minFloor
        self._maxFloor = _maxFloor
        self._elevators = _elevators
    def __str__(self):
        str = "Min floor is:  " + self._minFloor + "\n" +"Max floor is:  " + self._maxFloor + "\n" +"The elevators are:  " +self._elevators.__str__()
        return str;
