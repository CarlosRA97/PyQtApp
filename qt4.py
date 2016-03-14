import sys
from PyQt4.QtCore import *
from PyQt4.QtGui import *


class MainWindow():


def run():
    app = QApplication(sys.argv)
    main = MainWindow()
    main.show()
    app.exec_()


if __name__ == "__main__":
    run()