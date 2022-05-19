import pygame
from pygame.locals import *
import random
import time
import vars

user = ''

pink = (255, 200, 200)
blue = (0, 0, 255)
green = (0, 255, 0)
black = (0, 0, 0)
white = (255, 255, 255)
orange = (255, 165, 0)
red = (255, 0, 0)
brown = (210, 105, 30)
yellow = (255, 255, 0)

x = 0
y = 0
colors = [pink, blue, green, white]
pygame.init()
screen = pygame.display.set_mode((1000, 600))
pygame.display.set_caption("GAMEHUB")
# More Logos
titleLogo = pygame.image.load("Logo/titleLogo.png")
playButton = pygame.image.load("Logo/play.png")
plays = pygame.image.load("Logo/plays.png")
nftButton = pygame.image.load("Logo/nft.png")
nfts = pygame.image.load("Logo/nfts.png")
escButton = pygame.image.load("Logo/esc.png")
sescButton = pygame.image.load("Logo/sesc.png")
soundButton = pygame.image.load("Logo/sound.png")
cheaterdetected = pygame.image.load("Logo/cheaterdetected.png")

# Button Logos
pingLogo = pygame.image.load("Logo/ping.png")
pings = pygame.image.load("Logo/pings.png")
aimLogo = pygame.image.load("Logo/aim.png")
aims = pygame.image.load("Logo/aims.png")
wormLogo = pygame.image.load("Logo/worm.png")
worms = pygame.image.load("Logo/worms.png")
pastryLogo = pygame.image.load("Logo/pastry.png")
pastrys = pygame.image.load("Logo/pastrys.png")


# Show Text
def show_text(msg, xp, yp, color):
    fontobj = pygame.font.SysFont("comicsans", 32)
    msgobj = fontobj.render(msg, False, color)
    screen.blit(msgobj, (xp, yp))


def show_text_size(msg, xp, yp, color, size):
    fontobj = pygame.font.SysFont("comicsans", size)
    msgobj = fontobj.render(msg, False, color)
    screen.blit(msgobj, (xp, yp))


def showHubCoin(usern, xp, yp, color):
    if usern != "none":
        for users in vars.users:
            if users[0] == usern:
                if users[2] % 1 != 0:
                    show_text("HubCoin: " + str(round(users[2], 2)), xp, yp, color)
                if users[2] == 0:
                    show_text("HubCoin: " + str(0), xp, yp, color)


def drawTitle():  # Title Screen
    screen.fill(black)
    screen.blit(playButton, (333, 266))
    screen.blit(nftButton, (333, 430))
    screen.blit(titleLogo, (230, 30))
    screen.blit(soundButton, (930, 530))
    showHubCoin(vars.user, 775, 0, white)
    if vars.user == "":
        show_text_size("Playing as guest.", 0, 0, white, 15)
    else:
        show_text("Hi " + vars.user + "!", 0, 0, white)
        show_text_size("User: " + vars.user, 0, 580, white, 15)
    pygame.display.update()


def titlePlay():  # Play button animation
    screen.blit(plays, (355, 286))
    screen.blit(nftButton, (333, 430))
    screen.blit(titleLogo, (230, 30))
    screen.blit(soundButton, (930, 530))
    showHubCoin(vars.user, 775, 0, white)
    if vars.user == "":
        show_text_size("Playing as guest.", 0, 0, white, 15)
    else:
        show_text("Hi " + vars.user + "!", 0, 0, white)
        show_text_size("User: " + vars.user, 0, 580, white, 15)
    pygame.display.update()


def titleNFT():  # NFT animation
    screen.fill(black)
    screen.blit(playButton, (333, 266))
    screen.blit(nfts, (355, 430))
    screen.blit(titleLogo, (230, 30))
    screen.blit(soundButton, (930, 530))
    showHubCoin(vars.user, 775, 0, white)
    if vars.user == "":
        show_text_size("Playing as guest.", 0, 0, white, 15)
    else:
        show_text("Hi " + vars.user + "!", 0, 0, white)
        show_text_size("User: " + vars.user, 0, 580, white, 15)
    pygame.display.update()


def drawTitleoff():  # Title Screen
    screen.fill(black)
    screen.blit(playButton, (333, 266))
    screen.blit(nftButton, (333, 430))
    screen.blit(titleLogo, (230, 30))
    screen.blit(soundButton, (930, 530))
    showHubCoin(vars.user, 775, 0, white)
    pygame.draw.line(screen, red, (955, 555), (995, 595), 5)
    if vars.user == "":
        show_text_size("Playing as guest.", 0, 0, white, 15)
    else:
        show_text("Hi " + vars.user + "!", 0, 0, white)
        show_text_size("User: " + vars.user, 0, 580, white, 15)
    pygame.display.update()


def titlePlayoff():  # Play button animation
    screen.blit(plays, (355, 286))
    screen.blit(nftButton, (333, 430))
    screen.blit(titleLogo, (230, 30))
    screen.blit(soundButton, (930, 530))
    showHubCoin(vars.user, 775, 0, white)
    pygame.draw.line(screen, red, (955, 555), (995, 595), 5)
    if vars.user == "":
        show_text_size("Playing as guest.", 0, 0, white, 15)
    else:
        show_text("Hi " + vars.user + "!", 0, 0, white)
        show_text_size("User: " + vars.user, 0, 580, white, 15)
    pygame.display.update()


def titleNFToff():  # NFT animation
    screen.fill(black)
    screen.blit(playButton, (333, 266))
    screen.blit(nfts, (355, 430))
    screen.blit(titleLogo, (230, 30))
    screen.blit(soundButton, (930, 530))
    showHubCoin(vars.user, 775, 0, white)
    pygame.draw.line(screen, red, (955, 555), (995, 595), 5)
    if vars.user == "":
        show_text_size("Playing as guest.", 0, 0, white, 15)
    else:
        show_text("Hi " + vars.user + "!", 0, 0, white)
        show_text_size("User: " + vars.user, 0, 580, white, 15)
    pygame.display.update()


def drawNFT():  # 333x148
    screen.fill(black)
    showHubCoin(vars.user, 775, 0, white)
    screen.blit(nfts, (345, 25))
    pygame.draw.rect(screen, brown, (55, 200, 230, 130), 10)
    pygame.draw.rect(screen, orange, (370, 200, 230, 130), 10)
    pygame.draw.rect(screen, pink, (685, 200, 230, 130), 10)
    pygame.draw.rect(screen, yellow, (55, 380, 230, 130), 10)
    pygame.draw.rect(screen, red, (370, 380, 230, 130), 10)
    pygame.draw.rect(screen, blue, (685, 380, 230, 130), 10)


def drawNFTnoaccount():
    screen.fill(black)
    show_text("Howdy! You need money to buy things!", 200, 200, white)
    show_text("Create an account to access the NFT Shop!", 200, 268, white)
    pygame.display.update()


def drawNFT0():
    screen.fill(black)
    showHubCoin(vars.user, 775, 0, white)
    screen.blit(nfts, (345, 25))
    pygame.draw.rect(screen, brown, (55, 200, 230, 130), 75)
    pygame.draw.rect(screen, orange, (370, 200, 230, 130), 10)
    pygame.draw.rect(screen, pink, (685, 200, 230, 130), 10)
    pygame.draw.rect(screen, yellow, (55, 380, 230, 130), 10)
    pygame.draw.rect(screen, red, (370, 380, 230, 130), 10)
    pygame.draw.rect(screen, blue, (685, 380, 230, 130), 10)


def drawNFT1():
    screen.fill(black)
    showHubCoin(vars.user, 775, 0, white)
    screen.blit(nfts, (345, 25))
    pygame.draw.rect(screen, brown, (55, 200, 230, 130), 10)
    pygame.draw.rect(screen, orange, (370, 200, 230, 130), 75)
    pygame.draw.rect(screen, pink, (685, 200, 230, 130), 10)
    pygame.draw.rect(screen, yellow, (55, 380, 230, 130), 10)
    pygame.draw.rect(screen, red, (370, 380, 230, 130), 10)
    pygame.draw.rect(screen, blue, (685, 380, 230, 130), 10)


def drawNFT2():
    screen.fill(black)
    showHubCoin(vars.user, 775, 0, white)
    screen.blit(nfts, (345, 25))
    pygame.draw.rect(screen, brown, (55, 200, 230, 130), 10)
    pygame.draw.rect(screen, orange, (370, 200, 230, 130), 10)
    pygame.draw.rect(screen, pink, (685, 200, 230, 130), 75)
    pygame.draw.rect(screen, yellow, (55, 380, 230, 130), 10)
    pygame.draw.rect(screen, red, (370, 380, 230, 130), 10)
    pygame.draw.rect(screen, blue, (685, 380, 230, 130), 10)


def drawNFT3():
    screen.fill(black)
    showHubCoin(vars.user, 775, 0, white)
    screen.blit(nfts, (345, 25))
    pygame.draw.rect(screen, brown, (55, 200, 230, 130), 10)
    pygame.draw.rect(screen, orange, (370, 200, 230, 130), 10)
    pygame.draw.rect(screen, pink, (685, 200, 230, 130), 10)
    pygame.draw.rect(screen, yellow, (55, 380, 230, 130), 75)
    pygame.draw.rect(screen, red, (370, 380, 230, 130), 10)
    pygame.draw.rect(screen, blue, (685, 380, 230, 130), 10)


def drawNFT4():
    screen.fill(black)
    showHubCoin(vars.user, 775, 0, white)
    screen.blit(nfts, (345, 25))
    pygame.draw.rect(screen, brown, (55, 200, 230, 130), 10)
    pygame.draw.rect(screen, orange, (370, 200, 230, 130), 10)
    pygame.draw.rect(screen, pink, (685, 200, 230, 130), 10)
    pygame.draw.rect(screen, yellow, (55, 380, 230, 130), 10)
    pygame.draw.rect(screen, red, (370, 380, 230, 130), 75)
    pygame.draw.rect(screen, blue, (685, 380, 230, 130), 10)


def drawNFT5():
    screen.fill(black)
    showHubCoin(vars.user, 775, 0, white)
    screen.blit(nfts, (345, 25))
    pygame.draw.rect(screen, brown, (55, 200, 230, 130), 10)
    pygame.draw.rect(screen, orange, (370, 200, 230, 130), 10)
    pygame.draw.rect(screen, pink, (685, 200, 230, 130), 10)
    pygame.draw.rect(screen, yellow, (55, 380, 230, 130), 10)
    pygame.draw.rect(screen, red, (370, 380, 230, 130), 10)
    pygame.draw.rect(screen, blue, (685, 380, 230, 130), 75)


def drawSelect():  # select screen
    screen.fill(black)
    screen.blit(titleLogo, (230, 30))
    screen.blit(escButton, (20, 20))
    screen.blit(pingLogo, (143, 270))
    screen.blit(aimLogo, (143, 400))
    screen.blit(pastryLogo, (572, 270))
    screen.blit(wormLogo, (572, 400))
    showHubCoin(vars.user, 775, 0, white)
    pygame.display.update()


def pingSelect():  # ping anim
    screen.fill(black)
    screen.blit(titleLogo, (230, 30))
    screen.blit(escButton, (20, 20))
    screen.blit(pings, (162, 280))
    screen.blit(aimLogo, (143, 400))
    screen.blit(pastryLogo, (572, 270))
    screen.blit(wormLogo, (572, 400))
    showHubCoin(vars.user, 775, 0, white)
    pygame.display.update()


def pastrySelect():  # pastry actuator anim
    screen.fill(black)
    screen.blit(titleLogo, (230, 30))
    screen.blit(escButton, (20, 20))
    screen.blit(pingLogo, (143, 270))
    screen.blit(aimLogo, (143, 400))
    screen.blit(pastrys, (591, 280))
    screen.blit(wormLogo, (572, 400))
    showHubCoin(vars.user, 775, 0, white)
    pygame.display.update()


def aimSelect():  # skaavok anim
    screen.fill(black)
    screen.blit(titleLogo, (230, 30))
    screen.blit(escButton, (20, 20))
    screen.blit(pingLogo, (143, 270))
    screen.blit(aims, (162, 410))
    screen.blit(pastryLogo, (572, 270))
    screen.blit(wormLogo, (572, 400))
    showHubCoin(vars.user, 775, 0, white)
    pygame.display.update()


def wormSelect():  # worm anim
    screen.fill(black)
    screen.blit(titleLogo, (230, 30))
    screen.blit(escButton, (20, 20))
    screen.blit(pingLogo, (143, 270))
    screen.blit(aimLogo, (143, 400))
    screen.blit(pastryLogo, (572, 270))
    screen.blit(worms, (591, 410))
    showHubCoin(vars.user, 775, 0, white)
    pygame.display.update()


def drawSelectEsc():  # select screen
    screen.fill(black)
    screen.blit(titleLogo, (230, 30))
    screen.blit(sescButton, (20, 20))
    screen.blit(pingLogo, (143, 270))
    screen.blit(aimLogo, (143, 400))
    screen.blit(pastryLogo, (572, 270))
    screen.blit(wormLogo, (572, 400))
    showHubCoin(vars.user, 775, 0, white)
    pygame.display.update()


def countDownScreen():  # count down
    screen.fill(black)
    # show_text_size("5", 400, 100, white, 400)
    # pygame.display.update()
    # time.sleep(1)
    # screen.fill(black)
    # show_text_size("4", 400, 100, white, 400)
    # pygame.display.update()
    # time.sleep(1)
    # screen.fill(black)
    show_text_size("3", 400, 100, white, 400)
    pygame.display.update()
    time.sleep(1)
    screen.fill(black)
    show_text_size("2", 400, 100, white, 400)
    pygame.display.update()
    time.sleep(1)
    screen.fill(black)
    show_text_size("1", 400, 100, white, 400)
    pygame.display.update()
    time.sleep(1)
    screen.fill(black)
    show_text_size("GO", 450, 100, white, 400)
    pygame.display.update()
    time.sleep(1)


def banscreen():
    screen.fill(black)
    screen.blit(cheaterdetected, (0, 0))
    pygame.display.update()


def leaderboard():
    show_text_size("Leaderboard", 300, 25, white, 69)

    #show top 10 networth
    show_text_size("Number 1", 430, 100, white, 40)
    show_text_size("Number 2", 450, 150, white, 30)
    show_text_size("Number 3", 450, 175, white, 30)
    show_text_size("Number 4", 450, 200, white, 30)
    show_text_size("Number 5", 450, 225, white, 30)
    show_text_size("Number 6", 450, 250, white, 30)
    show_text_size("Number 7", 450, 275, white, 30)
    show_text_size("Number 8", 450, 300, white, 30)
    show_text_size("Number 9", 450, 325, white, 30)
    show_text_size("Number 10", 450, 350, white, 30)


    show_text_size("My net worth", 450, 425, white, 30) #This one shows your net worth and ranking if you're not top 10


    pygame.display.update()

