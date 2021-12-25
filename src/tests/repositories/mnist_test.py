import unittest
from repositories.mnist import _load_img
# mnist.test_imported()


class TestMnist(unittest.TestCase):
    def test_train_img_data_num_train(self):
        self.dataset = _load_img("train-images-idx3-ubyte.gz")
        self.assertEqual(len(self.dataset), 60000)

    def test_train_img_data_num_test(self):
        self.dataset = _load_img("t10k-images-idx3-ubyte.gz")
        self.assertEqual(len(self.dataset), 10000)
