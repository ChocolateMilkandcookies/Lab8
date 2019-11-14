import unittest #testing constuctor of Lab5
import Lab5 as prog
class TestMiProgram(unittest.TestCase):
    def test_EngineType(self):
        vios = prog.Vehicle(4,"petrol",5,200)
        self.assertEqual(vios.t, "petrol")
        self.assertEqual(vios.sp, "speed")
        self.assertEqual(vios.s, "seat")
        self.assertEqual(vios.w, "wheels")

if __name__ == "__main__":
    unittest.main()