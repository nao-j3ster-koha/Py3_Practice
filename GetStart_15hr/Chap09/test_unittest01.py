import unittest

class   TestSample(unittest.TestCase):

    def setup(self):
        print('setup')

    def testEasyCalc(self):
        self.assertEqual(4, 2 * 2, '計算が間違っています')

    def testEasycalcFail(self):
        self.assertEqual(12, 4 * 3,'計算が間違っています')

    def tearDown(self):
        print('tearDown')

