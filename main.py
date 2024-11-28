import sys
import random
from PyQt5.QtWidgets import QApplication, QMainWindow, QPushButton
from PyQt5.QtGui import QPainter, QColor


class MyForm(QMainWindow):
    def __init__(self):
        super(MyForm, self).__init__()
        self.setGeometry(200, 200, 400, 500)
        self.pushButton = QPushButton('Кнопка', self)
        self.pushButton.resize(self.pushButton.sizeHint())
        self.pushButton.clicked.connect(self.work)
        self.cs = 0

    def work(self):
        diameter = random.randint(20, 100)
        self.cs = diameter
        self.update()

    def paintEvent(self, event):
        a = QPainter(self)
        a.setBrush(QColor(random.randint(0, 255), random.randint(0, 255), random.randint(0, 255)))
        x = random.randint(0, self.width() - self.cs)
        y = random.randint(0, self.height() - self.cs)
        a.drawEllipse(x, y, self.cs, self.cs)


if __name__ == '__main__':
    app = QApplication(sys.argv)
    window = MyForm()
    window.show()
    sys.exit(app.exec())
