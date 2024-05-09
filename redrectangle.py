#!/usr/bin/env python3
import sys
from PyQt5.QtWidgets import QApplication, QWidget, QLabel, QPushButton, QColorDialog
from PyQt5.QtCore import Qt
from PyQt5.QtGui import QColor, QPainter

class TranslucentWidget(QWidget):
    def __init__(self):
        super().__init__()

        # Initialize the window
        self.color = QColor(220, 6, 70, 220)  # Initial color and transparency
        self.initUI()

    def initUI(self):
        self.setGeometry(300, 300, 250, 150)
        self.setWindowTitle('Red Overlay Adjustable')

        # Button to change color
        btn = QPushButton('Change Color', self)
        btn.move(10, 200)
        btn.clicked.connect(self.openColorDialog)

        self.setAttribute(Qt.WA_TranslucentBackground)
        self.setStyleSheet("background:transparent;")
        self.show()

    def paintEvent(self, event):
        painter = QPainter(self)
        painter.setBrush(self.color)  # Use dynamic color
        painter.setPen(Qt.NoPen)
        painter.drawRect(self.rect())
        painter.end()  # Properly end the painting

    def wheelEvent(self, event):
        numDegrees = event.angleDelta().y() / 8
        numSteps = numDegrees / 15
        alpha = max(0, min(255, self.color.alpha() + int(numSteps * 5)))
        self.color.setAlpha(alpha)
        self.update()

    def openColorDialog(self):
        # Use QColorDialog with the option to see color changes live
        colorDialog = QColorDialog(self.color, self)
        colorDialog.setOption(QColorDialog.ShowAlphaChannel, True)
        colorDialog.currentColorChanged.connect(self.colorUpdated)
        colorDialog.exec_()

    def colorUpdated(self, color):
        self.color = color
        self.update()

def main():
    app = QApplication(sys.argv)
    ex = TranslucentWidget()
    sys.exit(app.exec_())

if __name__ == '__main__':
    main()

