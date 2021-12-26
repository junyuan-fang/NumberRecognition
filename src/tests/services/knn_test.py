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
        percentage = knn.percentage(10,50,3,"D22")
        self.assertTrue(0.0<=percentage and percentage<=1)
        percentage = knn.percentage(10,50,3,"D23")
        self.assertTrue(0.0<=percentage and percentage<=1)

    def test_get_dataB_normal_range_correct(self):
        range = 10
        dataB = knn._get_dataB_normal(range)
        self.assertEqual(len(dataB[0]),range)
        self.assertEqual(len(dataB[1]),range)
    
    def test_update_nearest_neighbour_correctly_when_heap_is_full(self):
        k = 3
        neighbour1 = (0.9,8)
        neighbour2 = (0.3,2)
        neighbour3 = (0.2,1)
        neighbour4 = (0.4,3)
        maxheap = [neighbour1,neighbour2,neighbour3]
        knn.update_nearest_neighbour(k, maxheap, neighbour4[0], neighbour4[1])
        new_max_dist_label = maxheap[0][1]
        self.assertEqual(new_max_dist_label, neighbour4[1])
        
    def test_update_nearest_neighbour_correctly_when_heap_is_not_full(self):
        k = 3
        neighbour2 = (0.3,2)
        neighbour3 = (0.2,1)
        neighbour4 = (0.4,3)
        maxheap = [neighbour2,neighbour3]
        knn.update_nearest_neighbour(k, maxheap, neighbour4[0], neighbour4[1])
        new_max_dist_label = maxheap[0][1]
        self.assertEqual(new_max_dist_label, neighbour4[1])

    def test_get_result_select_by_min_dist_when_all_neighbors_are_different(self):
        neighbour1 = (0.9,8)
        neighbour2 = (0.3,2)
        neighbour3 = (0.2,1)
        maxheap = [neighbour1,neighbour2,neighbour3]
        result = knn.get_result(maxheap)
        self.assertEqual(result,1)

    def test_get_result_select_by_majority(self):
        neighbour1 = (0.9,8)
        neighbour2 = (0.3,8)
        neighbour3 = (0.2,2)
        maxheap = [neighbour1,neighbour2,neighbour3]
        result = knn.get_result(maxheap)
        self.assertEqual(result,8)

    def test_recognition_returns_int(self):
        result = knn.recognition()
        self.assertNotEqual(type(result),float)
        self.assertNotEqual(type(result),str)
    
    def test_recognition_D22_returns_valid_result(self):
        result = knn.recognition(3,0,1,"D22")
        self.assertTrue(result<=9)
        self.assertTrue(result>=0)

    def test_recognition_D23_returns_valid_result(self):
        result = knn.recognition(3,0,1,"D23")
        self.assertTrue(result<=9)
        self.assertTrue(result>=0)
    
    def test_recognition_from_mouse_painted_with_empty_img(self):
        img = [[ [0, 0, 0, 255] for _ in range(28)] for _ in range(28)]
        result = knn.recognition(3,-1,1,"D23",img)
        print(result)
        self.assertTrue(result<=9)
        self.assertTrue(result>=0)


    def test_get_test_img_method_get_img_with_index_success(self):
        i = 0
        result = knn.get_test_img(i)
        self.assertEqual(len(result),28)
        self.assertEqual(len(result[0]),28)