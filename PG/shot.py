import pygame
import random
from time import sleep

# 전역변수 정의
BLACK = (0, 0, 0) # 바탕화면의 색상
RED = (255, 0, 0)
pad_width = 480  # 화면의 가로크기
pad_height = 640  # 화면의 세로크기
fighter_width = 36
fighter_height = 38
enemy_width = 26
enemy_height = 20

# 적을 맞춘 개수 계산
def drawScore(count):
    global gamepad
    font = pygame.font.SysFont(None, 20)
    text = font.render('Enemy Kills:' + str(count), True, (255, 255, 255))
    gamepad.blit(text,(0, 0))

# 적이 화면 아래로 통과한 개수
def drawPassed(count):
    global gamepad
    font = pygame.font.SysFont(None, 20)
    text = font.render('Enemy Passed:' + str(count), True, RED)
    gamepad.blit(text, (360,0))

def dispMessage(text):
    global gamepad
    textfont = pygame.font.Font('freesansbold.ttf', 80)
    text = textfont.render(text, True, RED)
    textpos = text.get_rect()
    textpos.center = (pad_width/2, pad_height/2)
    gamepad.blit(text, textpos)
    pygame.display.update()
    sleep(2)
    runGame()

# 전투기가 적과 충돌했을 때 메시지 출력
def crash():
    global gamepad
    dispMessage('Crashed!')

# 오버 메시지 보이기
def gameover():
    global gamepad
    dispMessage('Game Over')
# 게임에 등장하는 객체를 드로잉
def drawObject(obj, x, y):
    global gamepad
    gamepad.blit(obj,(x, y))

# 실행 메인 함수
def runGame():
    global gamepad, clock, fighter, enemy, bullet

    # 적이 맞았을 경우 True로 설정되는 플래그
    isShot = False
    shotcount = 0
    enemypassed = 0

    # 무기 좌표를 위한 리스트 자료
    bullet_xy = []

    # 전투기 초기 위치 (x, y)
    x = pad_width * 0.45
    y = pad_height * 0.9
    x_change = 0

    # 적 초기위치 설정
    enemy_x = random.randrange(0, pad_width - enemy_width)
    enemy_y = 0
    enemy_speed = 3

    ongame = False
    while not ongame:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:  # 마우스로 창을 닫는 이벤트
                doneFlag = True

            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_LEFT:
                    x_change -= 5

                elif event.key == pygame.K_RIGHT:
                    x_change += 5

                # 왼쪽 컨트롤 키를 누르면 무기 발사. 무기는 한 번 에 2발만 발사됨
                elif event.key == pygame.K_SPACE:
                    if len(bullet_xy) < 3:
                        bullet_x = x + fighter_width/2
                        bullet_y = y - fighter_height
                        bullet_xy.append([bullet_x, bullet_y])

            if event.type == pygame.KEYUP:
                if event.key == pygame.K_LEFT or event.key == pygame.K_RIGHT:
                    x_change = 0

        gamepad.fill(BLACK)  #게임화면을 검은색으로 채우고 화면을 업데이트함

        # 전투기 위치를 재조정
        x += x_change
        if x < 0:
            x = 0
        elif x > pad_width - fighter_width:
            x = pad_width - fighter_width

        # 게이머 전투기가 적과 충돌했는지 체크