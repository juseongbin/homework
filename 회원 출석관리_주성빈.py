import csv
import re
f = open('member_payments.csv', 'r', encoding='utf-8')
lines = csv.reader(f)
header = next(lines)
members = {}
errors = []
month_days = {1 : 31, 2 : 28, 3 : 31, 4 : 30, 5 : 31, 6 : 30, 7 : 31, 8 : 31, 9 : 30, 10 : 31, 11 : 30, 12 : 31}
for i in lines:
    if i[3] not in ['일일권', '30일권', '90일권']:
        errors.append(f'[결제정보] ?행 - {i[0]}: 등록되지 않은 이용권 종류입니다.')
        continue
    if not re.match(r'^\d{4}-\d{2}-\d{2}$', i[2]):
        errors.append(f'[결제정보] ?행 - {i[0]}: 결제일자가 올바르지 않습니다.')
        continue
    id = i[0]
    name = i[1]
    payday = i[2]
    membership = i[3]
    members[id] = {'name' : name, 
                  'payday' : payday, 
                  'membership' : membership}
#    for member_id in members:
#        membership = members[member_id]['membership']
#        if membership == '일일권':
#            days = 1
#        elif membership == '30일권':
#            days = 30
#        elif membership == '90일권':
#            days = 90
#    date_list = payday.split('-')
#    year = int(date_list[0])
#    month = int(date_list[1])
#    day = int(date_list[2])
#    day = day + (days - 1)
#    last_day = month_days[month]
#    if day > last_day:
#       day = day - last_day
#       month = month + 1

f = open('gym_attendance.txt', 'r', encoding='utf-8')
for id in members:
    members[id]['attendance'] = 0
lines = f.readlines()
header = lines[0]
for i in lines[1:]:
    data = i.strip().split('|')
    number = data[0]
    name = data[1]
    attendance = data[2]
    if number not in members:
        errors.append(f'[출석정보] ?행 - {number}: 등록된 회원정보가 없습니다.')
        continue
    if not re.match(r'^\d{4}-\d{2}-\d{2}$', attendance):
        errors.append(f'[출석정보] ?행 - {number}: 출석일자가 올바르지 않습니다.')
        continue
    if number in members:
        members[number]['attendance'] += 1
