import sys
import time
import pyperclip
import os
import keyboard
import subprocess
import win32api
import win32com.client
from PyQt5 import QtGui
from PyQt5.QtWidgets import (QApplication, QMainWindow, QPushButton,
                             QToolTip, QMessageBox, QLabel)


class Window2(QMainWindow):
    def __init__(self, last_window):
        super().__init__()
        self.last_window = last_window
        self.setWindowTitle("Second window")

    def closeEvent(self, event):
        event.accept()
        self.last_window.show()


class Window(QMainWindow):
    def __init__(self):
        super().__init__()

        self.title = "First Window"
        self.top = 100
        self.left = 100
        self.width = 680
        self.height = 500

        self.buttonStart = QPushButton("Start WoW", self)
        self.buttonStart.move(275, 150)
        self.buttonCopy = QPushButton("Copy Ww to clipboard", self)
        self.buttonCopy.setObjectName("copyButton")
        self.buttonCopy.move(275, 200)
        self.buttonConfig = QPushButton("Configuration", self)
        self.buttonConfig.move(275, 250)
        self.buttonConfig.setToolTip("<h3>Open configuration panel</h3>")

        # self.buttonStart.clicked.connect(self.pressStart)
        self.buttonCopy.clicked.connect(self.pressCopy)
        self.buttonConfig.clicked.connect(
            self.pressWindow2)
        self.buttonStart.clicked.connect(self.pressStart)

        self.main_window()

    def main_window(self):
        self.label = QLabel("Hey Bar!", self)
        self.label.move(285, 100)
        self.setWindowTitle(self.title)
        self.setGeometry(self.top, self.left, self.width, self.height)
        self.show()

    def pressCopy(self):
        pyperclip.copy('Ww')

    def pressWindow2(self):
        self.w = Window2(self)
        self.w.show()
        self.hide()

    def pressStart(self):
        ruta="Data/{}/realmlist.wtf"
        if os.path.exists(ruta.format("enUS")): 
          with open('Data/enUS/realmlist.wtf','w') as f:
            f.write(str("Set realmlist logon.warmane.com "))
        if os.path.exists(ruta.format("enGB")):
          with open('Data/enGB/realmlist.wtf','w') as f:
            f.write(str("Set realmlist realm123"))      
        program = 'wow.exe'
        subprocess.Popen(program)
        shell = win32com.client.Dispatch("WScript.Shell") 
        win32api.Sleep(5000) 
        shell.SendKeys("bar") 
        shell.SendKeys("{TAB}") 
        shell.SendKeys("hola123") 
        shell.SendKeys("{ENTER}")

stylesheet = """
    QToolTip {
        border: 1px solid #76797C;
        background-color: rgb(90, 102, 117);
        color: red;
        padding: 5px;
        opacity: 200;
    }
    QPushButton#copyButton {
        min-width: 200px;
    }
"""


if __name__ == "__main__":
    app = QApplication(sys.argv)
    app.setStyleSheet(stylesheet)
    window = Window()
    sys.exit(app.exec())
