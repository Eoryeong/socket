import random
import time

# 플레이어
ph = 50
dice = 4
drem = 0
pda = 0
pdf = 0
Pmoney = 0
item = 0
Pdice = 0
plusp = 0
cri = 0
pcri = 0



# 몹
Dmoney = 0
zh = 20
zd = 0
skh = 30
skd = 0



# 아이템 여부
zdice = 0
skhead = 0



# 이벤트 함수

    # 힘의 제단
def powergod() :
    ppw = random.randint(0, 5)
    return ppw
    # 주사위 제단
def dicegod() :
    pdd = random.randint(0, 2)
    return pdd
    # 치료소
def heal() :
    heal = random.randint(5, 20)
    return heal



# 드랍 함수
    # 좀비
def zomdrop() :
    it = random.randint(1, 20)
    return it
    # 해골 기사
def skedrop() :
    shead = random.randint(1, 20)
    return shead


# 치명타 함수
def critical():
    cri = random.randint(1, 10)
    return cri



# 전투 함수
    # 좀비
def zombie() :
    print("좀비이즈 커밍")

    while True:
        global zh
        global ph
        global zd
        global pcri
        pda = 0
        pdf = 0
        zd = 0
        time.sleep(2)
        print("당신의 턴")
        print("주사위 갯수", dice)
        print("추가 주사위", Pdice)
        print("공격할 횟수 (나머진 방어)")
        att = int(input())
        if (att > dice+Pdice ):
            print("갯수 초과", dice+Pdice, "개로 변경")
            att = dice+Pdice
        drem = dice - att
        for i in range (0, att):
            pda = random.randint(1, 6) + pda
        pcri = critical()
        print(pcri)
        if (pcri >= 8) :
            print("크리티컬!!")
            time.sleep(2)
            pda = pda * 2
        for j in range (0, drem):
            pdf = random.randint(1, 6) + pdf
        print("공격력 : ", pda)
        print("방어도 : ", pdf)
        time.sleep(1)
        pf = pdf
        zh = zh - pda

        print("남은 좀비의 체력 : ", zh)
        print("------------------------------------")
        time.sleep(1)
        if (zh <= 0) :
            break
        print("좀비의 공격!")
        time.sleep(2)
        zd = random.randint(1, 6)
        print("좀비의 공격력 : ", zd)
        print("당신의 방어력 : ", pdf)
        time.sleep(2)
        if (pdf > 0) :
            pdf = pdf - zd
            zd = zd - pf
            if (zd < 0):
                zd = 0
        print("좀비의 남은 공격력 : ", zd)
        ph = ph - zd
        print("당신의 체력 : ", ph)
        print("------------------------------------")


    # 해골 기사
def skeleton():
    print("해골기사 커밍")

    while True:
        global skh
        global ph
        global skd
        global pcri
        pda = 0
        pdf = 0
        skd = 0
        time.sleep(2)
        print("당신의 턴")
        print("주사위 갯수", dice)
        print("추가 주사위", Pdice)
        print("공격할 횟수 (나머진 방어)")
        att = int(input())
        if (att > dice + Pdice):
            print("갯수 초과", dice + Pdice, "개로 변경")
            att = dice + Pdice
        drem = dice - att
        for i in range(0, att):
            pda = random.randint(1, 6) + pda
        pcri = critical()
        print(pcri)
        if (pcri >= 8):
            print("크리티컬!!")
            time.sleep(2)
            pda = pda * 2
        for j in range(0, drem):
            pdf = random.randint(1, 6) + pdf
        print("공격력 : ", pda)
        print("방어도 : ", pdf)
        time.sleep(1)
        pf = pdf
        skh = skh - pda

        print("남은 해골기사의 체력 : ", skh)
        print("------------------------------------")
        time.sleep(1)
        if (skh <= 0):
            break
        print("해골기사의 공격!")
        time.sleep(2)
        skd = random.randint(2, 12)
        print("해골기사의 공격력 : ", skd)
        print("당신의 방어력 : ", pdf)
        time.sleep(2)
        if (pdf > 0):
            pdf = pdf - skd
            skd = skd - pf
            if (skd < 0):
                skd = 0
        print("해골기사의 남은 공격력 : ", skd)
        ph = ph - skd
        print("당신의 체력 : ", ph)
        print("------------------------------------")



# 보상 함수
    # 좀비 보상
def zombiedrop():
    global Pmoney
    global zdice
    Dmoney = random.randint(20, 40)
    print(Dmoney, "원 드랍")
    Pmoney = Pmoney + Dmoney
    print("소지한 돈 : ", Pmoney)
    item = zomdrop()
    print(item)
    if (item%5 == 0):
        zdice = zdice + 1
        print("좀비 주사위를 발견했다.")
    # 해골기사 보상
def skeletondrop():
    global Pmoney
    global skhead
    Dmoney = random.randint(30, 50)
    print(Dmoney, "원 드랍")
    Pmoney = Pmoney + Dmoney
    print("소지한 돈 : ", Pmoney)
    item = skedrop()
    print(item)
    if (item%5 == 0):
        skhead = skhead + 1
        print("해골기사 머리를 발견했다.")

# 진행
zombie()
time.sleep(2)
zombiedrop()
Pdice = zdice + 0
zh = 20
zombie()
time.sleep(2)
zombiedrop()
Pdice = zdice + 0
zh = 20
zombie()
time.sleep(2)
zombiedrop()
Pdice = zdice + 0
zh = 20
time.sleep(2)
zone = random.randint(1, 3)
if (zone == 1):
    print("힘의 제단이다")
    time.sleep(2)
    pluspower = powergod()
    print("당신의 힘이 ", pluspower, " 만큼 증가 했다")
    plusp = pluspower + plusp
    print("힘 : ", plusp)
elif (zone == 2):
    print("주사위의 제단이다")
    time.sleep(2)
    plusdice = dicegod()
    print("당신의 주사위가 ", plusdice, " 만큼 증가 했다")
    Pdice = Pdice + plusdice
    print("추가 주사위 : ", Pdice)
else :
    print("치료소다")
    time.sleep(2)
    plushp = heal()
    print("당신의 체력이 ", plushp, " 만큼 증가되었다")
    ph = ph + plushp
    print("체력 : ", plusp)
time.sleep(2)
skeleton()
time.sleep(2)
skeletondrop()
Pdice = zdice + 0
skh = 30
time.sleep(2)
print("...")