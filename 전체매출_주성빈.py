#딕셔너리 문제
#상품 판매 정보(sales)와 상품 가격정보(prices)가 있을 때, 
# 전체 매출을 계산해보세요.

sales = {
    "키보드": 15,
    "마우스": 25,
    "모니터": 8
}

prices = {
    "키보드": 50000,
    "마우스": 20000,
    "모니터": 200000
}

keyboard = sales["키보드"]*prices["키보드"]
mouse = sales["마우스"]*prices["마우스"]
monitor = sales["모니터"]*prices["모니터"]

total = keyboard+mouse+monitor

print('총 매출은 %d원입니다.'%total)

total = (sales["키보드"]*prices["키보드"] + 
         sales["마우스"]*prices["마우스"] + 
         sales["모니터"]*prices["모니터"])

print(f'총 매출은 {total}원 입니다.')

total = 0

for x in  sales:
    total = total + sales[x]*prices[x]

print(f'총 매출은 {total}원 입니다.')

#while로는 어렵네요