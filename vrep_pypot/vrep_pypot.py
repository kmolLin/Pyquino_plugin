# -*- coding: utf-8 -*-

"""
Module implementing MainWindow.
"""

from PyQt5.QtCore import *
from PyQt5.QtWidgets import *
from PyQt5.QtGui import *

from Ui_vrep_pypot import Ui_MainWindow

#from kernel.pypot.vrep import from_vrep
from kernel.customize import from_vrep
from kernel.pypot.vrep.io import VrepIO

import matplotlib
matplotlib.use('Qt5Agg')
from matplotlib.backends.backend_qt5agg import FigureCanvasQTAgg as FigureCanvas
from matplotlib.figure import Figure
from matplotlib_Dialog import MyMplCanvas

import time ,  math


# Make sure that we are using QT5
import json



class MainWindow(QMainWindow, Ui_MainWindow):
    
    def __init__(self, parent=None):
        super(MainWindow, self).__init__(parent)
        self.setupUi(self)
        self.initForms()
    
    def initForms(self):
        
        self.globaltime = 500
        
        self.addMachine.clicked.connect(self.__test__send)
        self.simraution.clicked.connect(self.__close_vrep__)
        self.restart.clicked.connect(self.__restart_simulation__)
        self.motors.clicked.connect(self.__motors__)
        self.yAxisup.clicked.connect(self.__gotoPosition__)
        self.xAxisleft.clicked.connect(self.__draw__)
        self.xAxisrigh.clicked.connect(self.__motorsDetail__)
        self.addMachineVrep.clicked.connect(self. __addMachine__)
        self.motorTable.cellChanged.connect(self.draw_motorforce)
        self.dc = MyMplCanvas(self, width=5, height=4, dpi=100)
        self.mainLayout.insertWidget(1, self.dc)
        
    def __addMachine__(self):
        # self.poppy = PoppyHumanoid(simulator='vrep')  ##這行我在想有沒有別的辦法可以改  poppy_ergo_jr.json  poppy_ergo_jr.ttt testfile2.ttt  config.json
        filename, _ = QFileDialog.getOpenFileName(self, caption="Open json config")
        if filename:
            fi = QFileInfo(filename).baseName()
            with open(fi+'.json') as f:
                self.config = json.load(f)
                #ttt = QFileDialog.getOpenFileName(self, caption="Open ttt file")
                self.simula_robot = from_vrep(self.config, '127.0.0.1', 19997, fi+'.ttt')  #讀取檔案
            self.updateMotorTable()
    
    @pyqtSlot(int, int)
    def draw_motorforce(self, row, column):
        if column==4 and row==self.motorname.currentIndex():
            print(self.motorTable.item(row, column).text())
            
            
        
        
    def __motorsDetail__(self):
        {m.name: m.present_position for m in self.simula_robot.motors}
        #print("name", name, "present_position", present_position)
        
        print('test')
    
     
    def __gotoPosition__(self):
        
        current = []
        self.simula_robot.goto_position({self.motorname.currentText(): self.motorTable.cellWidget(self.motorname.currentIndex(),2).value()},  10, 'minjerk', wait=False)
        for second in range(0, self.globaltime, 4):
            current.append(math.degrees(self.simula_robot.get_motor_position(self.motorname.currentText())))
            time.sleep(0.04)
            
        self.current = current
        print(self.current)
        self.times = [i/100 for i in range(0, 500, 4)]


     
    def __motors__(self):
        self.reciver.insertPlainText(str(self.simula_robot.motors))
        for e in self.simula_robot.motors:
            #print(type(e))
            print(e.name, e.id, e.present_position)
        #print(type(self.simula_robot.motors))
        #print(len(self.simula_robot.motors))
  
    def __test__send(self):
        
        print("call the machine")
        
    def __restart_simulation__(self):
        self.simula_robot.reset_simulation()
        self.updateMotorTable()
        print("restart_simulation")
    
    def __draw__(self):
        #getfilename = self.simula_robot.get_motor_force('m1')
        #currenttime = self.simula_robot.current_simulation_time()
        #print(getfilename, type(getfilename))
        print(len(self.times),len(self.current) )
        self.dc.update_figure(self.times, self.current)

    def updateMotorTable(self):
        if hasattr(self, 'simula_robot'):
            source = {e.id:[e.name, e.present_position] for e in self.simula_robot.motors}
            lables = sorted(list(source.keys()))
            if self.motorname.count()==0:
                for i in lables: self.motorname.addItem(source[i][0])
            for i in lables:
                pos = lables.index(i)
                e = source[i]
                table = self.motorTable
                if table.rowCount()!=len(self.simula_robot.motors):
                    for k in range(len(self.simula_robot.motors)): table.insertRow(k)
                table.setItem(pos, 0, QTableWidgetItem(str(i)))
                table.setItem(pos, 1, QTableWidgetItem(e[0]))
                present_position = QDoubleSpinBox()
                present_position.setMaximum(720)
                present_position.setMinimum(-720)
                present_position.setValue(e[1])
                table.setCellWidget(pos, 2, present_position)
                minimum = self.config['motors'][e[0]]['angle_limit'][0]
                maximum = self.config['motors'][e[0]]['angle_limit'][1]
                table.setItem(pos, 3, QTableWidgetItem("{}, {}".format(minimum, maximum)))
                table.setItem(pos, 4, QTableWidgetItem('{}'.format(self.simula_robot.get_motor_force(e[0]))))
    
    def closeEvent(self, event):
        self.__close_vrep__()
    
    def __close_vrep__(self):
        try:
            self.simula_robot.stop_simulation()
            print("close")
        except:
            print("no close")
    
    @pyqtSlot()
    def on_updataButton_clicked(self):
        table = self.motorTable
        names = [table.item(i, 1).text() for i in range(table.rowCount())]
        positions = [table.cellWidget(i, 2).value() for i in range(table.rowCount())]
        pos = dict(zip(names, positions))
        
        self.simula_robot.goto_position(pos, 5, 'minjerk', wait=False)
        self.updateMotorTable()
        
        current = []
        #self.simula_robot.goto_position({self.motorname.currentText(): self.motorTable.cellWidget(self.motorname.currentIndex(),2).value()},  10, 'minjerk', wait=False)
        for second in range(0, self.globaltime, 4):
            current.append(math.degrees(self.simula_robot.get_motor_position(self.motorname.currentText())))
            time.sleep(0.04)
            
        self.current = current
        #print(self.current)
        self.times = [i/100 for i in range(0, 500, 4)]
        #print(pos)

