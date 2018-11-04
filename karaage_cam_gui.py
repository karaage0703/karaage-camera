#!/usr/bin/python
# -*- coding: utf-8 -*-

import pygame
from pygame.locals import *
import time
import os

hmi_state = 0
HOME_STATE = 0
PRVIEW_STATE = 1

# GUI Setting from here------
pygame.init()
pygame.mouse.set_visible(1)

size = (pygame.display.Info().current_w, pygame.display.Info().current_h)
print ("Framebuffer size: %d x %d" % (size[0], size[1]))
screen = pygame.display.set_mode(size, pygame.FULLSCREEN)
title_font = pygame.font.Font(os.path.join('/usr/share/fonts/truetype/fonts-japanese-gothic.ttf'), 48)
body_font = pygame.font.Font(os.path.join('/usr/share/fonts/truetype/fonts-japanese-gothic.ttf'), 32)
fpsclock = pygame.time.Clock()
# ----------- GUI

def make_button(text, xpo, ypo, height, width, colour):
    label=body_font.render(str(text), 1, (colour))
    screen.blit(label,(xpo,ypo))
    pygame.draw.rect(screen, (255,255,255), (xpo-10,ypo-10,width,height),3)

def screen_clear():
    screen.fill((0,0,0))
    pygame.display.update()

def screen_opening():
    title = title_font.render(u'からあげカメラ', True, (255,255,255))
    screen.fill((0,0,0))
    screen.blit(title, (30,100))
    pygame.display.update()
    time.sleep(3)
    screen_clear()

def screen_gan():
    title = title_font.render(u'GAN変換中', True, (255,255,255))
    screen.fill((0,0,0))
    screen.blit(title, (30,100))
    pygame.display.update()

def screen_countup():
    count = 0
    while count <= 100:
       count_str = str(count) + "%"
       count_text = title_font.render(count_str, True, (255,255,255))
       screen.fill((0,0,0))
       screen.blit(count_text,(100,100))
       pygame.display.update()
       time.sleep(2.5)
       count += 10

def screen_shutter():
    text = title_font.render('Taking Photo', True, (255,255,255))
    screen.fill((0,0,0))
    screen.blit(text, (50,100))
    pygame.display.update()

def screen_nophoto():
    text = title_font.render('No Photo',  True, (255,255,255))
    screen.fill((0,0,0))
    screen.blit(text, (50,100))
    pygame.display.update()

def screen_home():
    global hmi_state
    hmi_state = HOME_STATE

    screen.fill((0,0,0))

    make_button(u"撮影", 100, 100 , 55, 300, (255,255,255))
    make_button(u"からあげGAN", 100, 200 , 55, 300, (255,255,255))
    make_button(u"アナログカメラ変換", 100, 300 , 55, 300, (255,255,255))
    make_button(u"プレビュー", 500, 100 , 55, 250, (255,255,255))
    make_button(u"シャットダウン", 500, 400 , 55, 250, (255,255,255))

    pygame.display.update()

def on_touch_home():
    # get the position that was touched
    touch_pos = (pygame.mouse.get_pos() [0], pygame.mouse.get_pos() [1])
    #  x_min                 x_max   y_min                y_max
    # shutter button event
    if 100 <= touch_pos[0] <= 400 and 95 <= touch_pos[1] <=160:
        return 'shutter' 

    # gan button event
    if 100 <= touch_pos[0] <= 400 and 195 <= touch_pos[1] <=260:
        return 'gan'

    # digi2ana button event
    if 100 <= touch_pos[0] <= 400 and 295 <= touch_pos[1] <=360:
        return 'digi2ana' 

    # preview button event
    if 500 <= touch_pos[0] <= 750 and 95 <= touch_pos[1] <=160:
        return 'preview' 

    # shutdown button event
    if 500 <= touch_pos[0] <= 750 and 395 <= touch_pos[1] <=460:
        return 'shutdown'

def on_touch_preview():
    # get the position that was touched
    touch_pos = (pygame.mouse.get_pos() [0], pygame.mouse.get_pos() [1])
    #  x_min                 x_max   y_min                y_max
    if 100 <= touch_pos[0] <= 700 and 400 <= touch_pos[1] <=600:
        return 'home'
    if 100 <= touch_pos[0] <= 700 and 100 <= touch_pos[1] <=400:
        return 'preview'

def screen_preview(filename):
    global hmi_state
    hmi_state = PRVIEW_STATE

    img = pygame.image.load(filename).convert()
    img = pygame.transform.scale(img, (pygame.display.Info().current_w, pygame.display.Info().current_h))
    screen.blit(img, (0,0))
    pygame.display.update()

if __name__ == '__main__':
    pass
