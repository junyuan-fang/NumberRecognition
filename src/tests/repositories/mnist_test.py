import unittest
import repositories.mnist as mnist
# mnist.test_imported()


class TestMnist(unittest.TestCase):
    def test_load_train_img(self):
        self.dataset = mnist._load_img("train-images-idx3-ubyte.gz")
        self.assertEqual(len(self.dataset), 60000)

    def test_load_test_img(self):
        self.dataset = mnist._load_img("t10k-images-idx3-ubyte.gz")
        self.assertEqual(len(self.dataset), 10000)

    def test_load_train_label(self):
        self.dataset = mnist._load_label("train-labels-idx1-ubyte.gz")
        self.assertEqual(len(self.dataset), 60000)

    def test_load_test_label(self):
        self.dataset = mnist._load_label("t10k-labels-idx1-ubyte.gz")
        self.assertEqual(len(self.dataset), 10000)
