# LAB 7 check 1


s1 = [2,1,4,3]

s2 = ['c','a','b']

print(s1 + s2)
print(3 * s1 + 2 * s2)
print(s1[1])
print(s1[1:3])

## cant concatenate a str to a list
#print(s1 + s2[-1])

print()

s1 = [2,1,4,3]
s1.remove(2)
print(s1)

s1 = [2,1,4,3]
s1.sort()
print(s1)

s1 = [2,1,4,3]
s1.append([s2.index('b')])
print(s1)

## pop index is out of range
#s2 = ['c','a','b']
#s2.pop(s1.pop(2))
#print(s2)

s2 = ['c','a','b']
s2.insert(s1[0], 'd')
print(s2)

