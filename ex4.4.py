def remove_duplicates(text):
    lst = []
    for i in range(len(text)):
        lst.append(text[i])
        if len(lst) > 1:
            if text[i] == lst[-2]:
                del lst[-1]
    return (''.join(lst))
print(remove_duplicates("bookkeeeeeper"))
    
