# pylint: disable=invalid-name
#This file is for loading all mnist and boolean values
import gzip
import pickle
import os
import numpy as np

key_file = {
    'train_img':'train-images-idx3-ubyte.gz',
    'train_label':'train-labels-idx1-ubyte.gz',
    'test_img':'t10k-images-idx3-ubyte.gz',
    'test_label':'t10k-labels-idx1-ubyte.gz'
}
TRAIN_NUM = 60_000
TEST_NUM = 10_000
IMG_SIZE = 28*28 #784
GRAYSCALE = 73

#/home/fjunyuan/Codes/TiraLabra/Recognition_of_handwritten_numbers/src/MNIST_data/
DATASET_DIR = "./src/MNIST_data"
#os.path.abspath(os.path.dirname(os.getcwd()))+"/Recognition_of_handwritten_numbers/src/MNIST_data"
SAVE_LABEL_DIR = DATASET_DIR + "/label.pkl"
SAVE_IMG_DIR = DATASET_DIR + "/test_img_bit.pkl"
SAVE_IMG_BOOLEAN_DIR = DATASET_DIR + "/img_boolean.pkl"
SAVE_IMG_BOOLEAN_INDEX_DIR = DATASET_DIR + "/img_boolean_index.pkl"


def _load_img(file_name):
    """ Read one image .gz file. (Dataset read from MNIST_data folder)
    Args:
        file_name: file format would be .gz
    Returns:
        data: returns data bits, 60000x784 or  10000x784
    """

    file_path = DATASET_DIR + "/" + file_name

    print("Converting " + file_name + " to NumPy Array ...")
    with gzip.open(file_path, 'rb') as file:
        data = np.frombuffer(file.read(), np.uint8, offset=16)#according to the MNIST
    #-1 then we do not need to know the original size. train = 60000x784, test = 10000x784
    data = data.reshape(-1, IMG_SIZE)
    print("Done")

    #print(data.shape)
    return data

def _load_label(file_name):
    """ Read one label .gz file. (Dataset read from MNIST_data folder)
    Args:
        file_name: file format would be .gz
    Returns:
        labels: returns list of labels(1-9)
    """

    file_path = DATASET_DIR + "/" + file_name
    print(file_path)
    print("Converting " + file_name + " to NumPy Array ...")
    with gzip.open(file_path, 'rb') as file:
        labels = np.frombuffer(file.read(), np.uint8, offset=8)#according to the MNIST
    print("Done")

    #print(data.shape)
    return labels
def init_label():
    """ Creating pickle file for label
        Save as {'train_label': ... , 'test_label': ...}
    """

    dataset = {}
    dataset ['train_label'] = _load_label(key_file['train_label'])
    dataset ['test_label'] = _load_label(key_file['test_label'])

    print("Creating pickle file for label...")
    with open(SAVE_LABEL_DIR, 'wb') as file:
        pickle.dump(dataset, file, -1)#for later loading
    print("Done!")

def _load_label_pkl():
    """ If pickle file not exist, create it.
        Read pickle file.
        Returns:
            dataset: returns list(numpy.ndarray) of labels(1-9)
            dataset: {'train_label': __, 'test_label', __ }
    """
    if not os.path.exists(SAVE_LABEL_DIR):
        init_label()

    with open(SAVE_LABEL_DIR, 'rb') as file:
        dataset = pickle.load(file)

    return dataset
#------------------------------------------------------
def init_test_img():
    """ Creating pickle file for test img
        Save as {'train_img': ... , 'test_img': ...}
        for gui not algorithm
    """

    dataset = _load_img(key_file['test_img'])

    print("Creating pickle file for test image...")
    with open(SAVE_IMG_DIR, 'wb') as file:
        pickle.dump(dataset, file, -1)#for later loading
    print("Done!")

def load_test_img():
    """ If pickle file not exist, load .gz, and create pickle file.
        Read pickle file.
        Returns:
            dataset: returns matrix  10000x784 values are 0-255
    """

    if not os.path.exists(SAVE_IMG_DIR):
        init_test_img()

    with open(SAVE_IMG_DIR, 'rb') as file:
        dataset = pickle.load(file)# slow

    return dataset
#------------------------------------------------------
def conver_img_to_boolean(img_set, gray_scale=73):
    """ Go through 60000x28x28 or 10000x28x28
        turn value 0-255 to 0-1
        Arg:
            img_set: 60000x784 or 10000x784
            GRAYSCALE: identify a dark pixel if its value is greater than this
        Returns:
            set: 60000x28x28 or 10000x28x28 with values 0-1


    """
    new_img_set = []
    for img in img_set:
        new_img = img.reshape(28, 28)
        matrix = []
        for row in new_img:
            ele = []
            for index in range(len(row)):
                if row[index]<=gray_scale:
                    ele.append(0)
                else:
                    ele.append(1)
            matrix.append(ele)
        new_img_set.append(matrix)

    return new_img_set

def init_img_boolean(gray_scale=73):
    """ Creating pickle file for img
        Save as {'train_img': ... , 'test_img': ...}
    """

    dataset = {}
    train_img = _load_img(key_file['train_img'])
    test_img = _load_img(key_file['test_img'])

    dataset ['train_img'] = conver_img_to_boolean(train_img,gray_scale)
    dataset ['test_img'] = conver_img_to_boolean(test_img,gray_scale)

    print("Creating pickle file for image(boolean)...")
    with open(SAVE_IMG_BOOLEAN_DIR, 'wb') as file:
        pickle.dump(dataset, file, -1)#for later loading
    print("Done!")

def load_img_boolean(gray_scale=73):
    """ If pickle file not exist, load .gz,
        turn value 0-255 to 0-1 with grayscale and create pickle file.
        Read pickle file.
        Returns:
            dataset: returns matrix 60000x28x28 or 10000x28x28 values are 0-1 depends on grayscale
    """

    if not os.path.exists(SAVE_IMG_BOOLEAN_DIR):
        init_img_boolean(gray_scale)

    with open(SAVE_IMG_BOOLEAN_DIR, 'rb') as file:
        dataset = pickle.load(file)#takes 3s to load, which is slow

    return dataset
#------------------------------------------------------
def conver_img_to_y_x(img_set,gray_scale=73):
    """ Go through 60000x28x28 or 10000x28x28
        find grayscale which are greater than parameter
        append it to the list 60000 x unknow.
        Arg:
            img_set: 60000x784 or 10000x784
            GRAYSCALE: identify a dark pixel if its value is greater than this
        Returns:
            set: dark pixel's locations in list 60000x28x28 [i,j] or 10000x28x28 [i,j]

    """
    new_img_set = []
    for img in img_set:
        new_img = img.reshape(28, 28)
        matrix = []
        for y in range(28):
            for x in range(28):
                if new_img[y][x]>gray_scale:
                    matrix.append((y,x))
        new_img_set.append(matrix)
    return new_img_set

def init_img_to_y_x(gray_scale=73):
    """ Creating pickle file for img
        Save as {'train_img': ... , 'test_img': ...}
    """

    dataset = {}
    train_img = _load_img(key_file['train_img'])
    test_img = _load_img(key_file['test_img'])

    dataset ['train_img'] = conver_img_to_y_x(train_img, gray_scale)
    dataset ['test_img'] = conver_img_to_y_x(test_img, gray_scale)

    print("Creating pickle file for image(index)...")
    with open(SAVE_IMG_BOOLEAN_INDEX_DIR, 'wb') as file:
        pickle.dump(dataset, file, -1)#for later loading
    print("Done!")


def load_img_to_y_x_index(gray_scale=73):
    """ If pickle file not exist, load .gz,
        find location with grayscale and create pickle file.
        Read pickle file.
        Returns:
            dataset: returns matrix 60000x list of [i,j]
                or 10000x list of [i,j] depends on grayscale
    """
    if not os.path.exists(SAVE_IMG_BOOLEAN_INDEX_DIR):
        init_img_to_y_x(gray_scale)

    with open(SAVE_IMG_BOOLEAN_INDEX_DIR, 'rb') as file:
        dataset = pickle.load(file)

    return dataset


if __name__ == '__main__':
    _dataset = _load_label_pkl()
    print(_dataset['train_label'][0])
    load_img_boolean()
    load_img_to_y_x_index()#only value "1" location in the list
