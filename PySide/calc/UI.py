# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'C:\PyWorkspace\experiments\calc\calc_v0.1.ui'
#
# Created: Fri Feb 01 16:57:02 2013
#      by: pyside-uic 0.2.14 running on PySide 1.1.2
#
# WARNING! All changes made in this file will be lost!

from PySide import QtCore, QtGui

class Ui_Calc(object):
    def setupUi(self, Calc):
        Calc.setObjectName("Calc")
        Calc.resize(190, 260)
        self.KeyPad = QtGui.QGroupBox(Calc)
        self.KeyPad.setGeometry(QtCore.QRect(10, 80, 170, 170))
        self.KeyPad.setTitle("")
        self.KeyPad.setObjectName("KeyPad")
        self.B_Subtract = QtGui.QPushButton(self.KeyPad)
        self.B_Subtract.setGeometry(QtCore.QRect(130, 50, 30, 30))
        self.B_Subtract.setObjectName("B_Subtract")
        self.B08 = QtGui.QPushButton(self.KeyPad)
        self.B08.setGeometry(QtCore.QRect(50, 10, 30, 30))
        self.B08.setObjectName("B08")
        self.B07 = QtGui.QPushButton(self.KeyPad)
        self.B07.setGeometry(QtCore.QRect(10, 10, 30, 30))
        self.B07.setObjectName("B07")
        self.B01 = QtGui.QPushButton(self.KeyPad)
        self.B01.setGeometry(QtCore.QRect(10, 90, 30, 30))
        self.B01.setObjectName("B01")
        self.B03 = QtGui.QPushButton(self.KeyPad)
        self.B03.setGeometry(QtCore.QRect(90, 90, 30, 30))
        self.B03.setObjectName("B03")
        self.B00 = QtGui.QPushButton(self.KeyPad)
        self.B00.setGeometry(QtCore.QRect(10, 130, 71, 30))
        self.B00.setObjectName("B00")
        self.B05 = QtGui.QPushButton(self.KeyPad)
        self.B05.setGeometry(QtCore.QRect(50, 50, 30, 30))
        self.B05.setObjectName("B05")
        self.B06 = QtGui.QPushButton(self.KeyPad)
        self.B06.setGeometry(QtCore.QRect(90, 50, 30, 30))
        self.B06.setObjectName("B06")
        self.B02 = QtGui.QPushButton(self.KeyPad)
        self.B02.setGeometry(QtCore.QRect(50, 90, 30, 30))
        self.B02.setObjectName("B02")
        self.B_Add = QtGui.QPushButton(self.KeyPad)
        self.B_Add.setGeometry(QtCore.QRect(130, 10, 30, 30))
        self.B_Add.setObjectName("B_Add")
        self.B09 = QtGui.QPushButton(self.KeyPad)
        self.B09.setGeometry(QtCore.QRect(90, 10, 30, 30))
        self.B09.setObjectName("B09")
        self.B04 = QtGui.QPushButton(self.KeyPad)
        self.B04.setGeometry(QtCore.QRect(10, 50, 30, 30))
        self.B04.setObjectName("B04")
        self.B_Equals = QtGui.QPushButton(self.KeyPad)
        self.B_Equals.setGeometry(QtCore.QRect(130, 90, 30, 71))
        self.B_Equals.setObjectName("B_Equals")
        self.B_Decimal = QtGui.QPushButton(self.KeyPad)
        self.B_Decimal.setGeometry(QtCore.QRect(90, 130, 30, 30))
        self.B_Decimal.setObjectName("B_Decimal")
        self.Display = QtGui.QTextBrowser(Calc)
        self.Display.setGeometry(QtCore.QRect(10, 30, 170, 40))
        self.Display.setVerticalScrollBarPolicy(QtCore.Qt.ScrollBarAlwaysOff)
        self.Display.setHorizontalScrollBarPolicy(QtCore.Qt.ScrollBarAsNeeded)
        self.Display.setObjectName("Display")
        self.Equation = QtGui.QTextBrowser(Calc)
        self.Equation.setGeometry(QtCore.QRect(10, 10, 170, 23))
        self.Equation.setVerticalScrollBarPolicy(QtCore.Qt.ScrollBarAlwaysOff)
        self.Equation.setObjectName("Equation")

        self.retranslateUi(Calc)
        QtCore.QMetaObject.connectSlotsByName(Calc)
        Calc.setTabOrder(self.Equation, self.Display)
        Calc.setTabOrder(self.Display, self.B01)
        Calc.setTabOrder(self.B01, self.B02)
        Calc.setTabOrder(self.B02, self.B03)
        Calc.setTabOrder(self.B03, self.B04)
        Calc.setTabOrder(self.B04, self.B05)
        Calc.setTabOrder(self.B05, self.B06)
        Calc.setTabOrder(self.B06, self.B07)
        Calc.setTabOrder(self.B07, self.B08)
        Calc.setTabOrder(self.B08, self.B09)
        Calc.setTabOrder(self.B09, self.B00)
        Calc.setTabOrder(self.B00, self.B_Decimal)
        Calc.setTabOrder(self.B_Decimal, self.B_Add)
        Calc.setTabOrder(self.B_Add, self.B_Subtract)
        Calc.setTabOrder(self.B_Subtract, self.B_Equals)

    def retranslateUi(self, Calc):
        Calc.setWindowTitle(QtGui.QApplication.translate("Calc", "Calc", None, QtGui.QApplication.UnicodeUTF8))
        self.B_Subtract.setText(QtGui.QApplication.translate("Calc", "-", None, QtGui.QApplication.UnicodeUTF8))
        self.B08.setText(QtGui.QApplication.translate("Calc", "8", None, QtGui.QApplication.UnicodeUTF8))
        self.B07.setText(QtGui.QApplication.translate("Calc", "7", None, QtGui.QApplication.UnicodeUTF8))
        self.B01.setText(QtGui.QApplication.translate("Calc", "1", None, QtGui.QApplication.UnicodeUTF8))
        self.B03.setText(QtGui.QApplication.translate("Calc", "3", None, QtGui.QApplication.UnicodeUTF8))
        self.B00.setText(QtGui.QApplication.translate("Calc", "0", None, QtGui.QApplication.UnicodeUTF8))
        self.B05.setText(QtGui.QApplication.translate("Calc", "5", None, QtGui.QApplication.UnicodeUTF8))
        self.B06.setText(QtGui.QApplication.translate("Calc", "6", None, QtGui.QApplication.UnicodeUTF8))
        self.B02.setText(QtGui.QApplication.translate("Calc", "2", None, QtGui.QApplication.UnicodeUTF8))
        self.B_Add.setText(QtGui.QApplication.translate("Calc", "+", None, QtGui.QApplication.UnicodeUTF8))
        self.B09.setText(QtGui.QApplication.translate("Calc", "9", None, QtGui.QApplication.UnicodeUTF8))
        self.B04.setText(QtGui.QApplication.translate("Calc", "4", None, QtGui.QApplication.UnicodeUTF8))
        self.B_Equals.setText(QtGui.QApplication.translate("Calc", "=", None, QtGui.QApplication.UnicodeUTF8))
        self.B_Decimal.setText(QtGui.QApplication.translate("Calc", ".", None, QtGui.QApplication.UnicodeUTF8))
        self.Display.setHtml(QtGui.QApplication.translate("Calc", "<!DOCTYPE HTML PUBLIC \"-//W3C//DTD HTML 4.0//EN\" \"http://www.w3.org/TR/REC-html40/strict.dtd\">\n"
"<html><head><meta name=\"qrichtext\" content=\"1\" /><style type=\"text/css\">\n"
"p, li { white-space: pre-wrap; }\n"
"</style></head><body style=\" font-family:\'MS Shell Dlg 2\'; font-size:8.25pt; font-weight:400; font-style:normal;\">\n"
"<p align=\"right\" style=\"-qt-paragraph-type:empty; margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px; font-size:8pt;\"><br /></p></body></html>", None, QtGui.QApplication.UnicodeUTF8))
        self.Equation.setHtml(QtGui.QApplication.translate("Calc", "<!DOCTYPE HTML PUBLIC \"-//W3C//DTD HTML 4.0//EN\" \"http://www.w3.org/TR/REC-html40/strict.dtd\">\n"
"<html><head><meta name=\"qrichtext\" content=\"1\" /><style type=\"text/css\">\n"
"p, li { white-space: pre-wrap; }\n"
"</style></head><body style=\" font-family:\'MS Shell Dlg 2\'; font-size:8.25pt; font-weight:400; font-style:normal;\">\n"
"<p align=\"right\" style=\"-qt-paragraph-type:empty; margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px; font-size:8pt;\"><br /></p></body></html>", None, QtGui.QApplication.UnicodeUTF8))

