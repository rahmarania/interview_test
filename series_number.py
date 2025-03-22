# create output series based on the given length
def series_num(number):
  result = []
  for num in range(1, number+1):
    multiply_num = 2 ** (num-1)
    result.append(multiply_num)
  return result

number = 4
result = series_num(number)
print(",".join(map(str, result))) # expected 1,2,4,8
