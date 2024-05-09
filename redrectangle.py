import sys
from PyQt5.QtWidgets import QApplication, QWidget, QLabel
from PyQt5.QtCore import Qt
from PyQt5.QtGui import QColor, QPainter

class TranslucentWidget(QWidget):
    def __init__(self):
        super().__init__()

        # Initialize the window
        self.initUI()

    def initUI(self):
        self.setGeometry(300, 300, 250, 150)
        self.setWindowTitle('Red Overlay')

        self.setAttribute(Qt.WA_TranslucentBackground)
        self.setStyleSheet("background:transparent;")

        self.show()

    def paintEvent(self, event):
        painter = QPainter(self)
        painter.setBrush(QColor(255, 0, 0, 120))  # Semi-transparent red brush
        painter.setPen(Qt.NoPen)
        painter.drawRect(self.rect())

def main():
    app = QApplication(sys.argv)
    ex = TranslucentWidget()
    sys.exit(app.exec_())

if __name__ == '__main__':
    main()

