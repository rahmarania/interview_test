# check odd or even
def odd_even(num):
    for n in num:
        if n%2 == 0:
            print(f"{n} is even number")
        else:
            print(f"{n} is odd number")
            
num = odd_even([1,2,5])
print(num)
