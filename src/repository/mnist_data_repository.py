import mnist
class MnistRepository():
    """Class for loading MNIST data
    """
    def __init__(self, grayScale) -> None:
        self.__label = mnist._load_label_pkl()
        self.__images = mnist.load_img_boolean(grayScale)
        self.__images_location = mnist.load_img_boolean_index(grayScale)

    def get_test_label(self):
        return self.__label["test_label"]

    def get_train_label(self):
        return self.__label["train_label"]

    def get_test_image(self):
        return self.__images["test_img"]

    def get_test_image_location(self):
        return self.__images_location["test_img"]

    def get_train_image(self):
        return self.__images["train_img"]
        
    def get_train_image_location(self):
        return self.__images_location["train_img"]
    

    
mnist_data_repository = MnistRepository(73)
# label = mnist_data.get_test_label()[1]
# print(label)
# image = mnist_data.get_test_image()[1]
# for i in image:
    
#     print(i)
