def toBinary(num):
  if num==0 :
    return '0b0'
  else:
    binary_ = convert(num//2)
    return binary_ + str(num%2)
