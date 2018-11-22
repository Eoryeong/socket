import random
import time

# 플레이어
ph = 500
dice = 40
drem = 0
pda = 0
pdf = 0
Pmoney = 0
item = 0
Pdice = 0
plusa = 0
plusp = 0
cri = 0
pcri = 0
shop = 0



# 몹
# 1 stage
Dmoney = 0
# 좀비
zh = 20
zd = 0
# 해골기사
skh = 30
skd = 0
# 슬라임
sh = 15
sd = 0
# 광전사
berhp = 100
berda = 0
berpda = 10
# 2 stage
# 유령 회피
goh = 50
goa = 5
goda = 0
godo = 0
# 사냥꾼
huh = 70
hua = 5
hud = 0
hup = 3
# 거인
jh = 150
jd = 0
ja = 10
jg = 0
# 과학자
sch = 400
scd = 0
sca = 10
scp = 5


# 아이템 여부
zdice = 0
skhead = 0
gel = 0
paxe = 0
ghud = 0


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
    # 슬라임
def smdrop() :
    sgel = random.randint(1, 20)
    return sgel
    # 좀비
def zomdrop() :
    zomdice = random.randint(1, 20)
    return zomdice
    # 해골 기사
def skedrop() :
    shead = random.randint(1, 20)
    return shead
    # 유령
def ghdrop() :
    ghu = random.randint(1, 20)
    return ghu

# 치명타 함수
def critical():
    cri = random.randint(1, 10)
    return cri



# 전투 함수
    # 슬라임
def slime() :
    print("슬라임이즈 커밍")

    while True:
        global sh
        global ph
        global sd
        global pcri
        global pdf
        pda = 0
        pdf = 0
        sd = 0
        Pdice = zdice + 0
        time.sleep(2)
        print("당신의 턴")
        print("주사위 갯수", dice)
        print("추가 주사위", Pdice)
        print("공격할 횟수 (나머진 방어)")
        att = int(input())
        if (att > dice+Pdice ):
            print("갯수 초과", dice+Pdice, "개로 변경")
            att = dice+Pdice
        drem = dice + Pdice - att
        for i in range (0, att):
            pda = random.randint(1, 6) + pda
        pcri = critical()
        pcri = (paxe * 2) + pcri
        # print(pcri)
        if (pcri >= 8) :
            print("크리티컬!!")
            time.sleep(2)
            pda = pda * 2
        for j in range (0, drem):
            pdf = random.randint(1, 6) + pdf
        print("공격력 : ", pda, " + ", plusp)
        print("방어도 : ", pdf, " + ", skhead*5)
        time.sleep(1)
        pf = pdf
        sh = sh - (pda + plusp)

        print("남은 슬라임의 체력 : ", sh)
        print("------------------------------------")
        time.sleep(1)
        if (sh <= 0) :
            ph = ph + (gel * 3)
            print("남은체력 : ", ph)
            break
        print("슬라임의 공격!")
        time.sleep(2)
        sd = random.randint(2, 4)
        print("슬라임의 공격력 : ", sd)
        print("당신의 방어력 : ", pdf)
        time.sleep(2)
        if (pdf+skhead > 0) :
            pdf = skhead * 5 + pdf - sd
            sd = sd - pf
            if (sd < 0):
                sd = 0
        print("슬라임의 남은 공격력 : ", sd)
        ph = ph - sd
        print("당신의 체력 : ", ph)
        if (ph <= 0) :
            print("그렇습니다 당신은 망했습니다.")
            exit()
        print("------------------------------------")


    # 좀비
def zombie() :
    print("좀비이즈 커밍")

    while True:
        global zh
        global ph
        global zd
        global pcri
        global pdf
        pda = 0
        pdf = 0
        zd = 0
        Pdice = zdice + 0
        time.sleep(2)
        print("당신의 턴")
        print("주사위 갯수", dice)
        print("추가 주사위", Pdice)
        print("공격할 횟수 (나머진 방어)")
        att = int(input())
        if (att > dice+Pdice ):
            print("갯수 초과", dice+Pdice, "개로 변경")
            att = dice+Pdice
        drem = dice + Pdice - att
        for i in range (0, att):
            pda = random.randint(1, 6) + pda
        pcri = critical()
        pcri = (paxe * 2) + pcri
        # print(pcri)
        if (pcri >= 8) :
            print("크리티컬!!")
            time.sleep(2)
            pda = pda * 2
        for j in range (0, drem):
            pdf = random.randint(1, 6) + pdf
        print("공격력 : ", pda, " + ", plusp)
        print("방어도 : ", pdf, " + ", skhead*5)
        time.sleep(1)
        pf = pdf
        zh = zh - (pda + plusp)

        print("남은 좀비의 체력 : ", zh)
        print("------------------------------------")
        time.sleep(1)
        if (zh <= 0) :
            ph = ph + (gel * 3)
            print("남은체력 : ", ph)
            break
        print("좀비의 공격!")
        time.sleep(2)
        zd = random.randint(1, 6)
        print("좀비의 공격력 : ", zd)
        print("당신의 방어력 : ", pdf)
        time.sleep(2)
        if (pdf > 0) :
            pdf = skhead * 5 + pdf - zd
            zd = zd - pf
            if (zd < 0):
                zd = 0
        print("좀비의 남은 공격력 : ", zd)
        ph = ph - zd
        print("당신의 체력 : ", ph)
        if (ph <= 0) :
            print("그렇습니다 당신은 망했습니다.")
            exit()
        print("------------------------------------")


    # 해골 기사
def skeleton():
    print("해골기사 커밍")

    while True:
        global skh
        global ph
        global skd
        global pcri
        global pdf
        pda = 0
        pdf = 0
        skd = 0
        Pdice = zdice + 0
        time.sleep(2)
        print("당신의 턴")
        print("주사위 갯수", dice)
        print("추가 주사위", Pdice)
        print("공격할 횟수 (나머진 방어)")
        att = int(input())
        if (att > dice + Pdice):
            print("갯수 초과", dice + Pdice, "개로 변경")
            att = dice + Pdice
        drem = dice + Pdice - att
        for i in range(0, att):
            pda = random.randint(1, 6) + pda
        pcri = critical()
        pcri = (paxe * 2) + pcri
        # print(pcri)
        if (pcri >= 8):
            print("크리티컬!!")
            time.sleep(2)
            pda = pda * 2
        for j in range(0, drem):
            pdf = random.randint(1, 6) + pdf
        print("공격력 : ", pda, " + ", plusp)
        print("방어도 : ", pdf, " + ", skhead*5)
        time.sleep(1)
        pf = pdf
        skh = skh - (pda + plusp)

        print("남은 해골기사의 체력 : ", skh)
        print("------------------------------------")
        time.sleep(1)
        if (skh <= 0):
            ph = ph + (gel * 3)
            print("남은체력 : ", ph)
            break
        print("해골기사의 공격!")
        time.sleep(2)
        skd = random.randint(2, 12)
        print("해골기사의 공격력 : ", skd)
        print("당신의 방어력 : ", pdf)
        time.sleep(2)
        if (pdf > 0):
            pdf = skhead * 5 + pdf - skd
            skd = skd - pf
            if (skd < 0):
                skd = 0
        print("해골기사의 남은 공격력 : ", skd)
        ph = ph - skd
        print("당신의 체력 : ", ph)
        if (ph <= 0) :
            print("그렇습니다 당신은 망했습니다.")
            exit()
        print("------------------------------------")
    # 광전사
def berser():
    print("광전사 커밍")

    while True:
        global berhp
        global ph
        global berda
        global pcri
        global pdf
        pda = 0
        pdf = 0
        berda = 0
        Pdice = zdice + 0
        time.sleep(2)
        print("당신의 턴")
        print("주사위 갯수", dice)
        print("추가 주사위", Pdice)
        print("공격할 횟수 (나머진 방어)")
        att = int(input())
        if (att > dice + Pdice):
            print("갯수 초과", dice + Pdice, "개로 변경")
            att = dice + Pdice
        drem = dice + Pdice - att
        for i in range(0, att):
            pda = random.randint(1, 6) + pda
        pcri = critical()
        pcri = (paxe * 2) + pcri
        # print(pcri)
        if (pcri >= 8):
            print("크리티컬!!")
            time.sleep(2)
            pda = pda * 2
        for j in range(0, drem):
            pdf = random.randint(1, 6) + pdf
        print("공격력 : ", pda, " + ", plusp)
        print("방어도 : ", pdf, " + ", skhead*5)
        time.sleep(1)
        pf = pdf
        berhp = berhp - (pda + plusp)

        print("남은 광전사의 체력 : ", berhp)
        print("------------------------------------")
        time.sleep(1)
        if (berhp <= 0):
            ph = ph + (gel * 3)
            print("남은체력 : ", ph)
            break
        print("광전사의 공격!")
        time.sleep(2)
        berda = random.randint(10, 15)
        if (berhp <= 50) :
            print('"우어어어억!!"')
            print("광전사가 화났다")
            berda = berda + berpda
        print("광전사의 공격력 : ", berda)
        print("당신의 방어력 : ", pdf)
        time.sleep(2)
        if (pdf > 0):
            pdf = skhead * 5 + pdf - berda
            berda = berda - pf
            if (berda < 0):
                berda = 0
        print("광전사의 남은 공격력 : ", berda)
        ph = ph - berda
        print("당신의 체력 : ", ph)
        if (ph <= 0) :
            print("그렇습니다 당신은 망했습니다.")
            exit()
        print("------------------------------------")

    # 유령
def ghost() :
    print("유령이즈 커밍")

    while True:
        global goh
        global ph
        global goda
        global godo
        global pcri
        global pdf
        pda = 0
        pdf = 0
        goda = 0
        Pdice = zdice + 0
        time.sleep(2)
        print("당신의 턴")
        print("주사위 갯수", dice)
        print("추가 주사위", Pdice)
        print("공격할 횟수 (나머진 방어)")
        att = int(input())
        if (att > dice+Pdice ):
            print("갯수 초과", dice+Pdice, "개로 변경")
            att = dice+Pdice
        drem = dice + Pdice - att
        for i in range (0, att):
            pda = random.randint(1, 6) + pda
        pcri = critical()
        pcri = (paxe * 2) + pcri
        # print(pcri)
        if (pcri >= 8) :
            print("크리티컬!!")
            time.sleep(2)
            pda = pda * 2
        for j in range (0, drem):
            pdf = random.randint(1, 6) + pdf
        print("공격력 : ", pda, " + ", plusp)
        print("방어도 : ", pdf, " + ", skhead*5)
        godo = random.randint(1, 6)
        if (godo > 4) :
            time.sleep(1)
            pf = pdf
            goh = goh - (pda + plusp - goa)
        else :
            print("!감나빗")
            time.sleep(1)

        print("남은 유령의 체력 : ", goh," 방어력 : ", goa)
        print("------------------------------------")
        time.sleep(1)
        if (goh <= 0) :
            ph = ph + (gel * 3)
            print("남은체력 : ", ph)
            break
        print("유령의 공격!")
        time.sleep(2)
        goda = random.randint(5, 10)
        print("유령의 공격력 : ", goda)
        print("당신의 방어력 : ", pdf)
        time.sleep(2)
        if (pdf > 0) :
            pdf = skhead * 5 + pdf - goda
            goda = goda - pf
            if (goda < 0):
                goda = 0
        print("유령의 남은 공격력 : ", goda)
        ph = ph - goda
        print("당신의 체력 : ", ph)
        if (ph <= 0) :
            print("그렇습니다 당신은 망했습니다.")
            exit()
        print("------------------------------------")



# 보상 함수
    # 슬라임 보상
def smiledrop():
    global Pmoney
    global gel
    Dmoney = random.randint(20, 40)
    print(Dmoney, "원 드랍")
    Pmoney = Pmoney + Dmoney
    print("소지한 돈 : ", Pmoney)
    item = smdrop()
    print(item)
    if (item%5 == 0):
        gel = gel + 1
        print("점액을 발견했다.")
    print("------------------------------------")
    time.sleep(2)
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
    print("------------------------------------")
    time.sleep(2)
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
    print("------------------------------------")
    time.sleep(2)
    # 광전사 보상
def berdrop():
    global Pmoney
    global paxe
    Dmoney = random.randint(100, 150)
    print(Dmoney, "원 드랍")
    Pmoney = Pmoney + Dmoney
    print("소지한 돈 : ", Pmoney)
    paxe = paxe + 1
    print("광전사의 도끼를 발견했다.")
    print("------------------------------------")
    time.sleep(2)
 # 유령 보상
def ghostdrop():
    global Pmoney
    global ghud
    Dmoney = random.randint(50, 70)
    print(Dmoney, "원 드랍")
    Pmoney = Pmoney + Dmoney
    print("소지한 돈 : ", Pmoney)
    item = ghdrop()
    print(item)
    if (item%5 == 0):
        ghud = ghud + 1
        print("유령의 망토를 발견했다.")
    print("------------------------------------")
    time.sleep(2)
# 진행

ghost()
time.sleep(2)
ghostdrop()
goh = 50
time.sleep(2)
ghost()
time.sleep(2)
ghostdrop()
goh = 50
time.sleep(2)
ghost()
time.sleep(2)
ghostdrop()
goh = 50
time.sleep(2)
print("끝이다요")
