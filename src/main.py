#!/bin/env python3

"""Morse Translator version 0.1
Created by Mikhael Yolgin"""

import sys
import time

from PyQt5 import QtCore, QtGui, QtWidgets, uic
from PyQt5.QtCore import QThread
from PyQt5.QtWidgets import QMessageBox

import MorseTranslator as MT
from AudioGenerator import generate
from MorseReader import playMorse


class ReadMorseThread(QThread):
    def __init__(self, parent=None):
        super().__init__()
        self.parent = parent

    def run(self):
        morse_text = self.parent.lineEdit_Morse.text()

        # Add denote message: "...- ...- ...- -...- morse text -.-"
        if self.parent.checkBox_denoteMessage.isChecked() == True:
            morse_text = "...- ...- ...- -...- " + morse_text + " -.-"

        try:
            playMorse(
                morse_text,
                tone=self.parent.spinBox_soundFrequency.value(),
                level=self.parent.spinBox_soundLevel.value(),
                small_duration=self.parent.spinBox_soundSmallDuration.value(),
                middle_duration=self.parent.spinBox_soundMiddleDuration.value(),
                small_pause=self.parent.spinBox_soundSmallPause.value(),
                middle_pause=self.parent.spinBox_soundMiddlePause.value(),
                big_pause=self.parent.spinBox_soundBigPause.value(),
            )

        except:
            pass
        """
        small_duration=100,
        middle_duration=300,
        small_pause=50,
        middle_pause=250,
        big_pause=500,
        tone=500,
        """


class GenetarteSound(QThread):
    def __init__(self, parent=None):
        super().__init__()
        # self.parent = parent

    def run(self):
        generate(500, 10000)

    def stop(self):
        self.quit()
        self.threadactive = False
        self.wait()

    # def stop(self):
    #     # self.exit()
    #     # self.close()
    #     self.quit()
    #     # quit()


class MainWindow(QtWidgets.QMainWindow):
    def __init__(self):
        super(MainWindow, self).__init__()
        uic.loadUi("morse_UI.ui", self)
        self.connectUi()
        self.show()

        self.text_to_morse = ""
        self.morse_to_text = ""

        self.readMorse_instance = ReadMorseThread(parent=self)

        self.timeDict = []
        self.last_time = 0
        self.generateSound_instance = GenetarteSound(parent=self)

    def connectUi(self):

        self.lineEdit_Text.textChanged.connect(self.textChanged)
        self.lineEdit_Morse.textChanged.connect(self.morseChanged)

        # Buttons
        self.btn_Play.clicked.connect(self.readMorse)
        self.btn_Input.released.connect(self.btn_Input_onReleased)
        self.btn_Input.pressed.connect(self.btn_Input_onPress)

        # Actions
        self.actionAbout.triggered.connect(self.dialogAbout)
        self.actionExit.triggered.connect(self.close)

    def btn_Input_onPress(self):
        self.start_time = time.time()

    def btn_Input_onReleased(self):
        self.released_time = time.time()
        print("duration:", self.released_time - self.start_time)

        try:
            self.morseRecognition(self.start_time, self.released_time)

        except Exception as e:
            print(e)

    def morseRecognition(self, pressed_time, unpressed_time):

        # Time till event
        short_duration = self.spinBox_dotDuration.value() / 1000
        # long_duration = self.spinBox_minusDuration.value() / 1000
        space_duraction = self.spinBox_spaceDuration.value() / 1000
        separate_duration = self.spinBox_separateDuration.value() / 1000

        # Calculate press and unpress duration for DOT and MINUS
        duration_time = unpressed_time - pressed_time

        # Calculate press duration for SPACE and SEPARATOTR
        try:
            self.duration_last_unpressed_time = pressed_time - self.last_unpressed_time
            print(
                "duration form last unpressed time:", self.duration_last_unpressed_time
            )

        except:
            pass

        # Add space and separator
        try:
            if (
                self.duration_last_unpressed_time >= space_duraction
                and self.duration_last_unpressed_time < separate_duration
            ):
                print("' '")
                self.addMorseText(" ")

            elif self.duration_last_unpressed_time > separate_duration:
                print(" / ")
                self.addMorseText(" / ")
        except:
            pass

        # Add dot and minus
        if duration_time <= short_duration:
            print(".")
            self.addMorseText(".")

        elif duration_time > short_duration:
            print("-")
            self.addMorseText("-")

        self.last_unpressed_time = unpressed_time

    def addMorseText(self, text):
        morse = self.lineEdit_Morse.text()
        self.lineEdit_Morse.setText(morse + str(text))

    def textChanged(self):
        try:
            if self.readMorse_instance.isRunning() == True:
                self.readMorse_instance.terminate()
        except Exception as e:
            print(e)

        text_in_line = self.lineEdit_Text.text()
        text_in_line = text_in_line.upper()
        print(text_in_line)
        if text_in_line != self.morse_to_text:
            print("Text:", text_in_line)
            print(MT.encrypt(text_in_line))
            morse_in_line = MT.encrypt(text_in_line)
            self.text_to_morse = morse_in_line
            self.lineEdit_Morse.setText(morse_in_line)
            print(morse_in_line)

    def morseChanged(self):
        try:
            if self.readMorse_instance.isRunning() == True:
                self.readMorse_instance.terminate()
        except Exception as e:
            print(e)

        morse_in_line = self.lineEdit_Morse.text()

        # Вкл\Выкл кнопку "Воспроизвести" и очиска поля текса
        if morse_in_line == "":
            self.btn_Play.setEnabled(False)
            self.lineEdit_Text.setText("")
        else:
            self.btn_Play.setEnabled(True)

        if morse_in_line != self.text_to_morse:
            # Чистим от знаков
            for sing in morse_in_line:
                if sing != "-" and sing != "." and sing != " " and sing != "/":
                    morse_in_line = morse_in_line.replace(sing, "")

            self.lineEdit_Morse.setText(morse_in_line)

            decrypted_text = MT.decrypt(morse_in_line)
            self.morse_to_text = decrypted_text
            self.lineEdit_Text.setText(decrypted_text)

    def readMorse(self):
        self.readMorse_instance = ReadMorseThread(parent=self)
        if self.readMorse_instance.isRunning() == False:
            self.readMorse_instance.start()

    # UI Metods

    def dialogAbout(self):
        QMessageBox.about(
            self,
            "О Morse Translator",
            "Morse Translator — это программа для перевода текста в морзе и морзе в текст\n\nВерсия 0.1",
        )

    def dialogCritical(self, message):
        dlg = QMessageBox(self)
        dlg.setText(str(message))
        dlg.setIcon(QMessageBox.Critical)
        dlg.show()


if __name__ == "__main__":
    app = QtWidgets.QApplication(sys.argv)
    window = MainWindow()
    app.exec_()

