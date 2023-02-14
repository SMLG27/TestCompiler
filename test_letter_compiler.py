import unittest
from main import LetterCompiler

class TestCompiler(unittest.TestCase):

    def test_basic(self):
        testcase = "The best preparation for tomorrow is doing your best today."
        expected = ['b', 'a', 'a', 'b', 'a']
        self.assertEqual(LetterCompiler(testcase), expected)

class TestCompiler2(unittest.TestCase):

    def test_two(self):
        testcase = "A b c d e f g h i j k l m n o q r s t u v w x y z"
        expected = ['b', 'c']
        self.assertEqual(LetterCompiler(testcase), expected)

    def test_tree(self):
        testcase = ""
        expected = []
        self.assertEqual(LetterCompiler(testcase), expected)

    def test_for(self):
        testcase = "1,2,3,4,5"
        expected = []
        self.assertEqual(LetterCompiler(testcase), expected)

    def test_five(self):
        testcase = "A b. ---{c. d e f g<<<<<<7 h i j k l m n o q r s t u v w x y z"
        expected = ['b', 'c']
        self.assertEqual(LetterCompiler(testcase), expected)

    def test_six(self):
        testcase = "A     b        c     d e f g<<<<<<7 h i j k l m n o q r s t u v w x y z"
        expected = ['b', 'c']
        self.assertEqual(LetterCompiler(testcase), expected)

    def test_seven(self):
        testcase = 123
        expected = []
        self.assertEqual(LetterCompiler(testcase), expected)

    def test_eight(self):
        testcase = True
        expected = []
        self.assertEqual(LetterCompiler(testcase), expected)

    def test_nine(self):
        testcase = None
        expected = []
        self.assertEqual(LetterCompiler(testcase), expected)


if __name__ == '__main__':
    # EDGE CASES HERE
    unittest.main(argv=['first-arg-is-ignored'], exit=False)