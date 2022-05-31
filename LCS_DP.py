import numpy as np

# X = 'GTCGTTCGGAATGCCGTTGCTCTGTAAA'
# Y = 'ACCGGTCGAGTGCGCGGAAGCCGGCCGAA'

Y = 'ABAABA'
X = 'BABBAB'

X_size = len(X)
Y_size = len(Y)

Z = ''


mat = np.zeros((X_size+1, Y_size+1))

for i in range(X_size+1):
    for j in range(Y_size+1):
        if i == 0 or j == 0:
            mat[i][j] = 0
        elif X[i-1] == Y[j-1]:
            mat[i][j] = mat[i-1][j-1] + 1
        else:
            mat[i][j] = max(mat[i][j-1], mat[i-1][j])
        

for i in range(X_size):
    if mat[X_size][Y_size] == mat[X_size-1][Y_size]:
        X_size -= 1
        Y_size = Y_size
    else:
        Z = X[X_size-1] + Z
        X_size -= 1
        Y_size -= 1


print(Z)
