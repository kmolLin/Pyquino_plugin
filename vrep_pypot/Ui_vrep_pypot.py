# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'Y:\eric6_workspace\Pyquino_plugin\vrep_pypot\vrep_pypot.ui'
#
# Created by: PyQt5 UI code generator 5.7
#
# WARNING! All changes made in this file will be lost!

from PyQt5 import QtCore, QtGui, QtWidgets

class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        MainWindow.setObjectName("MainWindow")
        MainWindow.resize(682, 517)
        self.centralWidget = QtWidgets.QWidget(MainWindow)
        self.centralWidget.setObjectName("centralWidget")
        self.addMachine = QtWidgets.QPushButton(self.centralWidget)
        self.addMachine.setGeometry(QtCore.QRect(60, 70, 91, 41))
        self.addMachine.setObjectName("addMachine")
        self.simraution = QtWidgets.QPushButton(self.centralWidget)
        self.simraution.setGeometry(QtCore.QRect(60, 120, 91, 41))
        self.simraution.setObjectName("simraution")
        self.restart = QtWidgets.QPushButton(self.centralWidget)
        self.restart.setGeometry(QtCore.QRect(60, 170, 91, 41))
        self.restart.setObjectName("restart")
        self.motors = QtWidgets.QPushButton(self.centralWidget)
        self.motors.setGeometry(QtCore.QRect(60, 220, 91, 41))
        self.motors.setObjectName("motors")
        self.reciver = QtWidgets.QTextEdit(self.centralWidget)
        self.reciver.setGeometry(QtCore.QRect(170, 30, 441, 251))
        self.reciver.setObjectName("reciver")
        self.yAxisdown = QtWidgets.QPushButton(self.centralWidget)
        self.yAxisdown.setGeometry(QtCore.QRect(120, 450, 91, 61))
        icon = QtGui.QIcon()
        icon.addPixmap(QtGui.QPixmap("../../Pyquino/core/icon/arrow-down-b.png"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.yAxisdown.setIcon(icon)
        self.yAxisdown.setIconSize(QtCore.QSize(30, 30))
        self.yAxisdown.setObjectName("yAxisdown")
        self.xAxisleft = QtWidgets.QPushButton(self.centralWidget)
        self.xAxisleft.setGeometry(QtCore.QRect(20, 450, 91, 61))
        icon1 = QtGui.QIcon()
        icon1.addPixmap(QtGui.QPixmap("../../Pyquino/core/icon/arrow-left-b.png"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.xAxisleft.setIcon(icon1)
        self.xAxisleft.setIconSize(QtCore.QSize(30, 30))
        self.xAxisleft.setObjectName("xAxisleft")
        self.xAxisrigh = QtWidgets.QPushButton(self.centralWidget)
        self.xAxisrigh.setGeometry(QtCore.QRect(220, 450, 91, 61))
        icon2 = QtGui.QIcon()
        icon2.addPixmap(QtGui.QPixmap("../../Pyquino/core/icon/arrow-right-b.png"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.xAxisrigh.setIcon(icon2)
        self.xAxisrigh.setIconSize(QtCore.QSize(30, 30))
        self.xAxisrigh.setObjectName("xAxisrigh")
        self.yAxisup = QtWidgets.QPushButton(self.centralWidget)
        self.yAxisup.setGeometry(QtCore.QRect(120, 380, 91, 61))
        icon3 = QtGui.QIcon()
        icon3.addPixmap(QtGui.QPixmap("../../Pyquino/core/icon/arrow-up-b.png"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.yAxisup.setIcon(icon3)
        self.yAxisup.setIconSize(QtCore.QSize(30, 30))
        self.yAxisup.setObjectName("yAxisup")
        self.widget = QtWidgets.QWidget(self.centralWidget)
        self.widget.setGeometry(QtCore.QRect(330, 290, 301, 211))
        self.widget.setObjectName("widget")
        self.addMachineVrep = QtWidgets.QPushButton(self.centralWidget)
        self.addMachineVrep.setGeometry(QtCore.QRect(60, 20, 91, 41))
        self.addMachineVrep.setObjectName("addMachineVrep")
        MainWindow.setCentralWidget(self.centralWidget)

        self.retranslateUi(MainWindow)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "MainWindow"))
        self.addMachine.setText(_translate("MainWindow", "add_machine"))
        self.simraution.setText(_translate("MainWindow", "stop_simuration"))
        self.restart.setText(_translate("MainWindow", "restart_simulation"))
        self.motors.setText(_translate("MainWindow", "motors"))
        self.yAxisdown.setText(_translate("MainWindow", "back"))
        self.xAxisleft.setText(_translate("MainWindow", "left"))
        self.xAxisrigh.setText(_translate("MainWindow", "right"))
        self.yAxisup.setText(_translate("MainWindow", "up"))
        self.addMachineVrep.setText(_translate("MainWindow", "AddMachine"))


if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    MainWindow = QtWidgets.QMainWindow()
    ui = Ui_MainWindow()
    ui.setupUi(MainWindow)
    MainWindow.show()
    sys.exit(app.exec_())

