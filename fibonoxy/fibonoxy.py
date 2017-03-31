def fibonoxy(n):
    if n == 0:
        herd = 0
        return herd * ' :ox: '
    if n == 1:
        herd = 1
        return herd * ' :ox: '
    else:
        return fibonoxy(n-1) + fibonoxy(n-2)
    
