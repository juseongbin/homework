orders = [
    {"order_id": 1001, "user": "kim", "amount": 75000, "status": "완료"},
    {"order_id": 1002, "user": "lee", "amount": 32000, "status": "취소"},
    {"order_id": 1003, "user": "park", "amount": 120000, "status": "완료"},
    {"order_id": 1004, "user": "kim", "amount": 45000, "status": "배송중"},
    {"order_id": 1005, "user": "choi", "amount": 90000, "status": "완료"},
    {"order_id": 1006, "user": "lee", "amount": 180000, "status": "완료"}
]

name = [ordername['user'] for ordername in orders]
print(name)



name80000 = [order['user'] if order['amount'] >= 80000 else '소액'
             for order in orders]
print(name80000)
name80000 = list(set(name80000))
name80000.remove('소액')
print(name80000)
#set로 중복(소액)제거 못함