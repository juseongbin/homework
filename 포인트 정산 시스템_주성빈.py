# 2. 포인트 정신 및 집계 시스템
all_list = []
def claim_points(emp_name, *expenses, **options):
    total = sum(expenses)
    discount_rate = 0
    if options.get('category') == '도서구입':
        discount_rate = 0.1
    elif options.get('category') == '체력단련':
        discount_rate = 0.2
    else:
        discount_rate = 0
    result = total - total*discount_rate
    result = int(result)
    user_info = [emp_name, len(expenses), total, result, options.get('category')]
    all_list.append(user_info)
    print(f'성명 : {emp_name}, 신청금액 : {total}, 최종 차감 포인트 : {result}, 구분 : {options}')
    return result
kim_point = claim_points('김대리', 30000, 45000, 15000, category = '도서구입')
lee_point = claim_points('이과장', 150000, category = '체력단련')
park_point = claim_points('박팀장', 50000, 70000, 80000, category = '의료비')
choi_point = claim_points('최사원', 25000, 18000, category = '개인사유')
print(all_list)
sort_list = sorted(all_list, key=lambda x:x[3], reverse=True)
print(sort_list)
print('순위 | 성명  | 건수  |   신청금액 |   최종차감포인트 | 구분\n-----------------------------------------------------')

for i in range(len(sort_list)):
    print(f'{i+1}위 | {sort_list[i][0]} | {sort_list[i][1]} | {sort_list[i][2]} | {sort_list[i][3]} | {sort_list[i][4]}')
