import unittest

#from LSTM import *
from Pred import *


#test esetek
#1 egyes osztalyok konstruktorat ellenorzid failel.
# predict kepes / nem kepes feldolgozni bementeket
# meretekkel valo ellenorzesek
class TestingSum(unittest.TestCase):


    def test_sum(self):
        self.assertEqual(sum([2, 3, 5]), 10, "It should be 10")

    @unittest.expectedFailure
    def test_LSTM(self):
        try:
            qwe = LSTM(200000000000000000000000000000,4,12)
        except Exception as error:
            self.fail()

    def test2_LSTM(self):
        try:
            qwe = LSTM(2,4,12)
        except Exception as error:
            self.fail()

    def test3_Pred(self):
        try:
            test = Predictor()
        except Exception as error:
            self.fail('test3')



if __name__ == '__main__':
    unittest.main()