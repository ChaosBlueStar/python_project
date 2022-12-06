from tkinter import *

win = Tk() # 창 생성
win.geometry("1000x720") # 창의 크기
win.title("표 생성 테스트") # 창의 제목
win.option_add("*Font", "맑은고딕 11")

표생성 = (print('<style>table, tr, td {border: 1px solid #444444; border-collapse: collapse;}</style>')
print('<h2>구구단</h2><table>')
for i in range(1, 10):
    print(f'<tr>')
    for j in range(2, 10):
        print(f'<td>{j} x {i} = {i*j:2}</td>', end=' ')
    print(f'</tr>')

print('</table>'))


win.mainloop() # 창 실행