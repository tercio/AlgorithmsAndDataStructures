import unittest
import conversion as conv

class TestConversion(unittest.TestCase):

    def testStrToInt(self):
        self.assertEqual(conv.StrToInt('324'),324)
        self.assertEqual(conv.StrToInt('-123'),-123)
        self.assertEqual(conv.StrToInt('-1'),-1)
        self.assertEqual(conv.StrToInt('0'),0)
        self.assertEqual(conv.StrToInt('1'),1)

if __name__ == "__main__":

    unittest.main()
