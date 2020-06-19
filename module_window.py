from PyQt5 import QtCore, QtWidgets, QtGui
from PyQt5.QtCore import QSize

from images import *
from PyQt5.QtWidgets import *
from PyQt5.Qt import *
from PyQt5.QtGui import QFont, QColor, QIcon
import copy

class StandardItem(QStandardItem):
    def __init__(self, txt='', font_size=12, set_bold=False, color=QColor(0, 0, 0)):
        super().__init__()

        fnt = QFont('Open Sans', font_size)
        fnt.setBold(set_bold)
        self.setEditable(False)
        self.setForeground(color)
        self.setFont(fnt)
        self.setText(txt)

class moduleConfg(QMainWindow):
    switch_window = QtCore.pyqtSignal()
    x = 0
    listCheckModules = []
    listCheckModules1 = []

    def __init__(self, toolName, toolIcon):
        super(moduleConfg, self).__init__()
        self.setGeometry(80, 80, 950, 600)
        self.setWindowTitle(toolName)
        self.setWindowIcon(QtGui.QIcon(toolIcon))

        self.selectedItemPath = None
        self.selectedContainer = None
        self.clickedData = None
        self.selectedItemType = None
        self.selectedContainerContList = None
        self.selectedContainerContListPath = None

        self.parametersAndReferences = QScrollArea(self)
        self.parametersAndReferences.setWidgetResizable(True)
        self.parametersAndReferences.setGeometry(500, 70, 850, 500)
        self.parametersAndReferencesRows = QFormLayout()
        groupBox = QGroupBox("Parameters")
        groupBox.setLayout(self.parametersAndReferencesRows)
        self.parametersAndReferences.setWidget(groupBox)

        # Create the View
        self.checkedModulesView = QTreeView(self)
        # show header
        self.checkedModulesView.setHeaderHidden(True)
        self.checkedModulesView.setGeometry(20, 70, 450, 500)

        self.checkedModulesTree = QStandardItemModel()
        # root of tree
        self.rootNode = self.checkedModulesTree.invisibleRootItem()

        self.moduleRoot = StandardItem('Modules', 10)

        #self.checkedModulesView.clicked.connect(self.saveParameters)
        #self.checkedModulesView.clicked.connect(self.getValue)
        #self.checkedModulesView.clicked.connect(self.showParamters)

        #self.checkedModulesView.clicked.connect(self.showDescription)
        #self.checkedModulesView.clicked.connect(self.showMultiplicity)

        self.descriptionLabel = QtWidgets.QPlainTextEdit(self)
        self.descriptionLabel.appendPlainText("description information Label")
        self.descriptionLabel.setGeometry(20, 580, 450, 120)
        self.descriptionLabel.setFont(QtGui.QFont("Sanserif", 10))
        self.descriptionLabel.setStyleSheet("""QLabel {border: 1px solid #000;}""")
        self.descriptionLabel.setReadOnly(True)

        self.containerMultiplicityLabel = QtWidgets.QPlainTextEdit(self)
        self.containerMultiplicityLabel.appendPlainText("Container Multiplicity Label")
        self.containerMultiplicityLabel.setGeometry(500, 580, 350, 120)
        self.containerMultiplicityLabel.setFont(QtGui.QFont("Sanserif", 10))
        self.containerMultiplicityLabel.setStyleSheet("""QLabel {border: 1px solid #000;}""")
        self.containerMultiplicityLabel.setReadOnly(True)

        # buttons
        self.saveButton = QtWidgets.QPushButton(self)
        self.saveButton.setText("Save")
        self.saveButton.move(1100, 620)
        self.saveButton.resize(90, 60)
        # self.saveButton.setFont(QtGui.QFont("Sanserif", 15))
        self.saveButton.setToolTip('This is an example button')
        self.saveButton.setStyleSheet("QPushButton:hover:!pressed"
                                      "{background-color: rgba(0,0,255,0.8);"
                                      "border:4px solid #000;"
                                      "border-width: 2px;"
                                      "border-color: black;"
                                      "border-radius: 10px;"
                                      "font: 18px;}"
                                      "QPushButton:!hover:!pressed"
                                      "{background-color: rgba(0,0,255,1);"
                                      "color:white;"
                                      "border:4px solid #000;"
                                      "border-width: 2px;"
                                      "border-color: black;"
                                      "border-radius: 10px;"
                                      "font: bold 16px;}"
                                      "QPushButton:pressed"
                                      "{background-color: rgba(0,0,255,0.5);"
                                      "border:4px solid #000;"
                                      "border-width: 1px;"
                                      "border-color: grey;"
                                      "border-radius: 10px;"
                                      "font: bold 16px;}")

        #self.saveButton.clicked.connect(self.saveButtonFunction)

        self.generateButton = QtWidgets.QPushButton(self)
        self.generateButton.setText("Generate")
        self.generateButton.move(1200, 620)
        self.generateButton.resize(90, 60)
        # self.generateButton.setFont(QtGui.QFont("Sanserif", 12))
        self.generateButton.setToolTip('This is an example button')
        self.generateButton.setStyleSheet("QPushButton:hover:!pressed"
                                          "{background-color: rgba(255,0,0,0.8);"
                                          "border:4px solid #000;"
                                          "border-width: 2px;"
                                          "border-color: black;"
                                          "border-radius: 10px;"
                                          "font: 16px;}"
                                          "QPushButton:!hover:!pressed"
                                          "{background-color: rgba(255,0,0,1);"
                                          "color:white;"
                                          "border:4px solid #000;"
                                          "border-width: 2px;"
                                          "border-color: black;"
                                          "border-radius: 10px;"
                                          "font: bold 14px;}"
                                          "QPushButton:pressed"
                                          "{background-color: rgba(255,0,0,0.5);"
                                          "border:4px solid #000;"
                                          "border-width: 1px;"
                                          "border-color: grey;"
                                          "border-radius: 10px;"
                                          "font: bold 14px;}")
        #self.generateButton.clicked.connect(self.generateButtonFunction)

        self.showMenuBar()
        self.showToolBar()

    def showMenuBar(self):
        self.menuBar = QtWidgets.QMenuBar(self)
        self.setMenuBar(self.menuBar)
        self.menuBar.setStyleSheet("""QMenuBar {border: 1px solid #000;}""")

        self.fileMenu = self.menuBar.addMenu('File')
        self.newProjectItem = QAction('New Project', self)
        self.fileMenu.addAction(self.newProjectItem)
        #self.newProjectItem.triggered.connect(self.createProjectWindow)

        self.openExitProjectItem = QAction('Open Project', self)
        self.fileMenu.addAction(self.openExitProjectItem)
        #self.openExitProjectItem.triggered.connect(self.exitItemAction)

        self.saveProjectItem = QAction('Save', self)
        self.fileMenu.addAction(self.saveProjectItem)
        #self.saveProjectItem.triggered.connect(self.saveButtonFunction)

        self.exitItem = QAction('Exit', self)
        self.fileMenu.addAction(self.exitItem)
        #self.exitItem.triggered.connect(self.exitItemAction)

        self.generateMenu = self.menuBar.addMenu('Generate')
        self.generateMenuItem = QAction('C Generate', self)
        #self.generateMenu.addAction(self.generateMenuItem)

        self.settingMenu = self.menuBar.addMenu('Setting')
        self.settingMenuItem = QAction('Project Setting', self)
        #self.settingMenu.addAction(self.settingMenuItem)

        self.helpMenu = self.menuBar.addMenu('Help')
        self.helpMenuItem = QAction('About', self)
        #self.helpMenu.addAction(self.helpMenuItem)

    def exitItemAction(self):
        if self.saveFlag:
            QtWidgets.QApplication.quit()
        else:
            questionMessage = QMessageBox()
            ret = questionMessage.question(self, '', "Do you want to save project?",
                                           questionMessage.Yes | questionMessage.No | questionMessage.Cancel)
            questionMessage.setDefaultButton(questionMessage.Cancel)
            if ret == questionMessage.Yes:
                self.saveButtonFunction()
                QtWidgets.QApplication.quit()
            elif ret == questionMessage.No:
                QtWidgets.QApplication.quit()

    def showToolBar(self):
        self.toolBar = QtWidgets.QToolBar(self)
        self.addToolBar(self.toolBar)

        self.addToolBarItem = QAction("add", self)
        self.addToolBarItem.setIcon(QtGui.QIcon('plus.png'))
        self.toolBar.addAction(self.addToolBarItem)
        #self.addToolBarItem.triggered.connect(self.addContainers)

        self.deleteToolBarItem = QAction("delete", self)
        self.deleteToolBarItem.setIcon(QtGui.QIcon('delete.jpg'))
        self.toolBar.addAction(self.deleteToolBarItem)
        #self.deleteToolBarItem.triggered.connect(self.deleteSelectedContainer)

    def show_popup_message(self):
        msg = QMessageBox()
        msg.setWindowTitle("error message")
        msg.setText("No Module is Checked")
        msgRun = msg.exec_()

    def configure_button(self):
        if self.x == 1:
            self.switch_window.emit()
        else:
            self.show_popup_message()
