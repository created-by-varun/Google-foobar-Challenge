def solution(s):
    # Your code here
    if (len(s) > 100 or len(s) <1):
        raise ValueError('Out of bounds')
    
    s=list(s.replace("-", ""))
    left = []
    right = []
    res=0
    
    for i in range(0,len(s)):
        if s[i] == '<':
            left.append(i)
        if s[i] == '>':
            right.append(i)
            
    for i in right:
        for y in left:
            if i < y:
                res = res+1
    
    for i in left:
        for y in right:
            if y<i:
                res+=1
        
    return res
        

