import random
a=input("")
def monkey(file):
    with open(file,"r")as file:


        b = 'АаБбВвГгДдЕеЁёЖжЗзИиЙйКкЛлМмНнОоПпРрСсТтУуФфХхЦцЧчШшЩщЪъЫыЬьЭэЮюЯя'
        c=""
        while True:
            random.choice(b)
            c+=b
    return c
print(monkey(a))