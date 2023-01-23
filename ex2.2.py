def armstrong_numbers(n):
    if n <= 0:
        return
    if n == 1:
        print('0', end= " ")
    for item in range(10**(n-1), 10**n):
        if is_armstrong_number(item, n):
            print(item, end=" ")

def is_armstrong_number(i, n):
    sum = 0
    num = str(i)
    for item in num:
        item = int(item)
        sum += item**n
    if sum == i:
        return True
armstrong_numbers(1)
# print(is_armstrong_number(153, 3))