
from PyQt5 import QtWidgets, QtGui, QtCore
from PyQt5.QtCore import QSize, QDir
from PyQt5.QtGui import *
from images import *
from PyQt5.QtWidgets import *
#from GeneratedArxmlParser.GeneratedArxmlParser import *


class openExitProject(QtWidgets.QMdiSubWindow):
    switch_window = QtCore.pyqtSignal()
    filePath = ''

    def __init__(self,toolName,toolIcon):
        super(openExitProject,self).__init__()
        self.setGeometry(400, 150, 550, 350)
        self.setWindowTitle(toolName)
        self.setWindowIcon(QtGui.QIcon(toolIcon))
        self.initui()

    def initui(self):
        self.label = QtWidgets.QLabel(self)
        self.label.setText("Choose File")
        self.label.move(10, 110)
        self.label.setFont(QtGui.QFont("Sanserif", 15))

        self.folderTextBox = QLineEdit(self)
        self.folderTextBox.setPlaceholderText("Please Choose The Folder")
        self.folderTextBox.move(10, 140)
        self.folderTextBox.resize(200, 30)
        self.folderTextBox.setToolTip('This is an example button')

        self.dirButton = QtWidgets.QPushButton(self)
        self.dirButton.setText("Choose Folder")
        self.dirButton.move(220, 140)
        self.dirButton.resize(100, 30)
        self.dirButton.setFont(QtGui.QFont("Sanserif", 10))
        self.dirButton.setToolTip('This is an example button')
        self.dirButton.clicked.connect(self.changeFolder)

        self.createButton = QtWidgets.QPushButton(self)
        self.createButton.setText("Next")
        self.createButton.move(350, 250)
        self.createButton.resize(150, 50)
        self.createButton.setFont(QtGui.QFont("Sanserif", 15))
        self.createButton.setIcon(QIcon(":/images/plus.png"))
        self.createButton.setIconSize(QSize(30, 30))
        self.createButton.setToolTip('This is an example button')
        self.createButton.clicked.connect(self.openExitFile)

    def openExitFile(self):
        if self.filePath[0] == "" or self.dirFolder == " ":
            self.show_popup_folder_error()

        else:
            self.switch_window.emit()


    def changeFolder(self):
        # open select folder dialog
        self.filePath = QFileDialog.getOpenFileName(self, 'choose file')
        self.folderTextBox.setText(self.filePath[0])
        #self.parser = GeneratedArxmlParser(filepath=self.filePath)
        #self.moduleDataObject = self.parser.getModuleDataObject()

    def show_popup_folder_error(self):
        self.msg = QMessageBox()
        self.msg.setWindowTitle("error message")
        self.msg.setText("You must choose folder")
        msgRun = self.msg.exec_()
