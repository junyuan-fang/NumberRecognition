from repository import mnist
import time
class MnistRepository():
    """Class for loading MNIST data
    """
    def __init__(self, grayScale) -> None:
        self.__label = mnist._load_label_pkl()
        self.__images = mnist.load_img_boolean(grayScale)
        self.__images_location = mnist.load_img_to_y_x_index(grayScale)

    def get_test_label(self):
        """ 
        Returns:
            int[]: 0-9
        """
        return self.__label["test_label"]

    def get_train_label(self):
        """ 
        Returns:
            [int]: 0-9
        """
        return self.__label["train_label"]

    def get_test_image(self):
        """
        Returns:
            [ [[int]] ]: test image, values are 0 or 1
        """
        return self.__images["test_img"]

    def get_test_image_location(self):
        """
        Returns:
            [ [int,int] ]: test image, values are 0-27
        """
        return self.__images_location["test_img"]

    def get_train_image(self):
        """
        Returns:
            [ [[int]] ]: test image, values are 0 or 1
        """
        return self.__images["train_img"]
        
    def get_train_image_location(self):
        """ 
        Returns:
            self.__images_location["train_img"]: tarin image, values are 0-27
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
        return self.__label["test_label"], self.__label["train_label"], self.__images["test_img"], self.__images["train_img"], self.__images_location["test_img"], self.__images_location["train_img"]

    
mnist_data_repository = MnistRepository(73)

# label = mnist_data_repository.get_train_label()[6]
# print(label)
# image = mnist_data_repository.get_train_image()[6]
# for i in image:
    
#     print(i)
