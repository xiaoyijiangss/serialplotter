# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'D:/software_development_workspace/signal_displayer/PressureDisplayer/MainWindow.ui'
#
# Created by: PyQt5 UI code generator 5.15.7
#
# WARNING: Any manual changes made to this file will be lost when pyuic5 is
# run again.  Do not edit this file unless you know what you are doing.


from PyQt5 import QtCore, QtGui, QtWidgets


class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        MainWindow.setObjectName("MainWindow")
        MainWindow.resize(924, 437)
        self.gridLayout_2 = QtWidgets.QGridLayout(MainWindow)
        self.gridLayout_2.setObjectName("gridLayout_2")
        spacerItem = QtWidgets.QSpacerItem(245, 17, QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Minimum)
        self.gridLayout_2.addItem(spacerItem, 1, 4, 1, 1)
        self.frame_2 = QtWidgets.QFrame(MainWindow)
        self.frame_2.setFrameShape(QtWidgets.QFrame.Box)
        self.frame_2.setFrameShadow(QtWidgets.QFrame.Raised)
        self.frame_2.setObjectName("frame_2")
        self.horizontalLayout_2 = QtWidgets.QHBoxLayout(self.frame_2)
        self.horizontalLayout_2.setObjectName("horizontalLayout_2")
        self.pushButton = QtWidgets.QPushButton(self.frame_2)
        font = QtGui.QFont()
        font.setFamily("微软雅黑")
        self.pushButton.setFont(font)
        icon = QtGui.QIcon()
        icon.addPixmap(QtGui.QPixmap("D:/software_development_workspace/signal_displayer/PressureDisplayer\\delivery/Play.ico"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.pushButton.setIcon(icon)
        self.pushButton.setObjectName("pushButton")
        self.horizontalLayout_2.addWidget(self.pushButton)
        self.pushButton_2 = QtWidgets.QPushButton(self.frame_2)
        font = QtGui.QFont()
        font.setFamily("微软雅黑")
        self.pushButton_2.setFont(font)
        icon1 = QtGui.QIcon()
        icon1.addPixmap(QtGui.QPixmap("D:/software_development_workspace/signal_displayer/PressureDisplayer\\delivery/reload.ico"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.pushButton_2.setIcon(icon1)
        self.pushButton_2.setObjectName("pushButton_2")
        self.horizontalLayout_2.addWidget(self.pushButton_2)
        self.pushButton_10 = QtWidgets.QPushButton(self.frame_2)
        font = QtGui.QFont()
        font.setFamily("微软雅黑")
        self.pushButton_10.setFont(font)
        icon2 = QtGui.QIcon()
        icon2.addPixmap(QtGui.QPixmap("D:/software_development_workspace/signal_displayer/PressureDisplayer\\delivery/Delete.ico"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.pushButton_10.setIcon(icon2)
        self.pushButton_10.setObjectName("pushButton_10")
        self.horizontalLayout_2.addWidget(self.pushButton_10)
        self.pushButton_11 = QtWidgets.QPushButton(self.frame_2)
        font = QtGui.QFont()
        font.setFamily("微软雅黑")
        self.pushButton_11.setFont(font)
        icon3 = QtGui.QIcon()
        icon3.addPixmap(QtGui.QPixmap("D:/software_development_workspace/signal_displayer/PressureDisplayer\\delivery/Add.ico"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.pushButton_11.setIcon(icon3)
        self.pushButton_11.setObjectName("pushButton_11")
        self.horizontalLayout_2.addWidget(self.pushButton_11)
        self.pushButton_9 = QtWidgets.QPushButton(self.frame_2)
        font = QtGui.QFont()
        font.setFamily("微软雅黑")
        self.pushButton_9.setFont(font)
        icon4 = QtGui.QIcon()
        icon4.addPixmap(QtGui.QPixmap("D:/software_development_workspace/signal_displayer/PressureDisplayer\\delivery/Down arrow.ico"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.pushButton_9.setIcon(icon4)
        self.pushButton_9.setObjectName("pushButton_9")
        self.horizontalLayout_2.addWidget(self.pushButton_9)
        self.gridLayout_2.addWidget(self.frame_2, 1, 2, 1, 1)
        self.frame = QtWidgets.QFrame(MainWindow)
        self.frame.setFrameShape(QtWidgets.QFrame.Box)
        self.frame.setFrameShadow(QtWidgets.QFrame.Raised)
        self.frame.setObjectName("frame")
        self.gridLayout = QtWidgets.QGridLayout(self.frame)
        self.gridLayout.setObjectName("gridLayout")
        self.pushButton_7 = QtWidgets.QPushButton(self.frame)
        font = QtGui.QFont()
        font.setFamily("微软雅黑")
        self.pushButton_7.setFont(font)
        icon5 = QtGui.QIcon()
        icon5.addPixmap(QtGui.QPixmap("D:/software_development_workspace/signal_displayer/PressureDisplayer\\delivery/Green Ball.ico"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.pushButton_7.setIcon(icon5)
        self.pushButton_7.setObjectName("pushButton_7")
        self.gridLayout.addWidget(self.pushButton_7, 0, 5, 1, 1)
        self.radioButton = QtWidgets.QRadioButton(self.frame)
        self.radioButton.setText("")
        self.radioButton.setObjectName("radioButton")
        self.gridLayout.addWidget(self.radioButton, 0, 6, 1, 1)
        self.comboBox_2 = QtWidgets.QComboBox(self.frame)
        self.comboBox_2.setObjectName("comboBox_2")
        self.comboBox_2.addItem("")
        self.comboBox_2.addItem("")
        self.comboBox_2.addItem("")
        self.comboBox_2.addItem("")
        self.comboBox_2.addItem("")
        self.comboBox_2.addItem("")
        self.comboBox_2.addItem("")
        self.comboBox_2.addItem("")
        self.comboBox_2.addItem("")
        self.comboBox_2.addItem("")
        self.comboBox_2.addItem("")
        self.comboBox_2.addItem("")
        self.comboBox_2.addItem("")
        self.comboBox_2.addItem("")
        self.comboBox_2.addItem("")
        self.gridLayout.addWidget(self.comboBox_2, 0, 3, 1, 1)
        self.label = QtWidgets.QLabel(self.frame)
        font = QtGui.QFont()
        font.setFamily("微软雅黑")
        self.label.setFont(font)
        self.label.setObjectName("label")
        self.gridLayout.addWidget(self.label, 0, 0, 1, 1)
        self.comboBox = QtWidgets.QComboBox(self.frame)
        self.comboBox.setObjectName("comboBox")
        self.comboBox.addItem("")
        self.comboBox.addItem("")
        self.comboBox.addItem("")
        self.comboBox.addItem("")
        self.comboBox.addItem("")
        self.comboBox.addItem("")
        self.comboBox.addItem("")
        self.gridLayout.addWidget(self.comboBox, 0, 1, 1, 1)
        self.label_2 = QtWidgets.QLabel(self.frame)
        font = QtGui.QFont()
        font.setFamily("微软雅黑")
        self.label_2.setFont(font)
        self.label_2.setObjectName("label_2")
        self.gridLayout.addWidget(self.label_2, 0, 2, 1, 1)
        spacerItem1 = QtWidgets.QSpacerItem(10, 20, QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Minimum)
        self.gridLayout.addItem(spacerItem1, 0, 4, 1, 1)
        self.label.raise_()
        self.comboBox.raise_()
        self.pushButton_7.raise_()
        self.radioButton.raise_()
        self.comboBox_2.raise_()
        self.label_2.raise_()
        self.gridLayout_2.addWidget(self.frame, 1, 0, 1, 2)
        self.frame_3 = QtWidgets.QFrame(MainWindow)
        self.frame_3.setFrameShape(QtWidgets.QFrame.Box)
        self.frame_3.setFrameShadow(QtWidgets.QFrame.Raised)
        self.frame_3.setObjectName("frame_3")
        self.horizontalLayout_3 = QtWidgets.QHBoxLayout(self.frame_3)
        self.horizontalLayout_3.setObjectName("horizontalLayout_3")
        self.pushButton_3 = QtWidgets.QPushButton(self.frame_3)
        font = QtGui.QFont()
        font.setFamily("微软雅黑")
        self.pushButton_3.setFont(font)
        icon6 = QtGui.QIcon()
        icon6.addPixmap(QtGui.QPixmap("D:/software_development_workspace/signal_displayer/PressureDisplayer\\delivery/Blue Ball.ico"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.pushButton_3.setIcon(icon6)
        self.pushButton_3.setObjectName("pushButton_3")
        self.horizontalLayout_3.addWidget(self.pushButton_3)
        self.gridLayout_2.addWidget(self.frame_3, 1, 3, 1, 1)
        self.graphicsView = PlotWidget(MainWindow)
        font = QtGui.QFont()
        font.setFamily("微软雅黑")
        font.setBold(False)
        font.setUnderline(False)
        font.setWeight(50)
        self.graphicsView.setFont(font)
        self.graphicsView.setViewportUpdateMode(QtWidgets.QGraphicsView.SmartViewportUpdate)
        self.graphicsView.setObjectName("graphicsView")
        self.gridLayout_2.addWidget(self.graphicsView, 2, 0, 1, 5)

        self.retranslateUi(MainWindow)
        self.comboBox_2.setCurrentIndex(0)
        self.comboBox.setCurrentIndex(0)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "Form"))
        self.pushButton.setText(_translate("MainWindow", "开始"))
        self.pushButton_2.setText(_translate("MainWindow", "复位"))
        self.pushButton_10.setText(_translate("MainWindow", "停止"))
        self.pushButton_11.setText(_translate("MainWindow", "导入"))
        self.pushButton_9.setText(_translate("MainWindow", "导出"))
        self.frame.setWhatsThis(_translate("MainWindow", "Connect"))
        self.pushButton_7.setText(_translate("MainWindow", "连接"))
        self.comboBox_2.setCurrentText(_translate("MainWindow", "com0"))
        self.comboBox_2.setItemText(0, _translate("MainWindow", "com0"))
        self.comboBox_2.setItemText(1, _translate("MainWindow", "com1"))
        self.comboBox_2.setItemText(2, _translate("MainWindow", "com2"))
        self.comboBox_2.setItemText(3, _translate("MainWindow", "com3"))
        self.comboBox_2.setItemText(4, _translate("MainWindow", "com4"))
        self.comboBox_2.setItemText(5, _translate("MainWindow", "com5"))
        self.comboBox_2.setItemText(6, _translate("MainWindow", "com6"))
        self.comboBox_2.setItemText(7, _translate("MainWindow", "com7"))
        self.comboBox_2.setItemText(8, _translate("MainWindow", "com8"))
        self.comboBox_2.setItemText(9, _translate("MainWindow", "com9"))
        self.comboBox_2.setItemText(10, _translate("MainWindow", "com10"))
        self.comboBox_2.setItemText(11, _translate("MainWindow", "com11"))
        self.comboBox_2.setItemText(12, _translate("MainWindow", "com12"))
        self.comboBox_2.setItemText(13, _translate("MainWindow", "com13"))
        self.comboBox_2.setItemText(14, _translate("MainWindow", "com14"))
        self.label.setText(_translate("MainWindow", "波特率"))
        self.comboBox.setCurrentText(_translate("MainWindow", "600bps"))
        self.comboBox.setItemText(0, _translate("MainWindow", "600bps"))
        self.comboBox.setItemText(1, _translate("MainWindow", "1200bps"))
        self.comboBox.setItemText(2, _translate("MainWindow", "2400bps"))
        self.comboBox.setItemText(3, _translate("MainWindow", "4800bps"))
        self.comboBox.setItemText(4, _translate("MainWindow", "9600bps"))
        self.comboBox.setItemText(5, _translate("MainWindow", "19200bps"))
        self.comboBox.setItemText(6, _translate("MainWindow", "115200bps"))
        self.label_2.setText(_translate("MainWindow", "端口"))
        self.pushButton_3.setText(_translate("MainWindow", "标定"))
from pyqtgraph import PlotWidget