def solution(total_lambs):
    totals = [generous(total_lambs), stingy(total_lambs)]
    difference = max(totals) - min(totals)
    return difference

def generous(total_lambs):
    num = 1
    while True:
        total = 2**(num) - 1
        if total <= total_lambs:
            num += 1
        else:
            num -= 1
            break
    return num

def stingy(total_lambs):
    num = 1
    last = 0
    cur = 1
    total_lambs -= 1
    while total_lambs > 0:
        if total_lambs < last + cur:
            break
        num += 1
        cur, last = cur + last, cur
        total_lambs -= cur

    return num
