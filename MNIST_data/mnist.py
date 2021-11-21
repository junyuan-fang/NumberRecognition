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
train_num = 60000
test_num = 10000
img_dim = (1, 28, 28)
img_size = 28*28 #784

#/home/fjunyuan/Codes/TiraLabra/Recognition_of_handwritten_numbers/MNIST_data/
dataset_dir = os.path.dirname(os.path.abspath(__file__))
#print(dataset_dir)
save_file = dataset_dir + "/mnist.pkl"


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

def _convert_numpy():
    dataset = {}
    dataset['train_img'] =  _load_img(key_file['train_img'])
    dataset['train_label'] = _load_label(key_file['train_label'])    
    dataset['test_img'] = _load_img(key_file['test_img'])
    dataset['test_label'] = _load_label(key_file['test_label'])
    
    return dataset

def init_mnist():
    '''
    Note：Load the file for the first time and save it to pickle
    '''
    dataset = _convert_numpy()
    print("Creating pickle file ...")
    with open(save_file, 'wb') as f:
        pickle.dump(dataset, f, -1)#for later loading
    print("Done!")

def load_mnist():
    if not os.path.exists(save_file):
        init_mnist()
        
    with open(save_file, 'rb') as f:
        dataset = pickle.load(f)
    return dataset

def test_imported():
    print("Imported")
    
if __name__ == '__main__':
    #init_mnist()

    #tests
    dataset = {}
    dataset['train_img'] =  _load_img(key_file['train_img'])
    dataset['train_label'] =  _load_label(key_file['train_label'])

    #print(dataset['train_img'][0])
    print(os.path.abspath(__file__))

    img = dataset['train_img'][9]    # shape:[1,28,28] 
    img = img.reshape(28, 28)                   # shape:[28,28]  
    #imaging 0-127 are -128 - -1  negative
    #      128-255 are    0 - 127 positive
    img2 = img * 0xff      # outline/恢复灰度值大小 
    from pylab import *
    import matplotlib.pyplot as plt
    imshow(img2, 'gray')
    plt.show()
    #normalize

    # print(img2)

    # print(img)
    # print()
    # a=[[1,0],[1,0]]
    print(img[4])
    print(img[4][-5])
    print(img[4][-6])
    # print(dataset['train_label'][9])