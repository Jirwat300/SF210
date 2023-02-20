def print_average():
    sum = 0
    count = 0
    check = False
    while True:
        num = float(input('Type a number: '))
        if num < 0:
            break
        else:
            sum += num
        count += 1
        check = True
    if check:    
        ans = sum / count
        print(f'Average was {ans}')    
print_average()