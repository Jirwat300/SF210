def smallest_largest():
    lst =[]
    n_question = 1
    num_want = int(input('How many numbers do you want to enter? '))
    for item in range(1, num_want+1):
        x = int(input(f'Number {n_question}: '))
        n_question += 1
        lst.append(x)
    print(f'Smallest = {min(lst)}')
    print(f'Largest = {max(lst)}')

smallest_largest()