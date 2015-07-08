import unittest, problem_4

class FibonancciTest(unittest.TestCase):
	def testPositiveFibonancci(self):
		self.assertEqual(problem_4.generateSeries(5), 5, msg="fibonancci should return 5")
	def testNegativeFibonancci(self):
		self.assertEqual(problem_4.generateSeries(-9), -1, msg="Fibonancci should return false for a negative number")
	def testDecimalInput(self):
		self.assertEqual(problem_4.generateSeries(4.25), -1, msg="Fibonancci should return false for a decimal")
	def testAlphabeticalInput(self):
		self.assertEqual(problem_4.generateSeries('etuyuh'), -1, msg="Fibonancci should return false for a alphabetical letters")
	
		
	
'''	def testNegativeFactorial(self):
		self.assertEqual(factorial.factorial(-9), -1, msg="Factorial of a negative number should return false")

	def testAlphaticalInput(self):
		self.assertEqual(factorial.factorial('ieiee'), -1,  msg="Factorial should return false for alphatical input")

	def testDecimalInput(self):
		self.assertEqual(factorial.factorial(2.3453), -1,  msg="Factorial should return false for a decimal number")
'''
if __name__ == '__main__':
	unittest.main()