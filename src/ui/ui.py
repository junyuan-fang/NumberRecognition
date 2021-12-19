import sys
from PyQt5.QtWidgets import QApplication
from ui.mnist_knn_gui import Window
class UI:
    def start(self):
        app = QApplication(sys.argv)
        win = Window() 
        win.setWindowTitle("knn classifier")
        win.show()
        #app.exec()
        sys.exit(app.exec())