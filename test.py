import openpyxl
from tkinter import filedialog
file = filedialog.askopenfilename(initialdir='./',title = 'choose your file',filetypes=(("Excel Files","*.xlsx"),('all files','*.*'))) #file open
excelFile = openpyxl.load_workbook(file) #file name
sheet_lst = excelFile.sheetnames #call list of sheet
print(sheet_lst)
num = int(input("\n insert sheet's num : "))-1 #select sheet num
sheet = excelFile[sheet_lst[num]]
for row in sheet.rows: #print all rows
    for cell in row:
        print(cell.value,end='  ')
    print('\n')