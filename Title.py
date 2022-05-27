import pygame
from pygame.locals import *
import random
import time
import vars

pygame.init()
user = ''
comicsans = pygame.font.Font("fonts/COMIC.TTF", 32)
pink = (255, 200, 200)
blue = (0, 0, 255)
green = (0, 255, 0)
black = (0, 0, 0)
white = (255, 255, 255)
orange = (255, 165, 0)
red = (255, 0, 0)
brown = (210, 105, 30)
yellow = (255, 255, 0)
weed = (75, 155, 74)

x = 0
y = 0
colors = [pink, blue, green, white]
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
coin = pygame.image.load("coin/coin.png")

# Button Logos
pingLogo = pygame.image.load("Logo/ping.png")
pings = pygame.image.load("Logo/pings.png")
aimLogo = pygame.image.load("Logo/aim.png")
aims = pygame.image.load("Logo/aims.png")
wormLogo = pygame.image.load("Logo/worm.png")
worms = pygame.image.load("Logo/worms.png")
pastryLogo = pygame.image.load("Logo/pastry.png")
pastrys = pygame.image.load("Logo/pastrys.png")
leaderboards = pygame.image.load("Logo/leaderboard.png")
help = pygame.image.load("Logo/help button.png")
sleaderboard = pygame.image.load("Logo/sleaderboard.png")
shelp = pygame.image.load("Logo/shelp button.png")
equip = pygame.image.load("Logo/equip.png")
purchase = pygame.image.load("Logo/purchase.png")


# Show Text
def show_text(msg, xp, yp, color):
    fontobj = pygame.font.Font("fonts/COMIC.TTF", 21)
    msgobj = fontobj.render(msg, False, color)
    screen.blit(msgobj, (xp, yp))


def show_text_size(msg, xp, yp, color, size):
    size = int(size/1.5)
    fontobj = pygame.font.Font("fonts/COMIC.TTF", size)
    msgobj = fontobj.render(msg, False, color)
    screen.blit(msgobj, (xp, yp))

def displayHubCoin(msg, xh, yh, color):
    show_text(msg, xh + 28, yh - 3, color)
    screen.blit(coin, (xh, yh))

def displayprice():
    displayHubCoin("3.50", 135, 295, weed)
    displayHubCoin("100", 450, 295, weed)
    displayHubCoin("69", 770, 295, weed)
    displayHubCoin("75", 770, 475, weed)
    displayHubCoin("50", 450, 475, weed)
    displayHubCoin("420", 135, 475, weed)

def showHubCoin(usern, xhc, yhc, color):
    if usern != "none":
        for users in vars.users:
            if users[0] == usern:
                if users[2] % 1 != 0:
                    show_text(str(round(users[2], 2)), xhc, yhc+2, color)
                    screen.blit(coin, (xhc-28, yhc + 3))
                else:
                    show_text(str(round(users[2], 2)), xhc, yhc+2, color)
                    screen.blit(coin, (xhc-28, yhc + 3))
                if users[2] == 0:
                    show_text(str(0), xhc, yhc+2, color)
                    screen.blit(coin, (xhc-28, yhc + 3))


def drawTitle():  # Title Screen
    pygame.draw.rect(screen, white, (0,0, 1000, 600), 2)
    screen.blit(playButton, (333, 266))
    screen.blit(nftButton, (333, 430))
    screen.blit(titleLogo, (230, 30))
    screen.blit(soundButton, (935, 540))
    screen.blit(leaderboards, (5, 565))
    screen.blit(help, (120, 565))
    showHubCoin(vars.user, 775, 3, white)
    if vars.user == "":
        show_text_size("Playing as guest.", 3, 3, white, 20)
    else:
        show_text("Hi " + vars.user + "!", 3, 3, white)
    pygame.display.update()

def titleHelp():
    screen.fill(black)
    pygame.draw.rect(screen, white, (0,0, 1000, 600), 2)
    screen.blit(playButton, (333, 266))
    screen.blit(nftButton, (333, 430))
    screen.blit(titleLogo, (230, 30))
    screen.blit(soundButton, (935, 540))
    screen.blit(leaderboards, (5, 565))
    screen.blit(shelp, (129, 567))
    showHubCoin(vars.user, 775, 3, white)
    if vars.user == "":
        show_text_size("Playing as guest.", 3, 3, white, 20)
    else:
        show_text("Hi " + vars.user + "!", 3, 3, white)
    pygame.display.update()

def titleHelpv():
    screen.fill(black)
    pygame.draw.rect(screen, white, (0,0, 1000, 600), 2)
    screen.blit(playButton, (333, 266))
    screen.blit(nftButton, (333, 430))
    screen.blit(titleLogo, (230, 30))
    screen.blit(soundButton, (935, 540))
    screen.blit(leaderboards, (5, 565))
    screen.blit(shelp, (129, 567))
    pygame.draw.line(screen, red, (935, 540), (985, 580), 6)
    showHubCoin(vars.user, 775, 3, white)
    if vars.user == "":
        show_text_size("Playing as guest.", 3, 3, white, 20)
    else:
        show_text("Hi " + vars.user + "!", 3, 3, white)
    pygame.display.update()
  
def titleLeaderboard():
    screen.fill(black)
    pygame.draw.rect(screen, white, (0,0, 1000, 600), 2)
    screen.blit(playButton, (333, 266))
    screen.blit(nftButton, (333, 430))
    screen.blit(titleLogo, (230, 30))
    screen.blit(soundButton, (935, 540))
    screen.blit(sleaderboard, (15, 567))
    screen.blit(help, (120, 565))
    showHubCoin(vars.user, 775, 3, white)
    if vars.user == "":
        show_text_size("Playing as guest.", 3, 3, white, 20)
    else:
        show_text("Hi " + vars.user + "!", 3, 3, white)
    pygame.display.update()

def titleLeaderboardv():
    screen.fill(black)
    pygame.draw.rect(screen, white, (0,0, 1000, 600), 2)
    screen.blit(playButton, (333, 266))
    screen.blit(nftButton, (333, 430))
    screen.blit(titleLogo, (230, 30))
    screen.blit(soundButton, (935, 540))
    screen.blit(sleaderboard, (15, 567))
    screen.blit(help, (120, 565))
    pygame.draw.line(screen, red, (935, 540), (985, 580), 6)
    showHubCoin(vars.user, 775, 3, white)
    if vars.user == "":
        show_text_size("Playing as guest.", 3, 3, white, 20)
    else:
        show_text("Hi " + vars.user + "!", 3, 3, white)
    pygame.display.update()


def titlePlay():  # Play button animation
    screen.blit(plays, (355, 280))
    pygame.draw.rect(screen, white, (0,0, 1000, 600), 2)
    screen.blit(nftButton, (333, 430))
    screen.blit(titleLogo, (230, 30))
    screen.blit(soundButton, (935, 540))
    screen.blit(leaderboards, (5, 565))     
    screen.blit(help, (120, 565))
    showHubCoin(vars.user, 775, 3, white)
    if vars.user == "":
        show_text_size("Playing as guest.", 3, 3, white, 20)
    else:
        show_text("Hi " + vars.user + "!", 3, 3, white)
    pygame.display.update()


def titleNFT():  # NFT animation
    pygame.draw.rect(screen, white, (0,0, 1000, 600), 2)
    screen.blit(playButton, (333, 266))
    screen.blit(nfts, (355, 430))
    screen.blit(titleLogo, (230, 30))
    screen.blit(soundButton, (935, 540))
    screen.blit(leaderboards, (5, 565))     
    screen.blit(help, (120, 565))
    showHubCoin(vars.user, 775, 3, white)
    if vars.user == "":
        show_text_size("Playing as guest.", 3, 3, white, 20)
    else:
        show_text("Hi " + vars.user + "!", 3, 3, white)
    pygame.display.update()


def drawTitleoff():  # Title Screen
    pygame.draw.rect(screen, white, (0,0, 1000, 600), 2)
    screen.blit(playButton, (333, 266))
    screen.blit(nftButton, (333, 430))
    screen.blit(titleLogo, (230, 30))
    screen.blit(soundButton, (935, 540))
    showHubCoin(vars.user, 775, 3, white)
    screen.blit(leaderboards, (5, 565))     
    screen.blit(help, (120, 565))
    pygame.draw.line(screen, red, (935, 540), (985, 580), 6)
    if vars.user == "":
        show_text_size("Playing as guest.", 3, 3, white, 20)
    else:
        show_text("Hi " + vars.user + "!", 3, 3, white)
    pygame.display.update()


def titlePlayoff():  # Play button animation
    screen.blit(plays, (355, 280))
    pygame.draw.rect(screen, white, (0,0, 1000, 600), 2)
    screen.blit(nftButton, (333, 430))
    screen.blit(titleLogo, (230, 30))
    screen.blit(soundButton, (935, 540))
    showHubCoin(vars.user, 775, 3, white)
    screen.blit(leaderboards, (5, 565))     
    screen.blit(help, (120, 565))
    pygame.draw.line(screen, red, (935, 540), (985, 580), 6)
    if vars.user == "":
        show_text_size("Playing as guest.", 3, 3, white, 20)
    else:
        show_text("Hi " + vars.user + "!", 3, 3, white)
    pygame.display.update()


def titleNFToff():  # NFT animation
    pygame.draw.rect(screen, white, (0,0, 1000, 600), 2)
    screen.blit(playButton, (333, 266))
    screen.blit(nfts, (355, 430))
    screen.blit(titleLogo, (230, 30))
    screen.blit(soundButton, (935, 540))
    showHubCoin(vars.user, 775, 3, white)
    screen.blit(leaderboards, (5, 565))     
    screen.blit(help, (120, 565))
    pygame.draw.line(screen, red, (935, 540), (985, 580), 6)
    if vars.user == "":
        show_text_size("Playing as guest.", 3, 3, white, 20)
    else:
        show_text("Hi " + vars.user + "!", 3, 3, white)
    pygame.display.update()

def drawNFT():
    screen.fill(black)
    pygame.draw.rect(screen, white, (0,0, 1000, 600), 2)
    showHubCoin(vars.user, 775, 3, white)
    screen.blit(nfts, (345, 25))
    screen.blit(escButton, (20, 20))
    displayprice()
    pygame.draw.rect(screen, brown, (55, 200, 230, 130), 10)
    pygame.draw.rect(screen, orange, (370, 200, 230, 130), 10)
    pygame.draw.rect(screen, pink, (685, 200, 230, 130), 10)
    pygame.draw.rect(screen, yellow, (55, 380, 230, 130), 10)
    pygame.draw.rect(screen, red, (370, 380, 230, 130), 10)
    pygame.draw.rect(screen, blue, (685, 380, 230, 130), 10)
    displayprice()
    pygame.display.update()

def drawNFTesc():
    screen.fill(black)
    pygame.draw.rect(screen, white, (0,0, 1000, 600), 2)
    showHubCoin(vars.user, 775, 3, white)
    screen.blit(nfts, (345, 25))
    screen.blit(sescButton, (20, 20))
    displayprice()
    pygame.draw.rect(screen, brown, (55, 200, 230, 130), 10)
    pygame.draw.rect(screen, orange, (370, 200, 230, 130), 10)
    pygame.draw.rect(screen, pink, (685, 200, 230, 130), 10)
    pygame.draw.rect(screen, yellow, (55, 380, 230, 130), 10)
    pygame.draw.rect(screen, red, (370, 380, 230, 130), 10)
    pygame.draw.rect(screen, blue, (685, 380, 230, 130), 10)
    displayprice()
    pygame.display.update()

def drawNFTnoaccount():
    screen.fill(black)
    screen.blit(escButton, (20, 20))
    pygame.draw.rect(screen, white, (0,0, 1000, 600), 2)
    show_text("Howdy! You need money to buy things!", 200, 200, white)
    show_text("Create an account to access the NFT Shop!", 200, 268, white)
    pygame.display.update()

def drawNFTnoaccountesc():
    screen.fill(black)
    screen.blit(sescButton, (20, 20))
    pygame.draw.rect(screen, white, (0,0, 1000, 600), 2)
    show_text("Howdy! You need money to buy things!", 200, 200, white)
    show_text("Create an account to access the NFT Shop!", 200, 268, white)
    pygame.display.update()

def drawNFT0():
    screen.fill(black)
    pygame.draw.rect(screen, white, (0,0, 1000, 600), 2)
    showHubCoin(vars.user, 775, 3, white)
    screen.blit(nfts, (345, 25))
    screen.blit(escButton, (20, 20))
    displayprice()
    pygame.draw.rect(screen, brown, (55, 200, 230, 130), 75)
    pygame.draw.rect(screen, orange, (370, 200, 230, 130), 10)
    pygame.draw.rect(screen, pink, (685, 200, 230, 130), 10)
    pygame.draw.rect(screen, yellow, (55, 380, 230, 130), 10)
    pygame.draw.rect(screen, red, (370, 380, 230, 130), 10)
    pygame.draw.rect(screen, blue, (685, 380, 230, 130), 10)
    screen.blit(purchase, (450, 530))
    displayprice()
    pygame.display.update()

def drawNFT0esc():
    screen.fill(black)
    pygame.draw.rect(screen, white, (0,0, 1000, 600), 2)
    showHubCoin(vars.user, 775, 3, white)
    screen.blit(nfts, (345, 25))
    screen.blit(sescButton, (20, 20))
    displayprice()
    pygame.draw.rect(screen, brown, (55, 200, 230, 130), 75)
    pygame.draw.rect(screen, orange, (370, 200, 230, 130), 10)
    pygame.draw.rect(screen, pink, (685, 200, 230, 130), 10)
    pygame.draw.rect(screen, yellow, (55, 380, 230, 130), 10)
    pygame.draw.rect(screen, red, (370, 380, 230, 130), 10)
    pygame.draw.rect(screen, blue, (685, 380, 230, 130), 10)
    screen.blit(purchase, (450, 530))
    displayprice()
    pygame.display.update()

def drawNFT1():
    screen.fill(black)
    pygame.draw.rect(screen, white, (0,0, 1000, 600), 2)
    showHubCoin(vars.user, 775, 3, white)
    screen.blit(nfts, (345, 25))
    screen.blit(escButton, (20, 20))
    displayprice()
    pygame.draw.rect(screen, brown, (55, 200, 230, 130), 10)
    pygame.draw.rect(screen, orange, (370, 200, 230, 130), 75)
    pygame.draw.rect(screen, pink, (685, 200, 230, 130), 10)
    pygame.draw.rect(screen, yellow, (55, 380, 230, 130), 10)
    pygame.draw.rect(screen, red, (370, 380, 230, 130), 10)
    pygame.draw.rect(screen, blue, (685, 380, 230, 130), 10)
    screen.blit(purchase, (450, 530))
    displayprice()
    pygame.display.update()

def drawNFT1esc():
    screen.fill(black)
    pygame.draw.rect(screen, white, (0,0, 1000, 600), 2)
    showHubCoin(vars.user, 775, 3, white)
    screen.blit(nfts, (345, 25))
    screen.blit(sescButton, (20, 20))
    displayprice()
    pygame.draw.rect(screen, brown, (55, 200, 230, 130), 10)
    pygame.draw.rect(screen, orange, (370, 200, 230, 130), 75)
    pygame.draw.rect(screen, pink, (685, 200, 230, 130), 10)
    pygame.draw.rect(screen, yellow, (55, 380, 230, 130), 10)
    pygame.draw.rect(screen, red, (370, 380, 230, 130), 10)
    pygame.draw.rect(screen, blue, (685, 380, 230, 130), 10)
    screen.blit(purchase, (450, 530))
    displayprice()
    pygame.display.update()

def drawNFT2():
    screen.fill(black)
    pygame.draw.rect(screen, white, (0,0, 1000, 600), 2)
    showHubCoin(vars.user, 775, 3, white)
    screen.blit(nfts, (345, 25))
    screen.blit(escButton, (20, 20))
    displayprice()
    pygame.draw.rect(screen, brown, (55, 200, 230, 130), 10)
    pygame.draw.rect(screen, orange, (370, 200, 230, 130), 10)
    pygame.draw.rect(screen, pink, (685, 200, 230, 130), 75)
    pygame.draw.rect(screen, yellow, (55, 380, 230, 130), 10)
    pygame.draw.rect(screen, red, (370, 380, 230, 130), 10)
    pygame.draw.rect(screen, blue, (685, 380, 230, 130), 10)
    screen.blit(purchase, (450, 530))
    displayprice()
    pygame.display.update()

def drawNFT2esc():
    screen.fill(black)
    pygame.draw.rect(screen, white, (0,0, 1000, 600), 2)
    showHubCoin(vars.user, 775, 3, white)
    screen.blit(nfts, (345, 25))
    screen.blit(sescButton, (20, 20))
    displayprice()
    pygame.draw.rect(screen, brown, (55, 200, 230, 130), 10)
    pygame.draw.rect(screen, orange, (370, 200, 230, 130), 10)
    pygame.draw.rect(screen, pink, (685, 200, 230, 130), 75)
    pygame.draw.rect(screen, yellow, (55, 380, 230, 130), 10)
    pygame.draw.rect(screen, red, (370, 380, 230, 130), 10)
    pygame.draw.rect(screen, blue, (685, 380, 230, 130), 10)
    screen.blit(purchase, (450, 530))
    displayprice()
    pygame.display.update()

def drawNFT3():
    screen.fill(black)
    pygame.draw.rect(screen, white, (0,0, 1000, 600), 2)
    showHubCoin(vars.user, 775, 3, white)
    screen.blit(nfts, (345, 25))
    screen.blit(escButton, (20, 20))
    displayprice()
    pygame.draw.rect(screen, brown, (55, 200, 230, 130), 10)
    pygame.draw.rect(screen, orange, (370, 200, 230, 130), 10)
    pygame.draw.rect(screen, pink, (685, 200, 230, 130), 10)
    pygame.draw.rect(screen, yellow, (55, 380, 230, 130), 75)
    pygame.draw.rect(screen, red, (370, 380, 230, 130), 10)
    pygame.draw.rect(screen, blue, (685, 380, 230, 130), 10)
    screen.blit(purchase, (450, 530))
    displayprice()
    pygame.display.update()

def drawNFT3esc():
    screen.fill(black)
    pygame.draw.rect(screen, white, (0,0, 1000, 600), 2)
    showHubCoin(vars.user, 775, 3, white)
    screen.blit(nfts, (345, 25))
    screen.blit(sescButton, (20, 20))
    displayprice()
    pygame.draw.rect(screen, brown, (55, 200, 230, 130), 10)
    pygame.draw.rect(screen, orange, (370, 200, 230, 130), 10)
    pygame.draw.rect(screen, pink, (685, 200, 230, 130), 10)
    pygame.draw.rect(screen, yellow, (55, 380, 230, 130), 75)
    pygame.draw.rect(screen, red, (370, 380, 230, 130), 10)
    pygame.draw.rect(screen, blue, (685, 380, 230, 130), 10)
    screen.blit(purchase, (450, 530))
    displayprice()
    pygame.display.update()

def drawNFT4():
    screen.fill(black)
    pygame.draw.rect(screen, white, (0,0, 1000, 600), 2)
    showHubCoin(vars.user, 775, 3, white)
    screen.blit(nfts, (345, 25))
    screen.blit(escButton, (20, 20))
    displayprice()
    pygame.draw.rect(screen, brown, (55, 200, 230, 130), 10)
    pygame.draw.rect(screen, orange, (370, 200, 230, 130), 10)
    pygame.draw.rect(screen, pink, (685, 200, 230, 130), 10)
    pygame.draw.rect(screen, yellow, (55, 380, 230, 130), 10)
    pygame.draw.rect(screen, red, (370, 380, 230, 130), 75)
    pygame.draw.rect(screen, blue, (685, 380, 230, 130), 10)
    screen.blit(purchase, (450, 530))
    displayprice()
    pygame.display.update()

def drawNFT4esc():
    screen.fill(black)
    pygame.draw.rect(screen, white, (0,0, 1000, 600), 2)
    showHubCoin(vars.user, 775, 3, white)
    screen.blit(nfts, (345, 25))
    screen.blit(sescButton, (20, 20))
    displayprice()
    pygame.draw.rect(screen, brown, (55, 200, 230, 130), 10)
    pygame.draw.rect(screen, orange, (370, 200, 230, 130), 10)
    pygame.draw.rect(screen, pink, (685, 200, 230, 130), 10)
    pygame.draw.rect(screen, yellow, (55, 380, 230, 130), 10)
    pygame.draw.rect(screen, red, (370, 380, 230, 130), 75)
    pygame.draw.rect(screen, blue, (685, 380, 230, 130), 10)
    screen.blit(purchase, (450, 530))
    displayprice()
    pygame.display.update()

def drawNFT5():
    screen.fill(black)
    pygame.draw.rect(screen, white, (0,0, 1000, 600), 2)
    showHubCoin(vars.user, 775, 3, white)
    screen.blit(nfts, (345, 25))
    screen.blit(escButton, (20, 20))
    displayprice()
    pygame.draw.rect(screen, brown, (55, 200, 230, 130), 10)
    pygame.draw.rect(screen, orange, (370, 200, 230, 130), 10)
    pygame.draw.rect(screen, pink, (685, 200, 230, 130), 10)
    pygame.draw.rect(screen, yellow, (55, 380, 230, 130), 10)
    pygame.draw.rect(screen, red, (370, 380, 230, 130), 10)
    pygame.draw.rect(screen, blue, (685, 380, 230, 130), 75)
    screen.blit(purchase, (450, 530))
    displayprice()
    pygame.display.update()

def drawNFT5esc():
    screen.fill(black)
    pygame.draw.rect(screen, white, (0,0, 1000, 600), 2)
    showHubCoin(vars.user, 775, 3, white)
    screen.blit(nfts, (345, 25))
    screen.blit(sescButton, (20, 20))
    displayprice()
    pygame.draw.rect(screen, brown, (55, 200, 230, 130), 10)
    pygame.draw.rect(screen, orange, (370, 200, 230, 130), 10)
    pygame.draw.rect(screen, pink, (685, 200, 230, 130), 10)
    pygame.draw.rect(screen, yellow, (55, 380, 230, 130), 10)
    pygame.draw.rect(screen, red, (370, 380, 230, 130), 10)
    pygame.draw.rect(screen, blue, (685, 380, 230, 130), 75)
    screen.blit(purchase, (450, 530))
    displayprice()
    pygame.display.update()

def drawSelect():  # select screen
    screen.fill(black)
    pygame.draw.rect(screen, white, (0,0, 1000, 600), 2)
    screen.blit(titleLogo, (230, 30))
    screen.blit(escButton, (20, 20))
    screen.blit(pingLogo, (143, 270))
    screen.blit(aimLogo, (143, 400))
    screen.blit(pastryLogo, (572, 270))
    screen.blit(wormLogo, (572, 400))
    showHubCoin(vars.user, 775, 3, white)
    pygame.display.update()

def pingSelect():  # ping anim
    screen.fill(black)
    pygame.draw.rect(screen, white, (0,0, 1000, 600), 2)
    screen.blit(titleLogo, (230, 30))
    screen.blit(escButton, (20, 20))
    screen.blit(pings, (162, 280))
    screen.blit(aimLogo, (143, 400))
    screen.blit(pastryLogo, (572, 270))
    screen.blit(wormLogo, (572, 400))
    showHubCoin(vars.user, 775, 3, white)
    pygame.display.update()

def pastrySelect():  # pastry actuator anim
    screen.fill(black)
    pygame.draw.rect(screen, white, (0,0, 1000, 600), 2)
    screen.blit(titleLogo, (230, 30))
    screen.blit(escButton, (20, 20))
    screen.blit(pingLogo, (143, 270))
    screen.blit(aimLogo, (143, 400))
    screen.blit(pastrys, (591, 280))
    screen.blit(wormLogo, (572, 400))
    showHubCoin(vars.user, 775, 3, white)
    pygame.display.update()

def aimSelect():  # skaavok anim
    screen.fill(black)
    pygame.draw.rect(screen, white, (0,0, 1000, 600),2)
    screen.blit(titleLogo, (230, 30))
    screen.blit(escButton, (20, 20))
    screen.blit(pingLogo, (143, 270))
    screen.blit(aims, (162, 410))
    screen.blit(pastryLogo, (572, 270))
    screen.blit(wormLogo, (572, 400))
    showHubCoin(vars.user, 775, 3, white)
    pygame.display.update()

def wormSelect():  # worm anim
    screen.fill(black)
    pygame.draw.rect(screen, white, (0,0, 1000, 600),2)
    screen.blit(titleLogo, (230, 30))
    screen.blit(escButton, (20, 20))
    screen.blit(pingLogo, (143, 270))
    screen.blit(aimLogo, (143, 400))
    screen.blit(pastryLogo, (572, 270))
    screen.blit(worms, (591, 410))
    showHubCoin(vars.user, 775, 3, white)
    pygame.display.update()

def drawSelectEsc():  # select screen
    screen.fill(black)
    pygame.draw.rect(screen, white, (0,0, 1000, 600),2)
    screen.blit(titleLogo, (230, 30))
    screen.blit(sescButton, (20, 20))
    screen.blit(pingLogo, (143, 270))
    screen.blit(aimLogo, (143, 400))
    screen.blit(pastryLogo, (572, 270))
    screen.blit(wormLogo, (572, 400))
    showHubCoin(vars.user, 775, 3, white)
    pygame.display.update()

def countDownScreen():  # count down
    screen.fill(black)
    pygame.draw.rect(screen, white, (0,0, 1000, 600),2)
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
    show_text_size("1", 425, 100, white, 400)
    pygame.display.update()
    time.sleep(1)
    screen.fill(black)
    show_text_size("GO", 325, 100, white, 400)
    pygame.display.update()
    time.sleep(1)

def banscreen():
    screen.fill(black)
    pygame.draw.rect(screen, white, (0,0, 1000, 600),2)
    screen.blit(cheaterdetected, (0, 0))
    pygame.display.update()

def leaderboard():
    screen.fill(black)
    screen.blit(escButton, (20, 20))
    pygame.draw.rect(screen, white, (0,0, 1000, 600),2)
    show_text_size("Leaderboard", 380, 25, white, 69)
    #show top 10 networth
    show_text_size("1. " + str(vars.sorted[0][0]) + " - " + str(vars.sorted[0][2]) + " Hub Coin", 330, 100, white, 40)
    show_text_size("2. " + str(vars.sorted[1][0]) + " - " + str(vars.sorted[1][2]) + " Hub Coin", 350, 150, white, 30)
    show_text_size("3. " + str(vars.sorted[2][0]) + " - " + str(vars.sorted[2][2]) + " Hub Coin", 350, 175, white, 30)
    show_text_size("4. " + str(vars.sorted[3][0]) + " - " + str(vars.sorted[3][2]) + " Hub Coin", 350, 200, white, 30)
    show_text_size("5. " + str(vars.sorted[4][0]) + " - " + str(vars.sorted[4][2]) + " Hub Coin", 350, 225, white, 30)
    show_text_size("6. " + str(vars.sorted[5][0]) + " - " + str(vars.sorted[5][2]) + " Hub Coin", 350, 250, white, 30)
    show_text_size("7. " + str(vars.sorted[6][0]) + " - " + str(vars.sorted[6][2]) + " Hub Coin", 350, 275, white, 30)
    show_text_size("8. " + str(vars.sorted[7][0]) + " - " + str(vars.sorted[7][2]) + " Hub Coin", 350, 300, white, 30)
    show_text_size("9. " + str(vars.sorted[8][0]) + " - " + str(vars.sorted[8][2]) + " Hub Coin", 350, 325, white, 30)
    show_text_size("10. " + str(vars.sorted[9][0]) + " - " + str(vars.sorted[9][2]) + " Hub Coin", 350, 350, white, 30)
    moneys = 0.0
    for user in vars.users:
        if user[0] == vars.user:
            moneys = user[2]
    if vars.user != '':
        show_text_size(str(vars.user) + ": " + str(moneys), 450, 425, white, 30) #This one shows your net worth and ranking if you're not top 10
    pygame.display.update()

def leaderboardesc():
    screen.blit(sescButton, (20, 20))
    pygame.draw.rect(screen, white, (0,0, 1000, 600),2)
    show_text_size("Leaderboard", 380, 25, white, 69)
    #show top 10 networth
    show_text_size("1. " + str(vars.sorted[0][0]) + " - " + str(vars.sorted[0][2]) + " Hub Coin", 330, 100, white, 40)
    show_text_size("2. " + str(vars.sorted[1][0]) + " - " + str(vars.sorted[1][2]) + " Hub Coin", 350, 150, white, 30)
    show_text_size("3. " + str(vars.sorted[2][0]) + " - " + str(vars.sorted[2][2]) + " Hub Coin", 350, 175, white, 30)
    show_text_size("4. " + str(vars.sorted[3][0]) + " - " + str(vars.sorted[3][2]) + " Hub Coin", 350, 200, white, 30)
    show_text_size("5. " + str(vars.sorted[4][0]) + " - " + str(vars.sorted[4][2]) + " Hub Coin", 350, 225, white, 30)
    show_text_size("6. " + str(vars.sorted[5][0]) + " - " + str(vars.sorted[5][2]) + " Hub Coin", 350, 250, white, 30)
    show_text_size("7. " + str(vars.sorted[6][0]) + " - " + str(vars.sorted[6][2]) + " Hub Coin", 350, 275, white, 30)
    show_text_size("8. " + str(vars.sorted[7][0]) + " - " + str(vars.sorted[7][2]) + " Hub Coin", 350, 300, white, 30)
    show_text_size("9. " + str(vars.sorted[8][0]) + " - " + str(vars.sorted[8][2]) + " Hub Coin", 350, 325, white, 30)
    show_text_size("10. " + str(vars.sorted[9][0]) + " - " + str(vars.sorted[9][2]) + " Hub Coin", 350, 350, white, 30)
    moneys = 0.0
    for user in vars.users:
        if user[0] == vars.user:
            moneys = user[2]
    if vars.user != '':
        show_text_size(str(vars.user) + ": " + str(moneys), 450, 425, white, 30) #This one shows your net worth and ranking if you're not top 10
    pygame.display.update()

def drawHelp():
    screen.fill(black)
    #pygame.mixer.music.load("Music/angrychong.mp3")
    #pygame.mixer.music.play(0)
    screen.blit(escButton, (20, 20))
    pygame.draw.rect(screen, white, (0,0, 1000, 600),2)
    show_text_size("Help", 380, 25, white, 69)
    show_text_size("Ping", 24, 100, white, 45)
    show_text("This is a two-player game. It functions just like the popular game Pong.", 25, 130, white)
    show_text_size("Pastry Actuator", 24, 180, white, 45)
    show_text("This is a single player game where you click on the cupcake to gain clicks. Each 500 clicks ", 24, 210, white)
    show_text("is worth 1 HubCoin. ", 24, 235, white)

    show_text_size("S'kaavok", 24, 285, white, 45)
    show_text("This is a single player game where the goal is to click the targets as fast as you can before ", 24, 310, white)
    show_text("the time runs out. Every 15 targets hit in Sk'aavok gives 1 hub coin.", 24, 335, white)

    show_text_size("Worm", 24, 385, white, 45)
    show_text("This game is based on the popular game called Snake. You control a worm like object and ", 24, 410, white)
    show_text("eat as many apples as you can. Each time you eat an apple, the worm grows in length. Use the ", 24, 435, white)
    show_text("arrow keys to control your worm. If you run into yourself or hit the wall you will die.", 24, 460, white)
    show_text("Press [ESC] to close this window.", 450, 550, white)
    pygame.display.update()

def drawHelpesc():
    screen.fill(black)
    screen.blit(sescButton, (20, 20))
    pygame.draw.rect(screen, white, (0,0, 1000, 600),2)
    show_text_size("Help", 380, 25, white, 69)
  
    show_text_size("Ping", 24, 100, white, 45)
    show_text("This is a two-player game. It functions just like the popular game Pong.", 25, 130, white)
    show_text_size("Pastry Actuator", 24, 180, white, 45)
    show_text("This is a single player game where you click on the cupcake to gain clicks. Each 500 clicks ", 24, 210, white)
    show_text("is worth 1 HubCoin. ", 24, 235, white)

    show_text_size("S'kaavok", 24, 285, white, 45)
    show_text("This is a single player game where the goal is to click the targets as fast as you can before ", 24, 310, white)
    show_text("the time runs out. Every 15 targets hit in Sk'aavok gives 1 hub coin.", 24, 335, white)

    show_text_size("Worm", 24, 385, white, 45)
    show_text("This game is based on the popular game called Snake. You control a worm like object and ", 24, 410, white)
    show_text("eat as many apples as you can. Each time you eat an apple, the worm grows in length. Use the ", 24, 435, white)
    show_text("arrow keys to control your worm. If you run into yourself or hit the wall you will die.", 24, 460, white)
    show_text("Press [ESC] to close this window.", 450, 550, white)
    pygame.display.update()

 
