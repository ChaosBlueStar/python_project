from tkinter import *

import openpyxl

wb = openpyxl.load_workbook("C:\\Users\\semi4\\Desktop\\python\\연습용.xlsx")
시트 = wb["Sheet1"]
시트1 = print(시트['B1'].value)
