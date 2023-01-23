def ascii_figure(size):
    slash = '////'
    bslash = '\\\\\\\\'
    star = '****'
    nstar = 0
    for line in range(0, size):
        print(slash * ((size -1)-nstar) +(star * (nstar)) * 2 + (bslash * ((size -1) - nstar)))
        nstar += 1
ascii_figure(3)



