class Building:
    def __init__(self , _minFloor: int, _maxFloor : int, _elevators : list):
        self._minFloor = _minFloor
        self._maxFloor = _maxFloor
        self._elevators = _elevators
    def __str__(self):
        str = "Min floor is:  " + self._minFloor + "\n" +"Max floor is:  " + self._maxFloor + "\n" +"The elevators are:  " +self._elevators.__str__()
        return str

    def NumbersOfElevators(elevators : list):
        count = 0
        for i in elevators:
            count=count+1
        return count

