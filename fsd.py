import random
import time
start=time.time()
a= '他們說，天哪，我明白你的光芒親愛的，握住你的手，將它們都放在我的你知道我經過時你讓我死了現在我求你再跳舞一次哦，我見到你，見到你，每次見' \
    '到你哦，我，我，我喜歡你的風格你，你讓我，讓我，讓我想哭現在我求你再跳舞一次所以我說為我跳舞，為我跳舞，為我跳舞，哦，哦，哦我從未見過有人' \
    '做過你以前做的事他們說為我而動，為我而動，為我而動，是，是，是當你完成後，我會讓你再做一次，天哪，我看到你走過親愛的，握住我的手，看著我的' \
    '眼睛就像猴子一樣，我一生都在跳舞你只是請求我再跳舞一次哦，我見到你，見到你，每次見到你哦，我，我，我喜歡你的風格你，你讓我，讓我，讓我想哭' \
    '現在我求你再跳舞一次所以我說為我跳舞，為我跳舞，為我跳舞，哦，哦，哦我從未見過有人做過你以前做的事他們說為我而動，為我而動，為我而動，是，' \
    '是，是'
maxx=1024
data=[]
for i in range(3):
    elem=[]
    we=0
    while True:
        info=random.choice(a)
        we+=len(info.encode("UTF-8"))
        elem.append(info)
        if we>=maxx:
            break
    elem=" ".join(elem)
    data.append(elem)



new_maxx=1024*1024
with open("rrr.txt","wb")as file:
    while True:
        info=random.choice(data)
        info=info.encode("UTF-8")
        we+=maxx
        file.write(info)
        if we>= new_maxx:
            break
end=time.time()
print("time needed:",end-start)