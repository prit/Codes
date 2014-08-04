from sys import argv, exit

from PySide import QtCore, QtGui

from UI import Ui_Calc

class UI(QtGui.QWidget):
    
    DISPLAY="<!DOCTYPE HTML PUBLIC \"-//W3C//DTD HTML 4.0//EN\" \"http://www.w3.org/TR/REC-html40/strict.dtd\">\n"\
        "<html><head><meta name=\"qrichtext\" content=\"1\" /><style type=\"text/css\">\n"\
        "p, li { white-space: pre-wrap; }\n"\
        "</style></head><body style=\" font-family:\'MS Shell Dlg 2\'; font-size:8.25pt; font-weight:400; font-style:normal;\">\n"\
        "<p align=\"right\" style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><span style=\" font-size:20pt;\">%s</span></p></body></html>"
    EQUATION="<!DOCTYPE HTML PUBLIC \"-//W3C//DTD HTML 4.0//EN\" \"http://www.w3.org/TR/REC-html40/strict.dtd\">\n"\
        "<html><head><meta name=\"qrichtext\" content=\"1\" /><style type=\"text/css\">\n"\
        "p, li { white-space: pre-wrap; }\n"\
        "</style></head><body style=\" font-family:\'MS Shell Dlg 2\'; font-size:8.25pt; font-weight:400; font-style:normal;\">\n"\
        "<p align=\"right\" style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><span style=\" font-size:8pt;\">%s</span></p></body></html>"
    
    def __init__(self):
        # Setting up UI
        QtGui.QWidget.__init__(self)
        self.setupUi()
        
        self._equation=""
        self._display="0"
        
        self.updateUI()
    
    def updateUI(self):
        self._ui.Display.setHtml(QtGui.QApplication.translate("Calc", self.DISPLAY % self._display, None, QtGui.QApplication.UnicodeUTF8))
        self._ui.Equation.setHtml(QtGui.QApplication.translate("Calc", self.EQUATION % self._equation, None, QtGui.QApplication.UnicodeUTF8))
    
    def setupUi(self):
        # Creating widget
        self._ui=Ui_Calc()
        self._ui.setupUi(self)
        
        # Keeping fixed width and disabling maximize button on title bar
        self.setFixedWidth(self.width())
        self.setFixedHeight(self.height())
        
        # Linking all the gui objects with custome functions
        self._ui.B00.clicked.connect(self.clicked00)
        self._ui.B01.clicked.connect(self.clicked01)
        self._ui.B02.clicked.connect(self.clicked02)
        self._ui.B03.clicked.connect(self.clicked03)
        self._ui.B04.clicked.connect(self.clicked04)
        self._ui.B05.clicked.connect(self.clicked05)
        self._ui.B06.clicked.connect(self.clicked06)
        self._ui.B07.clicked.connect(self.clicked07)
        self._ui.B08.clicked.connect(self.clicked08)
        self._ui.B09.clicked.connect(self.clicked09)
        
        self._ui.B_Decimal.clicked.connect(self.clickedDecimal)
        
        self._ui.B_Add.clicked.connect(self.clickedAdd)
        self._ui.B_Subtract.clicked.connect(self.clickedSubtract)
        
        self._ui.B_Equals.clicked.connect(self.clickedEquals)
        
        # Showing up the module
        self.show()
        
    def clicked00(self):
        if "."in self._display or eval(self._display):
            self._display+="0"
        else:
            self._display="0"
        self.updateUI()
    def clicked01(self):
        if "."in self._display or eval(self._display):
            self._display+="1"
        else:
            self._display="1"
        self.updateUI()
    def clicked02(self):
        if "."in self._display or eval(self._display):
            self._display+="2"
        else:
            self._display="2"
        self.updateUI()
    def clicked03(self):
        if "."in self._display or eval(self._display):
            self._display+="3"
        else:
            self._display="3"
        self.updateUI()
    def clicked04(self):
        if "."in self._display or eval(self._display):
            self._display+="4"
        else:
            self._display="4"
        self.updateUI()
    def clicked05(self):
        if "."in self._display or eval(self._display):
            self._display+="5"
        else:
            self._display="5"
        self.updateUI()
    def clicked06(self):
        if "." in self._display or eval(self._display):
            self._display+="6"
        else:
            self._display="6"
        self.updateUI()
    def clicked07(self):
        if "."in self._display or eval(self._display):
            self._display+="7"
        else:
            self._display="7"
        self.updateUI()
    def clicked08(self):
        if "."in self._display or eval(self._display):
            self._display+="8"
        else:
            self._display="8"
        self.updateUI()
    def clicked09(self):
        if "."in self._display or eval(self._display):
            self._display+="9"
        else:
            self._display="9"
        self.updateUI()
        
    def clickedDecimal(self):
        if eval(self._display):
            self._display+="."
        else:
            self._display="0."
        self.updateUI()
    
    def clickedAdd(self):
        self._equation+="%s+" %self._display
        self._display=str(eval(self._equation + "0"))
        self.updateUI()
        self._display="0"
        
    def clickedSubtract(self):
        self._equation+="%s-" %self._display
        self._display=str(eval(self._equation + "0"))
        self.updateUI()
        self._display="0"
    
    def clickedEquals(self):
        self._display=str(eval(self._equation + self._display))
        self._equation=""
        self.updateUI()
        self._display="0"
    
if __name__=="__main__":
    app = QtGui.QApplication(argv)
    ui=UI()
    exit(app.exec_())