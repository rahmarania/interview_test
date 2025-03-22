def search_prime(num):
    if num < 2:
        return False  # Return False if the number is less than 2 (not prime)
    
    # Check for divisibility starting from 2 up to the square root of num
    for i in range(2, int(num ** 0.5) + 1):
        if num % i == 0:
            print(f"{num} is not a prime number")  # If divisible, it's not prime
            return False  

    print(f"{num} is a prime number")
    return True  

# Example usage
search_prime(5)
