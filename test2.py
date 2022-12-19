import  openpyxl  as  op  #openpyxl 모듈 import

wb = op.load_workbook('xl/personal.xlsx',data_only=True)
ws = wb['빈소1']

#해당 시트의 최대 행값, 최대 열값 구하기

col_max = ws.max_column
row_max = ws.max_row

#출력해보기
print("최대행값 : ", row_max)
print("최대열값 : ", col_max)






