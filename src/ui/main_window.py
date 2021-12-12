# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'main_window.ui'
#
# Created by: PyQt5 UI code generator 5.14.1
#
# WARNING! All changes made in this file will be lost!


from PyQt5 import QtCore, QtGui, QtWidgets


class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        MainWindow.setObjectName("MainWindow")
        MainWindow.resize(950, 615)
        self.centralwidget = QtWidgets.QWidget(MainWindow)
        self.centralwidget.setObjectName("centralwidget")
        self.picture_or_drawing = QtWidgets.QComboBox(self.centralwidget)
        self.picture_or_drawing.setGeometry(QtCore.QRect(80, 70, 221, 41))
        self.picture_or_drawing.setObjectName("picture_or_drawing")
        self.picture_or_drawing.addItem("")
        self.label_4 = QtWidgets.QLabel(self.centralwidget)
        self.label_4.setGeometry(QtCore.QRect(640, 70, 131, 20))
        self.label_4.setObjectName("label_4")
        self.method = QtWidgets.QComboBox(self.centralwidget)
        self.method.setGeometry(QtCore.QRect(80, 130, 171, 31))
        self.method.setObjectName("method")
        self.method.addItem("")
        self.method.addItem("")
        self.random_selection = QtWidgets.QPushButton(self.centralwidget)
        self.random_selection.setGeometry(QtCore.QRect(78, 184, 171, 31))
        self.random_selection.setObjectName("random_selection")
        self.clear_table = QtWidgets.QPushButton(self.centralwidget)
        self.clear_table.setGeometry(QtCore.QRect(80, 230, 171, 31))
        self.clear_table.setObjectName("clear_table")
        self.re = QtWidgets.QPushButton(self.centralwidget)
        self.re.setGeometry(QtCore.QRect(80, 280, 171, 31))
        self.re.setObjectName("re")
        self.verticalLayoutWidget = QtWidgets.QWidget(self.centralwidget)
        self.verticalLayoutWidget.setGeometry(QtCore.QRect(640, 90, 221, 221))
        self.verticalLayoutWidget.setObjectName("verticalLayoutWidget")
        self.dArea_Layout = QtWidgets.QVBoxLayout(self.verticalLayoutWidget)
        self.dArea_Layout.setContentsMargins(0, 0, 0, 0)
        self.dArea_Layout.setSpacing(0)
        self.dArea_Layout.setObjectName("dArea_Layout")
        self.result = QtWidgets.QLabel(self.centralwidget)
        self.result.setGeometry(QtCore.QRect(290, 110, 91, 51))
        self.result.setObjectName("result")
        self.knnResult = QtWidgets.QLabel(self.centralwidget)
        self.knnResult.setGeometry(QtCore.QRect(430, 140, 91, 131))
        font = QtGui.QFont()
        font.setPointSize(48)
        self.knnResult.setFont(font)
        self.knnResult.setObjectName("knnResult")
        MainWindow.setCentralWidget(self.centralwidget)
        self.statusbar = QtWidgets.QStatusBar(MainWindow)
        self.statusbar.setObjectName("statusbar")
        MainWindow.setStatusBar(self.statusbar)

        self.retranslateUi(MainWindow)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "MainWindow"))
        self.picture_or_drawing.setItemText(0, _translate("MainWindow", "1:  MNIST random selection"))
        self.label_4.setText(_translate("MainWindow", "Data Input area"))
        self.method.setItemText(0, _translate("MainWindow", "D22"))
        self.method.setItemText(1, _translate("MainWindow", "D23"))
        self.random_selection.setText(_translate("MainWindow", "Random Selection"))
        self.clear_table.setText(_translate("MainWindow", "Clear"))
        self.re.setText(_translate("MainWindow", "Recognization"))
        self.result.setText(_translate("MainWindow", "<html><head/><body><p><span style=\" font-weight:600;\">Result : </span></p></body></html>"))
        self.knnResult.setText(_translate("MainWindow", "9"))
