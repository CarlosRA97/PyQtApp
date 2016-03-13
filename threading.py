import sys
from PyQt4.QtCore import *
from PyQt4.QtGui import *
import showGui
import time

class MainDialog(QDialog, showGui.Ui_mainDialog):
    def __init__(self, parent=None):
        super(MainDialog, self).__init__(parent)
        self.setupUi(self)

        self.showButton.setText("Process")
        self.connect(self.showButton, SIGNAL("clicked()"), self.processData)
        self.workerThread = WorkerThread()


    def processData(self):
        self.workerThread.start()
        QMessageBox.information(self, "Done!", "Done")


class WorkerThread(QThread):
    def __init__(self, parent=None):
        super(WorkerThread, self).__init__(parent)

    def run(self):
        time.sleep(5)


def run():
    app = QApplication(sys.argv)
    form = MainDialog()
    form.show()
    app.exec_()


run()