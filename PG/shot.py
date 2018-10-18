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