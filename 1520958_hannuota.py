def hannuota(n,x1,x2,x3):
    if(n == 1):
        print('move:',x1,'-->',x3)
        return
    hannuota(n-1,x1,x3,x2)
    print('move:',x1,'-->',x3)
    hannuota(n-1,x2,x1,x3)
