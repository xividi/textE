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

        self.actionOpen.triggered.connect(self.open_file)
        self.actionSave.triggered.connect(self.save_file)
        self.actionClose.triggered.connect(self.close)

        self.actiongetfontsize.triggered.connect(self.get_font_size)
        self.actionFont_Type.triggered.connect(self.font_type_changer)

        self.actionLine_Wrap_Mode.setCheckable(True)
        self.actionLine_Wrap_Mode.triggered.connect(self.line_wrap_mode)

    def font_type_changer(self):
        font, ok = QFontDialog.getFont()
        if ok:
            self.plainTextEdit.setFont(font)

    def line_wrap_mode(self):
        if self.actionLine_Wrap_Mode.isChecked():
            self.plainTextEdit.setLineWrapMode(QPlainTextEdit.WidgetWidth)
        else:
            self.plainTextEdit.setLineWrapMode(QPlainTextEdit.NoWrap)

    def get_font_size(self):
        size, ok = QInputDialog.getInt(self, 'Font Size', 'Enter font size:', 12, 1, 130, 1)
        if ok:
            self.plainTextEdit.setFont(QFont('Arial', size))
            return size

    def open_file(self):
        options = QFileDialog.Options()
        filename, _ = QFileDialog.getOpenFileName(self, 'Open File', '', 'Text Files (*.txt);; Python Files (*.py)',
                                                  options=options)
        if filename != '':
            with open(filename, 'r') as f:
                self.plainTextEdit.setPlainText(f.read())

    def save_file(self):
        options = QFileDialog.Options()
        filename, _ = QFileDialog.getSaveFileName(self, 'Save File', '', 'Text Files (*.txt);;All Files (*)',
                                                  options=options)
        if filename != '':
            with open(filename, 'w') as f:
                f.write(self.plainTextEdit.toPlainText())

    def closeEvent(self, event):
        reply = QMessageBox()
        reply.setText("Do you want to save?")
        reply.addButton(QPushButton('Save'), QMessageBox.YesRole)
        reply.addButton(QPushButton("Don't save"), QMessageBox.NoRole)
        reply.addButton(QPushButton('Cancel'), QMessageBox.RejectRole)

        answer = reply.exec_()

        if answer == 0:
            self.save_file()
            event.accept()
        elif answer == 2:
            event.ignore()


def main():
    app = QApplication([])
    window = GUI()
    app.exec_()


if __name__ == '__main__':
    main()
