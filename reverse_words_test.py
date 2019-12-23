import unittest
import reverse_words as rw

class ReverWordsTest(unittest.TestCase):

    def testReverWord(self):
        self.assertEqual(rw.reverse_words("teste de python"),"python de teste")


if __name__ == "__main__":

    unittest.main()
