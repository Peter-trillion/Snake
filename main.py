import os
import pygame
import pyautogui as pag
import sys, json, random
from colorama import *

map_size = (500, 500)
pygame.mixer.init()
pygame.mixer.music.load('resourses\\music\\BGM.mp3')
pygame.mixer.music.play(-1)
failed_bgm = pygame.mixer.Sound('resourses\\music\\failed.wav')
pygame.init()
screen = pygame.display.set_mode(map_size)
pygame.display.set_icon(pygame.image.load('resourses\\img\\icon.ico'))
with open('resourses\\data.json', 'r') as f:
    data = json.load(f)
highest_score = data['highest_score']
white = (255, 255, 255)
green = (0, 255, 0)
snake_init_pos = [[250, 250], [240, 250], [230, 250], [220, 250]]
head_pos = [250, 250]
lenth = 4
food_pos = [random.randrange(1, map_size[0] / 10) * 10, random.randrange(1, map_size[1] / 10) * 10]
cell = 10
way = ''
replay = ''
clock = pygame.time.Clock()


def draw_rect(color, pos):
    global screen, cell
    if pos != head_pos:
        pygame.draw.rect(screen, color, pygame.Rect(pos[0], pos[1], cell, cell))
    else:
        pygame.draw.rect(screen, (125, 125, 255), pygame.Rect(pos[0], pos[1], cell, cell))


def change_pos():
    global food_pos, lenth
    snake_init_pos.insert(0, list(head_pos))
    if head_pos != food_pos:
        snake_init_pos.pop()
    else:
        food_pos = [random.randrange(1, 50) * 10, random.randrange(1, 50) * 10]
        while True:
            if food_pos in snake_init_pos:
                food_pos = [random.randrange(1, 50) * 10, random.randrange(1, 50) * 10]
            else:
                break
        lenth += 1


def hit_self():
    if head_pos in snake_init_pos[1:]:
        return True


def hit_wall():
    if head_pos[0] < 0 or head_pos[0] >= map_size[0] or head_pos[1] < 0 or head_pos[1] >= map_size[1]:
        return True
    
def startwindow():
    pag.alert(text='使用 ↑ ↓ ← → 控制方向，空格暂停', title='操作提示', button='我知道了')

def main():
    global way, replay, highest_score
    while True:
        screen.fill((0, 0, 0))
        if hit_self():
            failed_bgm.play()
            if lenth > highest_score:
                with open('resourses\\data.json', 'w') as w:
                    json.dump({'highest_score':lenth}, w)
                with open('resourses\\data.json', 'r') as f:
                    data = json.load(f)
                highest_score = data['highest_score']
            pag.alert(text=f'你撞到自己了！\n当前长度:{lenth};\n最高纪录为:{highest_score}', title='你失败了', button='OK')
            replay = pag.confirm(text='是否重新开始', title='', buttons=['重玩', '退出'])
            break
        if hit_wall():
            failed_bgm.play()
            if lenth > highest_score:
                with open('resourses\\data.json', 'w') as w:
                    json.dump({'highest_score':lenth}, w)
                with open('resourses\\data.json', 'r') as f:
                    data = json.load(f)
                highest_score = data['highest_score']
            pag.alert(text=f'你撞到墙了！\n当前长度:{lenth};\n最高纪录为:{highest_score}', title='你失败了', button='OK')
            replay = pag.confirm(text='是否重新开始', title='', buttons=['重玩', '退出'])
            break
        for pos in snake_init_pos:
            draw_rect(white, pos)
        draw_rect(green, food_pos)
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                sys.exit()
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_LEFT:
                    if way != 'right':
                        way = 'left'
                if event.key == pygame.K_RIGHT:
                    if way != 'left':
                        way = 'right'
                if event.key == pygame.K_UP:
                    if way != 'down':
                        way = 'up'
                if event.key == pygame.K_DOWN:
                    if way != 'up':
                        way = 'down'
                if event.key == pygame.K_SPACE:
                    way = 'pause'
        if way == 'left':
            head_pos[0] -= cell
            change_pos()
        elif way == 'right':
            head_pos[0] += cell
            change_pos()
        elif way == 'up':
            head_pos[1] -= cell
            change_pos()
        elif way == 'down':
            head_pos[1] += cell
            change_pos()
        if way != 'pause':
            pygame.mixer.music.set_volume(1.0)
            pygame.display.set_caption(f'贪吃蛇    长度:{lenth}')
        else:
            pygame.mixer.music.set_volume(0.0)
            pygame.display.set_caption('贪吃蛇    暂停中...')
        pygame.display.update()
        clock.tick(10)
        
def endwindow():
    pass

if __name__ == '__main__':
    startwindow()
    main()
    while True:
        if replay == '退出':
            break
        else:
            failed_bgm.stop()
            snake_init_pos = [[250, 250], [240, 250], [230, 250], [220, 250]]
            head_pos = [250, 250]
            lenth = 4
            food_pos = [random.randrange(1, map_size[0] / 10) * 10, random.randrange(1, map_size[1] / 10) * 10]
            way = 'pause'
            main()
    endwindow()