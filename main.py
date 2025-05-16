import sys

from PyQt6.QtGui import QPixmap
from PyQt6.QtWidgets import QDialog, QApplication

from layout import Ui_Dialog


class MyForm(QDialog):
    def __init__(self):
        super().__init__()
        self.ui = Ui_Dialog()
        self.ui.setupUi(self)
        self.ui.add.clicked.connect(self.add_food)
        self.ui.men.toggled.connect(self.men)
        self.ui.woman.toggled.connect(self.woman)
        self.ui.small.toggled.connect(self.woman)
        self.ui.average.toggled.connect(self.woman)
        self.ui.big.toggled.connect(self.woman)
        self.ui.small.toggled.connect(self.men)
        self.ui.average.toggled.connect(self.men)
        self.ui.big.toggled.connect(self.men)
        self.calories_sum = 0
        self.show()

    def add_food(self):
        food = self.ui.foodName.text()
        calories = int(self.ui.caloriesNumber.text())

        self.calories_sum += calories
        self.ui.sum.setText(str(self.calories_sum))
        self.ui.foodList.addItem(food)

        if self.calories_sum > 1000:
            self.ui.sum.setStyleSheet("color: red;")
        else:
            self.ui.sum.setStyleSheet("color: black;")

    def men(self):
        if self.ui.men.isChecked():
            if self.ui.small.isChecked():
                self.ui.image.setPixmap(QPixmap('./1.jpg'))
            elif self.ui.average.isChecked():
                self.ui.image.setPixmap(QPixmap('./2.jpg'))
            elif self.ui.big.isChecked():
                self.ui.image.setPixmap(QPixmap('./3.jpg'))

    def woman(self):
        if self.ui.woman.isChecked():
            if self.ui.small.isChecked():
                self.ui.image.setPixmap(QPixmap('./1.jpg'))
            elif self.ui.average.isChecked():
                self.ui.image.setPixmap(QPixmap('./2.jpg'))
            elif self.ui.big.isChecked():
                self.ui.image.setPixmap(QPixmap('./3.jpg'))

if __name__ == '__main__':
    app = QApplication(sys.argv)
    window = MyForm()
    sys.exit(app.exec())