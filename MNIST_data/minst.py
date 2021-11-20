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

train_num = 60000
test_num = 10000 

dataset_dir = os.path.dirname(os.path.abspath(__file__))

def _load_img(file_name):
    file_path = dataset_dir + "/" + file_name
    
    print("Converting " + file_name + " to NumPy Array ...")    
    with gzip.open(file_path, 'rb') as f:
            data = np.frombuffer(f.read(), np.uint8, offset=16)
    data = data.reshape(-1, img_size)
    print("Done")
    
    print(len(data))
    print(len(data[0]))
    return data

dataset = {}
dataset['train_img'] =  _load_img(key_file['train_img'])

#print(dataset['train_img'][0])
print(os.path.abspath(__file__))

img = dataset['train_img'][0]    # shape:[1,28,28] 
img = img.reshape(28, 28)                   # shape:[28,28]  

img = img * 0xff      # 恢复灰度值大小 
from pylab import *
imshow(img, interpolation='nearest')
grid(True)
print(img)  
import numpy as np
import matplotlib.pyplot as plt
import matplotlib.cm as cm

# Make an array with ones in the shape of an 'X'
a = np.eye(10,10)
print(a)
print(a[::,:])
a += a[::-1,:]

fig = plt.figure()
ax1 = fig.add_subplot(121)
# Bilinear interpolation - this will look blurry
ax1.imshow(a, interpolation='bilinear', cmap=cm.Greys_r)

ax2 = fig.add_subplot(122)
# 'nearest' interpolation - faithful but blocky
ax2.imshow(a, interpolation='nearest', cmap=cm.Greys_r)

plt.show()