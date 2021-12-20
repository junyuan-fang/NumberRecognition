import sys, os

from PyQt5.QtWidgets import (
    QApplication, QMainWindow, QMessageBox
)
from PyQt5.uic import loadUi#load dynamically

from ui.main_window import Ui_MainWindow #contains the GUI for your main window
#from ui.mnist_pic_widget import 

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

        #Value initialisation
        self.setSpinBox()
        self.setSlider()

        #PaintBoard initalisation

        #mnist_pic_wiget




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
    
    #mouse mode
    def Mouse_callback(self):
        self.selectImage.setEnabled(False)

    def selectImage_callback(self):
        pass
    def clear_callback(self):
        pass
    def recognization_callback(self):
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


