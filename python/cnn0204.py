def sel_sort(ls):
    length = len(ls)
    f_index = 0

    for i in range(1, length):
        m = max(ls[i:])
        m_index = ls.index(m)

        if ls[f_index] < m:
            ls[f_index], ls[m_index] = ls[m_index], ls[f_index]
        f_index += 1
        print(i, ls)

s = [3, 31, 50, 23, 45, 22, 64, 7]
sel_sort(s)



def b_sort(ls):
    length = len(ls)

    for i in range(length-1):
        for j in range(length-1 - i):
            if ls[j] > ls[j+1]:
                ls[j], ls[j+1] = ls[j+1], ls[j]
            print(i,j, ls)

s = [3, 31, 50, 23, 45, 22, 64, 7]
b_sort(s)
