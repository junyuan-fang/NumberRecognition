import unittest
from repositories.mnist_data_repository import mnist_data_repository
# mnist.test_imported()


class TestMnistDataRepo(unittest.TestCase):
    def setUp(self) -> None:
        self.data_repo = mnist_data_repository
    
    def test_get_training_label(self):
        labels = self.data_repo.get_train_label()
        self.assertEqual(len(labels), 60_000)

    def test_get_training_img(self):
        img = self.data_repo.get_train_image()
        self.assertEqual(len(img), 60_000)

    def test_get_train_image_location(self):
        img = self.data_repo.get_train_image_location()
        self.assertEqual(len(img), 60_000)

    def test_get_testing_label(self):
        labels = self.data_repo.get_test_label()
        self.assertEqual(len(labels), 10_000)
    
    def test_get_test_img(self):
        img = self.data_repo.get_test_image()
        self.assertEqual(len(img), 10_000)

    def test_get_test_image_location(self):
        img = self.data_repo.get_test_image_location()
        self.assertEqual(len(img), 10_000)
    
    def test_get_all(self):
        test_label, train_label, test_images, train_images, test_images_location, train_images_location = self.data_repo.get_all()
        self.assertEqual(len(train_label), 60_000)
        self.assertEqual(len(train_images), 60_000)
        self.assertEqual(len(train_images_location), 60_000)
        self.assertEqual(len(test_label), 10_000)
        self.assertEqual(len(test_images), 10_000)
        self.assertEqual(len(test_images_location), 10_000)
