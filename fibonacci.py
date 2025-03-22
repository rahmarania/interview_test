# fibonacci occure when current number is total sum of 2 number before
# F(n) = F(n-1) + F(n-2)
data = int(input("input total length of data: "))
n0 = 0 # first number is always 0
n1 = 1 # second number is always 1
result = []
for i in range(data):
  result.append(n0)
  add = n0 + n1
  n0 = n1
  n1 = add
print(result)

  
