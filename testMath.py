import unittest
from mathA import Operation

class testMath(unittest.TestCase):

    def test_minus(self):
        result = Operation.difference(492933, 175280)
        self.assertEqual(result, 317653)
        pass