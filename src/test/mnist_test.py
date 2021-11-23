import unittest
import sys, os
direction = sys.path.insert(0, os.path.join(os.path.dirname(__file__), '../..'))
from MNIST_data import mnist
#mnist.test_imported()

class TestMnist(unittest.TestCase):
    def test_train_img_data_num_train(self):
        self.dataset=mnist._load_img("train-images-idx3-ubyte.gz")
        self.assertEqual(len(self.dataset), 60000)

    def test_train_img_data_num_test(self):
        self.dataset=mnist._load_img("t10k-images-idx3-ubyte.gz")
        self.assertEqual(len(self.dataset), 10000)

    