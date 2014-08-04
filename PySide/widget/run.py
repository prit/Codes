from traceback import format_exc
from os import path
from sys import argv, exit

from PySide import QtCore, QtGui

from interface import main, chield1, chield2

class UI(QtGui.QWidget):
    def __init__(self):
        # Setting up UI
        QtGui.QWidget.__init__(self)
        self.setupUi()

    def setupUi(self):
        # Creating widget
        self._ui=main.Ui_Form()
        self._ui.setupUi(self)

        self._chield1=chield1.Ui__1_chield()
        self._chield1.setupUi(self._ui.widget)

        self._chield2=chield2.Ui__2_chield()
        self._chield2.setupUi(self._ui.widget_2)
        
        # Keeping fixed width and disabling maximize button on title bar
        #self.setFixedWidth(self.width()) 

        # Showing up the module
        self.show()

    def exitModule(self):
        # Called when Exit button clicked
        exit()
        
if __name__=="__main__":
    app = QtGui.QApplication(argv)
    ui=UI()
    exit(app.exec_())
