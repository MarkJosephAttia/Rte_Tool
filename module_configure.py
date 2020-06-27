from PyQt5 import QtCore, QtWidgets, QtGui
from PyQt5.QtCore import QSize
from moduleConfgFrames import *
from images import *
from PyQt5.QtWidgets import *
from PyQt5.Qt import *
from PyQt5.QtGui import QFont, QColor, QIcon
import copy
from Elements.Elements import Element
import functools
from PyQt5.QtCore import pyqtSlot
import sys
#import module_window


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
    windowFrame = Ui_MainWindow()

    checkedModulesTree = None
    rootNode = None
    Application_Root = None
    CDD_Root = None
    Service_Root = None
    BSW_Root = None
    comboBox = None


    def __init__(self,toolName,toolIcon):
        super(moduleConfg, self).__init__()

        self.windowFrame.setupUi(self)

        self.setWindowTitle(toolName)
        self.setWindowIcon(QtGui.QIcon(toolIcon))

        #self.parametersAndReferences = QScrollArea(self)
        self.windowFrame.parametersAndReferences.setWidgetResizable(True)
        #self.parametersAndReferences.setGeometry(500, 70, 850, 500)
        self.parametersAndReferencesRows = QFormLayout()
        groupBox = QGroupBox("Configurations")
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
        

        self.windowFrame.checkedModulesView.clicked.connect(self.getValue)
        self.windowFrame.checkedModulesView.clicked.connect(self.showConfigurations)

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

    def treeOfCheckedModulesInit(self):
        self.checkedModulesTree = QStandardItemModel()
        self.rootNode = self.checkedModulesTree.invisibleRootItem()
        self.Application_Root = StandardItem('Application Software Component', 10)
        self.CDD_Root = StandardItem('Complex Device Driver Software Component', 10)
        self.Service_Root = StandardItem('Service Software Component', 10)
        self.BSW_Root = StandardItem('BSW Functions', 10)

    def treeOfCheckedModules(self, SWC, key):
        for Module in SWC:
            self.treeChildren = StandardItem(Module, 10)
            if key == 0:
                self.Application_Root.appendRow(self.treeChildren)
            elif key == 1:
                self.CDD_Root.appendRow(self.treeChildren)
            elif key == 2:
                self.Service_Root.appendRow(self.treeChildren)

            self.PortSrandardItem = StandardItem('Ports', 8)
            self.P_PortSrandardItem = StandardItem('R Ports', 8)
            self.R_PortSrandardItem = StandardItem('P Ports', 8)
            self.RunnableSrandardItem = StandardItem('Runnables', 8)
            self.treeChildren.appendRow(self.PortSrandardItem)
            self.treeChildren.appendRow(self.RunnableSrandardItem)
            self.PortSrandardItem.appendRow(self.R_PortSrandardItem)
            self.PortSrandardItem.appendRow(self.P_PortSrandardItem)

        #set Tree root      
        self.rootNode.appendRow(self.Application_Root)
        self.rootNode.appendRow(self.CDD_Root)
        self.rootNode.appendRow(self.Service_Root)
        self.rootNode.appendRow(self.BSW_Root)
        self.windowFrame.checkedModulesView.setModel(self.checkedModulesTree)
        self.windowFrame.checkedModulesView.expandAll()

    def showConfigurations(self):
        for i in reversed(range(self.parametersAndReferencesRows.count())):
            if self.parametersAndReferencesRows.itemAt(i).widget() is not None:
                self.parametersAndReferencesRows.itemAt(i).widget().deleteLater()
            else:
                for j in reversed(range(self.parametersAndReferencesRows.itemAt(i).layout().count())):
                    self.parametersAndReferencesRows.itemAt(i).layout().itemAt(j).widget().deleteLater()
                self.parametersAndReferencesRows.removeItem(self.parametersAndReferencesRows.itemAt(i).layout())

        if self.windowFrame.checkedModulesView.selectedIndexes()[0].data(Qt.DisplayRole) == 'BSW Functions':
            for i in range(0,5):
                layout = QHBoxLayout()

                checkBox = QCheckBox("Is Included")
                
                taskCB = QComboBox()
                taskCB.addItem("None")
                posCB = QComboBox()
                posCB.addItem("None")

                priodCB = QSpinBox()

                taskL = QLabel()
                taskL.setText("Task")
                taskL.setAlignment(QtCore.Qt.AlignRight | QtCore.Qt.AlignVCenter)
                posL = QLabel()
                posL.setText("Position")
                posL.setAlignment(QtCore.Qt.AlignRight | QtCore.Qt.AlignVCenter)
                priodL = QLabel()
                priodL.setText("Priodicity")
                priodL.setAlignment(QtCore.Qt.AlignRight | QtCore.Qt.AlignVCenter)
                
                layout.addWidget(checkBox)
                layout.addWidget(taskL)
                layout.addWidget(taskCB)
                layout.addWidget(posL)
                layout.addWidget(posCB)
                layout.addWidget(priodL)
                layout.addWidget(priodCB)

                if i == 0:
                    self.parametersAndReferencesRows.addRow("Com_MainFunctionRx", layout)
                elif i == 1:
                    self.parametersAndReferencesRows.addRow("Com_MainFunctionTx", layout)
                elif i == 2:
                    self.parametersAndReferencesRows.addRow("CanTp_MainFunction", layout)
                elif i == 3:
                    self.parametersAndReferencesRows.addRow("Can_MainFunction_Read", layout)
                elif i == 4:
                    self.parametersAndReferencesRows.addRow("Can_MainFunction_Write", layout)
        elif self.windowFrame.checkedModulesView.selectedIndexes()[0].data(Qt.DisplayRole) == 'Runnables' :
            
            Elements = Element()
            Elements.update()

            for i in Elements.Application_SWC_Types:
                if self.windowFrame.checkedModulesView.selectedIndexes()[0].parent().data(Qt.DisplayRole) == i.Name:
                    for j in i.InternalBehavoirs:
                        for k in j.Runnables:
                            layoutRunnable = QHBoxLayout()
                            taskCBox = QComboBox()
                            taskCBox.addItem("None")
                            
                            posCBox = QSpinBox()

                            taskTypeSelectedLabel = QLabel()
                            taskTypeSelectedLabel.setText("Basic")

                            triggerSelectedLabel = QLabel()
                            triggerSelectedLabel.setText("Init Event")

                            priodCBox = QSpinBox()

                            taskLabel = QLabel()
                            taskLabel.setText("Task")
                            taskLabel.setAlignment(QtCore.Qt.AlignRight | QtCore.Qt.AlignVCenter)
                            taskTypeLabel = QLabel()
                            taskTypeLabel.setText("Type")
                            taskTypeLabel.setAlignment(QtCore.Qt.AlignRight | QtCore.Qt.AlignVCenter)
                            triggerLabel = QLabel()
                            triggerLabel.setText("Trigger")
                            triggerLabel.setAlignment(QtCore.Qt.AlignRight | QtCore.Qt.AlignVCenter)
                            posLabel = QLabel()
                            posLabel.setText("Position")
                            posLabel.setAlignment(QtCore.Qt.AlignRight | QtCore.Qt.AlignVCenter)
                            priodLabel = QLabel()
                            priodLabel.setText("Priodicity")
                            priodLabel.setAlignment(QtCore.Qt.AlignRight | QtCore.Qt.AlignVCenter)
                
                            layoutRunnable.addWidget(taskLabel)
                            layoutRunnable.addWidget(taskCBox)
                            layoutRunnable.addWidget(posLabel)
                            layoutRunnable.addWidget(posCBox)
                            layoutRunnable.addWidget(taskTypeLabel)
                            layoutRunnable.addWidget(taskTypeSelectedLabel)
                            layoutRunnable.addWidget(triggerLabel)
                            layoutRunnable.addWidget(triggerSelectedLabel)
                            layoutRunnable.addWidget(priodLabel)
                            layoutRunnable.addWidget(priodCBox)

                            self.parametersAndReferencesRows.addRow(k.Name, layoutRunnable)

        elif self.windowFrame.checkedModulesView.selectedIndexes()[0].data(Qt.DisplayRole) == 'R Ports':
            Elements = Element()
            Elements.update()
        
            for i in Elements.Application_SWC_Types:
                if self.windowFrame.checkedModulesView.selectedIndexes()[0].parent().parent().data(Qt.DisplayRole) == i.Name:
                    for a in i.Ports:
                        self.comboBox = QComboBox()
                        if a.Port_Type == 'R-Port':
                            self.comboBox.addItem("None")
                            for e in Elements.Application_SWC_Types:
                                for p in e.Ports:
                                    if  a.Interface_Type == 'Sender_Reciever_Interface' and p.Interface_Type == 'Sender_Reciever_Interface':
                                        if Elements.Sender_Reciever_Port_Interfaces[a.Interface_ID].Name == Elements.Sender_Reciever_Port_Interfaces[p.Interface_ID].Name:
                                            if p.Port_Type == 'P-Port':
                                                self.comboBox.addItem(p.Name)
                                    elif  a.Interface_Type == 'Client_Server_Interface' and p.Interface_Type == 'Client_Server_Interface':
                                        if Elements.Client_Server_Port_Interfaces[a.Interface_ID].Name == Elements.Client_Server_Port_Interfaces[p.Interface_ID].Name:
                                            if p.Port_Type == 'P-Port':
                                                self.comboBox.addItem(p.Name)

                            self.parametersAndReferencesRows.addRow(a.Name, self.comboBox)
                            print(a.Name)
                            self.comboBox.currentIndexChanged.connect(functools.partial(self.SelectedIndex, a.Name))

        elif self.windowFrame.checkedModulesView.selectedIndexes()[0].data(Qt.DisplayRole) == 'P Ports':
            Elements = Element()
            Elements.update()

            for i in Elements.Application_SWC_Types:
                if self.windowFrame.checkedModulesView.selectedIndexes()[0].parent().parent().data(Qt.DisplayRole) == i.Name:
                    for a in i.Ports:
                        comboBox = QComboBox()
                        if a.Port_Type == 'P-Port':
                            comboBox.addItem("None")
                            self.parametersAndReferencesRows.addRow(a.Name, comboBox)

    def getValue(self, val):
        print(val.data())
        print(val.row())

    def SelectedIndex(self,PortName):
        print(PortName)
        print(self.comboBox.currentText())

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
