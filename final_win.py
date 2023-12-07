from PyQt5.QtCore import Qt, QTimer, QTime, QLocale
from PyQt5.QtGui import QDoubleValidator, QIntValidator, QFont
from PyQt5.QtWidgets import (
        QApplication, QWidget, 
        QHBoxLayout, QVBoxLayout, QGridLayout, 
        QGroupBox, QRadioButton,
        QPushButton, QLabel, QListWidget, QLineEdit)
        
from instr import *
class FinalWin(QWidget):
    def __init__ (self, exp):
        super().__init__()
        self.exp = exp
        self.initUI()
        self.set_appear()
        self.show()


    def results(self):
        if self.exp.person.age < 7:
            self.index = 0
            return 'Нет данных для то кого возраста.'
        self.index = (4 * (int(self.exp.test_1) + int(self.exp.test_2) + int(self.exp.test_3)) - 200) / 10
        if self.exp.person.age == 7 or self.exp.person.age == 8:
            if self.index >= 21:
                return txt_res_1
            elif self.index < 21 and self.index >= 17:
                return txt_res_2
            elif self.index < 17 and self.index >= 12:
                return txt_res_3
            elif self.index < 12 and self.index >= 6.5:
                return txt_res_4
            else:
                return txt_res_5

        if self.exp.person.age == 9 or self.exp.person.age == 10:
            if self.index >= 19.5:
                return txt_res_1
            elif self.index < 19.5 and self.index >= 15.5:
                return txt_res_2
            elif self.index < 15.5 and self.index >= 10.5:
                return txt_res_3
            elif self.index < 10.5 and self.index >= 5:
                return txt_res_4
            else:
                return txt_res_5

        if self.exp.person.age == 11 or self.exp.person.age == 12:
            if self.index >= 18:
                return txt_res_1
            elif self.index < 18 and self.index >= 14:
                return txt_res_2
            elif self.index < 14 and self.index >= 9:
                return txt_res_3
            elif self.index < 9 and self.index >= 3.5:
                return txt_res_4
            else:
                return txt_res_5
        
        if self.exp.person.age == 13 or self.exp.person.age == 14:
            if self.index >= 16.5:
                return txt_res_1
            elif self.index < 16.5 and self.index >= 12.5:
                return txt_res_2
            elif self.index < 12.5 and self.index >= 7.5:
                return txt_res_3
            elif self.index < 7.5 and self.index >= 2:
                return txt_res_4
            else:
                return txt_res_5
        
        if self.exp.person.age >= 15:
            if self.index >= 15:
                return txt_res_1
            elif self.index < 15 and self.index >= 11:
                return txt_res_2
            elif self.index < 11 and self.index >= 6:
                return txt_res_3
            elif self.index < 6 and self.index >= 0.5:
                return txt_res_4
            else:
                return txt_res_5

    def initUI(self):
        self.work_txt = QLabel(txt_workheart + self.results())
        self.index_txt = QLabel(txt_index + str(self.index))
        self.layout_line = QVBoxLayout()
        self.layout_line.addWidget(self.index_txt, alignment = Qt.AlignCenter)
        self.layout_line.addWidget(self.work_txt, alignment = Qt.AlignCenter)
        self.setLayout(self.layout_line)
    
    def set_appear(self):
        self.setWindowTitle(txt_final_win)
        self.resize(win_width, win_height)
        self.move(win_x, win_y)
