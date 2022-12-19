import tkinter
from tkinter import * # tkinter의 모든 함수 가져오기
from tkinter import messagebox, filedialog
import os
from pathlib import Path
import openpyxl
from openpyxl import load_workbook
import os.path
from openpyxl.worksheet.table import Table, TableStyleInfo
import tkinter.ttk
import tkinter as tk



def te(info_sheets, cell):

    info_sheets.cell(row = 1, column = repeat().value)



def repeat():

    i = 0
    while True:
        print(i)
        i += 1
        if i == None:
            break


'''def exsave(): #물품명 읽어오기

    row = []

    for x in range(1, (info_sheets.max_row + 1)):
        row.append(info_sheets.cell(x, 1).value)


    print(row[0])'''



home = 'xl/test.xlsx'
info_xl = 'xl/personal.xlsx'

og_file = openpyxl.load_workbook(home, data_only=True)  # 초기 시트 위치 저장(값으로)
info_file = openpyxl.load_workbook(info_xl, data_only=True)  # 개인정보, 빈소별 물품정보 저장 공간(값으)

info_sheets = [info_file['빈소1']]  # 지금은 하나만 사용하지만 빈소 창이 생기면 9개로 늘어날 것임

#exsave()

#print(te())

print(hasattr(info_sheets, 'cell'))
print(hasattr(info_sheets, 'max_row'))