#매출 데이터 분석하기
# 행은 지점, 열은 월요일부터 일요일까지의 매출
# 1. 전체 배열의 shape를 출력하세요
import numpy as np
sales = np.array([
[120, 150, 130, 180, 200, 170, 190],
[100, 110, 140, 160, 150, 180, 200],
[200, 190, 210, 220, 230, 250, 240],
[90, 100, 110, 120, 130, 140, 150]
])

print('1. 배열 크기')
print(sales.shape)
print()

# 2. 첫번째 지점의 일주일 매출을 출력하세요

weekly_sales = sales.sum(axis=1)
print('2. 첫 번째 지점의 일주일 매출')
print(sales[0])
print()
#print(weekly_sales[0])

# 3. 모든 지점의 토요일 매출을 출력하세요

daily_sales = sales.sum(axis=0)
print('3. 모든 지점의 토요일 매출')
print(sales[:,-2])
print()
#print(daily_sales[-2])

# 4. 전체 매출의 합계를 구하세요

total_sales = sales.sum()
print('4. 전체 매출 합계')
print(total_sales)
print()

# 5. 각 지점의 일주일 평균 매출

print('5. 지점별 평균 매출')
print(sales.mean(axis=1).round(2))
print()

# 6. 총 매출이 가장 높은 지점

print('6. 총매출이 가장 높은 지점')
print(f'지점 번호: {weekly_sales.argmax()+1}번')
print(f'총매출 : {weekly_sales.max()}')