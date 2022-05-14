import pygame
import random
import math
import sqlite3
import time
import tkinter
from tkinter import *
from functools import partial
from tkinter import filedialog
pygame.init()


#################DB-highScores##################
#pastryHigh(int)#skaavokHigh(int)#wormHigh(int)#

###########################users############################
#username(String)#password(String)#money(int)#nftids(String)#c

connection = sqlite3.connect("DB.db")
c = connection.cursor()
#DISPLAY DBS#
result = c.execute("SELECT * FROM highScores")
result = result.fetchall()
print("High Scores:", result)
result = c.execute("SELECT * FROM users")
result = result.fetchall()
print("Users:", result)


#c.execute("CREATE TABLE users (username String, password int, money double, nftids String)")

#########################################LOGIN#################################################



#########################################LOGIN#################################################


pink = (255, 200, 200)
blue = (0, 0, 255)
green = (0, 255, 0)
black = (0, 0, 0)
white = (255, 255, 255)
orange = (255, 165, 0)
red = (255, 0, 0)
wormcolor = (251, 217, 177)

colors = [pink, blue, green]
pygame.init()
screen = pygame.display.set_mode((1000, 600))
escButton = pygame.image.load("Logo/esc.png")
trig = 0

##########PING VARS#################
xp = 300
yp = 300
ap = 300
bp = 300
xchangep = 2
ychangep = 2
acp = 0
bcp = 0
p1scorep = 0
p2scorep = 0
###################################
#######PASTRY ACTUATOR VARS########
totala = 0
displayscorea = ""
###################################
###########SKAAVOK VARS############
scores = 0
clock = pygame.time.Clock()
ADDITION = pygame.USEREVENT + 1
current_time = 0
start_time = 0
###################################
##############WORM#################
foodx = (random.randint(0,1000) // 20 ) * 20
foody = (random.randint(0,600) // 20 ) * 20
wormbody = [[500,300]]
headpos = [500,300]
dir = 2
scorew = 0
###################################
volume = 0.1
pygame.mixer.pre_init()
pygame.mixer.music.load("Music/GloriousSound.mp3")
pygame.mixer.music.play(-1)
pygame.mixer.music.set_volume(volume)
click = pygame.mixer.Sound("Music/click.wav")
balltap = pygame.mixer.Sound("Music/balltap.wav")
yum = pygame.mixer.Sound("Music/yum.wav")
pop = pygame.mixer.Sound("Music/pop.mp3")
## 0: title screen; 1:game selection; 2: nft market; 3: ping; 4: pastryactuator; 5: skaavok; 6:worm
selection = 0
titleLogo = pygame.image.load("Logo/titleLogo.png")


def show_text(msg, xp, yp, color):
    fontobj = pygame.font.SysFont("freesans", 32)
    msgobj = fontobj.render(msg, False, color)
    screen.blit(msgobj, (xp, yp))

while True:
    pygame.display.update()
    if selection == 0:  ###################TITLE###################
        if trig == 0:
          drawTitle()
        pygame.display.update()
        for event in pygame.event.get():
            if event.type == pygame.KEYDOWN and event.key == K_ESCAPE:
                print("quitting")
                result = c.execute("SELECT * FROM highScores")
                result = result.fetchall()
                print(result[0])
                connection.commit()
                connection.close()
                quit()
            if event.type == pygame.MOUSEBUTTONDOWN and event.button == 1:
                x, y = event.pos
                # print("coords:")
                # print("x:"+str(x))
                # print("y:"+str(y))
                if 333 <= x <= 666 and 266 <= y <= 414:
                    pygame.mixer.Sound.play(click)
                    screen.fill(black)
                    titlePlay()
                    time.sleep(0.1)
                    x = 0
                    y = 0
                    trig = 1  # go to game selection
            if event.type == pygame.MOUSEBUTTONUP and event.button == 1 and trig == 1:
                drawTitle()
                time.sleep(0.2)
                print("going to select")
                trig=0
                selection=1
            if event.type == pygame.MOUSEBUTTONDOWN and event.button == 1:
                x, y = event.pos
                if 333 <= x <= 666 and 430 <= y <= 578:
                    pygame.mixer.Sound.play(click)
                    screen.fill(black)
                    titleNFT()
                    time.sleep(0.1)
                    x = 0
                    y = 0
                    trig =2  # go to nft page
                    print("going to NFTS")
            if event.type == pygame.MOUSEBUTTONUP and event.button == 1 and trig == 2:
                selection = 2
                drawTitle()
                time.sleep(0.2)
                trig=0
                selection = 2


             # if 950 <= x <= 1000 and 550 <= y <= 600:
              ##     pygame.mixer.music.set_volume(volume) 

    if selection == 1:  #####################SELECT SCREEN###################
        if trig == 0:  
            drawSelect()
            time.sleep(0.2)
        for event in pygame.event.get():
            if event.type == pygame.KEYDOWN and event.key == K_ESCAPE:
                drawSelectEsc()
                time.sleep(0.1)
                trig = 1
                print("escape")
              
            if event.type == pygame.KEYUP and event.key == K_ESCAPE and trig == 1:
                drawSelect()
                time.sleep(0.2)
                selection = 0
                trig = 0
                print("up")
              
            if event.type == pygame.MOUSEBUTTONDOWN and event.button == 1:
                x, y = event.pos
                if 20 <= x <= 120 and 20 <= y <= 55:
                    pygame.mixer.Sound.play(click)
                    drawSelectEsc()
                    time.sleep(0.1)
                    trig = 1
                  
            if event.type == pygame.MOUSEBUTTONUP and event.button == 1 and trig == 1:
                  drawSelect()
                  time.sleep(0.2)
                  selection = 0
                  trig = 0
                  
            if event.type == pygame.MOUSEBUTTONDOWN and event.button == 1:
                x, y = event.pos
                # print("coords:")
                # print("x:"+str(x))
                # print("y:"+str(y))
                if 143 <= x <= 429 and 270 <= y <= 370:
                    pygame.mixer.Sound.play(click)
                    pygame.display.update()
                    x = 0
                    y = 0
                    trig=2
                    pingSelect()
                    time.sleep(0.1)
                    print("going to ping")
            if event.type == pygame.MOUSEBUTTONUP and event.button == 1 and trig == 2:
                  drawSelect()
                  time.sleep(0.2)
                  selection = 3
                  trig = 0

            if event.type == pygame.MOUSEBUTTONDOWN and event.button == 1:
                x, y = event.pos            
                if 143 <= x <= 429 and 400 <= y <= 500:
                    pygame.mixer.Sound.play(click)
                    screen.fill(black)
                    pygame.display.update()
                    x = 0
                    y = 0
                    trig=3
                    aimSelect()
                    time.sleep(0.1)
                    print("going to skaavok")
            if event.type == pygame.MOUSEBUTTONUP and event.button == 1 and trig == 3:
                  drawSelect()
                  time.sleep(0.2)
                  selection = 5
                  trig = 0
                
            if event.type == pygame.MOUSEBUTTONDOWN and event.button == 1:
                x, y = event.pos
                if 572 <= x <= 858 and 270 <= y <= 370:
                    pygame.mixer.Sound.play(click)
                    pygame.display.update()
                    x = 0
                    y = 0
                    trig=4
                    pastrySelect()
                    time.sleep(0.1)
                    print("going to pastry actuator")
            if event.type == pygame.MOUSEBUTTONUP and event.button == 1 and trig == 4:
                  drawSelect()
                  time.sleep(0.2)
                  selection = 4
                  trig = 0

            if event.type == pygame.MOUSEBUTTONDOWN and event.button == 1:
                x, y =event.pos
                if 572 <= x <= 858 and 400 <= y <= 500:
                    pygame.mixer.Sound.play(click)
                    screen.fill(black)
                    pygame.display.update()
                    x = 0
                    y = 0
                    wormSelect()
                    time.sleep(0.1)
                    trig=5
                    print("going to worm")
            if event.type == pygame.MOUSEBUTTONUP and event.button == 1 and trig == 5:
                  drawSelect()
                  time.sleep(0.2)
                  selection = 6
                  trig = 0
              

    if selection == 2: ###########################NFTS#######################
        screen.fill(black)
        show_text("NFTS", 0, 0, white)
        for event in pygame.event.get():
            if event.type == pygame.KEYDOWN and event.key == K_ESCAPE:
                selection = 0
                print("escape")

    if selection == 3:  ############################PING######################
        pygame.mixer.music.play(0)
        screen.fill(black)
        pygame.display.update()
        while selection == 3:
            if p1scorep == 5:
                screen.fill(black)
                show_text("WINNER", 40, 10, white)
                pygame.display.update()
                time.sleep(2)
                selection = 1 #title
            if p2scorep == 5:
                screen.fill(black)
                show_text("WINNER", 870, 10, white)
                pygame.display.update()
                time.sleep(2)
                selection = 1 #title
            pygame.display.update()
            screen.fill(black)
            show_text("Score:" + str(p1scorep), 40, 10, white)
            show_text("Score:" + str(p2scorep), 870, 10, white)
            pygame.draw.circle(screen, green, (xp, yp), 10, 0)
            pygame.draw.rect(screen, blue, (50, ap, 20, 150))
            pygame.draw.rect(screen, pink, (950, bp, 20, 150))
            pygame.draw.line(screen, white, (500, 0), (500, 600), 5)
            for event in pygame.event.get():
                if event.type == KEYDOWN:
                    if event.key == K_ESCAPE:
                        selection = 0
                        pygame.mixer.pre_init()
                        pygame.mixer.music.load("Music/GloriousSound.mp3")
                        pygame.mixer.music.play(-1)
                        print("escape")
                    if event.key == K_w:
                        acp = -2
                    if event.key == K_DOWN:
                        bcp = 2
                    if event.key == K_s:
                        acp = 2
                    if event.key == K_UP:
                        bcp = -2
                if event.type == KEYUP:
                    if event.key == K_w:
                        acp = 0
                    if event.key == K_DOWN:
                        bcp = 0
                    if event.key == K_s:
                        acp = 0
                    if event.key == K_UP:
                        bcp = 0

            if xp < 80 and ap < yp < ap + 150:
                xchangep = -xchangep
                pygame.mixer.Sound.play(balltap)
                
            if xp > 940 and bp < yp < bp + 150:
                xchangep = -xchangep
                pygame.mixer.Sound.play(balltap)
              

            ap = ap + acp
            bp = bp + bcp
            if ap <= 0:
                ap = 0

            if ap >= 450:
                ap = 450

            if bp >= 450:
                bp = 450
              
            if bp <= 0:
                bp = 0

            if xp == 990:
                xp = 500
                yp = 300
                p1scorep = p1scorep + 1
            if xp == 10:
                xp = 500
                yp = 300
                p2scorep = p2scorep + 1
            if yp > 590:
                ychangep = -2
            if yp < 10:
                ychangep = 2

            xp = xp + xchangep
            yp = yp + ychangep

    if selection == 4:  ######################PASTRY ACTUATOR########################
        pygame.mixer.music.play(0)
        pastrySelect()
        screen.fill(black)
        pygame.display.update()
        pygame.mixer.pre_init()
        pygame.mixer.music.load("Music/bangarang.mp3")
        pygame.mixer.music.play(-1)
        edp445 = pygame.image.load("Logo/edp455.jpg.png")
        screen.blit(edp445, (350, 150))
        pastryHigh = c.execute("SELECT pastryHigh FROM highScores")
        pastryHigh = pastryHigh.fetchall()
        show_text("Pastry Actuations: " + str(totala), 0, 0, white)
        show_text("HIGH SCORE: " + str(pastryHigh[0][0]), 500, 0, white)
        pygame.display.update()
        while selection == 4:
            for event in pygame.event.get():
                if event.type == pygame.KEYDOWN and event.key == K_ESCAPE:
                    selection = 0
                    pygame.mixer.pre_init()
                    pygame.mixer.music.load("Music/GloriousSound.mp3")
                    pygame.mixer.music.play(-1)
                    print("escape")
                if event.type == pygame.MOUSEBUTTONDOWN and event.button == 1:
                    xa, ya = event.pos
    
                    if xa >= 350 and xa <= 650 and ya >= 150 and ya <= 450:
                        pygame.mixer.Sound.play(click)
                        pastryHigh = c.execute("SELECT pastryHigh FROM highScores")
                        pastryHigh = pastryHigh.fetchall()
                        totala += 1
                        screen.fill(black)
                        screen.blit(edp445, (350, 150))
                        show_text("Pastry Actuations: " + str(totala), 0, 0, white)
                        if (totala > pastryHigh[0][0]):
                          c.execute("UPDATE highScores SET pastryHigh ="+ str(totala))
                        pastryHigh = c.execute("SELECT pastryHigh FROM highScores")
                        pastryHigh = pastryHigh.fetchall()
                        show_text("HIGH SCORE: " + str(pastryHigh[0][0]), 500, 0, white)
                        pygame.display.update()

    if selection == 5:  ####################SKAAVOK###################
        pygame.mixer.music.play(0)
        scores = 0
        countDownScreen()
        screen.fill(black)
        skaavokHigh = c.execute("SELECT skaavokHigh FROM highScores")
        skaavokHigh = skaavokHigh.fetchall()
        show_text(str(scores), 0, 0, white)
        show_text("HIGH SCORE: " + str(skaavokHigh[0][0]), 300, 0, white)
        randx = random.randint(100, 900)
        randy = random.randint(100, 500)
        pygame.draw.circle(screen, white, (randx, randy), 20)
        pygame.display.update()
        start_time = pygame.time.get_ticks()
        while selection == 5:
            pygame.draw.rect(screen, black, (700, 0, 300, 35))
            formatted_score = abs(((pygame.time.get_ticks()-start_time)/1000)-30)
            show_text(str(round(formatted_score, 2)), 700, 0, white)
            show_text("sec left", 800, 0, white)
            pygame.display.update()
            if (pygame.time.get_ticks()-start_time >= 30000):
                screen.fill(black)
                show_text("GAME OVER", 0, 0, white)
                
                pygame.display.update()
                time.sleep(2)
                selection = 0
                pygame.mixer.pre_init()
                pygame.mixer.music.load("Music/GloriousSound.mp3")
                pygame.mixer.music.play(-1)
                
                scores = 0
            for event in pygame.event.get():
                if event.type == pygame.KEYDOWN and event.key == K_ESCAPE:
                    selection = 0
                    pygame.mixer.pre_init()
                    pygame.mixer.music.load("Music/GloriousSound.mp3")
                    pygame.mixer.music.play(-1)
                    scores = 0
                    print("escape")
                if event.type == pygame.MOUSEBUTTONDOWN and event.button == 1:
                    xs, ys = event.pos
                    if (math.sqrt(abs(xs - randx)**2 + abs(ys - randy)**2) <= 20):
                        pygame.mixer.Sound.play(pop)
                        screen.fill(black)
                        scores = scores + 1
                        randx = random.randint(100, 900)
                        randy = random.randint(100, 500)
                        pygame.draw.circle(screen, white, (randx, randy), 20)
                        show_text(str(scores), 0, 0, white)
                        if (scores > skaavokHigh[0][0]):
                          c.execute("UPDATE highScores SET skaavokHigh ="+ str(scores))
                        skaavokHigh = c.execute("SELECT skaavokHigh FROM highScores")
                        skaavokHigh = skaavokHigh.fetchall()
                        show_text("HIGH SCORE: " + str(skaavokHigh[0][0]), 300, 0, white)
                        pygame.display.update()
                    else:
                        screen.fill(black)
                        scores = scores - 1
                        if (scores <= 0):
                            scores = 0
                        show_text(str(scores), 0, 0, white)
                        show_text("HIGH SCORE: " + str(skaavokHigh[0][0]), 300, 0, white)
                        pygame.draw.circle(screen, white, (randx, randy), 20)
                        pygame.display.update()
                    


    if selection == 6:  #####################WORM#####################
        pygame.mixer.music.play(0)
        time.sleep(0.075)
        #print(wormbody)
        wormHigh = c.execute("SELECT wormHigh FROM highScores")
        wormHigh = wormHigh.fetchall()
        screen.fill(black)
        for n in wormbody:
            pygame.draw.rect(screen, wormcolor, pygame.Rect(n[0], n[1], 20, 20))
        pygame.draw.rect(screen, red, (foodx, foody, 20, 20))
        show_text("Score: " + str(scorew), 0, 0, white)
        show_text("High Score: " + str(wormHigh[0][0]), 500, 0, white)
        pygame.display.update()
        for event in pygame.event.get():
            if event.type == pygame.KEYDOWN:
              if event.key == K_ESCAPE:
                  selection = 0
                  pygame.mixer.pre_init()
                  pygame.mixer.music.load("Music/GloriousSound.mp3")
                  pygame.mixer.music.play(-1)
                  print("escape")
              if event.key == K_DOWN:
                  dir = 0
              if event.key == K_UP:
                  dir = 1
              if event.key == K_RIGHT:
                  dir = 2
              if event.key == K_LEFT:
                  dir = 3
        if dir == 0:
            headpos[1] += 20
        if dir == 1:
            headpos[1] -= 20
        if dir == 2:
            headpos[0] += 20
        if dir == 3:
            headpos[0] -= 20

        #print(headpos)
        wormbody.insert(0, [headpos[0], headpos[1]])
        #print(wormbody)
        #print(" ")
        if foodx == wormbody[0][0] and foody == wormbody[0][1]:
            foodx = (random.randint(0,1000) // 20) * 20
            foody = (random.randint(0,600) // 20) * 20
            pygame.mixer.Sound.play(yum)
            scorew+=1
            c.execute("UPDATE highScores SET wormHigh ="+ str(scorew))
        else:
            wormbody.pop(-1)

        if headpos[0] < 0 or headpos[0] > 1000 or headpos[1] < 0 or headpos[1] > 600:
            screen.fill(black)
            selection = 0
            show_text(":( worm dead", 0, 0, white)
            pygame.display.update()
            wormbody.clear()
            wormbody.append([500,300])
            print(wormbody)
            scorew = 0
            time.sleep(3)