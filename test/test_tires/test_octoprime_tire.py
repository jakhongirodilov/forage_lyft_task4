import unittest
from tire.octoprime_tire import OctoprimeTire

class TestOctoprimeTire(unittest.TestCase):
    def test_needs_service_true(self):
        tires_condition = [0.7, 0.8, 0.9, 0.9]
        tire = OctoprimeTire(tires_condition)
        self.assertTrue(tire.needs_service())

    def test_needs_service_false(self):
        tires_condition = [0.4, 0.5, 0.2, 0.7]
        tire = OctoprimeTire(tires_condition)
        self.assertFalse(tire.needs_service())


if __name__ == "__main__":
    unittest.main()