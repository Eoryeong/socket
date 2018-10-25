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
def minecheck(i, j):
    global box
    c = 0
    if i == 0 and j == 0:
        if box[1][0] == 9:
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
        if box[1][j-1] == 9:
            c += 1
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
        if box[i-1][j] == 9:
            c += 1
        if box[i+1][j] == 9:
            c += 1
        if box[i-1][j-1] == 9:
            c += 1
        if box[i][j-1] == 9:
            c += 1
        if box[i+1][j-1] == 9:
            c += 1
    return c

def makemap():
    global box
    global mine

    box = []
    check = 0
    mine = []
    # 지뢰 10개를 랜덤으로 만듦
    for i in range(999):
        same = False

        x = random.randrange(0,box_num-1)
        y = random.randrange(0,box_num-1)

        # 중복 처리
        for j in range(i-1):
            if mine[j][0] == x and mine[j][1] == y:
                same = True
                break

        if same:
            continue
        elif not same :
            mine.append([x,y])
            check += 1

        if check == 10:
            break

    # 먼저 필드에 지뢰를 배치
    for i in range(box_num):
        temp = []
        for j in range(box_num):
            cm = False
            for a in range(10):
                if mine[a][0] == i and mine[a][1] == j:
                    cm = True
            if cm :
                temp.append(9)
            else:
                temp.append(0)
        box.append(temp)
    # minecheck 함수를 사용해 지뢰 갯수 표시
    for i in range(box_num):
        for j in range(box_num):
            if box[i][j] == 0:
                box[i][j] = minecheck(i,j);

# 재귀 함수를 사용한 공백 지우기
def blank_break(i, j):

    if box_show[i][j] == 1 :

        box_show[i][j] = 0
        if i == 0 and j == 0:

            if box[1][0] == 0:
                blank_break(1, 0)
            else:
                box_show[1][0] = 0

            if box[0][1] == 0:
                blank_break(0, 1)
            else:
                box_show[0][1] = 0

            if box[1][1] == 0:
                blank_break(1, 1)
            else:
                box_show[1][1] = 0

        elif i == 0 and j == box_num - 1:

            if box[1][box_num - 1] == 0:
                blank_break(1, box_num - 1)
            else:
                box_show[1][box_num - 1] = 0

            if box[0][box_num - 2] == 0:
                blank_break(0, box_num - 2)
            else:
                box_show[0][box_num - 2] = 0

            if box[1][box_num - 2] == 0:
                blank_break(1, box_num - 2)
            else:
                box_show[1][box_num - 2] = 0

        elif i == box_num-1 and j == box_num-1:

            if box[box_num - 2][box_num - 1] == 0:
                blank_break(box_num - 2, box_num - 1)
            else:
                box_show[box_num - 2][box_num - 1] = 0

            if box[box_num - 1][box_num - 2] == 0:
                blank_break(box_num - 1, box_num - 2)
            else:
                box_show[box_num - 1][box_num - 2] = 0

            if box[box_num - 2][box_num - 2] == 0:
                blank_break(box_num - 2, box_num - 2)
            else:
                box_show[box_num - 2][box_num - 2] = 0

        elif i == box_num-1 and j == 0:

            if box[box_num - 1][1] == 0:
                blank_break(box_num - 1, 1)
            else:
                box_show[box_num - 1][1] = 0

            if box[box_num - 2][0] == 0:
                blank_break(box_num - 2, 0)
            else:
                box_show[box_num - 2][0] = 0

            if box[box_num - 2][1] == 0:
                blank_break(box_num - 2, 1)
            else:
                box_show[box_num - 2][1] = 0

        elif i == 0:

            if box[0][j - 1] == 0:
                blank_break(0, j - 1)
            else:
                box_show[0][j - 1] = 0

            if box[0][j + 1] == 0:
                blank_break(0, j + 1)
            else:
                box_show[0][j + 1] = 0

            if box[1][j-1] == 0:
                blank_break(1, j-1)
            else:
                box_show[1][j-1] = 0

            if box[1][j] == 0:
                blank_break(1, j)
            else:
                box_show[1][j] = 0

            if box[1][j+1] == 0:
                blank_break(1, j+1)
            else:
                box_show[1][j+1] = 0

        elif j == 0:

            if box[i - 1][0] == 0:
                blank_break(i - 1, 0)
            else:
                box_show[i - 1][0] = 0

            if box[i + 1][0] == 0:
                blank_break(i + 1, 0)
            else:
                box_show[i + 1][0] = 0

            if box[i-1][1] == 0:
                blank_break(i-1, 1)
            else:
                box_show[i-1][1] = 0

            if box[i][1] == 0:
                blank_break(i, 1)
            else:
                box_show[i][1] = 0

            if box[i+1][1] == 0:
                blank_break(i+1, 1)
            else:
                box_show[i+1][1] = 0

        elif i == box_num - 1:

            if box[box_num - 1][j - 1] == 0:
                blank_break(box_num - 1, j - 1)
            else:
                box_show[box_num - 1][j - 1] = 0

            if box[box_num - 1][j + 1] == 0:
                blank_break(box_num - 1, j + 1)
            else:
                box_show[box_num - 1][j + 1] = 0

            if box[box_num - 2][j-1] == 0:
                blank_break(box_num - 2, j-1)
            else:
                box_show[box_num - 2][j-1] = 0

            if box[box_num - 2][j] == 0:
                blank_break(box_num - 2, j)
            else:
                box_show[box_num - 2][j] = 0

            if box[box_num - 2][j+1] == 0:
                blank_break(box_num - 2, j+1)
            else:
                box_show[box_num - 2][j+1] = 0

        elif j == box_num-1:

            if box[i - 1][box_num - 1] == 0:
                blank_break(i - 1, box_num - 1)
            else:
                box_show[i - 1][box_num - 1] = 0

            if box[i + 1][box_num - 1] == 0:
                blank_break(i + 1, box_num - 1)
            else:
                box_show[i + 1][box_num - 1] = 0

            if box[i-1][box_num - 2] == 0:
                blank_break(i-1, box_num - 2)
            else:
                box_show[i-1][box_num - 2] = 0

            if box[i][box_num - 2] == 0:
                blank_break(i, box_num - 2)
            else:
                box_show[i][box_num - 2] = 0

            if box[i+1][box_num - 2] == 0:
                blank_break(i+1, box_num - 2)
            else:
                box_show[i+1][box_num - 2] = 0


        else:

            if box[i - 1][j] == 0:
                blank_break(i - 1, j)
            else:
                box_show[i - 1][j] = 0

            if box[i - 1][j-1] == 0:
                blank_break(i - 1, j-1)
            else:
                box_show[i - 1][j-1] = 0

            if box[i - 1][j+1] == 0:
                blank_break(i - 1, j+1)
            else:
                box_show[i - 1][j+1] = 0

            if box[i][j - 1] == 0:
                blank_break(i, j - 1)
            else:
                box_show[i][j - 1] = 0

            if box[i][j+1] == 0:
                blank_break(i, j+1)
            else:
                box_show[i][j+1] = 0

            if box[i+1][j + 1] == 0:
                blank_break(i+1, j + 1)
            else:
                box_show[i+1][j + 1] = 0

            if box[i+1][j] == 0:
                blank_break(i+1, j)
            else:
                box_show[i+1][j] = 0

            if box[i+1][j - 1] == 0:
                blank_break(i+1, j - 1)
            else:
                box_show[i+1][j - 1] = 0

    return

#블럭 한칸 부수기
def break_block():
    global box
    global box_show

    print("가로 (1~9 세로 (1~9:")
    str = input().split(" ")

    y = int(str(0)-1)
    x = int(str)()

    if box_show[x][y] == 1:
        if box[x][y] == 9:
            print("Game Over OTL")
            box_show[x][y] = 0
            box_print()
            return 2
        elif box[x][y] == 0:
            blank_break(x,y)
        else :
            box_show[x][y] = 0

    elif box_show[x][y] == 0:
        print("이미 뚫린 곳입니다.")

    count = 0
    for i in range(box_num):
        for j in range(box_num):
            if box_show[i][j] == 0:
                count += 1
    if count == 71:
        print("성공!")
        box_print()
        return 0
    return 1

makemap()

# 블럭 부수기 및 지뢰 체크 반복
while True:
    box_print()
    print("좌표 뚫기 : 1 , 좌표 지뢰 체크 : 2")
    a1 = int(input())
    if a1 == 1:
        n = break_block()
        if n == 2:
            break
        if n == 0:
            break
        else:
            continue
    if a1 == 2:
        #지뢰 체크 코
        print("가로 (1~9) 세로 (1~9) : ")
        str1 = input().split(" ")
        y = int(str1[0]) - 1
        x = int(str1[1]) - 1
        if box_show[x][y] == 1:
            box_show[x][y] = 2
        elif box_show[x][y] == 2:
            box_show[x][y] = 1
        elif box_show[x][y] == 0:
            print("이미 뚫린 곳입니다.")