def three_consecutive(n1, n2, n3):
    lstnum = [n1, n2, n3]
    lieng = sorted(lstnum)
    if lieng[2] - 1 == lieng[1] and lieng[1] - 1 == lieng[0]:
        return True
    else:
        return False

print(three_consecutive(3, 2, 4))

    

