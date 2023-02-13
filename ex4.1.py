def print_num_range(num1, num2):
    lst = []
    if num1 < num2:
        for item in range(num1, num2 + 1):
            lst.append(item)
        print(lst)            
    else:
        for item in range (num1, num2-1, -1):
            lst.append(item)
        print(lst)  
            

print_num_range(-2, 17)

