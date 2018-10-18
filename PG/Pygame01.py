import sys
import pygame
from pygame.locals import *

# 초당 프레임수를 정의
TARGET_FPS = 30

clock = pygame.timeClock()

# 색 정의
BLACK = (0, 0, 0)
RED = (255, 0, 0)
GREEN = (0, 255, 0)
BLUE = (0, 0, 255)

# 마우스 버튼 인덱스 정의
LEFT = 1  # 왼쪽 버튼에 대한 버튼 인덱스
RIGHT = 3  # 오른쪽 버튼에 대한 버튼 인덱스

# 라이브러리 및 디스플레이 초기화
pygame.init()
screen = pygame.display.set_mode((480, 320), DOUBLEBUF)

# 이미지 파일을 로딩
img = pygame.image.load('image.jpg')

# 폰트 로딩 및 텍스트 객체 초기화
fontObj = pygame.font.Font('myfont.ttf', 32)
textSurfaceObj = fontObj.render('Hello Font', True, GREEN)
textRectObj = textSurfaceObj.get_rect();
textRectObj.center = (150, 200)

# 사운드 파일을 로딩
soundObj = pygame.mixer.Sound('beeps.wav')

# 메인 루프
while True:
    for event in pygame.event.get():
        # 이벤트를 처리하는 부분
        if event.type == QUIT:
            pygame.quit()
            sys.exit()

        # 키보드 이벤트 처리
        if event.type == KEYDOWN:
            if event.key == K_RIGHT:
                # 오른쪽 키가 눌리면 사운드를 플레이한다
                soundObj.play()

        # 마우스 이벤트 처리
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

    # 게임의 상태를 화면에 그려주는 부분

