import unittest
class TestMiProgram(unittest.TestCase):
    def test_upper(self):
        self.assertEqual("food".upper(),"FOOD")
    def test_isupper(self):
        self.assertTrue("FOOD".isupper())
        self.assertFalse("Food".isupper())

if __name__ is "__main__":
    unittest.main()