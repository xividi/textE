from PyQt5.QtGui import QIcon, QFont
from PyQt5.QtWidgets import *
from PyQt5 import uic

class GUI(QMainWindow):
    def __init__(self):
        super(GUI, self).__init__()
        uic.loadUi('editor.ui', self)
        self.show()

        self.setWindowTitle('TextEditor')
        self.setWindowIcon(QIcon('icon.png'))

    def change_size(self, size):
        self.plainTextEdit.setFont(QFont('Arial', size))

def main():
    app = QApplication([])
    window = GUI()
    app.exec_()

if __name__ == '__main__':
    main()