import unittest
from part1 import count_diffs

class TestPart1(unittest.TestCase):
    def test1(self):
        numbers = [16,10,15,5,1,11,7,19,6,12,4]
        result = count_diffs(numbers)
        self.assertTupleEqual((7, 5), result)

    def test2(self):
        numbers = [28,33,18,42,31,14,46,20,48,47,24,23,49,45,19,38,39,11,1,32,25,35,8,17,7,9,4,2,34,10,3]
        result = count_diffs(numbers)
        self.assertTupleEqual((22, 10), result)