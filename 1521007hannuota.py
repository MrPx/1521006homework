def move(n, a, b, c):
    count = 0
    if n==1:
        print(a, "==>", c)                
        return 1                                   
    else:
        count += Move_Tower(n-1, a, c, b) 
        count += Move_Tower(1, a, b, c)   
        count += Move_Tower(n-1, b, a, c) 
        return count
