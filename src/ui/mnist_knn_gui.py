import sys
import os
import random
import numpy as np

from PyQt5.QtWidgets import (
    QApplication, QMainWindow, QMessageBox,
)

from PyQt5.uic import loadUi
from numpy.core import numeric  # load dynamically
from repositories.mnist import load_test_img

# contains the GUI for your main window
from ui.main_window import Ui_MainWindow
from ui.paintboard_widget import PaintBoard
#from ui.paintboard import PaintBoard

from PyQt5.QtWidgets import QApplication, QMainWindow, QMessageBox
from PyQt5.QtGui import QPainter, QPen, QPixmap, QColor, QImage
from PyQt5.QtCore import Qt, QPoint, QSize, QStringListModel
from PIL import Image, ImageQt

from services import knn as K
# defines Window, which will provide your application’s main window.
# In this case, the class uses multiple inheritance.
# It inherits the main window functionality from QMainWindow
# and the GUI functionality from Ui_MainWindow.


class Window(QMainWindow, Ui_MainWindow):
    def __init__(self, parent=None):
        # initialisation
        super(Window, self).__init__()
        #src_dir = os.path.abspath(os.path.dirname(os.getcwd())) + "/Recognition_of_handwritten_numbers/src/"
        # loadUi(src_dir + "ui/main_window.ui", self)#use self.setupUi(self) if do not want to use loadUi
        self.setupUi(self)  # creates the whole GUI for your main window.
        self.test_pic = load_test_img()

        # Value initialisation
        self.setSpinBox()
        self.setSlider()
        self.have_value = False
        self.index = 0
        self.method = "D22"
        self.mode = 1
        self.trainningSlider.setValue(150)
        self.trainning_value.setValue(150)
        self.kSlider.setValue(3)
        self.k_value.setValue(3)
        self.knnResult.setText("No input")

        # Board initalisation
        self.paint_board = PaintBoard(
            self, Size=QSize(280, 280), Fill=QColor(0, 0, 0, 0))
        # self.MNIT_random_selection_callback()
        self.paint_board.setPenColor(QColor(0, 0, 0, 0))
        self.Area_Layout.addWidget(self.paint_board)
        
        #logic with recognization button
        self.paint_board.mousePressed.connect(lambda: self.recognization.setEnabled(True))

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

    # MNIST mode
    def MNIT_random_selection_callback(self):
        self.mode = 1
        self.clearDataArea()
        self.selectImage.setEnabled(True)

        self.paint_board.setBoardFill(QColor(0, 0, 0, 0))
        self.paint_board.setPenColor(QColor(0, 0, 0, 0))
        self.have_value = False

    # mouse mode
    def Mouse_callback(self):
        #logic with recognization button
        self.recognization.setEnabled(False)

        self.mode = 2
        self.clearDataArea()
        self.selectImage.setEnabled(False)

        self.paint_board.setBoardFill(QColor(0, 0, 0, 255))
        self.paint_board.setPenColor(QColor(255, 255, 255, 255))
        self.have_value = True

    def selectImage_callback(self):
        """Select a img from the test(10000) image, and display it on the paint_board
        data->pil_img->qimage->Pixmap()
        """
        #logic with recognization button
        self.recognization.setEnabled(True)

        self.have_value = True
        self.index = random.randint(0, 9999)
        img = self.test_pic[self.index]
        img = img.reshape(28, 28)
        # self.paint_board.setImg(img)

        # img = img * 0xff      # outline
        pil_img = Image.fromarray(np.uint8(img))
        pil_img = pil_img.resize((280, 280), Image.ANTIALIAS)        # zoom in

        # "pil" pic to the "qimage" tyoe
        qimage = ImageQt.ImageQt(pil_img)

        # display qimage in the label
        pix = QPixmap.fromImage(qimage)
        self.DataArea.setPixmap(pix)


    def clearDataArea(self):
        self.paint_board.clear()
        self.knnResult.clear()
        self.DataArea.clear()
        self.recognization.setEnabled(False)

    def clear_callback(self):
        self.clearDataArea()

    # 'recognization'
    def recognization_callback(self):
        # disable buttons, after task, enable it
        self.recognization.setEnabled(False)
        # self.clear.setEnabled(False)
        QApplication.processEvents()  # enable the one thread
        if self.have_value == True:
            # parameters
            k = self.k_value.value()
            index = self.index
            train_range = self.trainning_value.value()
            method = self.method

            if self.mode == 1:  # MNIST
                result = K.knn.recognition(k, index, train_range, method)
                self.knnResult.setText(f"{result}")
            if self.mode == 2:  # mouse
                # Pixmap()->qimage->pil_img->data
                qimage = self.paint_board.getContentAsQImage()
                pil_img = ImageQt.fromqimage(qimage)
                # resize
                pil_img = pil_img.resize((28, 28))
                img = np.asarray_chkfinite(pil_img)
                try:
                    result = K.knn.recognition(k, -1, train_range, method, img)
                    self.knnResult.setText(f"{result}")
                except:  # input might be empty
                    self.knnResult.setText("No input")
        self.recognization.setEnabled(True)
        # self.clear.setEnabled(True)

    def D22_callback(self):
        self.method = "D22"
        self.statusbar.showMessage(self.method)
        print(self.method)

    def D23_callback(self):
        self.method = "D23"
        self.statusbar.showMessage(self.method)
        print(self.method)

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
