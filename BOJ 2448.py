n = int(input())

def dac(k):
    if k == 3:
        return ["  *  ", " * * ", "*****"]

    star = dac(k//2)
    stars = []
    
    w = k//2
    
    for s in star:
        stars.append(" " * w + s + " " * w)
        
    for s in star:
        stars.append(s + " " + s)
        
    return stars

print("\n".join(dac(n)))