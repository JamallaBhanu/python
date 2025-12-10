n = "(1+3+(1+2)+(1-4) + (1+2))"


v = 0

def cal(k):
    lp = 0
    global v 
    for i in range(k+1 , len(n)):
        try:
            temp = int(n[i])
            if n[i-1] == "+" or n[i-1] != "-":
                lp = temp + lp
            if n[i-1] == "-":
                lp = lp - temp
        except:
            if n[i] == '(':
                v = lp + v
                cal(i)
                break
            if n[i] == ')':
                v = lp + v
                cal (i)
                break

cal(0)
print(v)