from PyQt5.QtGui import QIcon, QFont
from PyQt5.QtWidgets import *
from PyQt5 import uic

class GUI(QMainWindow):
    def __init__(self):
        super(GUI, self).__init__()
        uic.loadUi('editor.ui', self)
        self.show()
        self.plainTextEdit.setFont(QFont('Arial', 12))

        self.setWindowTitle('Notepad--')
        self.setWindowIcon(QIcon('icon.png'))

        self.action10pt.triggered.connect(lambda: self.change_size(10))
        self.action12pt.triggered.connect(lambda: self.change_size(12))
        self.action16pt.triggered.connect(lambda: self.change_size(16))
        self.action24pt.triggered.connect(lambda: self.change_size(24))

        self.actionOpen.triggered.connect(self.open_file)
        self.actionSave.triggered.connect(self.save_file)
        self.actionClose.triggered.connect(self.close)

    def change_size(self, size):
        self.plainTextEdit.setFont(QFont('Arial', size))

    def open_file(self):
        options = QFileDialog.Options()
        filename, _ = QFileDialog.getOpenFileName(self, 'Open File', '', 'Text Files (*.txt);; Python Files (*.py)', options=options)
        if filename != '':
            with open(filename, 'r') as f:
                self.plainTextEdit.setPlainText(f.read())

    def save_file(self):
        options = QFileDialog.Options()
        filename, _ = QFileDialog.getSaveFileName(self, 'Save File', '', 'Text Files (*.txt);;All Files (*)', options=options)
        if filename != '':
            with open(filename, 'w') as f:
                f.write(self.plainTextEdit.toPlainText())

    def closeEvent(self, event):
        reply = QMessageBox.question(self, 'Message', 'Are you sure to quit?', QMessageBox.Yes | QMessageBox.No, QMessageBox.No)
        if reply == QMessageBox.Yes:
            event.accept()
        else:
            event.ignore()

def main():
    app = QApplication([])
    window = GUI()
    app.exec_()

if __name__ == '__main__':
    main()