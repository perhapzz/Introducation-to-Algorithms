# Dynamic Programming
# 15.1 Cut Rod  O(2^n)
def cut_rod(p, n):
    if n == 0:
        return 0
    q = float("-inf")
    for i in range(1, n + 1):
        q = max(q, p[i] + cut_rod(p, n - i))
    return q

# Memorized O(n^2)
def memorized_cut_rod(p, n):
    r = []
    for i in range(n + 1):
        r.append(float("-inf"))
    return memorized_cut_rod_aux(p, n, r)

def memorized_cut_rod_aux(p, n, r):
    if r[n] >= 0:
        return r[n]
    if n == 0:
        q = 0
    else:
        q = float("-inf")
        for i in range(1, n + 1):
            q = max(q, p[i] + memorized_cut_rod_aux(p, n - i, r))
    r[n] = q
    return q

# Bottom Up O(n^2)
def bottom_up_cut_rod(p, n):
    r = [0]
    for i in range(1, n + 1):
        q = float("-inf")
        for j in range(1, i + 1):
            q = max(q, p[j] + r[i - j])
        r.append(q)
    return r[n]

# Extended Bottom Up
def extended_bottom_up_cut_rod(p, n):
    r = [0]
    s = []
    for i in range(n + 1):
        s.append(0)
    for i in range(1, n + 1):
        q = float("-inf")
        for j in range(1, i + 1):
            if q < p[j] + r[i - j]:
                s[i] = j
                q = p[j] + r[i - j]
        r.append(q)
    return r, s

# Matrix Chain Order O(n^3)
def matrix_chain_order(p):
    n = len(p)
    m = [[0 for col in range(n)] for row in range(n)]
    s = [[0 for col in range(n)] for row in range(n)]

    for l in range(1, n):   # l is the chain length
        for i in range(n - l):
            j = i + l
            m[i][j] = float("inf")
            # print(m)
            for k in range(i, j):
                q = m[i][k] + m[k + 1][j] + p[i][0] * p[k + 1][0] * p[j][1]
                # print(i, k, j, m[i][k], m[k + 1][j], p[i][0] * p[k + 1][0] * p[j][1], q)
                if q < m[i][j]:
                    m[i][j] = q
                    s[i][j] = k
    return m, s

def print_optimal_parens(s, i, j):
    if i == j:
        print(f"A{i + 1}", end='')
    else:
        print("(", end='')
        print_optimal_parens(s, i, s[i][j])
        print_optimal_parens(s, s[i][j] + 1, j)
        print(")", end='')


if __name__ == '__main__':
    # p = [0, 1, 5, 8, 9, 10, 17, 17, 20, 24, 30]
    # r, s = extended_bottom_up_cut_rod(p, 10)
    # for i in range(1, 11):
    #     r.append(memorized_cut_rod(p, i))

    p = [[30, 35], [35, 15], [15, 5], [5, 10], [10, 20], [20, 25]]
    r, s = matrix_chain_order(p)
    print_optimal_parens(s, 0, 5)
    # print(r)
    # print(s)

# [1, 5, 8, 10, 13, 17, 18, 22, 25, 30]