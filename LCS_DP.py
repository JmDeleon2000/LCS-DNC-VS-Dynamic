import numpy as np

X = 'GTCGTTCGGAATGCCGTTGCTCTGTAAA'
Y = 'ACCGGTCGAGTGCGCGGAAGCCGGCCGAA'


X_size = len(X)
Y_size = len(Y)

Z = ''


mat = np.zeros((X_size+1, Y_size+1))

for i in range(X_size):
    for j in range(Y_size):
        if  X[0] == Y[j]:
            mat[i+1][j+1] = 1
        else:
            mat[i+1][j+1] = max(mat[i+1][j], mat[i][j+1])
        if i != 0:
            if X[i] == Y[j]:
                mat[i+1][j+1] = mat[i][j]+1
            else:
                mat[i+1][j+1] = max(mat[i+1][j], mat[i][j+1])



for i in range(X_size):
    if mat[X_size][Y_size] == mat[X_size-1][Y_size]:
        X_size -= 1
        Y_size = Y_size
    else:
        Z = X[X_size-1] + Z
        X_size -= 1
        Y_size -= 1


print(Z)
