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
        #initialisation
        super(Window, self).__init__()
        src_dir = os.path.abspath(os.path.dirname(os.getcwd())) + "/Recognition_of_handwritten_numbers/src/"
        loadUi(src_dir + "ui/main_window.ui", self)#use self.setupUi(self) if do not want to use loadUi 
        #self.setupUi(self)#creates the whole GUI for your main window.
    def closeEvent(self, event):
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


