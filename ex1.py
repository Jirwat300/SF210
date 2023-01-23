def find_proper_divisors(value):
    divisors = [1]
    for item in range(2, value // 2+1):
        if value % item ==0:
            divisors.append(item)
    return divisors

def cals_perfect_numbers(max_exculsive):
    result = []
    for num in range(6, max_exculsive+1):
        if sum(find_proper_divisors(num)) == num:
            result.append(num)
    return result

print(cals_perfect_numbers(1000) == [6, 28, 496])
print(cals_perfect_numbers(10000) == [6, 28, 496, 8128])