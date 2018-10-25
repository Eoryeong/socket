import random

# 맵 생성 , 지뢰 좌표 랜덤저장

global box_num, box, mine

box_num = 9

box = []
mine = []
box_show = []

# 보여주는 리스트 초기화
for i in range(box_num):
    temp = []
    for j in range(box_num):
        temp.append(1)
    box_show.append(temp)

def box_print():
    print(" 1 2 3 4 5 6 7 8 9")
    for i in range(box_num):
        a = "" + str(i+1)
        for j in range(box_num):
            if (box_show[i][j] == 1):
                a += " ☐"
            elif (box_show[i][j] == 2):
                a += " ⦿"
            else:
                if box[i][j] == 9:
                    a += " ■"
                elif box[i][j] == 0:
                    a += "  "
                else:
                    a += " "+str(box[i][j])
        print(a)
    print()
