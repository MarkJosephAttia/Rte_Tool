from PyQt5 import QtCore, QtWidgets, QtGui
from PyQt5.QtCore import QSize
from moduleConfgFrames import *
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
    switch_create_window = QtCore.pyqtSignal()
    switch_open_window = QtCore.pyqtSignal()

    projectName = ''

    def __init__(self,toolName,toolIcon):
        super(moduleConfg, self).__init__()

        self.windowFrame = Ui_MainWindow()
        self.windowFrame.setupUi(self)

        self.setWindowTitle(toolName)
        self.setWindowIcon(QtGui.QIcon(toolIcon))

        #self.parametersAndReferences = QScrollArea(self)
        self.windowFrame.parametersAndReferences.setWidgetResizable(True)
        #self.parametersAndReferences.setGeometry(500, 70, 850, 500)
        self.parametersAndReferencesRows = QFormLayout()
        groupBox = QGroupBox("Parameters")
        groupBox.setLayout(self.parametersAndReferencesRows)
        self.windowFrame.parametersAndReferences.setWidget(groupBox)

        #Create the View
        #self.checkedModulesView = QTreeView(self)
        #show header
        self.windowFrame.checkedModulesView.setHeaderHidden(True)
        #self.checkedModulesView.setGeometry(20, 70, 450, 500)
        
        self.checkedModulesTree = QStandardItemModel()
        #root of tree
        self.rootNode = self.checkedModulesTree.invisibleRootItem()
        
        self.moduleRoot = StandardItem('Modules', 10)

        self.windowFrame.checkedModulesView.clicked.connect(self.getValue)
        self.windowFrame.checkedModulesView.clicked.connect(self.showParamters)

        #self.windowFrame.checkedModulesView.clicked.connect(self.showDescription)
        #self.windowFrame.checkedModulesView.clicked.connect(self.showMultiplicity)

        #self.windowFrame.descriptionLabel = QtWidgets.QPlainTextEdit(self)
        self.windowFrame.descriptionLabel.appendPlainText("description information Label")
        #self.windowFrame.descriptionLabel.setGeometry(20, 580, 450, 120)
        self.windowFrame.descriptionLabel.setFont(QtGui.QFont("Sanserif", 10))
        self.windowFrame.descriptionLabel.setStyleSheet("""QLabel {border: 1px solid #000;}""")
        self.windowFrame.descriptionLabel.setReadOnly(True)

        #self.windowFrame.containerMultiplicityLabel = QtWidgets.QPlainTextEdit(self)
        self.windowFrame.containerMultiplicityLabel.appendPlainText("Container Multiplicity Label")
        #self.containerMultiplicityLabel.setGeometry(500, 580, 350, 120)
        self.windowFrame.containerMultiplicityLabel.setFont(QtGui.QFont("Sanserif", 10))
        self.windowFrame.containerMultiplicityLabel.setStyleSheet("""QLabel {border: 1px solid #000;}""")
        self.windowFrame.containerMultiplicityLabel.setReadOnly(True)

        #buttons
        #self.saveButton = QtWidgets.QPushButton(self)
        self.windowFrame.saveButton.setText("Save")
        #self.saveButton.move(1100, 620)
        self.windowFrame.saveButton.resize(90, 60)
        self.windowFrame.saveButton.setFont(QtGui.QFont("Sanserif", 11))
        self.windowFrame.saveButton.setToolTip('This is an example button')
        self.windowFrame.saveButton.setIcon(QIcon("save.png"))
        self.windowFrame.saveButton.setIconSize(QSize(25, 25))
        self.windowFrame.saveButton.clicked.connect(self.saveButtonFunction)


        #self.generateButton = QtWidgets.QPushButton(self)
        self.windowFrame.generateButton.setText("Generate")
        #self.generateButton.move(1200, 620)
        self.windowFrame.generateButton.resize(90, 60)
        self.windowFrame.generateButton.setFont(QtGui.QFont("Sanserif", 10))
        self.windowFrame.generateButton.setToolTip('This is an example button')
        self.windowFrame.generateButton.setIcon(QIcon("cg.png"))
        self.windowFrame.generateButton.setIconSize(QSize(22, 22))
        self.windowFrame.generateButton.clicked.connect(self.generateButtonFunction)

        self.showMenuBar()
        self.showToolBar()

        self.treeOfCheckedModules()

    def treeOfCheckedModules(self):
        self.checkedModulesTree = QStandardItemModel()
        self.rootNode = self.checkedModulesTree.invisibleRootItem()
        self.moduleRoot = StandardItem('Modules', 10)
        self.modulesCheckedList = ['asef','efrr','tge','wegw','rerg']
        for Module in self.modulesCheckedList:
            self.treeChildren = StandardItem(Module, 10)
            self.moduleRoot.appendRow(self.treeChildren)

        #set Tree root      
        self.rootNode.appendRow(self.moduleRoot)
        self.windowFrame.checkedModulesView.setModel(self.checkedModulesTree)
        self.windowFrame.checkedModulesView.expandAll()

    def showParamters(self):
        #this for loop to delete the old paramters before write new paramters
        for i in reversed(range(self.parametersAndReferencesRows.count())):
            self.parametersAndReferencesRows.itemAt(i).widget().deleteLater()

        comboBox = QComboBox()
        comboBox.addItem("None")
        comboBox.addItem("item1")
        comboBox.addItem("item2")
        self.parametersAndReferencesRows.addRow("test1", comboBox)

        comboBox1 = QLineEdit()
        self.parametersAndReferencesRows.addRow("test2", comboBox1)
        #to read the user input
        print(comboBox1.text())

    def getValue(self, val):
        print(val.data())
        print(val.row())

    def showMenuBar(self):
        #self.menuBar = QtWidgets.QMenuBar(self)
        #self.setMenuBar(self.menuBar)
        self.windowFrame.menuBar.setStyleSheet("""QMenuBar {border: 1px solid #000;}""")

        self.fileMenu = self.windowFrame.menuBar.addMenu('File')
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

        self.generateMenu = self.windowFrame.menuBar.addMenu('Generate')
        self.generateMenuItem = QAction('C Generate', self)
        self.generateMenu.addAction(self.generateMenuItem)

        self.settingMenu = self.windowFrame.menuBar.addMenu('Setting')
        self.settingMenuItem = QAction('Project Setting', self)
        self.settingMenu.addAction(self.settingMenuItem)

        self.helpMenu = self.windowFrame.menuBar.addMenu('Help')
        self.helpMenuItem = QAction('About', self)
        self.helpMenu.addAction(self.helpMenuItem)

    def exitItemAction(self):
        questionMessage = QMessageBox()
        ret = questionMessage.question(self, '', "Do you want to save project?",
                                           questionMessage.Yes | questionMessage.No | questionMessage.Cancel)
        questionMessage.setDefaultButton(questionMessage.Cancel)
        if ret == questionMessage.Yes:
            self.saveButtonFunction()
            QtWidgets.QApplication.quit()
        elif ret == questionMessage.No:
            QtWidgets.QApplication.quit()
        else:
            pass
                
    def showToolBar(self):
        #self.toolBar = QtWidgets.QToolBar(self)
        #self.addToolBar(self.toolBar)

        self.addToolBarItem = QAction("add", self)
        self.addToolBarItem.setIcon(QtGui.QIcon('plus.png'))
        self.windowFrame.toolBar.addAction(self.addToolBarItem)
        #self.addToolBarItem.triggered.connect(self.addContainers)

        self.deleteToolBarItem = QAction("delete", self)
        self.deleteToolBarItem.setIcon(QtGui.QIcon('delete.jpg'))
        self.windowFrame.toolBar.addAction(self.deleteToolBarItem)
        #self.deleteToolBarItem.triggered.connect(self.deleteSelectedContainer)

    def createProjectWindow(self):
        self.switch_create_window.emit()

    def openProjectWindow(self):
        self.switch_open_window.emit()

    def saveButtonFunction(self):
        #when user press on sace button write here what do you want to execute
        pass

    def generateButtonFunction(self):
        # when user press on generate button write here what do you want to execute
        pass

    def showPopUpmCompleteMessage(self,massage):
        msg = QMessageBox()
        msg.setWindowTitle("message")
        msg.setText(massage)
        msgRun = msg.exec_()


    def getFolderDirection(self,folderdir):
        self.folderNameDir = folderdir
        print(self.folderNameDir)

    def closeEvent(self, a0: QtGui.QCloseEvent) -> None:
        questionMessage = QMessageBox()
        ret = questionMessage.question(self, '', "Do you want to save project?",questionMessage.Yes | questionMessage.No | questionMessage.Cancel)
        questionMessage.setDefaultButton(questionMessage.Cancel)
        if ret == questionMessage.Yes:
            self.saveButtonFunction()
            a0.accept()
        elif ret == questionMessage.No:
            a0.accept()
        else:
            a0.ignore()
    
    def errorMessageEnterNumber(self):
        self.msg = QMessageBox()
        self.msg.setWindowTitle("Error message")
        self.msg.setText("You must enter number only")
        msgRun = self.msg.exec_()
        
    def showDescription(self):
        self.windowFrame.descriptionLabel.clear()
        self.windowFrame.descriptionLabel.appendPlainText('put string here')

    def showMultiplicity(self):
        self.windowFrame.containerMultiplicityLabel.clear()
        self.windowFrame.containerMultiplicityLabel.appendPlainText('put string here')

    def projectName(self, name):
        self.projectName = name
        print(self.projectName)
