X = 'ABCD'
Y = 'ACBAD'

def LCS(a, b):
    if (a == '' or b == ''):
        return ''
    
    if a[0] == b[0]:
        return a[0] + LCS(a[1::], b[1::]) 
    x = LCS(a, b[1::])
    y = LCS(a[1::], b)


    if len(x) > len(y):
        return x
    return y
    

print(LCS(X, Y))
#print(X[1::])
