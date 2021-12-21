import sys, os
import random
import numpy as np

from PyQt5.QtWidgets import (
    QApplication, QMainWindow, QMessageBox
)

from PyQt5.uic import loadUi#load dynamically
from repositories.mnist import load_test_img

from ui.main_window import Ui_MainWindow #contains the GUI for your main window
from ui.paintboard_widget import PaintBoard

from PyQt5.QtGui import QPainter, QPen, QPixmap, QColor, QImage
from PyQt5.QtCore import Qt, QPoint, QSize
from PIL import Image,ImageQt

from services import knn as k
#defines Window, which will provide your application’s main window. 
# In this case, the class uses multiple inheritance. 
# It inherits the main window functionality from QMainWindow 
# and the GUI functionality from Ui_MainWindow.
class Window(QMainWindow, Ui_MainWindow):
    def __init__(self, parent=None):
        #initialisation
        super(Window, self).__init__(parent)
        src_dir = os.path.abspath(os.path.dirname(os.getcwd())) + "/Recognition_of_handwritten_numbers/src/"
        #loadUi(src_dir + "ui/main_window.ui", self)#use self.setupUi(self) if do not want to use loadUi 
        self.setupUi(self)#creates the whole GUI for your main window.
        self.test_pic = load_test_img()

        #Value initialisation
        self.setSpinBox()
        self.setSlider()
        self.have_value = False
        self.index = 0
        self.method = "D22"

        #Board initalisation
        self.board = PaintBoard(self, Size = QSize(224, 224), Fill = QColor(0,0,0,0))
        self.Area_Layout.addWidget(self.board)
        


    def setSpinBox(self):
        self.k_value.setMinimum(1)
        self.k_value.setMaximum(10)
        self.trainning_value.setMinimum(1)
        self.trainning_value.setMaximum(10000)
    
    def setSlider(self):
        self.kSlider.setMinimum(1)
        self.kSlider.setMaximum(10)
        self.trainningSlider.setMinimum(1)
        self.trainningSlider.setMaximum(10000)

    #MNIST mode 
    def MNIT_random_selection_callback(self):
        self.selectImage.setEnabled(True)
        self.board.setBoardFill(QColor(255,255,255,255))
        self.have_value = False
    
    #mouse mode
    def Mouse_callback(self):
        self.selectImage.setEnabled(False)
        self.board.setBoardFill(QColor(0,0,0,0))
        self.have_value = False

    def selectImage_callback(self):
        self.have_value = True
        index = random.randint(0,9999)
        img = self.test_pic[index]
        img = img.reshape(28,28)
        #self.board.setImg(img)

        #img = img * 0xff      # 恢复灰度值大小 
        pil_img = Image.fromarray(np.uint8(img))
        pil_img = pil_img.resize((261, 261))        # zoom in 


        # "pil" pic to the "qimage" tyoe
        qimage = ImageQt.ImageQt(pil_img)
        
        # display qimage in the label
        pix = QPixmap.fromImage(qimage)
        self.DataArea.setPixmap(pix)



    def clear_callback(self):
        self.board.clear()
        self.knnResult.clear()
        self.DataArea.clear()
        #clear index

    def recognization_callback(self):
        if self.have_value == True:
            pass
        

    def closeEvent(self, event):
        """ask again when quitting
        Args:
            event ([type]): [description]
        """
        reply = QMessageBox.question(self, 'Message',
            "Are you sure to quit?", QMessageBox.Yes | 
            QMessageBox.No, QMessageBox.Yes)

        if reply == QMessageBox.Yes:
            event.accept()
        else:
            event.ignore()  
    

if __name__ == "__main__":
    app = QApplication(sys.argv)
    win = Window()
    win.show()
    sys.exit(app.exec())


