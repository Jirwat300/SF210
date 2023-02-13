def binary_to_decimal(binary):
    n = 0
    ans = 0
    while binary > 0:
        karr = binary % 10
        ans += karr * (2**n)
        binary //= 10
        n += 1
    return ans

print(binary_to_decimal(101101101))