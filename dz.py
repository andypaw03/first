import random
a12 = [
        [0,1,0,1,0,1,0,1],
        [1,0,1,0,1,0,1,0],
        [0,1,0,1,0,1,0,1],
        [1,0,1,0,1,0,1,0],
        [0,1,0,1,0,1,0,1],
        [1,0,1,0,1,0,1,0],
        [0,1,0,1,0,1,0,1],
        [1,0,1,0,1,0,1,0],
    ];
def a():
    ch=0
    a=[]
    for i in range(8):
        b=[]
        for j in range(8):
            if ch % 2==0:
                b.append(j%2)
            else:
                b.append((j+1)%2)
        a.append(b)
        ch+=1
    return a
print(a())