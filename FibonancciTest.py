import unittest, problem_4

class FibonancciTest(unittest.TestCase):
	def testPositiveFibonancci(self):
		self.assertEqual(problem_4.generateSeries(5), [0,1,1,2,3,5], msg="fibonancci should return [0,1,1,2,3,5]")

	def testPositiveFibonancciTen(self):
		self.assertEqual(problem_4.generateSeries(10), [0,1,1,2,3,5,8,13,21,34,55], msg="fibonancci should return [0,1,1,2,3,5,8,13,21,34,55]")

	def testNegativeFibonancci(self):
		self.assertEqual(problem_4.generateSeries(-9), -1, msg="Fibonancci should return false for a negative number")

	def testDecimalInput(self):
		self.assertEqual(problem_4.generateSeries(4.25), -1, msg="Fibonancci should return false for a decimal")

	def testAlphabeticalInput(self):
		self.assertEqual(problem_4.generateSeries('etuyuh'), -1, msg="Fibonancci should return false for a alphabetical letters")

		'''This section handles the test for the Function generateSeriesSum'''
	def testPositiveFibonancciSum(self):
		self.assertEqual(problem_4.generateSeriesSum(5,None), 12, msg="fibonancci should return 12")	
	
	def testNegativeFibonancciSum(self):
		self.assertEqual(problem_4.generateSeriesSum(-9), -1, msg="Fibonancci should return false for a negative number")

	def testDecimalInputSum(self):
		self.assertEqual(problem_4.generateSeriesSum(4.25), -1, msg="Fibonancci should return false for a decimal")

	def testAlphabeticalInputSum(self):
		self.assertEqual(problem_4.generateSeriesSum('etuyuh'), -1, msg="Fibonancci should return false for a alphabetical letters")
	

if __name__ == '__main__':
	unittest.main()