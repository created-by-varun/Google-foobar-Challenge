def solution(M, F):
    m, f = long(M), long(F)
    total = 0
    while not (m == 1 and f == 1):
        if f <= 0 or m <= 0:
            return "impossible"
        if f == 1:
            return str(total + m - 1)
        else:
            total += long(m/f)
            m, f = f, m % f
    return str(total)

#print(solution(4,7))
