import unittest
import repositories.mnist as mnist
import os
import pathlib as pl
# mnist.test_imported()
dataset_dir = "./src/MNIST_data"
save_file_label = dataset_dir + "/label.pkl"
save_file_img = dataset_dir + "/test_img_bit.pkl"
save_file_img_boolean = dataset_dir + "/img_boolean.pkl"
save_file_img_boolean_index = dataset_dir + "/img_boolean_index.pkl"

class TestCaseBase(unittest.TestCase):
    def assertIsFile(self, path):
        if not pl.Path(path).resolve().is_file():
            raise AssertionError("File does not exist: %s" % str(path))

class TestMnist(TestCaseBase):#class TestCaseBase(unittest.TestCase):        
    def assertIsFile(self, path):
        if not pl.Path(path).resolve().is_file():
            raise AssertionError("File does not exist: %s" % str(path))
    def test_load_train_img(self):
        self.dataset = mnist._load_img("train-images-idx3-ubyte.gz")
        self.assertEqual(len(self.dataset), 60_000)

    def test_load_test_img(self):
        self.dataset = mnist._load_img("t10k-images-idx3-ubyte.gz")
        self.assertEqual(len(self.dataset), 10_000)

    def test_load_train_label(self):
        self.dataset = mnist._load_label("train-labels-idx1-ubyte.gz")
        self.assertEqual(len(self.dataset), 60_000)

    def test_load_test_label(self):
        self.dataset = mnist._load_label("t10k-labels-idx1-ubyte.gz")
        self.assertEqual(len(self.dataset), 10_000)


    def test_no_label_pickle_file_initialization_succes(self):
        if os.path.exists("./src/MNIST_data/label.pkl"):
            os.remove("./src/MNIST_data/label.pkl")
        mnist._load_label_pkl()
        path = pl.Path("./src/MNIST_data/label.pkl")
        self.assertIsFile(path)

    def test_is_label_file_loading_succes(self):
        self.dataset = mnist._load_label_pkl()
        self.assertEqual(len(self.dataset['train_label']), 60_000)
        self.assertEqual(len(self.dataset['test_label']), 10_000)


    #test image for gui with different form
    def test_no_test_image_pickle_file_initialization_succes(self):
        if os.path.exists("./src/MNIST_data/test_img_bit.pkl"):
            os.remove("./src/MNIST_data/test_img_bit.pkl")
        mnist.load_test_img()
        path = pl.Path("./src/MNIST_data/test_img_bit.pkl")
        self.assertIsFile(path)
    
    def test_no_test_image_pickle_file_loading_succes(self):
        if os.path.exists("./src/MNIST_data/test_img_bit.pkl"):
            os.remove("./src/MNIST_data/test_img_bit.pkl")
        self.dataset = mnist.load_test_img()
        self.assertEqual(len(self.dataset), 10_000)

    def test_is_test_image_file_loading_succes(self):
        self.dataset = mnist.load_test_img()
        self.assertEqual(len(self.dataset), 10_000)


    def test_no_image_boolean_pickle_file_initialization_succes(self):
        if os.path.exists("./src/MNIST_data/img_boolean.pkl"):
            os.remove("./src/MNIST_data/img_boolean.pkl")
        mnist.load_img_boolean()
        path = pl.Path("./src/MNIST_data/img_boolean.pkl")
        self.assertIsFile(path)

    def test_is_image_boolean_file_loading_succes(self):
        self.dataset = mnist.load_img_boolean()
        self.assertEqual(len(self.dataset['train_img']), 60_000)
        self.assertEqual(len(self.dataset['test_img']), 10_000)

    
    def test_no_image_boolean_index_pickle_file_initialization_succes(self):
        if os.path.exists("./src/MNIST_data/img_boolean_index.pkl"):
            os.remove("./src/MNIST_data/img_boolean_index.pkl")
        mnist.load_img_to_y_x_index()
        path = pl.Path("./src/MNIST_data/img_boolean_index.pkl")
        self.assertIsFile(path)

    def test_is_image_boolean_index_file_loading_succes(self):
        self.dataset = mnist.load_img_to_y_x_index()
        self.assertEqual(len(self.dataset['train_img']), 60_000)
        self.assertEqual(len(self.dataset['test_img']), 10_000)
    
    
