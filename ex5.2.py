def print_factors(num):
    lst =[]
    for i in range(1, num):
        if num % i == 0:
            lst.append(i)
    for item in lst:
        print(item, end =' and ')
    print(num)
print_factors(24)