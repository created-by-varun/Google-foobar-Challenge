# Note: this solution is failing 2 test cases at the moment

def solution(total_lambs):
    return stingy(total_lambs) - generous(total_lambs)

def generous(total_lambs):
    num = 1
    last = 0
    cur = 1
    total_lambs -= 1
    while total_lambs > 0:
        if total_lambs < cur * 2:
            if total_lambs >= cur + last:
                num += 1
            break
        num += 1
        cur, last = cur * 2, cur
        total_lambs -= cur

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
