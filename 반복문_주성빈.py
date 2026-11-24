count = 0
sales = 0
while sales < 1000000:
    pay = int(input('매출을 입력해주세요 : '))
    if pay < 0:
        print('음수는 계산할 수 없습니다.')
        count += 1
        print(f'현재 입력 횟수는 {count}회 입니다.')
    else:
        if sales < 1000000:
            sales = sales + pay
            count += 1
            print(f'현재 누적 매출은 {sales}원 입니다.')
            print(f'현재 입력 횟수는 {count}회 입니다.')
            if sales >= 1000000:
                print(f'최종 누적 매출은 {sales}원 입니다.')
                print(f'최종 입력 횟수는 {count}회 입니다.')