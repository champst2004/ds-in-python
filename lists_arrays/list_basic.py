l = [1, 3, 5, 'seven']

l.insert(0, 2)
print(l)

l.remove('seven') # removes value not index
print(l)

l.pop(2) # removes index not value
print(l)

l.reverse()
print(l)


x = list(range(5))
print(x)  # 0, 1, 2, 3, 4
x[1:4] = [45, 21, 83]
print(x)  # 0, 45, 21, 83, 4

del x[1:3]
print(x)


l2 = list(range(10))

print(l2[-2])