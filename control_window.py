from main_window import *
from create_window import *
from openExitProjectWindow import *
from module_window import *
import sys
from PyQt5 import QtCore, QtWidgets
from PyQt5.QtWidgets import QApplication, QMainWindow

class Controller:

    def __init__(self):
        self.window = MainWindow()
        self.create_window = createWindow()
        self.openExitWindow = openExitProject()
        self.module_Confg = moduleConfg("tool",':/images/FOE.png')

    def show_main(self):
        # self.window = MainWindow()
        self.window.switch_create_window.connect(self.show_create_window)
        self.window.switch_open_window.connect(self.show_openExitWindow)
        self.window.showMaximized()
        self.create_window.hide()
        self.openExitWindow.hide()

    def show_create_window(self):
        # self.login = Login()
        self.create_window.switch_window.connect(self.show_module_window)
        self.create_window.show()
        #self.window.hide()
        self.openExitWindow.hide()

    def show_openExitWindow(self):
        # self.login = Login()
        self.openExitWindow.switch_window.connect(self.show_main)
        self.openExitWindow.show()
        self.create_window.hide()

    def show_module_window(self):
        # self.login = Login()
        #self.module_window.switch_window.connect(self.show_moduleconfg_window)
        self.module_Confg.showMaximized()
        self.window.hide()
        self.create_window.hide()
        self.openExitWindow.hide()


def main():
    app = QtWidgets.QApplication(sys.argv)

    controller = Controller()
    controller.show_main()

    sys.exit(app.exec_())

if __name__ == '__main__':
    main()

