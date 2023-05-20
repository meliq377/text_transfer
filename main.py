import sys
import io

import serial
import time

from PyQt5 import QtCore, QtWidgets
from PyQt5.QtWidgets import QMainWindow, QWidget, QLabel, QLineEdit
from PyQt5.QtWidgets import QPushButton
from PyQt5.QtCore import QSize

lst = []
trans_dic = {"ա": 'a', "բ": 'b', "ց": 'c', "դ": 'd', "է": 'e', "ֆ": 'f', "գ": 'g', "հ": 'h', "ի": 'i', "ջ": 'j', "կ": 'k', "լ": 'l', "մ": 'm',
     "ն": 'n', "օ": 'o', "պ": 'p', "ք": 'q', "ռ": 'r', "ս": 's', "տ": 't', "ւ": 'u', "վ": 'v', "և": 'w', "խ": 'x', "ը": 'y', "զ": 'z',
     "ե": "ye", "թ": "th", "ժ": "dj", "ծ": "ts", "ձ": "dz", "ղ": "gh", "ճ": "tsh", "յ": "jh", "շ": "sh", "ո": "vo", "չ": "ch", "ր": "ry","ph": "փ",
    }

# arduino = serial.Serial(port='COM5', baudrate=9600, timeout=.1)


class MainWindow(QMainWindow):
    def __init__(self):
        QMainWindow.__init__(self)

        self.setMinimumSize(QSize(320, 140))
        self.setWindowTitle("FBF")

        self.nameLabel = QLabel(self)
        self.nameLabel.setText('''Enter the text:''')
        self.line = QLineEdit(self)

        self.line.move(110, 20)
        self.line.resize(200, 32)
        self.nameLabel.move(20, 20)

        pybutton = QPushButton('OK', self)
        pybutton.clicked.connect(self.clickMethod)
        pybutton.resize(200, 32)
        pybutton.move(110, 60)

    def clickMethod(self):
        # lst = []
        # t = self.line.text()
        # t = t.lower()
        # for char in t:
        #     if char.isalpha() or char.isalnum():
        #         if char in trans_dic.keys():
        #             lst.append(trans_dic[char])
        #             arduino.write(bytes(trans_dic[char] + " ", 'utf-8'))
        #             print("second time ։ " + trans_dic[char])

        #         else:
        #             lst.append(char)
        #             arduino.write(bytes(char + " ", 'utf-8'))
        #         time.sleep(0.05)
        #         print(arduino.readline(), " || ")
        #         time.sleep(0.05)
        # print(lst)

        output_file = open('text_output.txt', 'w')
        for selected_char in lst:
            with io.open('text_output.txt', 'w', encoding='utf8') as file:
                file.write(selected_char)
        output_file.close()
        self.line.clear()


if __name__ == "__main__":
    app = QtWidgets.QApplication(sys.argv)
    mainWin = MainWindow()
    mainWin.show()
    sys.exit(app.exec_())
