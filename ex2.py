def is_prime(n):
    for i in range(2, n // 2+1):
        if n % i == 0:
            return False
    return True

def find_relation(num , relation):
    lst = []
    for i in range(2, num, 1):
        if is_prime(i) and is_prime(i + relation):
            lst.append((i, i + relation))
    return lst

def main():
    limit = int(input('Enter limit: '))
    print(f'Twin: {find_relation(limit, 2)}')
    print(f'Cousin: {find_relation(limit, 4)}')
    print(f'Sexy: {find_relation(limit, 6)}')

main()


