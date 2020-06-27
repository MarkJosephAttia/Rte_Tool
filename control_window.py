from main_window import *
from create_window import *
from module_window import *
from module_configure import *
from openExitProjectWindow import *

import sys
from PyQt5 import QtCore, QtWidgets
from PyQt5.QtWidgets import QApplication, QMainWindow

class Controller:

    def __init__(self):
        self. x =0
        # pass
        # self.login = login()
        toolName = "Córdoba RTE Studio"
        toolIcon = ':/images/FOE.png' 
        self.create_window = createWindow(toolName, toolIcon)
        self.openExitWindow = openExitProject(toolName, toolIcon)
        self.module_window = moduleWindow(toolName, toolIcon)
        self.window = MainWindow(toolName, toolIcon)
        self.modconfg = moduleConfg(toolName, toolIcon)
        listCheckedModules = []
        moduleContainer = []

    def show_create_window(self):
        # self.login = Login()
        self.create_window.switch_window.connect(self.show_module_window)
        self.create_window.show()
        #self.window.hide()
        self.openExitWindow.hide()
        self.module_window.hide()
        self.modconfg.hide()


    def show_module_window(self):
        # self.login = Login()
        self.module_window.switch_window.connect(self.show_moduleconfg_window)
        self.module_window.show()
        #self.window.hide()
        self.create_window.hide()
        self.openExitWindow.hide()
        self.modconfg.hide()

    def show_moduleconfg_window(self):
        # self.login = Login()
        #self.modconfg.switch_window.connect(self.show_module_window)
        self.modconfg.switch_create_window.connect(self.show_create_window)
        self.modconfg.switch_open_window.connect(self.show_openExitWindow)
        self.modconfg.showMaximized()
        self.window.hide()
        self.create_window.hide()
        self.openExitWindow.hide()
        self.module_window.hide()

    def show_openExitWindow(self):
        # self.login = Login()
        self.openExitWindow.switch_window.connect(self.show_main)
        self.openExitWindow.show()
        #self.window.hide()
        self.module_window.hide()
        self.create_window.hide()
        self.modconfg.hide()


    def show_main(self):
        # self.window = MainWindow()
        self.window.switch_create_window.connect(self.show_create_window)
        self.window.switch_open_window.connect(self.show_openExitWindow)
        self.create_window.hide()
        self.module_window.hide()
        self.openExitWindow.hide()
        self.window.showMaximized()
        self.modconfg.hide()



def main():
    app = QtWidgets.QApplication(sys.argv)

    #list of checked modules
    controller = Controller()
    controller.show_main()

    sys.exit(app.exec_())

if __name__ == '__main__':
    main()

