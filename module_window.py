import os

from PyQt5 import QtWidgets, QtGui, QtCore
from PyQt5.QtCore import QSize, QDir, QFile
from PyQt5.QtGui import *
from images import *
from PyQt5.QtWidgets import *
from InputPathes.InputPathes import Inputs
import module_configure
from Elements.Elements import Element 

class moduleWindow(QtWidgets.QMdiSubWindow):
    switch_window = QtCore.pyqtSignal()
    osCheck = ""
    swcsCheck = ""
    dataTypeCheck = ""


    def __init__(self,toolName,toolIcon):
        super(moduleWindow, self).__init__()
        self.setGeometry(400, 150, 550, 350)
        self.setWindowTitle(toolName)
        self.setWindowIcon(QtGui.QIcon(toolIcon))
        self.initui()
        module_configure.moduleConfg.treeOfCheckedModulesInit(module_configure.moduleConfg)

    def initui(self):
        self.OSlabel = QtWidgets.QLabel(self)
        self.OSlabel.setText("OS")
        self.OSlabel.move(5, 10)
        self.OSlabel.resize(80, 30)
        self.OSlabel.setFont(QtGui.QFont("Sanserif", 15))

        self.osTextBox = QLineEdit(self)
        self.osTextBox.setPlaceholderText("Please Enter The Name")
        self.osTextBox.move(105, 10)
        self.osTextBox.resize(200, 30)
        self.osTextBox.setToolTip('This is an example button')

        self.osButton = QtWidgets.QPushButton(self)
        self.osButton.setText("Choose Folder")
        self.osButton.move(330, 10)
        self.osButton.resize(100, 30)
        self.osButton.setFont(QtGui.QFont("Sanserif", 10))
        self.osButton.setToolTip('This is an example button')
        self.osButton.clicked.connect(self.selectOSFile)

        self.comlabel = QtWidgets.QLabel(self)
        self.comlabel.setText("Com")
        self.comlabel.move(5, 50)
        self.comlabel.resize(80, 30)
        self.comlabel.setFont(QtGui.QFont("Sanserif", 13))

        self.comTextBox = QLineEdit(self)
        self.comTextBox.setPlaceholderText("Please Choose The Folder")
        self.comTextBox.move(105, 50)
        self.comTextBox.resize(200, 30)
        self.comTextBox.setToolTip('This is an example button')

        self.comButton = QtWidgets.QPushButton(self)
        self.comButton.setText("Choose File")
        self.comButton.move(330, 50)
        self.comButton.resize(100, 30)
        self.comButton.setFont(QtGui.QFont("Sanserif", 10))
        self.comButton.setToolTip('This is an example button')
        self.comButton.clicked.connect(self.sellectComFile)

        self.swcslabel = QtWidgets.QLabel(self)
        self.swcslabel.setText("SwCs")
        self.swcslabel.move(5, 90)
        self.swcslabel.resize(80, 30)
        self.swcslabel.setFont(QtGui.QFont("Sanserif", 13))

        self.swcsTextBox = QPlainTextEdit(self)
        self.swcsTextBox.setPlaceholderText("Please Choose The Folder")
        self.swcsTextBox.setGeometry(105, 90, 200, 60)
        self.swcsTextBox.setToolTip('This is an example button')

        self.swcsButton = QtWidgets.QPushButton(self)
        self.swcsButton.setText("Choose File")
        self.swcsButton.setGeometry(330, 90, 100, 30)
        self.swcsButton.setFont(QtGui.QFont("Sanserif", 10))
        self.swcsButton.setToolTip('This is an example button')
        self.swcsButton.clicked.connect(self.sellectSwCsFile)

        self.dataTypeslabel = QtWidgets.QLabel(self)
        self.dataTypeslabel.setText("Data Types")
        self.dataTypeslabel.move(5, 160)
        self.dataTypeslabel.resize(90, 30)
        self.dataTypeslabel.setFont(QtGui.QFont("Sanserif", 13))

        self.dataTypesTextBox = QPlainTextEdit(self)
        self.dataTypesTextBox.setPlaceholderText("Please Choose The Folder")
        self.dataTypesTextBox.setGeometry(105, 160, 200, 60)
        self.dataTypesTextBox.setToolTip('This is an example button')

        self.dataTypesButton = QtWidgets.QPushButton(self)
        self.dataTypesButton.setText("Choose File")
        self.dataTypesButton.setGeometry(330, 160, 100, 30)
        self.dataTypesButton.setFont(QtGui.QFont("Sanserif", 10))
        self.dataTypesButton.setToolTip('This is an example button')
        self.dataTypesButton.clicked.connect(self.sellectDataTypesFile)


        self.createButton = QtWidgets.QPushButton(self)
        self.createButton.setText("Finish")
        self.createButton.move(350, 250)
        self.createButton.resize(150, 50)
        self.createButton.setFont(QtGui.QFont("Sanserif", 15))
        self.createButton.setIcon(QIcon(":/images/plus.png"))
        self.createButton.setIconSize(QSize(30, 30))
        self.createButton.setToolTip('This is an example button')
        self.createButton.clicked.connect(self.createName)

    def createName(self):
        self.osCheck = self.osTextBox.text()
        self.swcsCheck = self.swcsTextBox.toPlainText()
        self.dataTypesCheck = self.dataTypesTextBox.toPlainText()
        self.switch_window.emit()
        swcFiles = []
        swcFiles = self.swcsTextBox.toPlainText().split()
        Inputs(swcFiles)
        Inputs.DataTypesAndInterfaces_filePath = self.dataTypesTextBox.toPlainText()
        
        App_SWC = []
        Complex_Driver_SWC = []
        Service_Software_SWC = []

        Elements = Element()
        Elements.update()

        for i in Elements.Application_SWC_Types:
            for j in i.Ports:
                if j.Port_Type == 'R-Port':
                    module_configure.moduleConfg.portConnections[j.Name] = 'None'
        
        for i in Elements.Application_SWC_Types:
            if i.Type == 'Application SWC':
                App_SWC.append(i.Name)
            elif i.Type == 'Complex Device Driver SWC':
                Complex_Driver_SWC.append(i.Name)
            elif i.Type == 'Service SWC':
                Service_Software_SWC.append(i.Name)
        
        module_configure.moduleConfg.treeOfCheckedModules(module_configure.moduleConfg, App_SWC, 0)
        module_configure.moduleConfg.treeOfCheckedModules(module_configure.moduleConfg, Complex_Driver_SWC, 1)
        module_configure.moduleConfg.treeOfCheckedModules(module_configure.moduleConfg, Service_Software_SWC, 2)

        """if self.osCheck == "" or self.osCheck == " ":
            self.showPopupFileError('OS')

        elif self.swcsCheck == "" or self.swcsCheck == " ":
            self.showPopupFileError('SwCs')

        elif self.dataTypesCheck == "" or self.dataTypesCheck == " ":
            self.showPopupFileError('dataTypes and interface')
        else:
            self.switch_window.emit()
"""
    def sellectComFile(self):
        # open select folder dialog
        self.filePath = QFileDialog.getOpenFileName(self, 'choose file')
        if "Com.arxml" in self.filePath[0]:
            self.comTextBox.setText(self.filePath[0])
            #self.parser = GeneratedArxmlParser(filepath=self.filePath[0])
            #self.comModuleDataObject = self.parser.getModuleDataObject()
        else:
            self.showPopupFileError('Com')

    def sellectDataTypesFile(self):
        self.filePath1 = QFileDialog.getOpenFileNames(self, 'OpenFile')
        self.cutString1(self.filePath1[0][0])

    def selectOSFile(self):
        # open select folder dialog
        self.filePath1 = QFileDialog.getOpenFileName(self, 'choose file')
        if "Os.arxml" in self.filePath1[0]:
            self.osTextBox.setText(self.filePath1[0])
            #self.parser = GeneratedArxmlParser(filepath=self.filePath1[0])
            #self.osModuleDataObject = self.parser.getModuleDataObject()
        else:
            self.showPopupFileError('Os')

    def sellectSwCsFile(self):
        self.filePath1 = QFileDialog.getOpenFileNames(self, 'OpenFile')
        #self.filePath1 = QFileDialog.getOpenFileNames(self, 'choose file')
        # self.swcsTextBox.setText(self.filePath1[0][0] + ' || ' + self.filePath1[0][1])
        self.cutString(self.filePath1[0][0])

        # s.rfind

    def showPopupFileError(self, s):
        self.msg = QMessageBox()
        self.msg.setWindowTitle("error message")
        self.msg.setText("You must choose " + s + ".arxml File")
        msgRun = self.msg.exec_()

    def cutString(self, arr):
        # for as1 in arr:
        #     indexch = as1.rfind('/')
        #     print(as1[indexch + 1:])
        #     self.swcsTextBox.appendPlainText(as1[indexch + 1:])
        self.swcsTextBox.appendPlainText(arr)

    def cutString1(self, arr):
        # for as1 in arr:
        #     indexch = as1.rfind('/')
        #     print(as1[indexch + 1:])
        #     self.dataTypesTextBox.appendPlainText(as1[indexch + 1:])
        self.dataTypesTextBox.appendPlainText(arr)
