import math


Abbr = ['', 'K', 'M', 'B', 'T', 'q', 'Q', 's', 'S', 'O']

def lg(N):
    if N <= 9:
        return 1
    return 1 + lg(int(N/10))

def output(N):
    counter = 0
    while True:
        if N/1000 < 1:
            break
        N /= 1000
        counter += 1
        
    round(N + 0.01, 1)
    return str(N)[0:3+lg(N)] + Abbr[counter]
    
