from second_win import *
from PyQt5.QtCore import Qt, QTimer, QTime, QLocale
from PyQt5.QtGui import QDoubleValidator, QIntValidator, QFont
from PyQt5.QtWidgets import (
        QApplication, QWidget, 
        QHBoxLayout, QVBoxLayout, QGridLayout, 
        QGroupBox, QRadioButton,
        QPushButton, QLabel, QListWidget, QLineEdit)
        
from instr import *
class MainWindow(QWidget):
    def __init__(self):
        super().__init__()
        self.initUI()
        self.connects()
        self.set_appear()
        self.show()
                                            
    def initUI(self):
        self.btn_next = QPushButton(txt_next, self)
        self.hello_txt = QLabel(txt_hello)
        self.instruction = QLabel(txt_instruction)
    
        self.layout_line = QVBoxLayout()
        self.layout_line.addWidget(self.hello_txt, alignment = Qt.AlignLeft)
        self.layout_line.addWidget(self.instruction, alignment = Qt.AlignLeft) 
        self.layout_line.addWidget(self.btn_next, alignment = Qt.AlignCenter)          
        self.setLayout(self.layout_line)

    def next_click(self):
        self.tw = TestWin()
        self.hide()
    
    def connects(self):
        self.btn_next.clicked.connect(self.next_click)
        
    def set_appear(self):
        self.setWindowTitle(txt_title)
        self.resize(win_width, win_height)
        self.move(win_x, win_y)

app = QApplication([])
mw = MainWindow()
app.exec_()
