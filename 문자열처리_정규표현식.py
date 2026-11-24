order = {"customer": {"name": "  Kim Minsu  ", "email": "  MINSU@EXAMPLE.COM  "}, 
          "order_id": "2026-00125"}
customer = order['customer']
#print(customer)
# 1. 고객 이름 정리
customer['name'] = customer['name'].strip()
#print(customer)
# 2. 이메일 정리
customer['email'] = customer['email'].strip().lower()
#print(customer)
# 3. 주문 번호 정리
order["order_id"] = 'COU-' + order["order_id"].replace('-', '')
#print(customer)
# 4. 결과 출력
print(order)

#-------------------------------------------------------

import re

html = "<title>상품 정보</title><title>가격 안내</title>"

# 여기에 코드 작성
result = re.findall(r'<title>([a-zA-Z가-힣\w\s]+)</title>', html)
print(result)