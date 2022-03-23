#Problem-1
import random
#คำนวณหาจำนวนครั้งเฉลี่ยที่ผู้เล่นต้องทอดลูกเต๋าในการเล่นจนจบเกม
def dice():
    count = 0
    n_round = 10000
    for _ in range(0, n_round):
        end = 0
        while end < 10:
            end += random.randint(1, 6)
            count += 1
    print(count/n_round)
    print()
dice()

#คำนวณหาโอกาสที่ผู้เล่นจะจบเกมภายในการทอดลูกเต๋า ... ครั้ง
#function dice1 = 1 ครั้ง
#function dice2 = 2 ครั้ง
#function dice3 = 3 ครั้ง
#...
dice7()
def dice1():
    mylist = []
    top = 0
    for i in range(6, 0, -1):
        mylist.append([i])

    for i in mylist:
        score = 0
        count = 0
        for j in range(0, len(i)):
            if(score < 10):
                score += i[j]
                count += 1
        if (score >= 10 and count == 1):
            top += 1
    print(str(top/(len(mylist))*100) + "%")

def dice2():
    mylist = []
    top = 0
    for i in range(6, 0, -1):
        for j in range(6, 0, -1):
            mylist.append([i, j])

    for i in mylist:
        score = 0
        count = 0
        for j in range(0, len(i)):
            if(score < 10):
                score += i[j]
                count += 1
        if (score >= 10 and count == 2):
            top += 1
    print(str(top/(len(mylist))*100) + "%")

def dice3():
    mylist = []
    top = 0
    for i in range(6, 0, -1):
        for j in range(6, 0, -1):
            for k in range(6, 0, -1):
                mylist.append([i, j, k])

    for i in mylist:
        score = 0
        count = 0
        for j in range(0, len(i)):
            if(score < 10):
                score += i[j]
                count += 1
        if (score >= 10 and count == 3):
            top += 1
    print(str(top/(len(mylist))*100) + "%")

def dice4():
    mylist = []
    top = 0
    for i in range(6, 0, -1):
        for j in range(6, 0, -1):
            for k in range(6, 0, -1):
                for l in range(6, 0, -1):
                    mylist.append([i, j, k, l])

    for i in mylist:
        score = 0
        count = 0
        for j in range(0, len(i)):
            if(score < 10):
                score += i[j]
                count += 1
        if (score >= 10 and count == 4):
            top += 1
    print(str(top/(len(mylist))*100) + "%")

def dice5():
    mylist = []
    top = 0
    for i in range(6, 0, -1):
        for j in range(6, 0, -1):
            for k in range(6, 0, -1):
                for l in range(6, 0, -1):
                    for m in range(6, 0, -1):
                        mylist.append([i, j, k, l, m])

    for i in mylist:
        score = 0
        count = 0
        for j in range(0, len(i)):
            if(score < 10):
                score += i[j]
                count += 1
        if (score >= 10 and count == 5):
            top += 1
    print(str(top/(len(mylist))*100) + "%")

def dice6():
    mylist = []
    top = 0
    for i in range(6, 0, -1):
        for j in range(6, 0, -1):
            for k in range(6, 0, -1):
                for l in range(6, 0, -1):
                    for m in range(6, 0, -1):
                        for n in range(6, 0, -1):
                            mylist.append([i, j, k, l, m, n])

    for i in mylist:
        score = 0
        count = 0
        for j in range(0, len(i)):
            if(score < 10):
                score += i[j]
                count += 1
        if (score >= 10 and count == 6):
            top += 1
    print(str(top/(len(mylist))*100) + "%")

def dice7():
    mylist = []
    top = 0
    for i in range(6, 0, -1):
        for j in range(6, 0, -1):
            for k in range(6, 0, -1):
                for l in range(6, 0, -1):
                    for m in range(6, 0, -1):
                        for n in range(6, 0, -1):
                            for o in range(6, 0, -1):
                                mylist.append([i, j, k, l, m, n, o])

    for i in mylist:
        score = 0
        count = 0
        for j in range(0, len(i)):
            if(score < 10):
                score += i[j]
                count += 1
        if (score >= 10 and count == 7):
            top += 1
    print(str(top/(len(mylist))*100) + "%")

def dice8():
    mylist = []
    top = 0
    for i in range(6, 0, -1):
        for j in range(6, 0, -1):
            for k in range(6, 0, -1):
                for l in range(6, 0, -1):
                    for m in range(6, 0, -1):
                        for n in range(6, 0, -1):
                            for o in range(6, 0, -1):
                                for p in range(6, 0, -1):
                                    mylist.append([i, j, k, l, m, n, o, p])

    for i in mylist:
        score = 0
        count = 0
        for j in range(0, len(i)):
            if(score < 10):
                score += i[j]
                count += 1
        if (score >= 10 and count == 8):
            top += 1
    print(str(top/(len(mylist))*100) + "%")

def dice9():
    mylist = []
    top = 0
    for i in range(6, 0, -1):
        for j in range(6, 0, -1):
            for k in range(6, 0, -1):
                for l in range(6, 0, -1):
                    for m in range(6, 0, -1):
                        for n in range(6, 0, -1):
                            for o in range(6, 0, -1):
                                for p in range(6, 0, -1):
                                    for q in range(6, 0, -1):
                                        mylist.append([i, j, k, l, m, n, o, p, q])

    for i in mylist:
        score = 0
        count = 0
        for j in range(0, len(i)):
            if(score < 10):
                score += i[j]
                count += 1
        if (score >= 10 and count == 9):
            top += 1
    print(str(top/(len(mylist))*100) + "%")

def dice10():
    mylist = []
    top = 0
    for i in range(6, 0, -1):
        for j in range(6, 0, -1):
            for k in range(6, 0, -1):
                for l in range(6, 0, -1):
                    for m in range(6, 0, -1):
                        for n in range(6, 0, -1):
                            for o in range(6, 0, -1):
                                for p in range(6, 0, -1):
                                    for q in range(6, 0, -1):
                                        for r in range(6, 0, -1):
                                            mylist.append([i, j, k, l, m, n, o, p, q, r])

    for i in mylist:
        score = 0
        count = 0
        for j in range(0, len(i)):
            if(score < 10):
                score += i[j]
                count += 1
        if (score >= 10 and count == 10):
            top += 1
    print(str(top/(len(mylist))*100) + "%")