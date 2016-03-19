import sys
from PyQt4.QtCore import *
from PyQt4.QtGui import *


class Form(QDialog):
    def __init__(self, parent=None):
        super(Form, self).__init__(parent)

    pass



def run():
    app = QApplication(sys.argv)
    main = Form()
    main.show()
    app.exec_()


if __name__ == "__main__":
    run()