# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'C:\Users\Prit Ranjan\Desktop\Workspace\PyWorkspace\experiments\widget\interface\chield1.ui'
#
# Created: Tue Apr 08 20:39:07 2014
#      by: pyside-uic 0.2.15 running on PySide 1.2.1
#
# WARNING! All changes made in this file will be lost!

from PySide import QtCore, QtGui

class Ui__1_chield(object):
    def setupUi(self, _1_chield):
        _1_chield.setObjectName("_1_chield")
        _1_chield.resize(360, 180)
        self.gridLayout_2 = QtGui.QGridLayout(_1_chield)
        self.gridLayout_2.setObjectName("gridLayout_2")
        self._1_groupBox = QtGui.QGroupBox(_1_chield)
        self._1_groupBox.setObjectName("_1_groupBox")
        self.gridLayout = QtGui.QGridLayout(self._1_groupBox)
        self.gridLayout.setObjectName("gridLayout")
        self._1_lineEdit_1 = QtGui.QLineEdit(self._1_groupBox)
        sizePolicy = QtGui.QSizePolicy(QtGui.QSizePolicy.Preferred, QtGui.QSizePolicy.Expanding)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self._1_lineEdit_1.sizePolicy().hasHeightForWidth())
        self._1_lineEdit_1.setSizePolicy(sizePolicy)
        self._1_lineEdit_1.setObjectName("_1_lineEdit_1")
        self.gridLayout.addWidget(self._1_lineEdit_1, 0, 0, 1, 1)
        self._1_lineEdit_2 = QtGui.QLineEdit(self._1_groupBox)
        self._1_lineEdit_2.setEnabled(True)
        sizePolicy = QtGui.QSizePolicy(QtGui.QSizePolicy.Preferred, QtGui.QSizePolicy.Preferred)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self._1_lineEdit_2.sizePolicy().hasHeightForWidth())
        self._1_lineEdit_2.setSizePolicy(sizePolicy)
        self._1_lineEdit_2.setObjectName("_1_lineEdit_2")
        self.gridLayout.addWidget(self._1_lineEdit_2, 1, 0, 1, 1)
        self.gridLayout_2.addWidget(self._1_groupBox, 0, 0, 1, 1)

        self.retranslateUi(_1_chield)
        QtCore.QMetaObject.connectSlotsByName(_1_chield)

    def retranslateUi(self, _1_chield):
        _1_chield.setWindowTitle(QtGui.QApplication.translate("_1_chield", "Form", None, QtGui.QApplication.UnicodeUTF8))
        self._1_groupBox.setTitle(QtGui.QApplication.translate("_1_chield", "GroupBox1", None, QtGui.QApplication.UnicodeUTF8))

