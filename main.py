import sys
import random
from PyQt5 import uic
from PyQt5.QtWidgets import QApplication, QMainWindow
from PyQt5.QtGui import QPainter, QColor


class MyForm(QMainWindow):
    def __init__(self):
        super(MyForm, self).__init__()
        uic.loadUi('UI.ui', self)
        self.pushButton.clicked.connect(self.work)
        self.cs = 0

    def work(self):
        diameter = random.randint(20, 100)
        self.cs = diameter
        self.update()

    def paintEvent(self, event):
        a = QPainter(self)
        a.setBrush(QColor(255, 255, 0))
        x = random.randint(0, self.width() - self.cs)
        y = random.randint(0, self.height() - self.cs)
        a.drawEllipse(x, y, self.cs, self.cs)


if __name__ == '__main__':
    app = QApplication(sys.argv)
    window = MyForm()
    window.show()
    sys.exit(app.exec())