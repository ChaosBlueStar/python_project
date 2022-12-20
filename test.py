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

home = 'xl/test.xlsx'
info_xl = 'xl/personal.xlsx'

og_file = openpyxl.load_workbook(home, data_only=True)  # 초기 시트 위치 저장(값으로)
info_file = openpyxl.load_workbook(info_xl, data_only=True)  # 개인정보, 빈소별 물품정보 저장 공간(값으)
trade_xl='xl/trade.xlsx'
trade_file=openpyxl.load_workbook(trade_xl,data_only=True)
info_sheets = [info_file['빈소1']]  # 지금은 하나만 사용하지만 빈소 창이 생기면 9개로 늘어날 것임
readsh=info_file['빈소1']  #Hong info_sheets에 리스트를 2개씩 사용해서 읽히지않아 추가 작성
readtrade=trade_file['거래명세서'] #거래명세서 시트 읽어오기

def exsave():  # 빈소에 등록 된 물품명 읽어오기

    row = []

    for x in range(1, (readsh.max_row + 1)):  # 행의 끝까지 반복
        row.append(readsh.cell(x, 1).value)  # row에 값 넣기 / 1을 바꾸면 열이 바뀜

    print(*row)  # row 내의 목록 전체 출력 (테스트용)


def exsave2():  # 거래명세서에 등록 된 물품명 읽어오기
    row = []

    for x in range(7, (readtrade.max_row + 1)):  # 7번행부터 (물품명 시작) 끝까지 반복
        row.append(readtrade.cell(x, 3).value)  # C열부터 (물품명) row에 값넣기

    #print(*row)  # row 내의 목록 전체 출력 (테스트용)

def compare():
    a = {exsave() == exsave2()}
    if a == "치즈김밥":
        print('일치')
    else:
        print('미일치')


def write():
    for x in range ((readtrade.max_row + 1), 6):
        readtrade.cell(x).value = '2'


write()
trade_file.save('xl/trade.xlsx')






compare()