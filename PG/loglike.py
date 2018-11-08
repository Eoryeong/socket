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
cri = 0
pcri = 0
# 몹
Dmoney = 0
zh = 20
zd = 0
# 아이템 여부
zdice = 0

# 드랍 함수
def zomdrop() :
    it = random.randint(1, 20)
    return it
# 치명타 함수
def critcal():
    cri = random.randint(1, 10)
    return cri

# 전투 함수
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
        pcri = critcal()
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
# 보상 함수
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
print("...")