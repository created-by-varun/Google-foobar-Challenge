from fractions import Fraction

def gcd(x, y):
    def gcd1(x, y):
        if y == 0:
            return x
        return gcd1(y, x%y)
    return gcd1(abs(x), abs(y))

def simplify(x, y):
    g = gcd(x, y)
    return Fraction(long(x/g), long(y/g))

def lcm(x, y):
    return long(x*y/gcd(x,y))

def transform(m):
    sum_list = list(map(sum, m))
    bool_indices = list(map(lambda x: x == 0, sum_list))
    indices = set([i for i, x in enumerate(bool_indices) if x])
    new_mat = []
    for i in range(len(m)):
        new_mat.append(list(map(lambda x: Fraction(0, 1) if(sum_list[i] == 0) else simplify(x, sum_list[i]), m[i])))
    transform_mat = []
    zeros_mat = []
    for i in range(len(new_mat)):
        if i not in indices:
            transform_mat.append(new_mat[i])
        else:
            zeros_mat.append(new_mat[i])
    transform_mat.extend(zeros_mat)
    tmat = []
    for i in range(len(transform_mat)):
        tmat.append([])
        extend_mat = []
        for j in range(len(transform_mat)):
            if j not in indices:
                tmat[i].append(transform_mat[i][j])
            else:
                extend_mat.append(transform_mat[i][j])
        tmat[i].extend(extend_mat)
    return [tmat, len(zeros_mat)]

def copy_mat(m):
    cmat = []
    for i in range(len(m)):
        cmat.append([])
        for j in range(len(m[i])):
            cmat[i].append(Fraction(m[i][j].numerator, m[i][j].denominator))
    return cmat

def gauss_elmination(m, values):
    m = copy_mat(m)
    for i in range(len(m)):
        index = -1
        for j in range(i, len(m)):
            if m[j][i].numerator != 0:
                index = j
                break
        if index == -1:
            raise ValueError('Gauss elimination failed!')
        m[i], m[index] = m[index], m[j]
        values[i], values[index] = values[index], values[i]
        for j in range(i+1, len(m)):
            if m[j][i].numerator == 0:
                continue
            ratio = -m[j][i]/m[i][i]
            for k in range(i, len(m)):
                m[j][k] += ratio * m[i][k]
            values[j] += ratio * values[i]
    res = [0 for i in range(len(m))]
    for i in range(len(m)):
        index = len(m) -1 -i
        end = len(m) - 1
        while end > index:
            values[index] -= m[index][end] * res[end]
            end -= 1
        res[index] = values[index]/m[index][index]
    return res

def transpose(m):
    tmat = []
    for i in range(len(m)):
        for j in range(len(m)):
            if i == 0:
                tmat.append([])
            tmat[j].append(m[i][j])
    return tmat

def inverse(m):
    tmat = transpose(m)
    mat_inv = []
    for i in range(len(tmat)):
        values = [Fraction(int(i==j), 1) for j in range(len(m))]
        mat_inv.append(gauss_elmination(tmat, values))
    return mat_inv

def mat_mult(mat1, mat2):
    res = []
    for i in range(len(mat1)):
        res.append([])
        for j in range(len(mat2[0])):
            res[i].append(Fraction(0, 1))
            for k in range(len(mat1[0])):
                res[i][j] += mat1[i][k] * mat2[k][j]
    return res

def splitQR(m, lengthR):
    lengthQ = len(m) - lengthR
    Q = []
    R = []
    for i in range(lengthQ):
        Q.append([int(i==j)-m[i][j] for j in range(lengthQ)])
        R.append(m[i][lengthQ:])
    return [Q, R]

def solution(m):
    res = transform(m)
    if res[1] == len(m):
        return [1, 1]
    Q, R = splitQR(*res)
    inv = inverse(Q)
    res = mat_mult(inv, R)
    row = res[0]
    l = 1
    for item in row:
        l = lcm(l, item.denominator)
    res = list(map(lambda x: long(x.numerator*l/x.denominator), row))
    res.append(l)
    return res

