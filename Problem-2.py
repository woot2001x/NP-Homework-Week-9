#Problem-2
import random
#หาโอกาสที่แต่ละรอบที่เล่นเกมนี้ จะมีผู้ชนะมากกว่า 1 คน
#สมมติให้มีผู้เล่น 10 คนในแต่ละรอบ
def dice1():
    n = 10
    n_round = 100000
    count = 0
    for _ in range(n_round):
        mylist = []
        mylist2 = []
        for i in range(n):
            ran1 = random.randint(1, 6)
            if (ran1 == 1):
                mylist.append(i)

        for i in range(len(mylist)):
            ran2 = random.randint(1, 6)
            if ((ran2 == 3) or (ran2 == 6)):
                mylist2.append(mylist[i])
        if (len(mylist2) > 1):
            count += 1
    print(str((count/n_round)*100) + "%")
dice1()

