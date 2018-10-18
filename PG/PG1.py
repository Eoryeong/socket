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
    ...
    #게임의 상태를 화면에 그려주는 부분 - > 화면을 지우고, 그리고, 업데이트하는 코드가 들어감
    ...

import sys
# 윈도우의 닫기 버튼이 눌렸을 때, 프로그램을 종료하도록 처리
for event in pygame.event.get():
    if event.type == QUIT:
        pygame.quit()
        sys.exit()