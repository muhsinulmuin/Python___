'''
a = [1,2,3,4,5]

result = 0 

i = 0
n = len(a)
while i<n: # 0<5, 1<5, 2<5, 3<5, 4<5, 5<5 
    result = result + a[i]  # 0+1, 1+2, 3+3, 6+4, 10+5
    i = i+1
    
print(result)
'''

a = [-10,2,19,-3,-5] # [0, 2, 19, -3, -5]

i = 0
while i<len(a):
    if a[i] < 0:
        a[i] = 0
    i += 1
print(a)