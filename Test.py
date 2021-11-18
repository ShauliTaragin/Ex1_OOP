import unittest
from Building import Building
from Calls import Calls

import main


class TestSet(unittest.TestCase):

    def test_reading_csv(self):
        csv = Calls('input/Calls_a.csv')
        self.assertEqual(csv.calls[0], ['Elevator call', '4.37472729', '0', '-1', '0', '-1'])

        csv1 = Calls('input/Calls_b.csv')
        self.assertEqual(csv1.calls[0], ['Elevator call', '15.74901825', '0', '-6', '0', '-1'])

    def test_reading_json(self):
        building0 = Building('input/B5.json')
        self.assertEqual(building0._maxFloor, 100)
        self.assertEqual(building0._minFloor, -10)

        building1 = Building('input/B1.json')
        self.assertEqual(building1.number_of_elevators(), 1)
        self.assertEqual(building0._maxFloor, 100)
        self.assertEqual(building0._minFloor, -10)

        building2 = Building('input/B2.json')
        self.assertEqual(building2.number_of_elevators(), 2)

        building3 = Building('input/B5.json')
        self.assertEqual(building3.number_of_elevators(), 10)

    def test_update_times(self):
        building4 = Building('input/B3.json')
        building4.elev[0].time = [10.9, 20.8, 30.5, 40.2]
        building4.elev[0].floors = [0, 10, 16, 26]
        main.update_times(building4.elev[0], 3)
        self.assertEqual(building4.elev[0].time, [10.9, 20.8, 30.5, 43.833333333333336])

        building1 = Building('input/B5.json')
        building1.elev[0].time = [39.10, 45, 95, 114]
        building1.elev[0].floors = [0, 40, 45, 80]
        main.update_times(building1.elev[0], 3)
        self.assertEqual(building1.elev[0].time, [39.1, 45, 95, 104.44444444444444])

    def test_add_to_elev(self):
        building1 = Building('input/B2.json')
        building1.elev[0].time = [10.9, 20.8, 30.5, 40.2]
        building1.elev[0].floors = [0, 10, 16, 26]
        self.assertEqual(main.add_to_elev(building1.elev[0], 10, 20.8), 4)

        building2 = Building('input/B5.json')
        building2.elev[0].time = [10, 12, 70, 110]
        building2.elev[0].floors = [0, 1, 30, 100]
        self.assertEqual(main.add_to_elev(building2.elev[0], 30, 70), 4)

        building3 = Building('input/B1.json')
        building3.elev[0].time = [5, 9, 11, 33]
        building3.elev[0].floors = [0, 1, 4, 10]
        self.assertEqual(main.add_to_elev(building3.elev[0], 10, 4), 4)
