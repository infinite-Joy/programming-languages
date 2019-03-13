import unittest

from code1 import get_data

class TestCode1(unittest.TestCase):

	def test_get_data(self):
		res = dict(get_data())
		self.assertEqual(res['sector'], {'item': 'Water and Sanitation'})


if __name__ == '__main__':
	unittest.main()