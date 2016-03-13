import sys
from PyQt4.QtCore import *
from PyQt4.QtGui import *

import showGui


class MainDialog(QDialog, showGui.Ui_mainDialog):
    def __init__(self, parent=None):
        super(MainDialog, self).__init__(parent)
        self.setupUi(self)

        self.connect(self.showButton, SIGNAL("clicked()"), self.showMessageBox)

    def showMessageBox(self):
        QMessageBox.information(self, "hello there", "hello, "+self.lineEdit.text())


def run():
    app = QApplication(sys.argv)
    form = MainDialog()
    form.show()
    app.exec_()


run()
