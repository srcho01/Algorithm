def dac(n, s):
    if n == 0:
        return "-"
    
    k = 3 ** (n-1)
    return dac(n-1, s[:k]) + " " * k + dac(n-1, s[-k:]) 

while True:
    try:
        n = int(input())
        s = "-" * (3**n)
        print(dac(n, s))
    except EOFError:
        break