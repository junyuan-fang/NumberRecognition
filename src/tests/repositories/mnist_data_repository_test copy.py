import unittest
from repositories.mnist_data_repository import mnist_data_repository
# mnist.test_imported()


class TestMnistDataRepo(unittest.TestCase):
    def setUp(self) -> None:
        self.data_repo = mnist_data_repository

    def test_get_testing_label(self):
        labels = self.data_repo.get_test_label()
        self.assertEqual(len(labels), 10_000)
