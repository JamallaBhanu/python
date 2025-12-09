n = "(1+3+(1+2)+4+(2+5))+6"
value = 0 
loopval = 0

def damn(i):
    global loopval , value
    #print("value" , value)
    loopval = 0
    for j in range(i+1 , len(n)):
        try:
            loopval = int(n[j]) + loopval
        except:
            if n[j] == "(":
                #print("loopval" , loopval)
                value = loopval + value
                damn(j)
            if n[j] == ')':
                value = loopval + value
                return
               
for i in range(len(n)):
    if n[i] =='(':
        damn(i)

    
print(value)