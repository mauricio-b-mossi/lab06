import unittest
import passwordtransformer as pt
import scrap as sc

class LabTests(unittest.TestCase):

    def test_encoder(self):
       self.assertEqual(sc.encoder("12345555", 3), ("45678888", True))

if __name__ == '__main__':
    unittest.main()
