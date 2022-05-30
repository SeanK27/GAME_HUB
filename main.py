import pygame
import random
import math
import sqlite3
import time
import tkinter
from tkinter import *
from functools import partial
from tkinter import filedialog
from Title import *
from tkinter import messagebox
import mysql.connector
# import os
from node_modules import vars
from better_profanity import profanity

##########

# host1 = os.environ['host']
# user1 = os.environ['user']
# password1 = os.environ['password']
# db1 = os.environ['db']

# host1 = os.getenv['host']
# user1 = os.getenv['user']
# password1 = os.getenv['password']
# db1 = os.getenv['db']

#################

pygame.init()
Clock = pygame.time.Clock()

#################DB-highScores##################
# pastryHigh(int)#skaavokHigh(int)#wormHigh(int)#

###########################users#############################
# username(String)#password(String)#money(int)#nftids(String)#

# connection = sqlite3.connect("DB.db")
# c = connection.cursor()

# conn = mysql.connector.connect(
#     host="bvhsdrtwwbrnsac2wlsc-mysql.services.clever-cloud.com",
#     user="ulkqho87c7b8tdam",
#     password="dmqctKjJsJYlyFq9369e1", ex 1 hee hee
#     db="bvhsdrtwwbrnsac2wlsc"
#     )

# conn = mysql.connector.connect(
#     host=host1,
#     user=user1,
#     password=password1,
#     db=db1
#     )

conn = mysql.connector.connect(
    host=vars.host1,
    user=vars.user1,
    password=vars.password1,
    db=vars.db1
)

c = conn.cursor()

####QUERY TESTING####

# c.execute("CREATE TABLE highScores (pastryHigh int, skaavokHigh int, wormHigh int)")

# c.execute("CREATE TABLE users (username VARCHAR(255), password VARCHAR(255), money DOUBLE, nftids int)")

# c.execute("INSERT INTO highScores VALUES (0, 0, 0)")

# c.execute("DELETE FROM highScores WHERE pastryHigh = 0")

# c.execute("UPDATE users SET money = 2000.0 WHERE username = 'sean'")

# c.execute("SELECT * FROM users")
# print(c.fetchall())

# c.execute("UPDATE users SET nftids = ''")


#####################
conn.commit()

# DISPLAY DBS#
result = c.execute("SELECT * FROM highScores")
result = c.fetchall()
# print("High Scores:", result)
result = c.execute("SELECT * FROM users")
result = c.fetchall()


# print("Users: ", result)

def getHubCoin(usern):
    r = c.execute("SELECT * FROM users")
    r = c.fetchall()
    for users in r:
        if users[0] == usern:
            return float(users[2])
    return "none"


#########################################LOGIN#################################################

def Login(username, password):
    n = 0
    print("username entered :", username.get())
    print("password entered :", password.get())
    result = c.execute("SELECT * FROM users")
    result = c.fetchall()
    for users in result:
        if username.get() == users[0] and password.get() == users[1]:
            messagebox.showinfo("Success!", "Welcome, " + profanity.censor(username.get()) + ", to GameHub!")
            vars.user = username.get()
            tkWindow.destroy()
            n = 1
    if n != 1:
        messagebox.showerror("Error", "Username or password is incorrect.\nPlease try again.")


def Register(username, password):
    m = 0
    l = 0
    print("username entered :", username.get())
    print("password entered :", password.get())
    tempuser = username.get()
    temppassword = password.get()
    result = c.execute("SELECT * FROM users")
    result = c.fetchall()
    for users in result:
        if username.get() == users[0]:
            messagebox.showerror("Error", "Username already in use.")
            m = 1
        if username.get() == '' or password.get() == '':
            l = 1
            m = 1
    if l == 1:
        messagebox.showerror("Error", "Please Enter valid credentials.")
    if m != 1:
        c.execute(f"INSERT INTO users VALUES ('{tempuser}', '{temppassword}', 0.0, '')")
        conn.commit()
        messagebox.showinfo("Success!", "Thank you for joining GameHub!\n\nPlease Login.")
        result1 = c.execute("SELECT * FROM users")
        result1 = c.fetchall()


tkWindow = Tk()
tkWindow.geometry('1000x600')
tkWindow.title('GameHub Login')

# username label and text entry box
usernameLabel = Label(tkWindow, text="User Name").grid(row=0, column=0)
username = StringVar()
usernameEntry = Entry(tkWindow, textvariable=username).grid(row=0, column=1)

# password label and password entry box
passwordLabel = Label(tkWindow, text="Password").grid(row=1, column=0)
password = StringVar()
passwordEntry = Entry(tkWindow, textvariable=password, show='*').grid(row=1, column=1)

Register = partial(Register, username, password)
Login = partial(Login, username, password)

# login button
loginButton = Button(tkWindow, text="Login", command=Login).grid(row=4, column=0)

# Register button
registerButton = Button(tkWindow, text="Register", command=Register).grid(row=4, column=1)

# Play as guest button
playasguestButton = Button(tkWindow, text="Play as guest", command=tkWindow.destroy).grid(row=10, column=0)


def disable_event():
    pass


tkWindow.protocol("WM_DELETE_WINDOW", disable_event)
tkWindow.mainloop()

#########################################LOGIN#################################################


pink = (255, 200, 200)
blue = (0, 0, 255)
green = (0, 255, 0)
black = (0, 0, 0)
white = (255, 255, 255)
orange = (247, 148, 30)
red = (255, 0, 0)
brown = (210, 105, 30)
wormcolor = (251, 217, 177)
purple = (102, 51, 153)
cyan = (0, 255, 255)

###################SKINS####################
vars.color = white
############################################

colors = [pink, blue, green]
pygame.init()
screen = pygame.display.set_mode((1000, 600))
escButton = pygame.image.load("Logo/esc.png")
trig = 0

xbg = 500
ybg = 300
xchangebg = 2
ychangebg = 2
yTitle = 0

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
pastryanimlist = []
edp4450 = pygame.image.load("pastryanim/edp445.jpg(0).png")
edp4451 = pygame.image.load("pastryanim/edp445(1).png")
edp4452 = pygame.image.load("pastryanim/edp445(2).png")
edp4453 = pygame.image.load("pastryanim/edp445(3).png")
edp4454 = pygame.image.load("pastryanim/edp445(4).png")
edp4455 = pygame.image.load("pastryanim/edp445(5).png")
pastryanimlist.append(edp4450)
pastryanimlist.append(edp4451)
pastryanimlist.append(edp4452)
pastryanimlist.append(edp4453)
pastryanimlist.append(edp4454)
pastryanimlist.append(edp4455)
toggleon = pygame.image.load("Logo/toggleon.jpg")
toggleoff = pygame.image.load("Logo/toggleoff.jpg")
###################################
###########SKAAVOK VARS############
scores = 0
clock = pygame.time.Clock()
ADDITION = pygame.USEREVENT + 1
current_time = 0
start_time = 0
deltas = 0
###################################
##############WORM#################
foodx = (random.randint(0, 1000) // 20) * 20
foody = (random.randint(0, 600) // 20) * 20
wormbody = [[500, 300]]
headpos = [500, 300]
dir = 2
scorew = 0
deltaw = 0.0
###################################
volume = 0.1
pygame.mixer.pre_init()
pygame.mixer.music.load("Music/GloriousSound.mp3")
pygame.mixer.music.play(-1)
pygame.mixer.music.set_volume(volume)
click = pygame.mixer.Sound("Music/click.wav")
balltap = pygame.mixer.Sound("Music/balltap.wav")
yum = pygame.mixer.Sound("Music/yum.wav")
pop = pygame.mixer.Sound("Music/pop.wav")
## 0: title screen; 1:game selection; 2: nft market; 3: ping; 4: pastryactuator; 5: skaavok; 6:worm
selection = 0
titleLogo = pygame.image.load("Logo/titleLogo.png")
trophy = pygame.image.load("Logo/trophy.png")
nn = 0
L = -1
equip = -1
badgeEquip = -1


def show_text(msg, xp, yp, color):
    fontobj = pygame.font.Font("fonts/COMIC.TTF", 21)
    msgobj = fontobj.render(msg, False, color)
    screen.blit(msgobj, (xp, yp))


def searchNFTS(usern, id):
    c.execute(f"SELECT nftids FROM users WHERE username = '{usern}'")
    tup = c.fetchall()
    strr = tup[0][0]
    for x in str(strr):
        if x == id:
            return True
    return False


def getNFTS(usern):
    c.execute(f"SELECT nftids FROM users WHERE username = '{usern}'")
    tup = c.fetchall()
    return tup[0][0]


def setNFTS(usern, id):
    strs = getNFTS(usern)
    strs = strs + str(id)
    c.execute(f"UPDATE users SET nftids = '{strs}' WHERE username = '{usern}'")
    print(strs)


# Add users to the global vars file
def addUsers():
    r = c.execute("SELECT * FROM users")
    r = c.fetchall()
    vars.users = r
    vars.sorted.clear()
    bigarr = []
    for user in r:
        bigarr.append(user[2])
    bigarr.sort(reverse=True)
    for num in bigarr:
        for user in vars.users:
            if user[2] == num:
                vars.sorted.append(user)


addUsers()
# print(vars.sorted)

while True:
    if selection == 0:  ###################TITLE###################

        # left worm
        if trig == 0:
            if volume == 0:
                drawTitleoff()
            else:
                drawTitle()

        pygame.display.update()

        for event in pygame.event.get():

            if event.type == pygame.KEYDOWN and event.key == K_ESCAPE:
                print("quitting")
                result = c.execute("SELECT * FROM highScores")
                result = c.fetchall()
                print(result[0])
                conn.commit()
                conn.close()
                quit()

            if event.type == pygame.MOUSEBUTTONDOWN and event.button == 1:
                x, y = event.pos
                if 935 <= x <= 985 and 540 <= y <= 580:
                    pygame.mixer.Sound.play(click)
                    if volume != 0:
                        volume = 0
                        pygame.mixer.music.set_volume(volume)
                        drawTitleoff()
                    else:
                        volume = 0.1
                        pygame.mixer.music.set_volume(volume)
                        drawTitle()
            if event.type == pygame.MOUSEBUTTONDOWN and event.button == 1:
                x, y = event.pos
                if 333 <= x <= 666 and 266 <= y <= 414:
                    pygame.mixer.Sound.play(click)
                    screen.fill(black)
                    if volume == 0:
                        titlePlayoff()
                    else:
                        titlePlay()
                    time.sleep(0.1)
                    x = 0
                    y = 0
                    trig = 1  # go to game selection
            if event.type == pygame.MOUSEBUTTONUP and event.button == 1 and trig == 1:
                if volume == 0:
                    drawTitleoff()
                else:
                    drawTitle()
                time.sleep(0.2)
                print("going to select")
                trig = 0
                selection = 1
            if event.type == pygame.MOUSEBUTTONDOWN and event.button == 1:
                x, y = event.pos
                if 333 <= x <= 666 and 430 <= y <= 578:
                    pygame.mixer.Sound.play(click)
                    screen.fill(black)
                    if volume == 0:
                        titleNFToff()
                    else:
                        titleNFT()
                    time.sleep(0.1)
                    x = 0
                    y = 0
                    trig = 2  # go to nft page
                    print("going to NFTS")
            if event.type == pygame.MOUSEBUTTONUP and event.button == 1 and trig == 2:
                if volume == 0:
                    drawTitleoff()
                else:
                    drawTitle()
                time.sleep(0.2)
                if getHubCoin(vars.user) == "none":
                    selection = 10
                else:
                    selection = 2
                    x = 0
                    y = 0
                trig = 0

            if event.type == pygame.MOUSEBUTTONDOWN and event.button == 1:
                x, y = event.pos
                if 5 <= x <= 115 and 565 <= y <= 595:
                    print("leaderboard")
                    pygame.mixer.Sound.play(click)
                    if volume == 0:
                        titleLeaderboardv()
                    else:
                        titleLeaderboard()
                    time.sleep(0.1)
                    # leaderboard
                    trig = 6
            if event.type == pygame.MOUSEBUTTONUP and event.button == 1 and trig == 6:
                if volume == 0:
                    drawTitleoff()
                else:
                    drawTitle()
                time.sleep(0.2)
                if getHubCoin(vars.user) == "none":
                    selection = 7
                else:
                    selection = 7
                    x = 0
                    y = 0
                trig = 0

            if event.type == pygame.MOUSEBUTTONDOWN and event.button == 1:
                x, y = event.pos
                if 120 <= x <= 202 and 565 <= y <= 595:
                    print("help")
                    pygame.mixer.Sound.play(click)
                    if volume == 0:
                        titleHelpv()
                    else:
                        titleHelp()

                    time.sleep(0.1)
                    trig = 7
            if event.type == pygame.MOUSEBUTTONUP and event.button == 1 and trig == 7:
                if volume == 0:
                    drawTitleoff()
                else:
                    drawTitle()
                time.sleep(0.2)
                trig = 0
                x = 0
                y = 0
                selection = 11

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
                screen.fill(black)
                selection = 0
                trig = 0

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
                screen.fill(black)
                selection = 0
                trig = 0

            if event.type == pygame.MOUSEBUTTONDOWN and event.button == 1:
                x, y = event.pos
                if 143 <= x <= 429 and 270 <= y <= 370:
                    pygame.mixer.Sound.play(click)
                    pygame.display.update()
                    x = 0
                    y = 0
                    trig = 2
                    pingSelect()
                    time.sleep(.1)
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
                    pygame.display.update()
                    x = 0
                    y = 0
                    trig = 3
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
                    trig = 4
                    pastrySelect()
                    time.sleep(0.1)
                    print("going to pastry actuator")
            if event.type == pygame.MOUSEBUTTONUP and event.button == 1 and trig == 4:
                drawSelect()
                time.sleep(0.2)
                selection = 4
                trig = 0

            if event.type == pygame.MOUSEBUTTONDOWN and event.button == 1:
                x, y = event.pos
                if 572 <= x <= 858 and 400 <= y <= 500:
                    pygame.mixer.Sound.play(click)
                    pygame.display.update()
                    x = 0
                    y = 0
                    wormSelect()
                    time.sleep(0.1)
                    trig = 5
                    print("going to worm")
            if event.type == pygame.MOUSEBUTTONUP and event.button == 1 and trig == 5:
                drawSelect()
                time.sleep(0.2)
                selection = 6
                trig = 0
    if selection == 10:  #####################NO ACCOUNT NFT##################
        drawNFTnoaccount()
        while selection == 10:
            for event in pygame.event.get():
                if event.type == pygame.KEYDOWN and event.key == K_ESCAPE:
                    drawNFTnoaccountesc()
                    time.sleep(0.1)
                    trig = 1
                    print("escape")

                if event.type == pygame.KEYUP and event.key == K_ESCAPE and trig == 1:
                    drawNFTnoaccount()
                    time.sleep(0.2)
                    screen.fill(black)
                    selection = 0
                    trig = 0

    if selection == 7:  ########################LEADERBOARD##################
        screen.fill(black)
        addUsers()
        leaderboard()
        while selection == 7:
            for event in pygame.event.get():
                if event.type == pygame.KEYDOWN and event.key == K_ESCAPE:
                    leaderboardesc()
                    time.sleep(0.1)
                    trig = 1
                    print("escape")

                if event.type == pygame.KEYUP and event.key == K_ESCAPE and trig == 1:
                    leaderboard()
                    time.sleep(0.2)
                    screen.fill(black)
                    selection = 0
                    trig = 0

    if selection == 11:  ###################HELP######################
        screen.fill(black)
        drawHelp()
        while selection == 11:
            for event in pygame.event.get():
                if event.type == pygame.KEYDOWN and event.key == K_ESCAPE:
                    drawHelpesc()
                    time.sleep(0.1)
                    trig = 1
                    print("escape")

                if event.type == pygame.KEYUP and event.key == K_ESCAPE and trig == 1:
                    drawHelp()
                    time.sleep(0.2)
                    screen.fill(black)
                    selection = 0
                    trig = 0

    if selection == 2:  ###########################NFTS#######################
        screen.fill(black)
        showHubCoin(vars.user, 800, 0, white)
        drawNFT()
        while selection == 2:
            if equip < 0 or equip > 5:
                vars.color = white

            if equip == 0:
                screen.fill(black)
                drawNFT0()
                vars.color = red

            if equip == 1:
                screen.fill(black)
                drawNFT1()
                vars.color = blue

            if equip == 2:
                screen.fill(black)
                drawNFT2()
                vars.color = purple

            if equip == 3:
                screen.fill(black)
                drawNFT3()
                vars.color = orange

            if equip == 4:
                screen.fill(black)
                drawNFT4()
                vars.color = cyan

            if equip == 5:
                screen.fill(black)
                drawNFT5()

            for event in pygame.event.get():
                if event.type == pygame.KEYDOWN and event.key == K_ESCAPE:
                    drawNFTesc()
                    time.sleep(0.1)
                    trig = 1
                    print("escape")

                if event.type == pygame.KEYUP and event.key == K_ESCAPE and trig == 1:
                    drawNFT()
                    time.sleep(0.2)
                    screen.fill(black)
                    trig = 0
                    selection = 0
                    x = 0
                    y = 0

                if event.type == pygame.MOUSEBUTTONDOWN and event.button == 1:
                    x, y = event.pos

                    if 450 <= x <= 532 and 530 <= y <= 570 and L >= 0 and getHubCoin(vars.user):
                        if L == 3.5:
                            print(getHubCoin(vars.user))
                            diff = getHubCoin(vars.user) - L
                            if getHubCoin(vars.user) >= L:
                                if searchNFTS(vars.user, '0') != True:
                                    c.execute(f"UPDATE users SET money = '{diff}' WHERE username = '{vars.user}'")
                                    c.execute(setNFTS(vars.user, 0))
                                    print("bought")
                                    addUsers()
                                    screen.fill(black)
                                    drawNFT0()
                                    equip = 0
                                    diff = 0
                                    pygame.display.update()
                                else:
                                    print("u already hav it bruh")
                                    drawHave()
                            else:
                                print("broke ahh")
                                drawBroke()

                        if L == 5:
                            print(getHubCoin(vars.user))
                            diff = getHubCoin(vars.user) - L
                            if getHubCoin(vars.user) >= L:
                                if searchNFTS(vars.user, '1') != True:
                                    c.execute(f"UPDATE users SET money = '{diff}' WHERE username = '{vars.user}'")
                                    c.execute(setNFTS(vars.user, 1))
                                    print("updated")
                                    addUsers()
                                    screen.fill(black)
                                    drawNFT1()
                                    equip = 1
                                    diff = 0
                                    pygame.display.update()
                                else:
                                    print("u already hav it bruh")
                                    drawHave()
                            else:
                                print("broke ahh")
                                drawBroke()

                        if L == 69:
                            print(getHubCoin(vars.user))
                            diff = getHubCoin(vars.user) - L
                            if getHubCoin(vars.user) >= L:
                                if searchNFTS(vars.user, '2') != True:
                                    c.execute(f"UPDATE users SET money = '{diff}' WHERE username = '{vars.user}'")
                                    c.execute(setNFTS(vars.user, 2))
                                    print("updated")
                                    addUsers()
                                    screen.fill(black)
                                    drawNFT2()
                                    equip = 2
                                    diff = 0
                                    pygame.display.update()
                                else:
                                    print("u already hav it bruh")
                                    drawHave()
                            else:
                                print("broke ahh")
                                drawBroke()

                        if L == 50:
                            print(getHubCoin(vars.user))
                            diff = getHubCoin(vars.user) - L
                            if getHubCoin(vars.user) >= L:
                                if searchNFTS(vars.user, '3') != True:
                                    c.execute(f"UPDATE users SET money = '{diff}' WHERE username = '{vars.user}'")
                                    c.execute(setNFTS(vars.user, 3))
                                    print("updated")
                                    addUsers()
                                    screen.fill(black)
                                    drawNFT3()
                                    badgeEquip = 3
                                    diff = 0
                                    pygame.display.update()
                                else:
                                    print("u already hav it bruh")
                                    drawHave()
                            else:
                                print("broke ahh")
                                drawBroke()

                        if L == 75:
                            print(getHubCoin(vars.user))
                            diff = getHubCoin(vars.user) - L
                            if getHubCoin(vars.user) >= L:
                                if searchNFTS(vars.user, '4') != True:
                                    c.execute(f"UPDATE users SET money = '{diff}' WHERE username = '{vars.user}'")
                                    c.execute(setNFTS(vars.user, 4))
                                    print("updated")
                                    addUsers()
                                    screen.fill(black)
                                    drawNFT4()
                                    badgeEquip = 4
                                    diff = 0
                                    pygame.display.update()
                                else:
                                    print("u already hav it bruh")
                                    drawHave()
                                    drawHave()
                            else:
                                print("broke ahh")
                                drawBroke()
                                drawBroke()

                        if L == 100:
                            print(getHubCoin(vars.user))
                            diff = getHubCoin(vars.user) - L
                            if getHubCoin(vars.user) >= L:
                                if searchNFTS(vars.user, '5') != True:
                                    c.execute(f"UPDATE users SET money = '{diff}' WHERE username = '{vars.user}'")
                                    c.execute(setNFTS(vars.user, 5))
                                    print("updated")
                                    addUsers()
                                    screen.fill(black)
                                    drawNFT5()
                                    diff = 0
                                    pygame.display.update()
                                else:
                                    print("u already hav it bruh")
                                    drawHave()
                            else:
                                print("broke ahh")
                                drawBroke()

            if 55 <= x <= 305 and 200 <= y <= 350:
                if searchNFTS(vars.user, '0') == True:
                    equip = 0
                    L = 3.5
                else:
                    L = 3.5
                    drawNFT0()
                    equip = 10

            if 370 <= x <= 620 and 200 <= y <= 350:
                if searchNFTS(vars.user, '1') == True:
                    equip = 1
                    L = 5
                else:
                    L = 5
                    drawNFT1()
                    equip = 10

            if 685 <= x <= 935 and 200 <= y <= 350:
                if searchNFTS(vars.user, '2') == True:
                    equip = 2
                    L = 69
                else:
                    L = 69
                    drawNFT2()
                    equip = 10

            if 55 <= x <= 305 and 380 <= y <= 530:
                if searchNFTS(vars.user, '3') == True:
                    equip = 3
                    L = 50
                else:
                    L = 50
                    drawNFT3()
                    equip = 10

            if 370 <= x <= 620 and 380 <= y <= 530:
                if searchNFTS(vars.user, '4') == True:
                    equip = 4
                    L = 75
                else:
                    L = 75
                    drawNFT4()
                    equip = 10

            if 685 <= x <= 935 and 380 <= y <= 530:
                if searchNFTS(vars.user, '5') == True:
                    equip = 5
                    L = 100
                else:
                    L = 100
                    drawNFT5()
                    equip = 10

    if selection == 3:  ############################PING######################
        screen.fill(black)
        pygame.display.update()
        while selection == 3:
            if p1scorep == 5:
                screen.fill(black)
                show_text("BLUE IS THE WINNER", 40, 10, white)
                screen.blit(trophy, (40, 40))
                pygame.display.update()
                time.sleep(2)
                p2scorep = 0
                p1scorep = 0
                screen.fill(black)
                selection = 1  # title
            if p2scorep == 5:
                screen.fill(black)
                show_text("RED IS THE WINNER", 800, 10, white)
                screen.blit(trophy, (800, 40))
                pygame.display.update()
                time.sleep(2)
                p2scorep = 0
                p1scorep = 0
                screen.fill(black)
                selection = 1  # title
            pygame.display.update()
            screen.fill(black)
            show_text("Score:" + str(p1scorep), 40, 10, white)
            show_text("Score:" + str(p2scorep), 870, 10, white)
            pygame.draw.circle(screen, vars.color, (xp, yp), 10, 0)
            pygame.draw.rect(screen, blue, (50, ap, 20, 150))
            pygame.draw.rect(screen, red, (950, bp, 20, 150))
            pygame.draw.line(screen, white, (500, 0), (500, 600), 5)
            for event in pygame.event.get():
                if event.type == KEYDOWN:
                    if event.key == K_ESCAPE:
                        screen.fill(black)
                        selection = 0
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

            if xp <= 80 and ap < yp < ap + 150:
                xchangep = -xchangep
                pygame.mixer.Sound.play(balltap)

            if xp >= 940 and bp < yp < bp + 150:
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

            if xp >= 990:
                xp = 500
                yp = 300
                p1scorep = p1scorep + 1
            if xp <= 10:
                xp = 500
                yp = 300
                p2scorep = p2scorep + 1
            if yp > 590:
                ychangep = -2
            if yp < 10:
                ychangep = 2

            time.sleep(.005)
            xp = xp + xchangep
            yp = yp + ychangep

    if selection == 4:  ######################PASTRY ACTUATOR########################
        pastrySelect()
        screen.fill(black)
        pygame.display.update()

        end = -1
        choose = 1
        cutloop = 1

        screen.blit(edp4450, (350, 150))
        show_text("Toggle Animation", 0, 258, white)
        screen.blit(toggleon, (0, 290))
        pastryHigh = c.execute("SELECT pastryHigh FROM highScores")
        pastryHigh = c.fetchall()
        show_text("Actuations: " + str(totala), 0, 0, white)
        show_text("HIGH SCORE: " + str(pastryHigh[0][0]), 0, 40, white)
        coinamt = getHubCoin(vars.user)
        if coinamt != "none":
            showHubCoin(vars.user, 700, 0, white)
        pygame.display.update()
        start = pygame.time.get_ticks()
        click_count = 0
        while selection == 4:

            elapsed = abs(pygame.time.get_ticks() - start)
            for event in pygame.event.get():
                if event.type == pygame.KEYDOWN and event.key == K_ESCAPE:
                    screen.fill(black)
                    selection = 0
                    print("escape")
                if event.type == pygame.MOUSEBUTTONDOWN and event.button == 1:
                    xa, ya = event.pos

                    if xa >= 0 and xa <= 83 and ya >= 290 and ya <= 332:
                        if choose > 0:
                            end = 1
                            pygame.draw.rect(screen, black, (0, 290, 100, 100))
                            show_text("Toggle Animation", 0, 258, white)
                            screen.blit(toggleoff, (0, 290))
                            pygame.display.update()
                            choose = -1
                        else:
                            end = -1
                            pygame.draw.rect(screen, black, (0, 290, 100, 100))
                            show_text("Toggle Animation", 0, 258, white)
                            screen.blit(toggleon, (0, 290))
                            pygame.display.update()
                            choose = 1

                    if xa >= 350 and xa <= 650 and ya >= 150 and ya <= 450:

                        # Anti Cheat
                        ip = str(random.randint(100, 999)) + "." + str(random.randint(100, 999)) + "." + str(
                            random.randint(10, 99)) + "." + str(random.randint(10, 99))
                        start = pygame.time.get_ticks()
                        # print(prev)
                        # print(" ")
                        # print(elapsed)
                        if elapsed <= 150:
                            prev = elapsed
                            click_count += 1
                        else:
                            click_count = 0
                        if click_count == 400:
                            banscreen()
                            show_text("Your IP, " + ip + ", has been saved to our database", 0, 0, white)
                            pygame.display.update()
                            pygame.mixer.music.load("Music/happynoise.mp3")  # death
                            pygame.mixer.music.play(-1)
                            pygame.mixer.music.set_volume(99999)
                            time.sleep(99999)
                        ############
                        pygame.mixer.Sound.play(click)
                        pastryHigh = c.execute("SELECT pastryHigh FROM highScores")
                        pastryHigh = c.fetchall()
                        totala += 1
                        coinamt = getHubCoin(vars.user)
                        if coinamt != "none":
                            coinamt += 1.0 / 500.0
                            c.execute(f"UPDATE users SET money = '{round(coinamt, 4)}' WHERE username = '{vars.user}'")
                            addUsers()
                        screen.fill(black)

                        # for frame in pastryanimlist:
                        #    pygame.draw.rect(screen, black, (350, 150, 1000, 1000))
                        #    screen.blit(frame, (465, 270))
                        #    pygame.display.update()

                        #################ANIMATION##################
                        while end < 0 and cutloop > 0:
                            pygame.draw.rect(screen, black, (350, 150, 1000, 1000))
                            screen.blit(edp4451, (353, 153))  # fifth
                            show_text("Toggle Animation", 0, 258, white)
                            screen.blit(toggleon, (0, 290))
                            pastryHigh = c.execute("SELECT pastryHigh FROM highScores")
                            pastryHigh = c.fetchall()
                            show_text("Actuations: " + str(totala), 0, 0, white)
                            show_text("HIGH SCORE: " + str(pastryHigh[0][0]), 0, 40, white)
                            coinamt = getHubCoin(vars.user)
                            if coinamt != "none":
                                showHubCoin(vars.user, 700, 0, white)
                            pygame.display.update()
                            time.sleep(0.0001)

                            pygame.draw.rect(screen, black, (350, 150, 1000, 1000))
                            screen.blit(edp4452, (354, 154))  # fourth
                            show_text("Toggle Animation", 0, 258, white)
                            screen.blit(toggleon, (0, 290))
                            pastryHigh = c.execute("SELECT pastryHigh FROM highScores")
                            pastryHigh = c.fetchall()
                            show_text("Actuations: " + str(totala), 0, 0, white)
                            show_text("HIGH SCORE: " + str(pastryHigh[0][0]), 0, 40, white)
                            coinamt = getHubCoin(vars.user)
                            if coinamt != "none":
                                showHubCoin(vars.user, 700, 0, white)
                            pygame.display.update()
                            time.sleep(0.0001)

                            pygame.draw.rect(screen, black, (350, 150, 1000, 1000))
                            screen.blit(edp4453, (356, 155))  # third
                            show_text("Toggle Animation", 0, 258, white)
                            screen.blit(toggleon, (0, 290))
                            pastryHigh = c.execute("SELECT pastryHigh FROM highScores")
                            pastryHigh = c.fetchall()
                            show_text("Actuations: " + str(totala), 0, 0, white)
                            show_text("HIGH SCORE: " + str(pastryHigh[0][0]), 0, 40, white)
                            coinamt = getHubCoin(vars.user)
                            if coinamt != "none":
                                showHubCoin(vars.user, 700, 0, white)
                            pygame.display.update()
                            time.sleep(0.0001)

                            pygame.draw.rect(screen, black, (350, 150, 1000, 1000))
                            screen.blit(edp4454, (358, 156))  # second
                            show_text("Toggle Animation", 0, 258, white)
                            screen.blit(toggleon, (0, 290))
                            pastryHigh = c.execute("SELECT pastryHigh FROM highScores")
                            pastryHigh = c.fetchall()
                            show_text("Actuations: " + str(totala), 0, 0, white)
                            show_text("HIGH SCORE: " + str(pastryHigh[0][0]), 0, 40, white)
                            coinamt = getHubCoin(vars.user)
                            if coinamt != "none":
                                showHubCoin(vars.user, 700, 0, white)
                            pygame.display.update()
                            time.sleep(0.0001)

                            pygame.draw.rect(screen, black, (350, 150, 1000, 1000))
                            screen.blit(edp4455, (358, 156))  # first
                            show_text("Toggle Animation", 0, 258, white)
                            screen.blit(toggleon, (0, 290))
                            pastryHigh = c.execute("SELECT pastryHigh FROM highScores")
                            pastryHigh = c.fetchall()
                            show_text("Actuations: " + str(totala), 0, 0, white)
                            show_text("HIGH SCORE: " + str(pastryHigh[0][0]), 0, 40, white)
                            coinamt = getHubCoin(vars.user)
                            if coinamt != "none":
                                showHubCoin(vars.user, 700, 0, white)
                            pygame.display.update()
                            time.sleep(0.0001)

                            pygame.draw.rect(screen, black, (0, 290, 100, 100))
                            screen.blit(toggleon, (0, 290))
                            show_text("Toggle Animation", 0, 258, white)
                            show_text("Toggle Animation", 0, 258, white)
                            screen.blit(toggleon, (0, 290))
                            pastryHigh = c.execute("SELECT pastryHigh FROM highScores")
                            pastryHigh = c.fetchall()
                            show_text("Actuations: " + str(totala), 0, 0, white)
                            show_text("HIGH SCORE: " + str(pastryHigh[0][0]), 0, 40, white)
                            coinamt = getHubCoin(vars.user)
                            if coinamt != "none":
                                showHubCoin(vars.user, 700, 0, white)
                            pygame.display.update()
                            cutloop = -1
                            # end = 0

                        while end > 0 and cutloop > 0:
                            screen.blit(edp4450, (350, 150))
                            screen.blit(toggleoff, (0, 290))
                            show_text("Toggle Animation", 0, 258, white)
                            show_text("Toggle Animation", 0, 258, white)
                            pastryHigh = c.execute("SELECT pastryHigh FROM highScores")
                            pastryHigh = c.fetchall()
                            show_text("Actuations: " + str(totala), 0, 0, white)
                            show_text("HIGH SCORE: " + str(pastryHigh[0][0]), 0, 40, white)
                            coinamt = getHubCoin(vars.user)
                            if coinamt != "none":
                                showHubCoin(vars.user, 700, 0, white)
                            pygame.display.update()
                            cutloop = -1
                            # end = 0

                        if end > 0:
                            end = 1
                        else:
                            end = -1

                        # cutloop = 1
                        ##########################################################

                        show_text("Actuations: " + str(totala), 0, 0, white)
                        if totala > pastryHigh[0][0]:
                            c.execute("UPDATE highScores SET pastryHigh =" + str(totala))
                        pastryHigh = c.execute("SELECT pastryHigh FROM highScores")
                        pastryHigh = c.fetchall()
                        show_text("HIGH SCORE: " + str(pastryHigh[0][0]), 0, 40, white)
                        if coinamt != "none":
                            showHubCoin(vars.user, 700, 0, white)
                        pygame.display.update()
                if event.type == pygame.MOUSEBUTTONUP and event.button == 1:
                    xa, ya = event.pos
                    if xa >= 350 and xa <= 650 and ya >= 150 and ya <= 450:
                        while end < 0 and cutloop < 0:
                            pygame.draw.rect(screen, black, (350, 150, 1000, 1000))
                            screen.blit(edp4455, (358, 156))  # first
                            pygame.display.update()
                            time.sleep(0.0001)

                            pygame.draw.rect(screen, black, (350, 150, 1000, 1000))
                            screen.blit(edp4454, (358, 156))  # second
                            pygame.display.update()
                            time.sleep(0.0001)

                            pygame.draw.rect(screen, black, (350, 150, 1000, 1000))
                            screen.blit(edp4453, (356, 155))  # third
                            pygame.display.update()
                            time.sleep(0.0001)

                            pygame.draw.rect(screen, black, (350, 150, 1000, 1000))
                            screen.blit(edp4452, (354, 154))  # fourth
                            pygame.display.update()
                            time.sleep(0.0001)

                            pygame.draw.rect(screen, black, (350, 150, 1000, 1000))
                            screen.blit(edp4451, (353, 153))  # fifth
                            pygame.display.update()
                            time.sleep(0.0001)

                            pygame.draw.rect(screen, black, (350, 150, 1000, 1000))
                            screen.blit(edp4450, (350, 150))  # back to original
                            pygame.display.update()
                            time.sleep(0.0001)

                            pygame.draw.rect(screen, black, (0, 290, 100, 100))
                            screen.blit(toggleon, (0, 290))
                            show_text("Toggle Animation", 0, 258, white)
                            pygame.display.update()
                            cutloop = 1
                            # end = 0

                        while end > 0 and cutloop < 0:
                            screen.blit(edp4450, (350, 150))
                            screen.blit(toggleoff, (0, 290))
                            show_text("Toggle Animation", 0, 258, white)
                            pygame.display.update()
                            cutloop = 1
                            # end = 0

                        if end > 0:
                            end = 1
                        else:
                            end = -1

    if selection == 5:  ####################SKAAVOK###################
        scores = 0
        countDownScreen()
        screen.fill(black)
        skaavokHigh = c.execute("SELECT skaavokHigh FROM highScores")
        skaavokHigh = c.fetchall()
        show_text("Score: " + str(scores), 0, 0, white)
        show_text("HIGH SCORE: " + str(skaavokHigh[0][0]), 300, 0, white)
        randx = random.randint(100, 900)
        randy = random.randint(100, 500)
        pygame.draw.circle(screen, vars.color, (randx, randy), 20)
        coinamt = getHubCoin(vars.user)
        if coinamt != "none":
            showHubCoin(vars.user, 700, 0, white)
        pygame.display.update()
        start_time = pygame.time.get_ticks()
        while selection == 5:
            pygame.draw.rect(screen, black, (770, 560, 1000, 600))
            formatted_score = abs(((pygame.time.get_ticks() - start_time) / 1000) - 30)
            show_text(str(round(formatted_score, 2)), 770, 560, white)
            show_text("sec left", 870, 560, white)
            pygame.display.update()
            if (pygame.time.get_ticks() - start_time >= 30000):
                screen.fill(black)
                show_text("GAME OVER", 0, 0, white)
                pygame.display.update()
                time.sleep(2)
                screen.fill(black)
                selection = 0

                scores = 0
            for event in pygame.event.get():
                if event.type == pygame.KEYDOWN and event.key == K_ESCAPE:
                    screen.fill(black)
                    selection = 0
                    scores = 0
                    print("escape")
                if event.type == pygame.MOUSEBUTTONDOWN and event.button == 1:
                    xs, ys = event.pos
                    if math.sqrt(abs(xs - randx) ** 2 + abs(ys - randy) ** 2) <= 20:
                        pygame.mixer.Sound.play(pop)
                        screen.fill(black)
                        scores = scores + 1
                        randx = random.randint(100, 900)
                        randy = random.randint(100, 500)
                        pygame.draw.circle(screen, vars.color, (randx, randy), 20)
                        show_text("Score: " + str(scores), 0, 0, white)
                        if (scores > skaavokHigh[0][0]):
                            c.execute("UPDATE highScores SET skaavokHigh =" + str(scores))
                            conn.commit()
                        skaavokHigh = c.execute("SELECT skaavokHigh FROM highScores")
                        skaavokHigh = c.fetchall()
                        coinamt = getHubCoin(vars.user)
                        if coinamt != "none":
                            coinamt += 0.06666666
                            c.execute(f"UPDATE users SET money = '{round(coinamt, 4)}' WHERE username = '{vars.user}'")
                            conn.commit()
                            addUsers()
                        show_text("HIGH SCORE: " + str(skaavokHigh[0][0]), 300, 0, white)
                        if coinamt != "none":
                            showHubCoin(vars.user, 700, 0, white)
                        pygame.display.update()
                    else:
                        screen.fill(black)
                        scores = scores - 1
                        if scores <= 0:
                            scores = 0
                        show_text("Score: " + str(scores), 0, 0, white)
                        if coinamt != "none":
                            showHubCoin(vars.user, 700, 0, white)
                        show_text("HIGH SCORE: " + str(skaavokHigh[0][0]), 300, 0, white)
                        pygame.draw.circle(screen, vars.color, (randx, randy), 20)
                        pygame.display.update()

    if selection == 6:  #####################WORM#####################
        def crash(score1, num):
            screen.fill(black)
            show_text("Your worm died.", 480, 30, white)
            show_text("Score: " + str(score1), 490, 60, white)
            show_text("High Score: " + str(wormHigh[0][0]), 490, 90, white)
            show_text("You now have " + str(round(num, 2)) + " HubCoins", 480, 120, white)
            screen.blit(trophy, (200, 20))
            pygame.display.update()
            wormbody.clear()
            wormbody.append([500, 300])
            headpos.clear()
            headpos.append(500)
            headpos.append(300)
            scorew = 0

            time.sleep(2)


        time.sleep(0.075)
        # print(wormbody)
        wormHigh = c.execute("SELECT wormHigh FROM highScores")
        wormHigh = c.fetchall()
        screen.fill(black)
        for n in wormbody:
            pygame.draw.rect(screen, vars.color, pygame.Rect(n[0], n[1], 20, 20))
        pygame.draw.rect(screen, red, (foodx, foody, 20, 20))
        show_text("Score: " + str(scorew), 0, 0, white)
        show_text("High Score: " + str(wormHigh[0][0]), 300, 0, white)
        coinamtw = getHubCoin(vars.user)
        if coinamtw != "none":
            showHubCoin(vars.user, 700, 0, white)
        pygame.display.update()
        for event in pygame.event.get():
            if event.type == pygame.KEYDOWN:
                if event.key == K_ESCAPE:
                    screen.fill(black)
                    selection = 0
                    print("escape")
                if event.key == K_DOWN and dir != 1:
                    dir = 0
                if event.key == K_UP and dir != 0:
                    dir = 1
                if event.key == K_RIGHT and dir != 3:
                    dir = 2
                if event.key == K_LEFT and dir != 2:
                    dir = 3
        if dir == 0:
            headpos[1] += 20
        if dir == 1:
            headpos[1] -= 20
        if dir == 2:
            headpos[0] += 20
        if dir == 3:
            headpos[0] -= 20

        # print(headpos)
        wormbody.insert(0, [headpos[0], headpos[1]])
        # print(wormbody)
        # print(" ")
        if foodx == wormbody[0][0] and foody == wormbody[0][1]:
            foodx = (random.randint(0, 1000) // 20) * 20
            foody = (random.randint(0, 600) // 20) * 20
            pygame.mixer.Sound.play(yum)
            scorew += 1

            coinamtw = getHubCoin(vars.user)
            if coinamtw != "none":
                deltaw += 1.0 / 15.0
                coinamtw += deltaw
                c.execute(f"UPDATE users SET money = '{round(coinamtw, 4)}' WHERE username = '{vars.user}'")
                conn.commit()
                addUsers()
            if coinamtw != "none":
                showHubCoin(vars.user, 700, 0, white)

            if (scorew > wormHigh[0][0]):
                c.execute("UPDATE highScores SET wormHigh =" + str(scorew))
                conn.commit()
        else:
            wormbody.pop(-1)

        if headpos[0] < 0 or headpos[0] > 1000 or headpos[1] < 0 or headpos[1] > 600:
            crash(scorew, coinamtw)
            screen.fill(black)
            selection = 0
            scorew = 0

        for segment in wormbody[1:]:
            if headpos[0] == segment[0] and headpos[1] == segment[1]:
                crash(scorew, coinamtw)
                screen.fill(black)
                selection = 0
                scorew = 0
