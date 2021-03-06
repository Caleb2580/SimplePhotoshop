# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'photoshop.ui'
#
# Created by: PyQt5 UI code generator 5.15.4
#
# WARNING: Any manual changes made to this file will be lost when pyuic5 is
# run again.  Do not edit this file unless you know what you are doing.


from PyQt5 import QtCore, QtGui, QtWidgets


class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        MainWindow.setObjectName("MainWindow")
        MainWindow.resize(1000, 600)
        MainWindow.setMinimumSize(QtCore.QSize(1000, 600))
        MainWindow.setMaximumSize(QtCore.QSize(1000, 600))
        self.centralwidget = QtWidgets.QWidget(MainWindow)
        self.centralwidget.setObjectName("centralwidget")
        self.MinusSizeButton = QtWidgets.QPushButton(self.centralwidget)
        self.MinusSizeButton.setGeometry(QtCore.QRect(5, 550, 35, 35))
        self.MinusSizeButton.setObjectName("MinusSizeButton")
        self.PlusSizeButton = QtWidgets.QPushButton(self.centralwidget)
        self.PlusSizeButton.setGeometry(QtCore.QRect(90, 550, 35, 35))
        self.PlusSizeButton.setObjectName("PlusSizeButton")
        self.canvas = QtWidgets.QLabel(self.centralwidget)
        self.canvas.setGeometry(QtCore.QRect(150, 50, 700, 500))
        self.canvas.setText("")
        self.canvas.setAlignment(QtCore.Qt.AlignLeading|QtCore.Qt.AlignLeft|QtCore.Qt.AlignTop)
        self.canvas.setObjectName("canvas")
        self.ColorExample = QtWidgets.QPushButton(self.centralwidget)
        self.ColorExample.setGeometry(QtCore.QRect(49, 550, 35, 35))
        self.ColorExample.setText("")
        self.ColorExample.setObjectName("ColorExample")
        self.ToolsFrame = QtWidgets.QFrame(self.centralwidget)
        self.ToolsFrame.setGeometry(QtCore.QRect(0, 0, 130, 530))
        self.ToolsFrame.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.ToolsFrame.setFrameShadow(QtWidgets.QFrame.Raised)
        self.ToolsFrame.setObjectName("ToolsFrame")
        self.verticalLayoutWidget = QtWidgets.QWidget(self.ToolsFrame)
        self.verticalLayoutWidget.setGeometry(QtCore.QRect(0, 0, 131, 531))
        self.verticalLayoutWidget.setObjectName("verticalLayoutWidget")
        self.ToolsLayout = QtWidgets.QVBoxLayout(self.verticalLayoutWidget)
        self.ToolsLayout.setContentsMargins(0, 0, 0, 0)
        self.ToolsLayout.setObjectName("ToolsLayout")
        self.Move = QtWidgets.QPushButton(self.verticalLayoutWidget)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.Move.sizePolicy().hasHeightForWidth())
        self.Move.setSizePolicy(sizePolicy)
        self.Move.setMinimumSize(QtCore.QSize(70, 30))
        self.Move.setMaximumSize(QtCore.QSize(70, 30))
        self.Move.setLayoutDirection(QtCore.Qt.LeftToRight)
        self.Move.setObjectName("Move")
        self.ToolsLayout.addWidget(self.Move, 0, QtCore.Qt.AlignHCenter)
        self.Eraser = QtWidgets.QPushButton(self.verticalLayoutWidget)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.Eraser.sizePolicy().hasHeightForWidth())
        self.Eraser.setSizePolicy(sizePolicy)
        self.Eraser.setMinimumSize(QtCore.QSize(70, 30))
        self.Eraser.setMaximumSize(QtCore.QSize(70, 30))
        self.Eraser.setLayoutDirection(QtCore.Qt.LeftToRight)
        self.Eraser.setObjectName("Eraser")
        self.ToolsLayout.addWidget(self.Eraser, 0, QtCore.Qt.AlignHCenter)
        self.Brush = QtWidgets.QPushButton(self.verticalLayoutWidget)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.Brush.sizePolicy().hasHeightForWidth())
        self.Brush.setSizePolicy(sizePolicy)
        self.Brush.setMinimumSize(QtCore.QSize(70, 30))
        self.Brush.setMaximumSize(QtCore.QSize(70, 30))
        self.Brush.setLayoutDirection(QtCore.Qt.LeftToRight)
        self.Brush.setObjectName("Brush")
        self.ToolsLayout.addWidget(self.Brush, 0, QtCore.Qt.AlignHCenter)
        self.Smooth = QtWidgets.QPushButton(self.verticalLayoutWidget)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.Smooth.sizePolicy().hasHeightForWidth())
        self.Smooth.setSizePolicy(sizePolicy)
        self.Smooth.setMinimumSize(QtCore.QSize(70, 30))
        self.Smooth.setMaximumSize(QtCore.QSize(70, 30))
        self.Smooth.setLayoutDirection(QtCore.Qt.LeftToRight)
        self.Smooth.setObjectName("Smooth")
        self.ToolsLayout.addWidget(self.Smooth, 0, QtCore.Qt.AlignHCenter)
        self.LayersFrame = QtWidgets.QFrame(self.centralwidget)
        self.LayersFrame.setGeometry(QtCore.QRect(870, 50, 130, 500))
        self.LayersFrame.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.LayersFrame.setFrameShadow(QtWidgets.QFrame.Raised)
        self.LayersFrame.setObjectName("LayersFrame")
        self.verticalLayoutWidget_2 = QtWidgets.QWidget(self.LayersFrame)
        self.verticalLayoutWidget_2.setGeometry(QtCore.QRect(0, 0, 131, 501))
        self.verticalLayoutWidget_2.setObjectName("verticalLayoutWidget_2")
        self.LayersLayout = QtWidgets.QVBoxLayout(self.verticalLayoutWidget_2)
        self.LayersLayout.setContentsMargins(0, 0, 0, 0)
        self.LayersLayout.setObjectName("LayersLayout")
        self.DeleteLayerButton = QtWidgets.QPushButton(self.centralwidget)
        self.DeleteLayerButton.setGeometry(QtCore.QRect(885, 555, 40, 40))
        self.DeleteLayerButton.setObjectName("DeleteLayerButton")
        self.AddLayerButton = QtWidgets.QPushButton(self.centralwidget)
        self.AddLayerButton.setGeometry(QtCore.QRect(945, 555, 40, 40))
        self.AddLayerButton.setObjectName("AddLayerButton")
        self.SaveButton = QtWidgets.QPushButton(self.centralwidget)
        self.SaveButton.setEnabled(True)
        self.SaveButton.setGeometry(QtCore.QRect(470, 560, 70, 30))
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.SaveButton.sizePolicy().hasHeightForWidth())
        self.SaveButton.setSizePolicy(sizePolicy)
        self.SaveButton.setMinimumSize(QtCore.QSize(70, 30))
        self.SaveButton.setMaximumSize(QtCore.QSize(70, 30))
        self.SaveButton.setLayoutDirection(QtCore.Qt.LeftToRight)
        self.SaveButton.setObjectName("SaveButton")
        MainWindow.setCentralWidget(self.centralwidget)

        self.retranslateUi(MainWindow)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "MainWindow"))
        self.MinusSizeButton.setText(_translate("MainWindow", "-"))
        self.PlusSizeButton.setText(_translate("MainWindow", "+"))
        self.Move.setText(_translate("MainWindow", "Move"))
        self.Eraser.setText(_translate("MainWindow", "Eraser"))
        self.Brush.setText(_translate("MainWindow", "Brush"))
        self.Smooth.setText(_translate("MainWindow", "Smooth"))
        self.DeleteLayerButton.setText(_translate("MainWindow", "-"))
        self.AddLayerButton.setText(_translate("MainWindow", "+"))
        self.SaveButton.setText(_translate("MainWindow", "Save"))


if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    MainWindow = QtWidgets.QMainWindow()
    ui = Ui_MainWindow()
    ui.setupUi(MainWindow)
    MainWindow.show()
    sys.exit(app.exec_())
