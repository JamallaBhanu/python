n = "(1+3+(1+2)+4+(2+5))+6+(1+2)"

lp = 0
v = 0

def cal(k):
    global lp , v
    for i in range(k+1 , len(n)):
        lp = 0
        try:
            lp = int(n[i]) + lp
            v = lp + v
        except:
            if n[i] == '(':
                cal(i)
                break
            if n[i] == ')':
                cal (i)
                break

cal(0)
print(v)