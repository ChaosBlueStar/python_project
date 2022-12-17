age = int(input('나이를 입력하세요 :'))

if age < 11:  # 10세 이하
    price = '1000원'

elif age >= 65:  # 65세 이상
    price = '0원'

else:  # 나머지 (기본)
    price = '2000원'

print('입장료는', price, '입니다.')