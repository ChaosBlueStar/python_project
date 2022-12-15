import random
import time
import numpy as np
import sys

def check(x):                       #정답 체크
    global correct_count
    if(x == int(result)):
        print("정답!! :",str(result))
        correct_count = correct_count + 1
    elif( int(x) !=  int(result)):
        print("오답!! :",str(result))
        # correct_count = correct_count - 1
    else:
        print("뭐야??")

def question(a):                    #문제 생성하기
    global result
    b = random.randint(2, 4)
    numbers = [random.randint(2, 12) for i in range(b)]
    print(" * ".join([str(i) for i in numbers]))  # 출력을 위해 numbers를 str로 변환
    result = np.prod(nu
if(__name__ == '__main__'):             #메인함수
    fp = open("time_record.txt","a",encoding='utf - 8')
    name = input("이름을 입력하세요")
    t = time.time()                     #시간 측정
    correct_count = 0
    count = 1                           #문제 번호

    while(correct_count<4):             #문제 갯수
        question(name)                   #문제 생성 함수로 이동합니다 ->괄호안에는 아무거나 넣음 괜찮은건가?
        count = count + 1
        try:                            #정수가 아닌 문자열이나 엔터만 눌렀을때
            answer = int(input("답을 입력하세요: "))
        except ValueError:
            print("\n숫자를 입력하세요!!!!!!!\n")
            answer = int(input("답을 입력하세요: "))
        check(int(answer))          #문제의 답과 사용자의 답 비교 함수
        t2 = time.time()            #시간측정
        t3 = (t2) - (t)             #시간측정

        lines = [name,'    ',str(correct_count),'/',str(count-1),'개    ',str(round(t3,2)),'초']
        print(correct_count,'개 맞았습니다',str(round(t3,2)),"초\n")

    fp.write('\n')
    fp.writelines(lines)            #파일에 데이터 입력
    fp.write('\n')
    fp.close()