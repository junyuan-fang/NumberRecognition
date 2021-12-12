import sys, os

from PyQt5.QtWidgets import (
    QApplication, QDialog, QMainWindow, QMessageBox
)
from PyQt5.uic import loadUi#load dynamically

from ui.main_window import Ui_MainWindow #contains the GUI for your main window


#defines Window, which will provide your application’s main window. 
# In this case, the class uses multiple inheritance. 
# It inherits the main window functionality from QMainWindow 
# and the GUI functionality from Ui_MainWindow.
class Window(QMainWindow, Ui_MainWindow):
    def __init__(self, parent=None):
        super(Window, self).__init__()
        #super().__init__(parent)
        src_dir = os.path.abspath(os.path.dirname(os.getcwd())) + "/Recognition_of_handwritten_numbers/src/"
        loadUi(src_dir + "ui/main_window.ui", self)
        #self.setupUi(self)#creates the whole GUI for your main window.
        #self.show()
class Ui(QMainWindow):
    def __init__(self):
        super(Ui, self).__init__() # Call the inherited classes __init__ method
        src_dir = os.path.abspath(os.path.dirname(os.getcwd())) + "/Recognition_of_handwritten_numbers/src/"
        loadUi(src_dir + "ui/main_window.ui", self)
        self.show() # Show the GUI
if __name__ == "__main__":
    app = QApplication(sys.argv)
    win = Window()
    win.show()
    sys.exit(app.exec())

# import tensorflow as tf
# from tensorflow.examples.tutorials.mnist import input_data
# mnist = input_data.read_data_sets("./MNIST_data/",one_hot=True)
# print (mnist.train.images.shape)
# #(55000, 784)

