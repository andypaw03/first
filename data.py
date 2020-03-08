import time
def datA(file_name, data):
    with open(file_name,"r",encoding="UTF-8")as file:
        a=" "
        for aa in file:
            aa=aa.split()
            current=a+aa
            a=aa
            if data in current:
                return True
    return True

start=time.time()
print(datA("p.txt", "050408"))
print(time.time()-start)