s = input()

### 수식을 리스트로
expression = []
tmp = ''
for c in s:
    if c.isdigit():
        tmp += c
    elif c == '+':
        tmp = int(tmp)
        expression += [tmp, '+']
        tmp = ''
    else:
        tmp = int(tmp)
        expression += [tmp, '-']
        tmp = ''
expression.append(int(tmp))

### 계산
answer = expression[0]
subtotal = 0
isFirst = True
for c in expression[1:]:
    if str(c).isdigit():
        subtotal += c
    elif c == '-':
        if isFirst:
            answer += subtotal
            isFirst = False
        else:
            answer -= subtotal
        subtotal = 0
            
if not isFirst:
    answer -= subtotal
else:
    answer += subtotal

print(answer)