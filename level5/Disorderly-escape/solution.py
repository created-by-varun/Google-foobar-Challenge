from fractions import *
from copy import *

def expand(frac, terminal):
    for term in terminal:
        term[0] *= frac
    return terminal

def multiply(sub, terminal):
    terminal = deepcopy(terminal)
    for term in terminal:
        alreadyIncluded = False
        for a in term[1]:
            if a[0] == sub:
                alreadyIncluded = True
                a[1] += 1
                break
        if not alreadyIncluded:
            term[1].append([sub, 1])
    return terminal

def add(terminala, terminalb):
    terminal = terminala + terminalb
    if len(terminal) <= 1:
        return terminal
    for i in range(len(terminal) - 1):
        for j in range(i + 1, len(terminal)):
            if set([(a[0], a[1]) for a in terminal[i][1]]) == set([(b[0], b[1]) for b in terminal[j][1]]):
                terminal[i][0] = terminal[i][0] + terminal[j][0]
                terminal[j][0] = Fraction(0, 1)
    return [term for term in terminal if term[0] != Fraction(0, 1)]

def lcm(a, b):
    return abs(a * b) / gcd(a, b) if a and b else 0

petCache = {}

def petCycleSimm(n):
    global petCache
    if n == 0:
        return [[Fraction(1.0), []]]
    if n in petCache:
        return petCache[n]
    terminal = []
    for l in range(1, n + 1):
        terminal = add(terminal, multiply(l, petCycleSimm(n - l)))
    petCache[n] = expand(Fraction(1, n), terminal)
    return petCache[n]

def petCycleProdA(cyca, cycb):
    alist = []
    for ca in cyca:
        lena = ca[0]
        insta = ca[1]
        for cb in cycb:
            lenb = cb[0]
            instb = cb[1]
            vlcm = lcm(lena, lenb)
            alist.append([vlcm, (insta * instb * lena * lenb) / vlcm])
    if len(alist) <= 1:
        return alist
    for i in range(len(alist) - 1):
        for j in range(i + 1, len(alist)):
            if alist[i][0] == alist[j][0] and alist[i][1] != -1:
                alist[i][1] += alist[j][1]
                alist[j][1] = -1
    return [a for a in alist if a[1] != -1]

def petCycleSimmNM(n, m):
    indA = petCycleSimm(n)
    indB = petCycleSimm(m)
    terminal = []
    for flatA in indA:
        for flatB in indB:
            newterminal = [[flatA[0] * flatB[0], petCycleProdA(flatA[1], flatB[1])]]
            terminal.extend(newterminal)
    return terminal

def substitute(term, v):
    total = 1
    for a in term[1]:
        total *= v**a[1]
    return (term[0] * total)

def solution(w, h, s):
    terminal = petCycleSimmNM(w, h)
    total = 0
    for term in terminal:
        total += substitute(term, s)
    return str(int(total))
