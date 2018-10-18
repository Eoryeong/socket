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


