import os
from pathlib import Path
import openpyxl
import os.path
from openpyxl.worksheet.table import Table, TableStyleInfo
import tkinter.ttk
import tkinter as tk
from PyQt5.QtWidgets import QWidget
from PyQt5.QtWidgets import QFileDialog
from PyQt5.QtWidgets import QPushButton
from PyQt5.QtWidgets import QLabel
from PyQt5.QtWidgets import QApplication
from PyQt5.QtWidgets import QBoxLayout
from PyQt5.QtCore import Qt
import sys
from PyQt5.QtWidgets import * # PyQt5, Designer, tool 인스톨하셈
from PyQt5 import uic
#from PyQt5.QAxContaniner import *
from PyQt5.QtGui import *
import subprocess # 외부프로그램 여는 라이브러리
import pandas as pd # xlrd, pandas 인스톨하셈

wb = openpyxl.load_workbook('excelhere/List.xlsx')
sheet = wb.active
df = pd.DataFrame(sheet.values)

from_class = uic.loadUiType("This.ui")[0]
#QMainWindo, from_class를 상속받아 내 클래스 MyWindow
class MyWindow(QMainWindow, from_class):
    def __init__(self):
        super().__init__()
        self.setupUi(self) #this가 상속받은곳에 없으면 부모를 찾아감

    def setUI(self):
        self.setupUi(self) # UI 관련 함수
        self.print_bt.clicked.connect(self.print) # 프린트 버튼을 클릭 이벤트

    def initTableWidget(self, id):
        # 테이블 위젯 값 쓰기
        self.table.clear()
        # select dataframe
        df = self.df_list[id];
        # table write
        col = len(df.keys())
        self.table.setColumnCount(col)
        self.table.setHorizontalHeaderLabels(df.keys())

        row = len(df.index)
        self.table.setRowCount(row)
        self.writeTableWidget(id, df, row, col)

    def tb1(self, id, df, row, col):
        for r in range(row):
            for c in range(col):
                item = QTableWidgetItem(str(df.iloc[r][c]))
                self.table.setItem(r, c, item)
        self.table.resizeColumnsToContents()

    def table1(self):
        pass

    def table2(self):
        pass

    def load(self):
        pass

    # 외부 프로그램 실행
    def print(self):
        subprocess.run('Print/WinFormsApp11.exe')

    # 재고관리 엑셀 실행
    def item(self):
        pass
        #subprocess.run('C:/Garam/Print/List.xlsx')

    def list1(self):
        pd.read_excel('List.xlsx')


if __name__ == "__main__":

    app = QApplication(sys.argv)
    mywindow = MyWindow()
    mywindow.show()
    app.exec_()