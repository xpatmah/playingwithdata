import unittest
import pythonTestCode


class PythonTestCode(unittest.TestCase):

    def test_one_word(self):
        text = 'python'
        capitalize_text = pythonTestCode.cap_test(text)
        self.assertEqual(capitalize_text, 'Python')


if __name__ == '__main__':
    unittest.main()
