from operator import itemgetter, attrgetter, methodcaller

n = int(input())

arr = []
for i in range(n):
    arr.append([input(),float(input())])

# sort là hàm tự thay đổi biến số truyền vào, còn sorted thì không
# arr = sorted(arr,key = lambda grade: grade[1]) # sort by 2nd value
sorted(arr,key = itemgetter(1,0))
# arr = sorted(arr,key = attrgetter('<name of value>'))
print(arr)

