#This file is for loading all mnist and boolean values 
import gzip
import pickle
import os
import numpy as np

def test_imported():
    print("Imported")

key_file = {
    'train_img':'train-images-idx3-ubyte.gz',
    'train_label':'train-labels-idx1-ubyte.gz',
    'test_img':'t10k-images-idx3-ubyte.gz',
    'test_label':'t10k-labels-idx1-ubyte.gz'
}
train_num = 60000
test_num = 10000
img_dim = (1, 28, 28)
img_size = 28*28 #784
RANGE = 73

#/home/fjunyuan/Codes/TiraLabra/Recognition_of_handwritten_numbers/MNIST_data/
dataset_dir = os.path.dirname(os.path.abspath(__file__))
#print(dataset_dir)
save_file_label = dataset_dir + "/label.pkl"
save_file_img_boolean = dataset_dir + "/img_boolean.pkl"
save_file_img_boolean_index = dataset_dir + "/img_boolean_index.pkl"


def _load_img(file_name):
    file_path = dataset_dir + "/" + file_name
    
    print("Converting " + file_name + " to NumPy Array ...")    
    with gzip.open(file_path, 'rb') as f:
            data = np.frombuffer(f.read(), np.uint8, offset=16)#according to the MNIST
    data = data.reshape(-1, img_size)#-1 then we do not need to know the original size. train = 60000x784, test = 10000x784
    print("Done")
    

    #print(data.shape)
    return data

def _load_label(file_name):
    file_path = dataset_dir + "/" + file_name
    
    print("Converting " + file_name + " to NumPy Array ...")
    with gzip.open(file_path, 'rb') as f:
            labels = np.frombuffer(f.read(), np.uint8, offset=8)#according to the MNIST
    print("Done")

    #print(data.shape)
    return labels
def init_label():
    dataset = {}
    dataset ['train_label'] = _load_label(key_file['train_label'])
    dataset ['test_label'] = _load_label(key_file['test_label'])

    print("Creating pickle file for label...")
    with open(save_file_label, 'wb') as f:
        pickle.dump(dataset, f, -1)#for later loading
    print("Done!")

def _load_label_pkl():
    if not os.path.exists(save_file_label):
        init_label()

    with open(save_file_label, 'rb') as f:
        dataset = pickle.load(f)

    # value = dataset['train_img'][9]
    
    # for w in value:
    #     print(w) 

    return dataset

#------------------------------------------------------
def conver_img_to_boolean(img_set):
    set = []
    for img in img_set:
        new_img = img.reshape(28, 28)
        matrix = [] 
        for row in new_img:
            list = []
            for x in range(len(row)):
                if row[x]<=RANGE:
                    list.append(0)
                else:
                    list.append(1)
            matrix.append(list)
        set.append(matrix)
    
    return set

def init_img_boolean():
    dataset = {}
    train_img = _load_img(key_file['train_img'])
    test_img = _load_img(key_file['test_img'])

    dataset ['train_img'] = conver_img_to_boolean(train_img)
    dataset ['test_img'] = conver_img_to_boolean(test_img)

    print("Creating pickle file for image(boolean)...")
    with open(save_file_img_boolean, 'wb') as f:
        pickle.dump(dataset, f, -1)#for later loading
    print("Done!")

def load_img_boolean():
    if not os.path.exists(save_file_img_boolean):
        init_img_boolean()

    with open(save_file_img_boolean, 'rb') as f:
        dataset = pickle.load(f)

    # value = dataset['train_img'][9]
    
    # for w in value:
    #     print(w) 

    return dataset
#------------------------------------------------------
def conver_img_to_x_y(img_set):
    set = []
    for img in img_set:
        new_img = img.reshape(28, 28)
        matrix = []
        for y in range(28):
            for x in range(28):
                if new_img[y][x]<=RANGE:
                    continue
                else:
                    matrix.append((y,x))
        set.append(matrix)
    return set

def init_img_boolean_index():
    dataset = {}
    train_img = _load_img(key_file['train_img'])
    test_img = _load_img(key_file['test_img'])

    dataset ['train_img'] = conver_img_to_x_y(train_img)
    dataset ['test_img'] = conver_img_to_x_y(test_img)

    print("Creating pickle file for image(index)...")
    with open(save_file_img_boolean_index, 'wb') as f:
        pickle.dump(dataset, f, -1)#for later loading
    print("Done!")


def load_img_boolean_index():
    if not os.path.exists(save_file_img_boolean_index):
        init_img_boolean_index()

    with open(save_file_img_boolean_index, 'rb') as f:
        dataset = pickle.load(f)
    
    # matrix = [['#']*28 for i in range(28)]
    # value = dataset['train_img'][9]
    # for q in value:
    #     y = q[0]
    #     x = q[1]
    #     matrix[y][x] = '.'
    # for w in matrix:
    #     print(w) 
    # print(dataset['train_label'][9])

    return dataset


if __name__ == '__main__':
    _load_label_pkl()
    load_img_boolean() 
    load_img_boolean_index()#only value "1" location in the list
    # #tests
    # dataset = {}
    # dataset['train_img'] =  _load_img(key_file['train_img'])
    # dataset['train_label'] =  _load_label(key_file['train_label'])

    # #print(dataset['train_img'][0])
    # print(os.path.abspath(__file__))

    # img = dataset['train_img'][9]    # shape:[1,28,28] 
    # img = img.reshape(28, 28)                   # shape:[28,28]  
    # #imaging 0-127 are -128 - -1  negative
    # #      128-255 are    0 - 127 positive
    # img2 = img * 0xff      # outline/恢复灰度值大小 
    # from pylab import *
    # import matplotlib.pyplot as plt
    # imshow(img, 'gray')
    # plt.show()
