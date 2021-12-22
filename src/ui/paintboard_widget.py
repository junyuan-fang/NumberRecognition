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

        self.__thickness = 20               #pen
        self.__penColor = QColor(0,0,0,255)

        self.__begin_point = QPoint()
        self.__end_point = QPoint()

        # init board
        self.__board = QPixmap(self.__size)
        self.__board.fill(Fill) 
        self.setFixedSize(self.__size)
        self.__painter = QPainter()          #Qpainter    

    def clear(self):
        self.__board.fill(self.__fill)
        self.update()
    
    def setBoardFill(self, fill):
        self.__fill = fill
        self.__board.fill(fill)
        self.update()
    
    # get QImage
    def getContentAsQImage(self):
        image = self.__board.toImage()
        return image 
    
    # pen color  
    def setPenColor(self, color):
        self.__penColor = color

    # pen thickness
    def setPenThickness(self, thickness=20):    
        self.__thickness = thickness  
        
    # painting event
    def paintEvent(self, paintEvent):         
        self.__painter.begin(self)
        self.__painter.drawPixmap(0,0,self.__board)
        self.__painter.end()

    def mousePressEvent(self, mouseEvent):
        if mouseEvent.button() == Qt.LeftButton:
            self.__begin_point = mouseEvent.pos()
            self.__end_point = self.__begin_point
            # self.update()

    def mouseMoveEvent(self, mouseEvent):
        if mouseEvent.buttons() == Qt.LeftButton:
            self.__end_point = mouseEvent.pos()

            # buffer
            self.__painter.begin(self.__board)
            self.__painter.setPen(QPen(self.__penColor,self.__thickness))  
            self.__painter.drawLine(self.__begin_point, self.__end_point)
            self.__painter.end()

            self.__begin_point = self.__end_point
            self.update()

    

if __name__ == '__main__':
    app = QApplication(sys.argv)
    demo = PaintBoard()
    demo.show()
    sys.exit(app.exec_())