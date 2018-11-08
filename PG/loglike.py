import random
import threading
import time

# 플레이어
ph = 50
dice = 4
drem = 0
pda = 0
pdf = 0
# 몹
zh = 20
zd = 0

# 공격 함수

# 싸움
print("좀비이즈 커밍")

while True:
    pda = 0
    pdf = 0
    zd = 0
    time.sleep(2)
    print("당신의 턴")
    print("주사위 갯수", dice)
    print("공격할 횟수 (나머진 방어)")
    att = int(input())
    drem = dice - att
    for i in range (0, att):
        pda = random.randint(1, 6) + pda
    for j in range (0, drem):
        pdf = random.randint(1, 6) + pdf
    print("공격력 : ", pda)
    print("방어도 : ", pdf)
    time.sleep(1)
    pf = pdf
    zh = zh - pda
    print("남은 좀비의 체력 : ", zh)
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
print("...")