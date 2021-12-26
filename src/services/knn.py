from repositories.mnist import GRAYSCALE
from repositories.mnist_data_repository import mnist_data_repository as data_repo
from math import sqrt
from heapq import _heapify_max
import random


class Knn:
    """
    Attributes:
        _test_label: testing image labels
        _train_label: training image labels
        _test_img: testing image data, 2d matrix with values 0 or 1
        _test_img_location: testing image data, 1d list with values 0-27 coordinates
        _train_img: trainning image data, 2d matrix with values 0 or 1
        _train_img_location: trainning image data, 1d list with values 0-27 coordinates
    """

    def __init__(self):
        """KNN constructor"""

        self._test_label, self._train_label, self._test_img, self._train_img, self._test_img_location, self._train_img_location = data_repo.get_all()
        self.percent = 100.0

    def recognition(self, k=3, input_img_index=0, train_range=200, method="D22", img=None):
        """Classifier, with method D22 and D23. We assume that 0-9 data's appearance are equal
            Nomal condition: 

        Args:
            k (int, optional): [description]. Defaults to 3.
            input_img_index (int, optional): [description]. Defaults to 0.
            train_range (int, optional): Because this method takes a lot of time for trainning. Defaults to 200.
            method (str, optional): [description]. Defaults to "D22".

        Returns:
            result (int) : 0-9 number 
        """
        # Training set are same
        imagesB_location, imagesB = self._get_dataB_normal(
            train_range)  # self._get_dataB_random(train_range)
        # test set
        imageA_location = []
        imageA = [[0 for _ in range(28)] for _ in range(28)]

        if input_img_index < 0:  # img from the mouse
            for y in range(len(img)):
                for x in range(len(img[0])):
                    if img[y][x][0] > GRAYSCALE:
                        imageA_location.append((y, x))
                        imageA[y][x] = 1

        else:
            imageA_location = self._test_img_location[input_img_index]
            imageA = self._test_img[input_img_index]

        heap_k = []
        # go through the tainning set
        for index in range(train_range):
            if method == "D22":
                dist = self._D_22(imageA_location, imageA,
                                  imagesB_location[index], imagesB[index])
            if method == "D23":
                dist = self._D_23(imageA_location, imageA,
                                  imagesB_location[index], imagesB[index])
            if len(heap_k) < k:
                # add tuple (dist,label)
                label = self._train_label[index]
                heap_k.append((dist, label))
                _heapify_max(heap_k)
            # not < k and dist is smaller
            else:
                heap_k_max_dist = heap_k[0][0]
                if dist < heap_k_max_dist:
                    label = self._train_label[index]
                    heap_k[0] = (dist, label)
                    _heapify_max(heap_k)

        # get the reseult
        #print (self.get_result(heap_k))
        return self.get_result(heap_k)

    def percentage(self,  testing_range=200, trainning_range=1000, k=3, method="D22"):
        """return a float num with percentage%

        Args:
            test_range (int, optional): [description]. Defaults to 200.
            trainning_range (int, optional): [description]. Defaults to 1000.
        """
        imagesB_location, imagesB = self._get_dataB_normal(
            trainning_range)  # self._get_dataB_random(train_range)
        # test set
        #imagesA_location, imagesA = self._get_dataA_normal(testing_range)

        correct_times = 0.0
        for indexA in range(testing_range):
            # imagesA_location[indexA]#
            imageA_location = self._test_img_location[indexA]
            imageA = self._test_img[indexA]  # imagesA[indexA]#
            heap_k = []
            # go through the tainning set
            for indexB in range(trainning_range):
                if method == "D22":
                    dist = self._D_22(imageA_location, imageA,
                                      imagesB_location[indexB], imagesB[indexB])
                if method == "D23":
                    dist = self._D_23(imageA_location, imageA,
                                      imagesB_location[indexB], imagesB[indexB])
                if len(heap_k) < k:
                    # add tuple (dist,label)
                    label = self._train_label[indexB]
                    heap_k.append((dist, label))
                    _heapify_max(heap_k)
                # not < k and dist is smaller
                else:
                    heap_k_max_dist = heap_k[0][0]
                    if dist < heap_k_max_dist:
                        label = self._train_label[indexB]
                        heap_k[0] = (dist, label)
                        _heapify_max(heap_k)

            if self.get_result(heap_k) == self.get_label(indexA):
                correct_times += 1

        return correct_times/testing_range

    def get_result(self, heap_k): 
        """return the most frequence number in the list
           what if frequences are same
        Args:
            heap_k (tuple list(dist, label)): max heap, according to the dist

        Returns:
            label (int 0-9): most frequence number 
        """
        results = []
        for item in heap_k:
            results.append(item[1])
        return max(set(results), key=results.count)

    def _get_dataB_normal(self, train_range):
        """ 0 - train_range-1 index's data from the trainning list 
        Args:
            train_range (int): <=60000
        Returns:
            imageB: trainning image data, 1d list with values 0-27 coordinates, size = train_range
        """

        return self._train_img_location[:train_range], self._train_img[:train_range]

    def _get_dataA_normal(self, test_range):
        """ 0 - test_range-1 index's data from the testing list 
        Args:
            test_range (int): <=60000
        Returns:
            imageB: testing image data, 1d list with values 0-27 coordinates, size = train_range
        """

        return self._test_img_location[:test_range], self._test_img[:test_range]

    # def _get_dataB_random(self, train_range):
    #     """ Data from the trainning list. Selecting data randomly
    #     Args:
    #         train_range (int): <=60000
    #     Returns:
    #         imageB: trainning image data, 1d list with values 0-27 coordinates, size = train_range
    #     """

    #     return random.sample(self._train_img_location, train_range), random.sample(self._train_img, train_range)

    def _D_22(self, imageA_location: list, imageA, imageB_location: list, imageB):
        """Distance measure D22 from
        https://citeseerx.ist.psu.edu/viewdoc/download;jsessionid=6F7642FDC63869C9A005AB4B14ED484E?doi=10.1.1.1.8155&rep=rep1&type=pdf

        Args:
            imageA_location : 1d list with values 0-27 coordinates
            imageA : 2d matrix with values 0 or 1
            imageB_location : 1d list with values 0-27 coordinates
            imageB : 2d matrix with values 0 or 1

        Returns:
            float: distance between two images
        """
        ### f_2 = max(d(A, B), d(B, A))
        return max(self._d_6(imageA_location, imageB), self._d_6(imageB_location, imageA))

    def _d_6(self, imageA_location: list, imageB):
        """Distance between two datasets A and B. Directed distance measure d6 from
        https://citeseerx.ist.psu.edu/viewdoc/download;jsessionid=6F7642FDC63869C9A005AB4B14ED484E?doi=10.1.1.1.8155&rep=rep1&type=pdf

        Args:
            imageA_location : 1d list with values 0-27 coordinates
            imageB : 2d matrix with values 0 or 1

        Returns:
            float: distance between two datasets
        """
        # d_6 = 1/N_a * ∑(a ∈ A) d(a, B) = ∑(a ∈ A) d(a, B)/N_a
        N_a = len(imageA_location)
        dist = 0.0
        for point in imageA_location:
            dist += self._from_point_to_set_dist(point, imageB)
        return dist/N_a

    def _D_23(self, imageA_location: list, imageA, imageB_location: list, imageB):
        """Distance measure D23 from
        https://citeseerx.ist.psu.edu/viewdoc/download;jsessionid=6F7642FDC63869C9A005AB4B14ED484E?doi=10.1.1.1.8155&rep=rep1&type=pdf

        Args:
            imageA_location : 1d list with values 0-27 coordinates
            imageA : 2d matrix with values 0 or 1
            imageB_location : 1d list with values 0-27 coordinates
            imageB : 2d matrix with values 0 or 1

        Returns:
            float: distance between two images
        """
        ### f_2 = max(d(A, B), d(B, A))
        return max(self._d_5(imageA_location, imageB), self._d_5(imageB_location, imageA))

    def _d_5(self, imageA_location: list, imageB):
        """Distance between two datasets A and B. Directed distance measure d5 from
        https://citeseerx.ist.psu.edu/viewdoc/download;jsessionid=6F7642FDC63869C9A005AB4B14ED484E?doi=10.1.1.1.8155&rep=rep1&type=pdf

        Args:
            imageA_location : 1d list with values 0-27 coordinates
            imageB : 2d matrix with values 0 or 1

        Returns:
            float: distance between two datasets
        """
        # d_5 = max (a ∈ A) d(a, B)
        dist = 0.0
        for point in imageA_location:
            dist = max(dist, self._from_point_to_set_dist(point, imageB))
        return dist

    def _from_point_to_set_dist(self, point: list, B):
        """calculatiing the shortest dist, d(a, B)

        Args:
            point (list): [y,x]
            imageB : 2d matrix with values 0 or 1, index are 0-27

        Returns:
            dist : shortest dist
        """
        size_B = len(B)
        visited = [[False for j in range(size_B)] for i in range(size_B)]
        min_y = point[0]
        max_y = min_y
        min_x = point[1]
        max_x = min_x
        found = False
        dist = sqrt(pow(size_B - 0, 2) + pow(size_B - 0, 2))  # longest is about 39.598
        while not found:
            for row_index in range(min_x, max_x+1):
                # up
                visited[min_y][row_index] = True
                if B[min_y][row_index] == 1:
                    dist = min(dist, self._get_dist(
                        point[0], point[1], min_y, row_index))
                    found = True
                # down
                visited[max_y][row_index] = True
                if B[max_y][row_index] == 1:
                    dist = min(dist, self._get_dist(
                        point[0], point[1], max_y, row_index))
                    found = True

            for colum_index in range(min_y, max_y+1):
                # left
                visited[colum_index][min_x] = True
                if B[colum_index][min_x] == 1:
                    dist = min(dist, self._get_dist(
                        point[0], point[1], colum_index, min_x))
                    found = True
                # right
                visited[colum_index][max_x] = True
                if B[colum_index][max_x] == 1:
                    dist = min(dist, self._get_dist(
                        point[0], point[1], colum_index, max_x))
                    found = True
            if (min_y == 0 and max_y == (size_B-1) and min_x == 0 and max_x == (size_B-1)):
                break
            if not found:
                if min_y > 0:
                    min_y -= 1
                if max_y < (size_B-1):
                    max_y += 1
                if min_x > 0:
                    min_x -= 1
                if max_x < (size_B-1):
                    max_x += 1
        return dist

    def _get_dist(self, Ay, Ax, By, Bx):
        """Euclidean distance

        Args:
            Ay ([type]): [description]
            Ax ([type]): [description]
            By ([type]): [description]
            Bx ([type]): [description]

        Returns:
            dist : Euclidean distance
        """
        return sqrt(pow(Ay - By, 2) + pow(Ax - Bx, 2))

    # for checkling

    def get_label(self, i):#used in test
        return self._test_label[i]

    def get_test_img(self, i):
        return self._test_img[i]


knn = Knn()
# "Start recognition"
# from time import time
# start = time()
# index = 0
# k = 3
# result = knn.recognition(k,index)
# print(time()-start)
# print(result)
# print(knn.get_label(index))
