# Operators in Python
print('ab' > 'ad')
print(7.0 > 7)
print(6 == 6)


x = 7
y = 8
z = 0

result1 = x==y
result2 = y>x
result3 = z < x + 2

print(result1,result2,result3)

result4 = result1 or result2 or result3
print(result4)

print(not True)
print(not False)
print(not(False and True))