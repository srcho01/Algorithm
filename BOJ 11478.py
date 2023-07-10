s = input()

sub_s = set()

for i in range(1, len(s)+1):
    for j in range(len(s)-i+1):
        sub_s.add(s[j:j+i])
        
print(len(sub_s))