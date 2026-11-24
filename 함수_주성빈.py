orders = [
    {"order_id": 1001, "user": "kim", "category": "의류", "amount": 75000, "status": "완료"},
    {"order_id": 1002, "user": "lee", "category": "식품", "amount": 32000, "status": "취소"},
    {"order_id": 1003, "user": "park", "category": "전자제품", "amount": 120000, "status": "완료"},
    {"order_id": 1004, "user": "kim", "category": "식품", "amount": 45000, "status": "배송중"},
    {"order_id": 1005, "user": "choi", "category": "의류", "amount": 90000, "status": "완료"},
    {"order_id": 1006, "user": "lee", "category": "전자제품", "amount": 180000, "status": "완료"},
    {"order_id": 1007, "user": "park", "category": "식품", "amount": 25000, "status": "완료"},
    {"order_id": 1008, "user": "kim", "category": "의류", "amount": 65000, "status": "취소"},
    {"order_id": 1009, "user": "choi", "category": "전자제품", "amount": 210000, "status": "완료"},
    {"order_id": 1010, "user": "lee", "category": "식품", "amount": 55000, "status": "배송중"}
]

#def get_sales_by_category(orders, category):
#    total = 0
#    category_sales = {}
#    category = category
#    for order in orders:
#        if order['category'] == category and order['status'] == '완료':
#            total += order['amount']
#            category_sales = category, total
#
#    return category_sales
#
#print(get_sales_by_category(orders, '의류'))

def get_sales_by_category(orders):
    category_sales = {}
#    for i in range(len(orders)):
    for order in orders:
        if order['status'] == '완료':
            product = order['category']
            if product not in category_sales:
                category_sales[product] = order['amount']
            else:
                category_sales[product] += order['amount']
    return category_sales
print(get_sales_by_category(orders))

def get_vip_customers(orders, min_amount):
    vip_name = []
    total_amount = {}
    for order in orders:
        if order['status'] == '완료':
            amount = order['amount']
            user = order['user']
            if user not in total_amount:
                total_amount[user] = amount
            else:
                total_amount[user] += amount
    for name, all_amount in total_amount.items():
            if all_amount >= min_amount:
                vip_name.append(name)

    return vip_name

print(get_vip_customers(orders, 300000))
print(get_vip_customers(orders, 100))