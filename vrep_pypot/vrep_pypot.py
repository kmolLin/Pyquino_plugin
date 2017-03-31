# -*- coding: utf-8 -*-

"""
Module implementing MainWindow.
"""

from PyQt5.QtCore import pyqtSlot
from PyQt5.QtWidgets import QMainWindow

from Ui_vrep_pypot import Ui_MainWindow

from pypot.vrep import from_vrep
from poppy_humanoid import PoppyHumanoid

import random
import matplotlib
# Make sure that we are using QT5
matplotlib.use('Qt5Agg')
from matplotlib.backends.backend_qt5agg import FigureCanvasQTAgg as FigureCanvas
from matplotlib.figure import Figure
from numpy import arange, sin, pi
from mpl_toolkits.mplot3d import Axes3D


class MainWindow(QMainWindow, Ui_MainWindow):
    """
    Class documentation goes here.
    """
    def __init__(self, parent=None):
        """
        Constructor
        
        @param parent reference to the parent widget
        @type QWidget
        """
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
        self.poppy = PoppyHumanoid(simulator='vrep')  ##這行我在想有沒有別的辦法可以改
        
        
        
    def __motorsDetail__(self):
        {m.name: m.present_position for m in self.poppy.motors  }
        #print("name", name, "present_position", present_position)
        
        print('test')
    
     
    def __gotoPosition__(self):
        
        self.poppy.head_z.goto_position(45, 2, wait=False)
        self.poppy.head_y.goto_position(-30, 2, wait=True)
        self.poppy.head_z.goto_position(0, 2, wait=True)
        self.poppy.head_y.goto_position(20, 1, wait=True)
     
    def __motors__(self):
        self.reciver.insertPlainText(str(self.poppy.motors))
        print(self.poppy.motors)
  
    def __test__send(self):
        self.poppy = PoppyHumanoid(simulator='vrep')
        print("call the machine")
        
    def __restart_simulation__(self):
        self.poppy.reset_simulation()
        print("restart_simulation")
        
    def __draw__(self):
        reached_pt = []

        for m in self.poppy.l_arm:
            m.goto_behavior = 'minjerk'
            print(m)

        # We generate 25 random arm configuration
        # and stores the reached position of the forearm
        for _ in range(25):
            #self.poppy.reset_simulation()
            
            # Generate a position by setting random position (within the angle limit) to each joint
            # This can be hacked to define other exploration
            #print(min(m.angle_limit),max(m.angle_limit) )
            pos = {m.name: random.randint(-148, 1) for m in self.poppy.l_arm}    
            self.poppy.goto_position(pos, 2., wait=True)
                
            reached_pt.append(self.poppy.get_object_position('l_forearm_visual'))
            
    
    def __close_vrep__(self):
        self.poppy.stop_simulation()
        print("close")
        
