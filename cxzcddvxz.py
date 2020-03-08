import random
b=0
m=1024*1024*100
with open("rrr.txt", "rb")as file:
    for i in file:

        while b < m:
            r = random.choice(i)
            c = r.encode("UTF-8")
            file.write(c)
            b+=len(c)
            if c >= m:
                break
        print(len(i))