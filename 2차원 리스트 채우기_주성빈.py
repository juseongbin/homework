# 1. 2차원 리스트 채우기
# 1-1
list1 = []
num = 1
for f in range(5):
    list2 = []
    for i in range(5):
        list2.append(num)
        num += 1
    list1.append(list2)
print(list1)

# 1-2
list1 = []
num = 1
for f in range(5):
    list2 = []
    for i in range(5):
        list2.append(num + i * 5)
    list1.append(list2)
    num += 1
print(list1)

# 1-3
list1 = []
num = 1
for f in range(5):
    list2 = []
    for i in range(5):
        if int(len(list1)) % 2 == 0:    
            list2.append(num)
        else:
            list2.insert(0, num)
        num += 1
    list1.append(list2)
print(list1)

# 1-4
list1 = []
num = 1
for f in range(5):
    list2 = []
    for i in range(5):
        if int(len(list1)) % 2 == 0:    
            list2.append(num)
        else:
            list2.insert(0, num)
        num += 1
    list1.append(list2)
print(list1)
