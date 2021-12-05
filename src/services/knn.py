from repository.mnist_data_repository import mnist_data_repository as data_repo
from math import sqrt
from heapq import heappop, heappush

class Knn:
    def __init__(self):
        self._test_label, self._train_label, self._test_img, self._train_img, self._test_img_location, self._train_img_location = data_repo.get_all()
        
    def recognition(self, k = 3, input_img_index = 0 , train_range = 150, method = "D22"):
        """[summary]

        Args:
            k ([type]): [description]
            input_img_index ([type]): [description]
            train_range ([type]): [description]
            method (str, optional): [description]. Defaults to "D22".
        Returns:
            retult
        """
        imagesB_location, imagesB = self._get_dataB_normal(train_range)
        imageA_location = self._test_img_location[input_img_index]
        imageA = self._test_img[input_img_index]

        heap = [(40,None) for _ in range(k)]
        for i in range (train_range):
            




    def _get_dataB_normal(self, train_range):
        """ 0 - train_range-1 index's data from the trainning list 
        Args:
            train_range ([type]): [description]
        Returns:
            [type]: [description]
        """
        
        return self._train_img_location[:train_range], self._train_img[:train_range]

    def _D_22(self, imageA_location:list, imageA, imageB_location:list, imageB):
        """Distance measure D22 from
        https://citeseerx.ist.psu.edu/viewdoc/download;jsessionid=6F7642FDC63869C9A005AB4B14ED484E?doi=10.1.1.1.8155&rep=rep1&type=pdf

        Args:
            img1 (int[]): image data
            img2 (int[]): image data

        Returns:
            float: distance between two images
        """
        ### f_2 = max(d(A, B), d(B, A))
        return max( self._d_6(imageA_location, imageB), self._d_6(imageB_location, imageA))


    def _d_6(self, imageA_location:list, imageB):
        """Distance between two datasets A and B. Directed distance measure d6 from
        https://citeseerx.ist.psu.edu/viewdoc/download;jsessionid=6F7642FDC63869C9A005AB4B14ED484E?doi=10.1.1.1.8155&rep=rep1&type=pdf
        
        Args:
            A (int[]): dataset
            B (int[]): dataset

        Returns:
            float: distance between two datasets
        """
        # d_6 = 1/N_a * ∑(a ∈ A) d(a, B) = ∑(a ∈ A) d(a, B)/N_a
        N_a = len(imageA_location)
        dist = 0.0
        for point in imageA_location:
            dist += self._from_point_to_set_dist(point, imageB)
        return dist/N_a
        

    
    def _from_point_to_set_dist(self, point:list, B):
        visited = [[False for j in range(28)] for i in range(28)]
        min_y = point[0]
        max_y = min_y
        min_x = point[1]
        max_x = min_x
        found = False
        dist = 40#longest is about 39.598
        while not found:
            for row_index in range(min_x,max_x+1):
                #up
                visited[min_y][row_index] = True
                if B[min_y][row_index] == 1:
                    dist = min(dist, self._get_dist(point[0], point[1], min_y, row_index))
                    found =True
                #down
                visited[max_y][row_index] = True
                if B[max_y][row_index] == 1:
                    dist = min(dist, self._get_dist(point[0], point[1], max_y, row_index))
                    found =True

            for colum_index in range(min_y, max_y+1):
                #left 
                visited[colum_index][min_x] = True
                if B[colum_index][min_x] == 1:
                    dist = min(dist, self._get_dist(point[0], point[1], colum_index, min_x))
                    found =True
                #right
                visited[colum_index][max_x] = True
                if B[colum_index][max_x] == 1:
                    dist = min(dist, self._get_dist(point[0], point[1], colum_index, max_x))
                    found =True
            if (min_y == 0 and max_y == 27 and min_x == 0 and max_x == 27):
                break
            if not found:
                if min_y > 0:
                    min_y -= 1
                if max_y < 27:
                    max_y += 1
                if min_x > 0:
                    min_x -= 1
                if max_x < 27:
                    max_x += 1
        return dist
    
    def _get_dist(self, Ay, Ax, By, Bx):
         return sqrt(pow(Ay - By, 2) + pow(Ax - Bx, 2))




knn = Knn()

