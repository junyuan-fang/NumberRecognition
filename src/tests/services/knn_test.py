import unittest
from math import sqrt
from services.knn import knn
# mnist.test_imported()


class TestKnn(unittest.TestCase):
    def setUp(self) -> None:
        self.knn = knn

    def test_get_dist_right(self):
        Ay, Ax, By, Bx = 0, 2, 2, 0
        dist = sqrt(pow(Ay - By, 2) + pow(Ax - Bx, 2))
        dist_from_knn = self.knn._get_dist(Ay, Ax, By, Bx)
        self.assertEqual(dist, dist_from_knn)
