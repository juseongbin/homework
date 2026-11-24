list_empty = []
list_empty.append(1)
print(list_empty)
#list_empty.append(2, 3, 4, 5, 6, 7, 8, 9, 10)
#print(list_empty)
list_empty.remove(1)
print(list_empty)
for x in range(10):
    list_empty.append(x+1)
    print(list_empty)

a=1
list_while = []
while a < 11:
    list_while.append(a)
    print(list_while)
    a += 1