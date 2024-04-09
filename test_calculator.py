import unittest
from calculator import calculate_floor


class Test(unittest.TestCase):

	def test_calculate_floor(self):
		self.assertEqual(calculate_floor('UUDU'),2)

	def test_calculate_floor1(self):
		self.assertEqual(calculate_floor('DDDD'),-4)

if __name__ == '__main__':
    	unittest.main()
	