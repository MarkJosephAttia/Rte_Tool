from PyQt5 import QtWidgets, QtGui, QtCore
from PyQt5.QtWidgets import *
from PyQt5.QtGui import *
from images import *



class MainWindow(QMainWindow):
    switch_create_window = QtCore.pyqtSignal()
    switch_open_window = QtCore.pyqtSignal()
    def __init__(self,toolName,toolIcon):
        super(MainWindow, self).__init__()
        self.setWindowTitle(toolName)
        self.setWindowIcon(QtGui.QIcon(toolIcon))

        self.menuBar = QtWidgets.QMenuBar(self)
        self.setMenuBar(self.menuBar)
        self.fileMenu = self.menuBar.addMenu('File')

        self.newProjectItem = QAction('New Project', self)
        self.fileMenu.addAction(self.newProjectItem)
        self.newProjectItem.triggered.connect(self.createProjectWindow)

        self.openExitProjectItem = QAction('Open Project', self)
        self.fileMenu.addAction(self.openExitProjectItem)
        self.openExitProjectItem.triggered.connect(self.openProjectWindow)

        self.exitItem = QAction('Exit', self)
        self.fileMenu.addAction(self.exitItem)
        self.exitItem.triggered.connect(self.exitItemAction)

        self.helpMenu = self.menuBar.addMenu('Help')
        self.helpMenuItem = QAction('About', self)
        self.helpMenu.addAction(self.helpMenuItem)

    def exitItemAction(self):
        QtWidgets.QApplication.quit()

    def createProjectWindow(self):
        self.switch_create_window.emit()

    def openProjectWindow(self):
        self.switch_open_window.emit()


