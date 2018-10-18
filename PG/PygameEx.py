import pygame
from pygame.locals import *

pygame.init()

# 화면 해상도를 480*320으로 초기화 윈도우 모드, 더블 버퍼 모드로 초기화하는 경우
screen = pygame.display.set_mode((480, 320), DOUBLEBUF)
pygame.display.set_caption('Hello World!') # 타이틀바의 텍스트를 설정

# 화면 해상도를 480*320, 전체 화면 모드, 하드웨어 가속 사용, 더블 버퍼 모드로 초기화하는 경우
# screen = pygame.display.set_mode((480, 320), FULLSCREEN | HWSURFACE | DOUBLEBUF)

# 색 정의
BLACK = (0, 0, 0) # R G B
RED = (255, 0, 0)
GREEN = (0, 255, 0)
BLUE = (0, 0, 255)
BLUE_A = (0, 0, 255, 127)  # R G B Alpha(투명도, 255 : 완전 불투명)

#사각형 정의
rectangle = (0, 10, 100, 100) # 왼쪽 X, 위 Y, 너비, 높이

while True:
    for event in pygame.event.get():
        # 이벤트의 처리하는 부분 - > 키보드, 마우스 등의 이벤트 처리 코드가 들어감
        if not hasattr(event, 'key'):           # 키 관련 이벤트가 아닐 경우, 건너뛰도록 처리하는 부분
            continue
        if event.type == KEYDOWN:
            if event.key == K_RIGHT:
                # 오른쪽 키에 대한 처리
                ...
            elif event.key == K_LEFT:
                # 왼쪽 키에 대한 처리
                ...
            elif event.key == K_UP:
                #위쪽 키에 대한 처리
                ...
            elif event.key == K_DOWN:
                #아래 키에 대한 처리
                ...
            elif event.key == K_ESCAPE:
                # ESC 키에 대한 처리
                ...
        LEFT = 1 # 왼쪽 버튼에 대한 버튼 인덱스
        RIGHT = 3 # 오른쪽 버튼에 대한 버튼 인덱스

        if event.type == MOUSEBUTTONDOWN and event.button == LEFT:
            # 왼쪽 버튼이 눌렸을 때의 처리
            print("left mouse up (%d, %d)" % event.pos)
        elif event.type == MOUSEBUTTONUP and event.button == LEFT:
            # 왼쪽 버튼이 떨어졌을 때의 처리
            print("left mouse down (%d, %d)" % event.pos)
        elif event.type == pygame.MOUSEMOTION:
            # 마우스 이동시의 처리
            print("mouse move (%d, %d)" % event.pos)

    # 게임의 상태를 업데이트 하는 부분

    # 전체 화면을 업데이트 할 경우
    pygame.display.flip()       # 화면 전체를 업데이트

    # 화면의 일부만 업데이트할 경우
    pygame.display.update(rectangle)        # 업데이트할 rectangle을 지정
    # pygame.display.update(rectangle_list)   # 업데이트할 rectangle을 여러개 지정

    # 게임의 상태를 화면에 그려주는 부분 - > 화면을 지우고, 그리고, 업데이트하는 코드가 들어감
    # 화면을 그리기에 앞서 지우기 위해 호출한다
    screen.fill(BLACK)

 #도형 그리기

    # 네 점을 지나는 폴리곤을 그린다
    pygame.draw.polygon(screen, RED, ((10, 10), (20, 10), (30, 20), (10, 20)))

    # 두 점을 지나는 선을 그린다
    pygame.draw.line(screen, BLUE, (10, 10), (20, 20))

    # 사각형을 그린다 (왼쪽, 위, 너비, 높이 순)
    pygame.draw.rect(screen, RED, (10, 10, 100, 50))

    # (100, 100)을 중심으로 하는 반지름 10인 원을 그린다
    pygame.draw.circle(screen, BLUE, (100, 100), 10)

    # 사각형 안을 지나는 타원을 그린다
    pygame.draw.ellipse(screen, RED, (10, 10, 100, 50))

    # 두 점을 지나는 두께 4의 선을 그린다 (모든 그리기 함수에 두께가 추가될 수 있다)
    pygame.draw.line(screen, BLUE, (10, 10), (20, 20), 4)

# 점찍기
    pixelArray = pygame.PixelArray(screen)
    pixelArray[10][100] = RED
    pixelArray[50][100] = BLUE
    del pixelArray # 사용 후, 반드시 PixelArray를 del해줘야 Sunface가 lock되는 것을 방지할 수 있다

# 이미지 파일 다루기

    # 이미지 파일 그리기
    img = pygame.image.load('image.jpg')
    screen.blit(img, (50, 100))             # 지정한 좌표가 이미지의 왼쪽 위에 위치하도록 출력된다

    # 이미지 파일 회전하여 그리기
    img = pygame.image.load('image.jpg')
    x = 100
    y = 100
    degree = 45                             # 회전할 각도를 도(degree) 단위로 지정
    rotated = pygame.transform.rotate(img, degree)
    rect = rotated.get_rect()
    rect.center = (x, y)                    # 지정한 좌표가 이미지의 중심에 오도록 출력된다
    screen.blit(rotated, rect)

# 투명도 처리

    t_surface = screen.convert_alpha()      # 기본 Surface(screen)로부터 투명도 처리를 위한 Sunface 생성

    ...

    t_surface.fill((0, 0, 0, 0))                    # t_surface 전체를 투명한 검정색으로 지운다

    pygame.draw.rect(t_surface, (0, 0, 255, 127), (30, 30, 40, 40))  # t_surface에 투명도를 적용하여 그려줌
    screen.blit(t_surface, (0, 0))                  # t_surface를 기본 Surface에 blit

# 텍스트 출력하기

    fontObj = pygame.font.Font('myfont.ttf', 32)                    # 현재 디렉토리로부터 myfont.ttf 폰트 파일을 로딩한다. 텍스트 크기를 32로 한다
    textSurfaceObj = fontObj.render('Hello Font!', True, GREEN)     # 텍스트 객체를 생성한다. 첫번째 파라미터는 텍스트 내용, 두번재는 Anti-aliasing 사용 여부, 세번째는 텍스트 컬러를 나타낸다
    textRectObj = textSurfaceObj.get_rect();                        # 텍스트 객체의 출력 위치를 가져온다
    textRectObj.center = (150, 150)                                 # 텍스트 객체의 출력 중심 좌표를 설정한다
    screen.blit(textSurfaceObj, textRectObj)                        # 설정한 위치에 텍스트 객체를 출력한다

    # Font 객체 생성의 다른 예
    fontObj = pygame.font.Font(None, 32)                                # 폰트 파일에 None을 지정할 경우 기본 폰트가 사용된다
    fontObj = pygame.font.Font('C:\\Window\\Fonts\\tahoma.ttf', 32)     # 윈도우 경로에 있는 폰트를 사용할 경우

    # render 함수 사용의 다른 예
    textSurfaceObj = fontObj.render('Hello font!', True, GREEN, BLUE)   # 텍스트 색을 녹색, 배경색을 파란색으로 설정한다

# 사운드 출력하기

    soundObj = pygame.mixer.Sound('beeps.wav')          # 사운드 파일을 로딩한다
    soundObj.play()                                     # 사운드 파일을 플레이한다 (플레이가 끝나는 것을 기다리지 않고 바로 리턴된다)

    # 5초 후에 플레이를 정지하는 경우
    import time

    soundObj.play()
    time.sleep(5)
    soundObj.stop()

    # 반복해서 플레이하는 경우 (BGM)
    pygame.mixer.music.load('background.mp3')
    pygame.mixer.music.play(-1, 0, 0)

import sys
# 윈도우의 닫기 버튼이 눌렸을 때, 프로그램을 종료하도록 처리
for event in pygame.event.get():
    if event.type == QUIT:
        pygame.quit()
        sys.exit()