#!/usr/bin/python
# -*- coding: utf-8 -*-

import time
import os
import syslog
import shutter as sh
import karaage_cam_gui as gui
import pygame
from pygame.locals import *
import sys
import client
import karaage_gan_generator as gan

# global
preview_numb = 0

def go_home():
    global preview_numb
    preview_numb = sh.shutter_numb
    gui.screen_home()

def shutter():
    if gui.hmi_state == gui.PRVIEW_STATE:
        go_home()
    else:
        gui.screen_shutter()
        sh.setting()
        sh.preview()
        sh.shutter()
        go_home()

def CallShutdown():
    print("Going shutdown by GPIO.")
    sh.camera.close()
    syslog.syslog(syslog.LOG_NOTICE, "Going shutdown by GPIO.")
    os.system("/sbin/shutdown -h now 'Poweroff by GPIO'")

def karaage_gan():
    if preview_numb == 0:
        gui.screen_nophoto()
    else:
        gui.screen_gan()
        global preview_numb
        filename = os.path.join(sh.photo_dir, str("{0:06d}".format(preview_numb)) + '.jpg')
        gan.karaage_gan(filename)
        gui.screen_preview('karaage_gen.jpg')

def digi2ana():
    if preview_numb == 0:
        gui.screen_nophoto()
    else:
        gui.screen_gan()
        global preview_numb
        filename = str("{0:06d}".format(preview_numb)) + '.jpg'
        filename = bytes(filename, 'UTF-8')
        client.communicate(filename)

        gui.screen_preview('pix2pix-outputs.png')

def preview():
    print ("preview")
    if preview_numb == 0:
        gui.screen_nophoto()
    else:
        global preview_numb
        filename = os.path.join(sh.photo_dir, str("{0:06d}".format(preview_numb)) + '.jpg')
        gui.screen_preview(filename)

        preview_numb -= 1
        if preview_numb < 1:
            preview_numb = sh.shutter_numb

if __name__ == '__main__':
    sh.loadFile()
    preview_numb = sh.shutter_numb

    gui.screen_opening()

    gui.screen_home()

    while True:
        gui.fpsclock.tick(10)
        for event in pygame.event.get():
            #if event.type == pygame.MOUSEBUTTONDOWN or event.type == MOUSEMOTION:
            if event.type == pygame.MOUSEBUTTONDOWN:
                pos = event.pos
                #print(pos) #for checking
                #pygame.draw.circle(gui.screen, (255,255,255), pos, 2, 0) #for debugging purposes - adds a small dot where the screen is pressed
                #pygame.display.update()

                if gui.hmi_state == gui.PRVIEW_STATE:
                    button = gui.on_touch_preview()
                    if button == 'home':
                        print('go home')
                        go_home()
                    if button == 'preview':
                        preview()


                if gui.hmi_state == gui.HOME_STATE:
                    button = gui.on_touch_home() 
                    print(button)
                    if button == 'shutter':
                        print('shutter')
                        shutter()
                    if button == 'gan':
                        print('gan')
                        karaage_gan()
                    if button == 'digi2ana':
                        print('digi2ana')
                        digi2ana()
                    if button == 'preview':
                        print('preview')
                        preview()
                    if button == 'shutdown':
                        print('shutdown')
                        CallShutdown()

            #ensure there is always a safe way to end the program if the touch screen fails
            if event.type == KEYDOWN:
                if event.key == K_ESCAPE:
                    sh.camera.close()
                    sys.exit()
