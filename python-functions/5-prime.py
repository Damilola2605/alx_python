def is_prime(number):
    if number <= 1:
        return False
    elif number == 2:
        return True
    
    # Check divisibility from 2 to the square root of the number
    for divisor in range(2, int(number**0.5) + 1):
        if number % divisor == 0:
            return False

    return True
