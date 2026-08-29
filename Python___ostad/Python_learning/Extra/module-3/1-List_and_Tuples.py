a = [1, 2, 3, 'Naim', 'Fahim', 8.9, 3.4]

# list mutable -> চাইলেই কোন ডাটা আপডেট বা মোটিফাই করতে পারি
'''
a[0] = 100
print(a)
print(a[-1])
print(len(a))

# s = "Hello" --> ['H', 'e', "l", 'o']

s = "Hello"
print(list(s))
'''

a.append([1,2,3])
#print(a.index(3))
a.reverse()
print(a)

# tuple() --> Immutable 

t = (1,2,3)

# t[0] = 100

print(t)