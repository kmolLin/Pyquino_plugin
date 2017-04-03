# -*- coding: utf-8 -*-

"""
Module implementing MainWindow.
"""

from PyQt5.QtCore import pyqtSlot
from PyQt5.QtWidgets import QMainWindow

from Ui_vrep_pypot import Ui_MainWindow

from pypot.vrep import from_vrep

import random
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
       with open('config.json') as f:
        config = json.load(f)
        print(config)
        self.simula_robot = from_vrep(config, '127.0.0.1', 19997, 'testfile2.ttt')  #讀取檔案
        
        
    def __motorsDetail__(self):
        {m.name: m.present_position for m in self.simula_robot.motors  }
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
        print(len(self.simula_robot.motors))
  
    def __test__send(self):
        
        print("call the machine")
        
    def __restart_simulation__(self):
        self.simula_robot.reset_simulation()
        print("restart_simulation")
        
    def __draw__(self):
        reached_pt = []
        reached_pos=[]
        for m in self.simula_robot.tip:
            m.goto_behavior = 'minjerk'
            print(m)
            

        # We generate 25 random arm configuration
        # and stores the reached position of the forearm
        for _ in range(10):
            #self.poppy.reset_simulation()
            
            # Generate a position by setting random position (within the angle limit) to each joint
            # This can be hacked to define other exploration
            #print(min(m.angle_limit),max(m.angle_limit) )
            
            pos = {m.name: random.randint(180, 360) for m in self.simula_robot.tip}    
            self.simula_robot.goto_position(pos, 2., wait=True)
            reached_pt.append(self.simula_robot.get_object_position)
            reached_pos.append(pos)
            #reached_pt.append(self.simula_robot.get_object_position('l_forearm_visual'))
            
        print(reached_pt)
        #print(reached_pos, end='\n')
            
    
    def __close_vrep__(self):
        self.simula_robot.stop_simulation()
        print("close")
        
