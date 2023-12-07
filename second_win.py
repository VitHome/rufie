from PyQt5.QtCore import Qt, QTimer, QTime, QLocale
from PyQt5.QtGui import QDoubleValidator, QIntValidator, QFont
from PyQt5.QtWidgets import (
        QApplication, QWidget, 
        QHBoxLayout, QVBoxLayout, QGridLayout, 
        QGroupBox, QRadioButton,
        QPushButton, QLabel, QListWidget, QLineEdit)
        
from instr import *
from final_win import *

class Person():
    def __init__(self, name, age):
        self.name = name
        self.age = age

class Experiment():
    def __init__(self, person, test_1, test_2, test_3):
        self.person = person
        self.test_1 = test_1
        self.test_2 = test_2
        self.test_3 = test_3

class TestWin(QWidget):
    def __init__(self):
        super().__init__()

        self.initUI()

        self.connects()

        self.set_appear()

        self.show()
    
    def next_click(self):
        self.tw = TestWin()

        self.hide()
    
    def connects(self):
        self.btn_next.clicked.connect(self.next_click)
    
    def set_appear(self):
        self.setWindowTitle(txt_title)

        self.resize(win_width, win_height)

        self.move(win_x, win_y)

    def initUI(self):
        self.btn_next = QPushButton(txt_sendresults, self)
        self.btn_test_1 = QPushButton(txt_startest1, self)
        self.btn_test_2 = QPushButton(txt_startest2, self)
        self.btn_test_3 = QPushButton(txt_startest3, self)
        
        self.text_name = QLabel(txt_name)
        self.text_age = QLabel(txt_age)
        self.text_test_1 = QLabel(txt_test_1)
        self.text_test_2 = QLabel(txt_test_2)
        self.text_test_3 = QLabel(txt_test_3)
        self.text_timer = QLabel(txt_timer)
        self.text_timer.setFont(QFont('Times', 36, QFont.Bold))

        self.loc = QLocale(QLocale.English, QLocale.UnitedStates)
        self.validator = QDoubleValidator()
        self.validator.setLocale(self.loc)

        self.line_name = QLineEdit(txt_name_2)
        self.line_age = QLineEdit(txt_age_2)
        self.line_age.setValidator(self.validator)
        self.line_age.setValidator(QIntValidator(7, 150))

        self.line_test_1 = QLineEdit(txt_hinttest1)
        self.line_test_1.setValidator(self.validator)
        self.line_test_1.setValidator(QIntValidator(0, 150))

        self.line_test_2 = QLineEdit(txt_hinttest2)
        self.line_test_2.setValidator(self.validator)
        self.line_test_2.setValidator(QIntValidator(0, 150))

        self.line_test_3 = QLineEdit(txt_hinttest3)
        self.line_test_3.setValidator(self.validator)
        self.line_test_3.setValidator(QIntValidator(0, 150))
        
        self.line_v = QVBoxLayout()
        self.line_v_2 = QVBoxLayout()
        self.line_h = QVBoxLayout()

        self.line_v_2.addWidget(self.text_timer, alignment = Qt.AlignCenter)
        self.line_v.addWidget(self.text_name, alignment = Qt.AlignLeft)
        self.line_v.addWidget(self.line_name, alignment = Qt.AlignLeft)
        self.line_v.addWidget(self.text_age, alignment = Qt.AlignLeft)
        self.line_v.addWidget(self.line_age, alignment = Qt.AlignLeft)

        self.line_v.addWidget(self.text_test_1, alignment = Qt.AlignLeft)
        self.line_v.addWidget(self.btn_test_1, alignment = Qt.AlignLeft)
        self.line_v.addWidget(self.line_test_1, alignment = Qt.AlignLeft)

        self.line_v.addWidget(self.text_test_2, alignment = Qt.AlignLeft)
        self.line_v.addWidget(self.btn_test_2, alignment = Qt.AlignLeft)
        
        self.line_v.addWidget(self.text_test_3, alignment = Qt.AlignLeft)
        self.line_v.addWidget(self.btn_test_3, alignment = Qt.AlignLeft)

        self.line_v.addWidget(self.line_test_2, alignment = Qt.AlignLeft)
        self.line_v.addWidget(self.line_test_3, alignment = Qt.AlignLeft)
        self.line_v.addWidget(self.btn_next, alignment = Qt.AlignCenter)
        self.line_h.addLayout(self.line_v)
        self.line_h.addLayout(self.line_v_2)
        self.setLayout(self.line_h)

    def next_click(self):
        self.hide()
        self.prs = Person(self.line_name.text, int(self.line_age.text()))
        self.exp = Experiment(self.prs, self.line_test_1.text(), self.line_test_2.text(), self.line_test_3.text())
        self.fw = FinalWin(self.exp)

    def timer_test_1(self):
        global time
        
        time = QTime(0, 0, 15)

        self.timer = QTimer()
        self.timer.timeout.connect(self.timer1Event)
        self.timer.start(1000)

    def timer1Event(self):
        global time

        time = time.addSecs(-1)
        self.text_timer.setText(time.toString("hh:mm:ss"))
        self.text_timer.setFont(QFont('Times', 36, QFont.Bold))
        self.text_timer.setStyleSheet('color: rgb(0,0,0)')
        if time.toString("hh:mm:ss") == '00:00:00':
            self.timer.stop()

    def timer2Event(self):
        global time

        time = time.addSecs(-1)
        self.text_timer.setText(time.toString("hh:mm:ss")[6:8])
        self.text_timer.setStyleSheet("color: rgb(0,0,0)")
        self.text_timer.setFont(QFont("Times", 36, QFont.Bold))
        if time.toString("hh:mm:ss") == "00:00:00":
            self.timer.stop()

            
    def timer_bob(self):
        global time 

        time = QTime(0, 0, 30)
        self.timer = QTimer()
        self.timer.timeout.connect(self.timer2Event)
        self.timer.start(1500)
    
    def timer3Event(self):
        global time

        time = time.addSecs(-1)
        self.text_timer.setText(time.toString("hh:mm:ss"))
        if int(time.toString("hh:mm:ss")[6:8]) >= 45:
            self.text_timer.setStyleSheet('color: rgb(0, 250, 0)')
        elif int(time.toString("hh:mm:ss")[6:8]) <= 15:
            self.text_timer.setStyleSheet('color: rgb(0, 250, 0)')
        else:
            self.text_timer.setStyleSheet('color: rgb(0, 0, 0)')
        self.text_timer.setFont(QFont("Times", 36, QFont.Bold))
        if time.toString("hh:mm:ss") == '00:00:00':
            self.timer.stop()
    def timer_final(self):
        global time 

        time = QTime(0, 1, 0)
        self.timer = QTimer()
        self.timer.timeout.connect(self.timer3Event)
        self.timer.start(1000)
    
    def connects(self):
        self.btn_next.clicked.connect(self.next_click)
        self.btn_test_1.clicked.connect(self.timer_test_1)
        self.btn_test_2.clicked.connect(self.timer_bob)
        self.btn_test_3.clicked.connect(self.timer_final)

    def set_appear(self):
        self.setWindowTitle(txt_title)
        self.resize(win_width, win_height)
        self.move(win_x, win_y)
