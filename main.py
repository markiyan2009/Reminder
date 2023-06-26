import sys

from PyQt5 import QtCore

from PyQt5.QtCore import QDate
from PyQt5.QtWidgets import QApplication, QWidget
from PyQt5.QtWidgets import QMainWindow
from main_win import Ui_MainWindow
from bs4 import BeautifulSoup
import requests as re
import lxml
from dates2 import Ui_MainWindow as DatesWin

import json
import io

# Створення пустого словника для дат
dates_dict = dict()

class Main(QMainWindow):
    def __init__(self):
        super().__init__()
        self.ui = Ui_MainWindow()
        self.ui.setupUi(self)
        self.ui.ruotine.clicked.connect(self.showDate)
        
    def showDate(self):
        self.hide()
        dates.show()
        

class Dates2(QMainWindow):
    def __init__(self):
        super().__init__()
        self.ui = DatesWin()
        self.ui.setupUi(self)
        self.hide()
        self.ui.exit.clicked.connect(self.click_exit)
        self.ui.add.clicked.connect(self.add)
        self.ui.event.setText("Подія")
        global dates_dict
        
        # Завантаження збережених дат з файлу JSON
        
            
        self.ui.update.clicked.connect(self.update)
            

    def click_exit(self):
        self.hide()
        main.show()
        
    def add(self):
        name = self.ui.calendar.selectedDate().toString()
        
        # Додавання події до словника дат
        dates_dict[self.ui.calendar.selectedDate().toString()] = self.ui.event.toPlainText()
        
        # Збереження словника дат у файл JSON
        with io.open("dates.json","w",encoding="utf-8") as file:
            if dates_dict[self.ui.calendar.selectedDate().toString()] not in dates_dict:
                json.dump(dates_dict,ensure_ascii=False,fp=file)
        
    def update(self):
        if self.ui.calendar.selectedDate().toString() in dates_dict:
            self.ui.event.setText(dates_dict[self.ui.calendar.selectedDate().toString()])
        else:
            self.ui.event.setText("На цей день подія не встановлена")

if __name__ == "__main__":
    app = QApplication(sys.argv)
    main = Main()
    dates = Dates2()
    main.show()
    sys.exit(app.exec_())