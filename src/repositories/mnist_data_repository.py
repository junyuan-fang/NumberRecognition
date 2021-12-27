# pylint: disable=import-error
from repositories import mnist


class MnistRepository():
    """Class for loading MNIST data
    """

    def __init__(self, gray_scale) -> None:
        self.__label = mnist._load_label_pkl()
        self.__images = mnist.load_img_boolean(gray_scale)
        self.__images_location = mnist.load_img_to_y_x_index(gray_scale)

    def get_test_label(self):
        """Return the test label from the label set

        Returns:
            list<int>: 10_000 labels, which value is 0-9
        """
        return self.__label["test_label"]

    def get_train_label(self):
        """Return the train label from the label set

        Returns:
            list<int>: 60_000 labels, which value is 0-9
        """
        return self.__label["train_label"]

    def get_test_image(self):
        """Return the test img from the img set

        Returns:
            list<list<int>>: 10_000 test images, values are 0 or 1, size is 28x28
        """
        return self.__images["test_img"]

    def get_test_image_location(self):
        """Return the test img location from the img_location set

        Returns:
            list<list<int,int>>: 10_000 test image locations, values are 0-27, 0-27
        """
        return self.__images_location["test_img"]

    def get_train_image(self):
        """Return the train img from the img set

        Returns:
            list<list<int>>: 60_000 test images, values are 0 or 1, size is 28x28
        """
        return self.__images["train_img"]

    def get_train_image_location(self):
        """Return the training img location from the img_location set

        Returns:
            list<list<int,int>>: 10_000 training image locations, values are 0-27, 0-27
        """
        return self.__images_location["train_img"]

    def get_all(self):
        """
        Returns:
            self.__label["test_label"]:
            self.__label["train_label"]:
            self.__images["test_img"]:
            self.__images["train_img"]:
            self.__images_location["test_img"]:
            self.__images_location["train_img"]
        """
        return self.__label["test_label"], self.__label["train_label"], \
                self.__images["test_img"], self.__images["train_img"], \
                self.__images_location["test_img"], self.__images_location["train_img"]


mnist_data_repository = MnistRepository(73)

# label = mnist_data_repository.get_train_label()[6]
# print(label)
# image = mnist_data_repository.get_train_image()[6]
# for i in image:

#     print(i)
