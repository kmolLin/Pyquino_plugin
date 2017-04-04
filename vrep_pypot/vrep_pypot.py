# -*- coding: utf-8 -*-

"""
Module implementing MainWindow.
"""

from PyQt5.QtCore import *
from PyQt5.QtWidgets import *

from Ui_vrep_pypot import Ui_MainWindow

from pypot.vrep import from_vrep
import matplotlib
# Make sure that we are using QT5
import json



class MainWindow(QMainWindow, Ui_MainWindow):
    
    def __init__(self, parent=None):
        
        super(MainWindow, self).__init__(parent)
        self.setupUi(self)
        self.initForms()
        
        
    def initForms(self):
        
        self.addMachine.clicked.connect(self.__test__send)
        self.simraution.clicked.connect(self.__close_vrep__)
        self.restart.clicked.connect(self.__restart_simulation__)
        self.motors.clicked.connect(self.__motors__)
        self.yAxisup.clicked.connect(self.__gotoPosition__)
        self.xAxisleft.clicked.connect(self.__draw__)
        self.xAxisrigh.clicked.connect(self.__motorsDetail__)
        self.addMachineVrep.clicked.connect(self. __addMachine__)
        
        
        
    def __addMachine__(self):
        # self.poppy = PoppyHumanoid(simulator='vrep')  ##這行我在想有沒有別的辦法可以改  poppy_ergo_jr.json  poppy_ergo_jr.ttt testfile2.ttt  config.json
        with open('poppy_humanoid.json') as f:
            self.config = json.load(f)
            self.simula_robot = from_vrep(self.config, '127.0.0.1', 19997, 'poppy_humanoid.ttt')  #讀取檔案
        self.updateMotorTable()
        
    def __motorsDetail__(self):
        {m.name: m.present_position for m in self.simula_robot.motors}
        #print("name", name, "present_position", present_position)
        
        print('test')
    
     
    def __gotoPosition__(self):
        
        #self.simula_robot.m1.goto_position(45, 2, wait=False)
        
        self.simula_robot.m1.goto_position(45, 10, 'minjerk' ,wait=True)
        self.simula_robot.m6.goto_position(30, 10, 'minjerk' ,wait=True)
        self.simula_robot.m1.goto_position(0, 10,'minjerk' , wait=True)
        self.simula_robot.m6.goto_position(20, 10, 'minjerk' ,wait=True)
        
        #self.simula_robot.m3.goto_position(45, 10, wait=False)
        #self.simula_robot.m3.goto_position(0, 2, wait=True)
        
     
    def __motors__(self):
        self.reciver.insertPlainText(str(self.simula_robot.motors))
        for e in self.simula_robot.motors:
            #print(type(e))
            print(e.name, e.id, e.present_position)
        print(type(self.simula_robot.motors))
        #print(len(self.simula_robot.motors))
  
    def __test__send(self):
        
        print("call the machine")
        
    def __restart_simulation__(self):
        self.simula_robot.reset_simulation()
        self.updateMotorTable()
        print("restart_simulation")
        
    def __draw__(self):
        reached_pt = []
        reached_pos=[]
        for m in self.simula_robot.tip:
            m.goto_behavior = 'minjerk'
        
        for _ in range(1):
            #print(min(m.angle_limit),max(m.angle_limit) )
            names = [e.name for e in self.simula_robot.tip]
            #print(names)
            currentPositions = [e.present_position for e in self.simula_robot.tip]
            positions = [currentPositions[0]+10, currentPositions[1]+10, currentPositions[2]+10]
            pos = dict(zip(names, positions))
            self.simula_robot.goto_position(pos, 2., wait=True)
            reached_pt.append(self.simula_robot.get_object_position)
            reached_pos.append(pos)
            #reached_pt.append(self.simula_robot.get_object_position('l_forearm_visual'))
        self.updateMotorTable()
            
        #print(reached_pt)

    def updateMotorTable(self):
        if hasattr(self, 'simula_robot'):
            source = {e.id:[e.name, e.present_position] for e in self.simula_robot.motors}
            lables = sorted(list(source.keys()))
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
    
    def closeEvent(self, event):
        self.__close_vrep__()
    
    def __close_vrep__(self):
        self.simula_robot.stop_simulation()
        print("close")
    
    @pyqtSlot()
    def on_updataButton_clicked(self):
        table = self.motorTable
        names = [table.item(i, 1).text() for i in range(table.rowCount())]
        positions = [table.cellWidget(i, 2).value() for i in range(table.rowCount())]
        pos = dict(zip(names, positions))
        print(pos)
        self.simula_robot.goto_position(pos, 2., 'minjerk', wait=True)
