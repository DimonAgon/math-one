set_A = []
set_B = []
set_C = []
universum = []
set_X = []
set_Y = []

def getOriginSet(A):
    list_set = []
    for ch in A:
        if ch != "\n":
            list_set.append(ch)

    return set(list_set)

def makeFormatedSet(A):
    i = 1
    frmtd_set = ''
    for el in A:
        if i < 20:
            frmtd_set += str(el)+", "
        else:
            i = 0
            frmtd_set += str(el) + ",\n"
        i += 1
    return frmtd_set[:-2]

def getMyInfo():
    G = 4
    N = 5
    M = "ІО"
    if M == "ІО": N += 2
    if __name__ == "__main__":
        print("Моя група: ", M + "-0" + str(G))
        print("Мій номер у групі:", (N - 2))
        print("Мій варіант:", (N + G % 60) % 30 + 1)

    return ((M + "-0"+ str(G)), (N-2), ((N + G % 60) % 30 + 1) )

def getNotSet(A):
    #Возвращет множество - отрицание переданного множества
    not_A = []
    for i in universum:
        if i not in A:
            not_A.append(i)

    return not_A

def culcSimplifiedFirstExpression(A, B, C):
    # B \ A
    returned_set = []
    for i in range(0, len(B)):
        boolean = True
        for ii in range(0, len(A)):
            if B[i] == A[ii]:
                boolean = False
            else:
                continue
        if boolean:
            returned_set.append(B[i])

    # (B\A) + C
    returned_set.extend(C)
    return returned_set

def culcFirstExpression(A, B, C):
    prom_set = []
    returned_set = []
    not_B = getNotSet(B)

    for i in range(0, len(A)):
        if A[i] in not_B:
            prom_set.append(A[i])
    prom_set.extend(B)

    for i in range(0, len(prom_set)):
        boolean = True
        for ii in range(0, len(A)):
            if prom_set[i] == A[ii]:
                boolean = False
            else:
                continue
        if boolean:
            returned_set.append(prom_set[i])
    returned_set.extend(C)
    return returned_set

def culcSecondExp(A, B):
    C = []
    for x in A:
        if x in B or x in C:
            continue
        else:
            C.append(x)
    for x in B:
        if x in A or x in C:
            continue
        else:
            C.append(x)
    return C
