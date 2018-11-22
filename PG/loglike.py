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
goh = 30
goa = 5
goda = 0
godo = 0
# 사냥꾼
huh = 50
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
        if (att == 4444):
            print("죽어라")
            print("-------------------")
            break
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
        if (att == 4444):
            print("죽어라")
            print("-------------------")
            break
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
        if (att == 4444):
            print("죽어라")
            print("-------------------")
            break
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
        pdf = pdf + (skhead*5)
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
        if (att == 4444):
            print("죽어라")
            print("-------------------")
            break
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
        pdf = pdf + (skhead * 5)
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
        if (att == 4444):
            print("죽어라")
            print("-------------------")
            break
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
        print("공격력 : ", pda, " + ", plusp + (ghud*5))
        print("방어도 : ", pdf, " + ", skhead*5)
        pdf = pdf + (skhead * 5)
        pf = pdf
        godo = random.randint(1, 6)
        if (godo > 4) :
            print("!감나빗")
            time.sleep(1)
        else :
            time.sleep(1)
            goh = goh - (pda + plusp - goa)
        print("남은 유령의 체력 : ", goh," 방어력 : ", goa)
        godo = 0
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
    
while True:  
    # 진행
    slime()
    time.sleep(2)
    smiledrop()
    sh = 15
    slime()
    time.sleep(2)
    smiledrop()
    sh = 15
    slime()
    time.sleep(2)
    smiledrop()
    sh = 15
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
        dice = dice + plusdice
        print("주사위 : ", dice)
    else :
        print("치료소다")
        time.sleep(2)
        plushp = heal()
        print("당신의 체력이 ", plushp, " 만큼 증가되었다")
        ph = ph + plushp
        print("체력 : ", ph)
    zone = 0
    time.sleep(2)
    zombie()
    time.sleep(2)
    zombiedrop()
    zh = 20
    zombie()
    time.sleep(2)
    zombiedrop()
    zh = 20
    zombie()
    time.sleep(2)
    zombiedrop()
    zh = 20
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
        dice = dice + plusdice
        print("주사위 : ", dice)
    else :
        print("치료소다")
        time.sleep(2)
        plushp = heal()
        print("당신의 체력이 ", plushp, " 만큼 증가되었다")
        ph = ph + plushp
        print("체력 : ", ph)
    zone = 0
    time.sleep(2)
    skeleton()
    time.sleep(2)
    skeletondrop()
    skh = 30
    skeleton()
    time.sleep(2)
    skeletondrop()
    skh = 30
    skeleton()
    time.sleep(2)
    skeletondrop()
    skh = 30
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
        dice = dice + plusdice
        print("주사위 : ", dice)
    else :
        print("치료소다")
        time.sleep(2)
        plushp = heal()
        print("당신의 체력이 ", plushp, " 만큼 증가되었다")
        ph = ph + plushp
        print("체력 : ", ph)
    zone = 0
    time.sleep(2)
    while True :
        print("----------상점----------")
        print("아이템 사기 : 숫자 입력")
        print("보유한 돈 : ", Pmoney)
        print("1. 슬라임 점액 100원 | 2. 좀비 주사위 120원 | 3. 해골기사 머리 120원 | 4. 힘의 문장 80원 | 5. 가기")
        print("----------상점----------")
        shop = int(input())
        if (shop == 1 and Pmoney >= 100) :
            gel = gel + 1
            Pmoney = Pmoney - 100
            print("점액을 샀다")
        elif (shop == 2 and Pmoney >= 120) :
            zdice = zdice + 1
            Pmoney = Pmoney - 120
            print("주사위를 샀다")
        elif (shop == 3 and Pmoney >= 120) :
            skhead = skhead + 1
            Pmoney = Pmoney - 120
            print("머리를 샀다.")
        elif (shop == 4 and Pmoney >= 80) :
            plusp = plusp + 2
            Pmoney = Pmoney - 80
            print("강해졌다 힘 + 2")
        elif (shop == 5):
            print("나갔다")
            break
    time.sleep(2)
    berser()
    time.sleep(2)
    berdrop()
    berhp = 100
    zone = random.randint(1, 3)
    if (zone == 1):
        print("강력한 힘의 제단이다")
        time.sleep(2)
        pluspower = powergod()
        print("당신의 힘이 ", pluspower + 5, " 만큼 증가 했다")
        plusp = pluspower + plusp
        print("힘 : ", plusp)
    elif (zone == 2):
        print("강력한 주사위의 제단이다")
        time.sleep(2)
        plusdice = dicegod()
        print("당신의 주사위가 ", plusdice + 2, " 만큼 증가 했다")
        dice = dice + plusdice
        print("주사위 : ", dice)
    else :
        print("고급 치료소다")
        time.sleep(2)
        plushp = heal()
        print("당신의 체력이 ", plushp + 20, " 만큼 증가되었다")
        ph = ph + plushp
        print("체력 : ", ph)
    zone = 0
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
    print ("계속할가?      1 한다      2 안한다")
    again = int(input())
    if (again == 1):
        print ("ㅇㅇ")
    else :
        print("끝이다요")
        break
    print ("다시간다")