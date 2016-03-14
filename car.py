import sys
from PyQt4.QtCore import *
from PyQt4.QtGui import *


class Dialog():


def run():
    app = QApplication(sys.argv)
    main = Dialog()
    main.show()
    app.exec_()


run()