import unittest
from vector import Vector

class TestVectors(unittest.TestCase):
    def setUp(self):
        self.v1 = Vector(1., -2., -2.)
        self.v2 = Vector(3., -4., 5.)

    def test_magnitude(self):
        self.assertEqual(self.v1.mag(), 3.)

    def test_addition(self):
        sum  = self.v1 + self.v2
        self.assertEqual(getattr(sum,"x"), 4.)

    def test_mul(self):
        prd1 = self.v1 * 2
        prd2 = self.v1 * self.v2
        self.assertEqual(getattr(prd1,"x"), 2.)
        self.assertEqual(getattr(prd2,"x"), 3.)

    def test_div(self):
        div1 = self.v1 / 2
        div2 = self.v2 / self.v1
        self.assertEqual(getattr(div1,"x"), .5)
        self.assertEqual(getattr(div2,"y"),2.)

if __name__ == "__main__":
    unittest.main()