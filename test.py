import unittest
import password as pw

class LabTests(unittest.TestCase):

    def test_encode(self):
       self.assertEqual(pw.encode("12345555", 3), ("45678888", True))
       self.assertEqual(pw.encode("00009962", 3), ("33332295", True))
       self.assertEqual(pw.encode("this shall not pass", 3), ("", False))
       self.assertEqual(pw.encode("neither", 3), ("", False))

    def test_decode(self):
        self.assertEqual(pw.decode("45678888", 3), ("12345555", True))
        self.assertEqual(pw.decode("33332295", 3), ("00009962", True))
        self.assertEqual(pw.decode("11111111", 3), ("88888888", True))
        self.assertEqual(pw.decode("00000000", 3), ("77777777", True))
        self.assertEqual(pw.decode("this shall not pass", 3), ("", False))
        self.assertEqual(pw.decode("neither", 3), ("", False))

if __name__ == '__main__':
    unittest.main()
