import unittest
def cuboid_volume(l):
    return(l*l*l)
class Test_Cuboid(unittest.TestCase):

    def test_volume(self):
        self.assertAlmostEqual(cuboid_volume(2),8)
        self.assertAlmostEqual(cuboid_volume(3),27)
        self.assertAlmostEqual(cuboid_volume(4),64)
unittest.main()

