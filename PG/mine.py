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

# 디버그용 출력
def Print():
    for i in range(box_num):
        a = ""
        for j in range(box_num):
            if (box[i][j] == 9):
                a += " ■"
            else:
                a += " "+str(box[i][j])
        print(a)
    print()

# 주위의 지뢰 찾는 함수
def minecheck(i,j):
    global box
    c = 0
    if i == 0 and j == 0:
        if box[i][0] == 9:
            c += 1
        if box[0][1] == 9:
            c += 1
        if box [1][1] == 9:
            c += 1
    elif i == 0 and j == box_num-1:
        if box[1][box_num-1] == 9:
            c += 1
        if box[0][box_num-2] == 9:
            c += 1
        if box[1][box_num-2] == 9:
            c += 1
    elif i == box_num-1 and j == box_num-1:
        if box[box_num-2][box_num-1] == 9:
            c += 1
        if box[box_num-2][box_num-2] == 9:
            c += 1
        if box[box_num-1][box_num-2] == 9:
            c += 1
    elif i == box_num-1 and j == 0:
            if box[box_num-2][1] == 9:
                c += 1
            if box[box_num-1][1] == 9:
                c += 1
            if box[box_num-2][0] == 9:
                c += 1
    elif i == 0:
        if box[1][j] == 9:
            c += 1
        if box[0][j+1] == 9:
            c += 1
        if box[0][j-1] == 9:
            c += 1
        if box[1][j+1] == 9:
            c += 1
        if box[1][j+1] == 9:
            c ++ 1
    elif j == 0:
        if box[i][1] == 9:
            c += 1
        if box[i-1][0] == 9:
            c += 1
        if box[i+1][0] == 9:
            c += 1
        if box[i+1][1] == 9:
            c += 1
        if box[i-1][1] == 9:
            c += 1
    elif i == box_num -1:
        if box[box_num-2][j] == 9:
            c += 1
        if box[box_num-1][j+1] == 9:
            c += 1
        if box[box_num-1][j-1] == 9:
            c += 1
        if box[box_num-2][j+1] == 9:
            c += 1
        if box[box_num-2][j-1] == 9:
            c += 1

    elif j == box_num-1:
        if box[i][box_num-2] == 9:
            c += 1
        if box[i-1][box_num-1] == 9:
            c += 1
        if box[i+1][box_num-1] == 9:
            c += 1
        if box[i+1][box_num-2] == 9:
            c += 1
        if box[i-1][box_num-2] == 9:
            c += 1
    else :
        if box[i-1][j+1] == 9:
            c += 1
        if box[i][j+1] == 9:
            c += 1
        if box[i+1][j+1] == 9:
            c += 1
        if [i-1][j] == 9:
            c += 1
        if [i+1][j] == 9:
            c += 1
        if box[i-1][j-1] == 9:
            c += 1
        if box[i][j-1] == 9:
            c += 1
        if box[i+1][j-1] == 9:
            c += 1
    return c
