import unittest
import numpy as np
from dlbfsa import FinancialSentimentAnalysis

class TestDLBFSA(unittest.TestCase):
    def setUp(self):
        self.texts = np.random.randint(10000, size=(1000, 100))
        self.labels = np.random.randint(2, size=(1000, 1))
        self.dlbfsa = FinancialSentimentAnalysis()

    def test_train_model(self):
        self.dlbfsa.train_model(self.texts, self.labels)
        self.assertIsNotNone(self.dlbfsa.model)

    def test_predict_sentiment(self):
        self.dlbfsa.train_model(self.texts, self.labels)
        predictions = self.dlbfsa.predict_sentiment(self.texts[:5])
        self.assertEqual(len(predictions), 5)

if __name__ == '__main__':
    unittest.main()
