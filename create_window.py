import os

from PyQt5 import QtWidgets, QtGui, QtCore
from PyQt5.QtCore import *
from PyQt5.QtGui import *

from images import *
from PyQt5.QtWidgets import *
import module_configure
from Elements.Elements import Element 

class createWindow(QtWidgets.QMdiSubWindow):
    switch_window = QtCore.pyqtSignal()
    name = ""
    dirFolder = ""
    newdir = ""

    def __init__(self,toolName,toolIcon):
        super(createWindow,self).__init__()
        self.setGeometry(400, 150, 550, 350)
        self.setWindowTitle(toolName)
        self.setWindowIcon(QtGui.QIcon(toolIcon))

        self.initui()

    def initui(self):
        self.label = QtWidgets.QLabel(self)
        self.label.setText("Project Name:")
        self.label.move(5, 60)
        self.label.resize(200, 30)
        self.label.setFont(QtGui.QFont("Sanserif", 15))

        self.nameTextBox = QLineEdit(self)
        self.nameTextBox.setPlaceholderText("Please Enter The Name")
        self.nameTextBox.move(10, 90)
        self.nameTextBox.resize(200, 30)
        self.nameTextBox.setToolTip('This is an example button')

        self.createButton = QtWidgets.QPushButton(self)
        self.createButton.setText("Next")
        self.createButton.move(350, 250)
        self.createButton.resize(150, 50)
        self.createButton.setFont(QtGui.QFont("Sanserif", 15))
        self.createButton.setIcon(QIcon(":/images/plus.png"))
        self.createButton.setIconSize(QSize(30, 30))
        self.createButton.setToolTip('This is an example button')
        self.createButton.clicked.connect(self.createName)

        self.folderTextBox = QLineEdit(self)
        self.folderTextBox.setPlaceholderText("Please Choose The Folder")
        self.folderTextBox.move(10, 140)
        self.folderTextBox.resize(200, 30)
        self.folderTextBox.setToolTip('This is an example button')

        self.dirButton = QtWidgets.QPushButton(self)
        self.dirButton.setText("Folder")
        self.dirButton.setIcon(QIcon("folder1.png"))
        self.dirButton.setIconSize(QSize(20, 20))
        self.dirButton.move(220, 140)
        self.dirButton.resize(100, 30)
        self.dirButton.setFont(QtGui.QFont("Sanserif", 10))
        self.dirButton.setToolTip('This is an example button')
        self.dirButton.clicked.connect(self.changeFolder)

    def createName(self):
        self.name = self.nameTextBox.text()
        if self.name == "" or self.name == " ":
            #self.show_popup_name_error()
            #MARK#
            self.switch_window.emit()

        elif self.dirFolder == "" or self.dirFolder == " ":
            self.show_popup_folder_error()

        else:

            self.directory = QDir()

            pathCheck = self.dirFolder + '/' + self.nameTextBox.text()
            isFile = os.path.isdir(pathCheck)
            print(isFile)
            print(pathCheck)
            if isFile:
                self.show_popup_changename_error()
            else:
                self.directory.setPath(self.dirFolder)
                self.directory.mkdir(self.nameTextBox.text())
                self.newdir = self.dirFolder + '/' + self.nameTextBox.text()
                #self.directory.setPath(self.newdir)
                #self.directory.mkdir('ECUC')
                #self.directory.mkdir('Cgen')
                #self.directory.mkdir('Cgenerators')
                #self.directory.mkdir('inputs')

                #filenameex = self.nameTextBox.text() + '.asu'

                #filepath = os.path.join(self.newdir, filenameex)
                #if not os.path.exists(self.newdir):
                    #os.makedirs(self.newdir)
                #f = open(filepath, "a")

                self.switch_window.emit()

    def show_popup_changename_error(self):
        self.msg = QMessageBox()
        self.msg.setWindowTitle("error message")
        self.msg.setText("The name of the project exists , you should change the name")
        msgRun = self.msg.exec_()

    def show_popup_name_error(self):
        self.msg = QMessageBox()
        self.msg.setWindowTitle("error message")
        self.msg.setText("You must put name")
        msgRun = self.msg.exec_()

    def show_popup_folder_error(self):
        self.msg = QMessageBox()
        self.msg.setWindowTitle("error message")
        self.msg.setText("You must choose folder")
        msgRun = self.msg.exec_()

    def changeFolder(self):
        # open select folder dialog
        self.dirFolder = QFileDialog.getExistingDirectory(self, 'Select a directory')
        self.folderTextBox.setText(self.dirFolder)










