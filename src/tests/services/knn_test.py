import unittest
from math import sqrt
from services.knn import knn
# mnist.test_imported()


class TestKnn(unittest.TestCase):
    def setUp(self):
        self.knn = knn

    def test_get_dist_right(self):
        Ay, Ax, By, Bx = 0, 2, 2, 0
        dist = sqrt(pow(Ay - By, 2) + pow(Ax - Bx, 2))
        dist_from_knn = self.knn._get_dist(Ay, Ax, By, Bx)
        self.assertEqual(dist, dist_from_knn)
    
    def test_from_point_to_set_dist_returns_correct_distance(self):
        fake_2D = [
            [0, 0, 0],
            [0, 0, 0],
            [0, 0, 1],
        ]
        dist1 = knn._from_point_to_set_dist([0,0],fake_2D)
        dist2 = knn._from_point_to_set_dist([1,0],fake_2D)
        dist3 = knn._from_point_to_set_dist([2,2],fake_2D)
        self.assertEqual(dist1, sqrt(8))
        self.assertEqual(dist2, sqrt(5))
        self.assertEqual(dist3, 0.0)
    
    def test_from_point_to_set_dist_returns_correct_type(self):
        fake_2D = [
            [0, 0, 0],
            [0, 1, 0],
            [0, 0, 0],
        ]
        dist1 = knn._from_point_to_set_dist([0,0],fake_2D)
        self.assertEqual(type(dist1), float)

    def test_percentage(self):
        percentage = knn.percentage(5,100)
        self.assertTrue(0.0<=percentage)
        self.assertTrue(percentage<=1)
