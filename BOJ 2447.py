def dac(n):
    if n == 1:
        return ["*"]
    
    star = dac(n//3)
    stars = []
    
    for s in star:
        stars.append(s * 3)

    for s in star:
        stars.append(s + " " * (n//3) + s)
    
    for s in star:
        stars.append(s * 3)
        
    return stars
        
n = int(input())
print("\n".join(dac(n)))