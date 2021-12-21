import sys
import numpy as np
from PIL import Image,ImageQt
from PyQt5.QtWidgets import QWidget, QApplication
from PyQt5.QtGui import QPixmap, QPainter, QPen, QColor
from PyQt5.QtCore import Qt, QPoint, QSize



class PaintBoard(QWidget):
    def __init__(self,Parent = None, Size = QSize(280, 280), Fill = QColor(255,255,255,255)):
        super().__init__(Parent)
        # init parameter
        self.__size = Size
        self.__fill = Fill

        # init board
        self.__board = QPixmap(self.__size)
        self.__board.fill(Fill) 
        self.setFixedSize(self.__size)

    def clear(self):
        self.__board.fill(self.__fill)
        self.update()
    
    def setBoardFill(self, fill):
        self.__fill = fill
        self.__board.fill(fill)
        self.update()
        

    

if __name__ == '__main__':
    app = QApplication(sys.argv)
    demo = PaintBoard()
    demo.show()
    sys.exit(app.exec_())