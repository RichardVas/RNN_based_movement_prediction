import unittest

#from LSTM import *
from Pred import *
from videoprocessor import *

#test esetek
#1 egyes osztalyok konstruktorat ellenorzid failel.
# predict kepes / nem kepes feldolgozni bementeket
# meretekkel valo ellenorzesek
class TestModules(unittest.TestCase):

    @unittest.expectedFailure
    def test_LSTM_Constructor_fail(self):
        try:
            faulty_lstm = LSTM(200000000000000000000000000000,4,12)
        except Exception as error:
            self.fail()

    def test_LSTM_Constructor(self):
        try:
            good_lstm = LSTM(2,4,12)
        except Exception as error:
            self.fail()

    def test_Pred_Constructor(self):
        try:
            test_pred = Predictor()
        except Exception as error:
            self.fail('Predictor')

    def test_Tracker_Constructor(self):
        try:
            test_track = EuclideanTracker()
        except Exception as error:
            self.fail('Tracker')

    def test_Detector_Constructor(self):
        try:
            test_det = Detector()
        except Exception as error:
            self.fail('Detector')
    



if __name__ == '__main__':
    unittest.main()