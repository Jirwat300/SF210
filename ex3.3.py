def get_first_digit(num):
    num = abs(num)
    while num > 10:
        num //= 10
    return num

print(get_first_digit(-23))    
