# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'C:\Users\Prit Ranjan\Desktop\Workspace\PyWorkspace\experiments\widget\interface\chield2.ui'
#
# Created: Tue Apr 08 20:33:09 2014
#      by: pyside-uic 0.2.15 running on PySide 1.2.1
#
# WARNING! All changes made in this file will be lost!

from PySide import QtCore, QtGui

class Ui__2_chield(object):
    def setupUi(self, _2_chield):
        _2_chield.setObjectName("_2_chield")
        _2_chield.resize(360, 180)
        self.gridLayout_2 = QtGui.QGridLayout(_2_chield)
        self.gridLayout_2.setObjectName("gridLayout_2")
        self._2_groupBox = QtGui.QGroupBox(_2_chield)
        self._2_groupBox.setObjectName("_2_groupBox")
        self.gridLayout = QtGui.QGridLayout(self._2_groupBox)
        self.gridLayout.setObjectName("gridLayout")
        self._1_checkBox_1 = QtGui.QCheckBox(self._2_groupBox)
        self._1_checkBox_1.setObjectName("_1_checkBox_1")
        self.gridLayout.addWidget(self._1_checkBox_1, 0, 0, 1, 1)
        self._1_checkBox_2 = QtGui.QCheckBox(self._2_groupBox)
        self._1_checkBox_2.setObjectName("_1_checkBox_2")
        self.gridLayout.addWidget(self._1_checkBox_2, 1, 0, 1, 1)
        self.gridLayout_2.addWidget(self._2_groupBox, 0, 0, 1, 1)

        self.retranslateUi(_2_chield)
        QtCore.QMetaObject.connectSlotsByName(_2_chield)

    def retranslateUi(self, _2_chield):
        _2_chield.setWindowTitle(QtGui.QApplication.translate("_2_chield", "Form", None, QtGui.QApplication.UnicodeUTF8))
        self._2_groupBox.setTitle(QtGui.QApplication.translate("_2_chield", "GroupBox2", None, QtGui.QApplication.UnicodeUTF8))
        self._1_checkBox_1.setText(QtGui.QApplication.translate("_2_chield", "CheckBox", None, QtGui.QApplication.UnicodeUTF8))
        self._1_checkBox_2.setText(QtGui.QApplication.translate("_2_chield", "CheckBox", None, QtGui.QApplication.UnicodeUTF8))

