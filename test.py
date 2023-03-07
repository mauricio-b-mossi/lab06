import unittest
import passwordtransformer as pt
import scrap as sc

class LabTests(unittest.TestCase):

    def test_encode(self):
       self.assertEqual(sc.encode("12345555", 3), ("45678888", True))
       self.assertEqual(sc.encode("00009962", 3), ("33332295", True))
       self.assertEqual(sc.encode("this shall not pass", 3), ("", False))
       self.assertEqual(sc.encode("neither", 3), ("", False))

    def test_decode(self):
        self.assertEqual(sc.decode())

if __name__ == '__main__':
    unittest.main()
