def contain_twice(sstr, cchr):
    # sstr = (sstr.lower())
    count_chr = sstr.count(cchr)
    if count_chr >= 2:
        return True
    else:
        return False

contain_twice("hello", 'l')
