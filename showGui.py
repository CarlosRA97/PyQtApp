# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'show.ui'
#
# Created by: PyQt4 UI code generator 4.11.4
#
# WARNING! All changes made in this file will be lost!

from PyQt4 import QtCore, QtGui

try:
    _fromUtf8 = QtCore.QString.fromUtf8
except AttributeError:
    def _fromUtf8(s):
        return s

try:
    _encoding = QtGui.QApplication.UnicodeUTF8
    def _translate(context, text, disambig):
        return QtGui.QApplication.translate(context, text, disambig, _encoding)
except AttributeError:
    def _translate(context, text, disambig):
        return QtGui.QApplication.translate(context, text, disambig)

class Ui_mainDialog(object):
    def setupUi(self, mainDialog):
        mainDialog.setObjectName(_fromUtf8("mainDialog"))
        mainDialog.resize(307, 67)
        mainDialog.setFocusPolicy(QtCore.Qt.ClickFocus)
        self.showButton = QtGui.QPushButton(mainDialog)
        self.showButton.setGeometry(QtCore.QRect(190, 20, 110, 31))
        self.showButton.setObjectName(_fromUtf8("pushButton"))
        self.lineEdit = QtGui.QLineEdit(mainDialog)
        self.lineEdit.setGeometry(QtCore.QRect(10, 20, 161, 21))
        self.lineEdit.setFocusPolicy(QtCore.Qt.ClickFocus)
        self.lineEdit.setInputMask(_fromUtf8(""))
        self.lineEdit.setText(_fromUtf8(""))
        self.lineEdit.setObjectName(_fromUtf8("lineEdit"))

        self.retranslateUi(mainDialog)
        QtCore.QMetaObject.connectSlotsByName(mainDialog)

    def retranslateUi(self, mainDialog):
        mainDialog.setWindowTitle(_translate("mainDialog", "Dialog", None))
        self.showButton.setText(_translate("mainDialog", "Show!", None))
        self.lineEdit.setPlaceholderText(_translate("mainDialog", "What is your name?", None))

