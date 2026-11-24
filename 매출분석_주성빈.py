sales = [
    ["강남점", 120, 150, 130, 170, 200, 250, 220],
    ["홍대점", 90, 110, 100, 130, 160, 180, 140],
    ["잠실점", 200, 220, 210, 250, 300, 350, 320],
    ["부산점", 80, 75, 95, 100, 120, 150, 130]
]

days = ["월요일", "화요일", "수요일", "목요일", "금요일", "토요일", "일요일"]

everyday = []

for x in sales:
    for i in range(len(days)):
        everyday.append([days[i], x[0], x[i+1]])
print(everyday)
print('------매장별------')
for a in sales:
    total = 0
    for day in everyday:
        if day[1] == a[0]:
            total += day[2]
    print(f'{a[0]} 총 매출 : {total}원')


print('----요일별----')
for day in days:
    total = 0
    for a in everyday:
        if a[0] == day:
            total += a[2]
    print(f'{day} 총 매출 : {total} 원')

print('---최고매출이 가장 높은 매장---')
highsales = 0
for a in sales:
    for day in everyday:
        if day[1] == a[0]:
            if day[2] > highsales:
                highsales = day[2]
                highscore = day[1]
#for high in everyday:
#    if high[2] == highsales:
#        print(f'최고매출지점 : {high[1]}, 최고매출액 :{highsales}원')
print(f'최고매출지점은 {highscore}이고, 매출은 {highsales}원 입니다.')

print('-----최고매출요일-----')
highsales = 0
for a in days:
    total = 0
    for day in everyday:
        if day[0] == a:
            total += day[2]
            if total > highsales:
                highsales = total
                peakday = day[0]

print(f'최고매출요일은 {peakday}이고, 매출은 {highsales}원 입니다.')            