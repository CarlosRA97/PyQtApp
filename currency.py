import sys
from PySide.QtCore import *
from PySide.QtGui import *

import urllib2


class Form(QDialog):
    def __init__(self, parent=None):
        super(Form, self).__init__(parent)

        self.rates = {}
        date = self.getdate()
        rates = sorted(self.rates.keys())

        date_label = QLabel(date)
        self.fromComboBox = QComboBox()
        self.fromComboBox.addItems(rates)
        self.fromSpinBox = QDoubleSpinBox()
        self.fromSpinBox.setRange(0.01, 100000000.0)
        self.fromSpinBox.setValue(1.00)
        self.toComboBox = QComboBox()
        self.toComboBox.addItems(rates)
        self.toLabel = QLabel("1.00")

        grid = QGridLayout()
        grid.addWidget(date_label, 0, 0)
        grid.addWidget(self.fromComboBox, 1, 0)
        grid.addWidget(self.fromSpinBox, 1, 1)
        grid.addWidget(self.toComboBox, 2, 0)
        grid.addWidget(self.toLabel, 2, 1)
        self.setLayout(grid)

        self.connect(self.fromComboBox, SIGNAL("currentIndexChanged(int)"), self.update_ui)
        self.connect(self.toComboBox, SIGNAL("currentIndexChanged(int)"), self.update_ui)
        self.connect(self.fromSpinBox, SIGNAL("valueChanged(double)"), self.update_ui)

    def update_ui(self):
        to = self.toComboBox.currentText()
        from_ = self.fromComboBox.currentText()

        amount = (self.rates[from_] / self.rates[to] * self.fromSpinBox.value())
        self.toLabel.setText("%0.2f" % amount)

    def getdate(self):

        try:
            date = "Unknown"

            fh = urllib2.urlopen("http://www.bankofcanada.ca/en/markets/csv/exchange_eng.csv")

            for line in fh:
                line = line.rstrip()
                if not line or line.startswith(("#", "Closing ")):
                    continue

                fields = line.split(",")
                if line.startswith("Date "):
                    date = fields[-1]

                else:
                    try:
                        value = float(fields[-1])
                        self.rates[fields[0]] = value

                    except ValueError:
                        pass

            return "Exchange rates date: " + date
        except Exception as e:
            return "Failured to download:\n%s" % e


def run():
    app = QApplication(sys.argv)
    form = Form()
    form.show()
    app.exec_()


run()
