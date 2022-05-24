X = 'ABCD'
Y = 'ACBAD'

def LCS(a, b):
    def LCS_i(a, b, i, j):
        if (len(a) == i or len(b) == j):
            return ''
    
        if a[i] == b[j]:
            return a[i] + LCS_i(a, b, i+1, j+1) 
        x = LCS_i(a, b, i, j+1)
        y = LCS_i(a, b, i+1, j)


        if len(x) > len(y):
            return x
        return y
    
    return LCS_i(a, b, 0, 0)

print(LCS(X, Y))

