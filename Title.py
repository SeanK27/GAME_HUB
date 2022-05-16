import pygame
from pygame.locals import*
import random
import time
import vars

user = ''


pink = (255,200,200)
blue = (0,0,255)
green = (0,255,0)
black = (0,0,0)
white = (255,255,255)
orange = (255,165,0)
red = (255,0,0)

x=0
y=0
colors=[pink,blue,green,white]
pygame.init()
screen = pygame.display.set_mode((1000,600)) 
pygame.display.set_caption("GAMEHUB")
#More Logos
titleLogo = pygame.image.load("Logo/titleLogo.png")
playButton = pygame.image.load("Logo/play.png")
nftButton = pygame.image.load("Logo/nft.png")
escButton = pygame.image.load("Logo/esc.png")
sescButton = pygame.image.load("Logo/sesc.png")
soundButton = pygame.image.load("Logo/sound.png")
cheaterdetected = pygame.image.load("Logo/cheaterdetected.png")

#Button Logos
pingLogo = pygame.image.load("Logo/ping.png")
aimLogo = pygame.image.load("Logo/aim.png")
wormLogo = pygame.image.load("Logo/worm.png")
pastryLogo = pygame.image.load("Logo/pastry.png")

#Show Text
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
                if users[2]%1 != 0:
                    show_text("HubCoin: " + str(round(users[2])), xp, yp, color)
                if users[2] == 0:
                    show_text("HubCoin: " + str(0), xp, yp, color)
                else:
                    show_text("HubCoin: " + str(users[2]), xp, yp, color)

def drawTitle(): #Title Screen
  screen.fill(black)
  screen.blit(playButton, (333,266))
  screen.blit(nftButton, (333,430))
  screen.blit(titleLogo, (250, 30))
  screen.blit(soundButton, (950, 550))
  showHubCoin(vars.user, 800, 0, white)
  if vars.user == "":
    show_text_size("Playing as guest.", 0, 0, white, 15)
  else:
    show_text("Hi " + vars.user + "!", 0, 0, white)
  pygame.display.update()

def titlePlay(): #Play button animation
  pygame.display.set_caption("window")
  screen.blit(playButton, (338, 271))
  screen.blit(nftButton, (333, 430))
  screen.blit(titleLogo, (250, 30))
  screen.blit(soundButton, (950, 550))
  showHubCoin(vars.user, 800, 0, white)
  if vars.user == "":
    show_text_size("Playing as guest.", 0, 0, white, 15)
  else:
    show_text("Hi " + vars.user + "!", 0, 0, white)
  pygame.display.update()

def titleNFT(): #NFT animation
  screen.fill(black)
  pygame.display.set_caption("window")
  screen.blit(playButton, (333, 266))
  screen.blit(nftButton, (338, 435))
  screen.blit(titleLogo, (250, 30))
  screen.blit(soundButton, (950, 550))
  showHubCoin(vars.user, 800, 0, white)
  if vars.user == "":
    show_text_size("Playing as guest.", 0, 0, white, 15)
  else:
    show_text("Hi " + vars.user + "!", 0, 0, white)
  pygame.display.update()

def drawTitleoff(): #Title Screen
  screen.fill(black)
  screen.blit(playButton, (333,266))
  screen.blit(nftButton, (333,430))
  screen.blit(titleLogo, (250, 30))
  screen.blit(soundButton, (950, 550))
  showHubCoin(vars.user, 800, 0, white)
  pygame.draw.line(screen, red, (955, 555), (995, 595), 5)
  if vars.user == "":
    show_text_size("Playing as guest.", 0, 0, white, 15)
  else:
    show_text("Hi " + vars.user + "!", 0, 0, white)
  pygame.display.update()

def titlePlayoff(): #Play button animation
  pygame.display.set_caption("window")
  screen.blit(playButton, (338, 271))
  screen.blit(nftButton, (333, 430))
  screen.blit(titleLogo, (250, 30))
  screen.blit(soundButton, (950, 550))
  showHubCoin(vars.user, 800, 0, white)
  pygame.draw.line(screen, red, (955, 555), (995, 595), 5)
  if vars.user == "":
    show_text_size("Playing as guest.", 0, 0, white, 15)
  else:
    show_text("Hi " + vars.user + "!", 0, 0, white)
  pygame.display.update()

def titleNFToff(): #NFT animation
  screen.fill(black)
  pygame.display.set_caption("window")
  screen.blit(playButton, (333, 266))
  screen.blit(nftButton, (338, 435))
  screen.blit(titleLogo, (250, 30))
  screen.blit(soundButton, (950, 550))
  showHubCoin(vars.user, 800, 0, white)
  pygame.draw.line(screen, red, (955, 555), (995, 595), 5)
  if vars.user == "":
    show_text_size("Playing as guest.", 0, 0, white, 15)
  else:
    show_text("Hi " + vars.user + "!", 0, 0, white)
  pygame.display.update()

def drawSelect(): #select screen
  screen.fill(black)
  screen.blit(titleLogo, (250, 30))
  screen.blit(escButton,(20,20))
  screen.blit(pingLogo, (143,270))
  screen.blit(aimLogo, (143,400))
  screen.blit(pastryLogo, (572,270))
  screen.blit(wormLogo, (572,400))
  showHubCoin(vars.user, 800, 0, white)
  pygame.display.update()

def pingSelect(): #ping anim
  screen.fill(black)
  screen.blit(titleLogo, (250, 30))
  screen.blit(escButton,(20,20))
  screen.blit(pingLogo, (148,275))
  screen.blit(aimLogo, (143,400))
  screen.blit(pastryLogo, (572,270))
  screen.blit(wormLogo, (572,400))
  showHubCoin(vars.user, 800, 0, white)
  pygame.display.update()


def pastrySelect(): #pastry actuator anim
  screen.fill(black)
  screen.blit(titleLogo, (250, 30))
  screen.blit(escButton,(20,20))
  screen.blit(pingLogo, (143,270))
  screen.blit(aimLogo, (143,400))
  screen.blit(pastryLogo, (577,275))
  screen.blit(wormLogo, (572,400))
  showHubCoin(vars.user, 800, 0, white)
  pygame.display.update()

def aimSelect(): #skaavok anim
  screen.blit(titleLogo, (250, 30))
  screen.blit(escButton,(20,20))
  screen.blit(pingLogo, (143,270))
  screen.blit(aimLogo, (148,405))
  screen.blit(pastryLogo, (572,270))
  screen.blit(wormLogo, (572,400))
  showHubCoin(vars.user, 800, 0, white)
  pygame.display.update()

def wormSelect(): #worm anim
  screen.fill(black)
  screen.blit(titleLogo, (250, 30))
  screen.blit(escButton,(20,20))
  screen.blit(pingLogo, (143,270))
  screen.blit(aimLogo, (143,400))
  screen.blit(pastryLogo, (572,270))
  screen.blit(wormLogo, (577,405))
  showHubCoin(vars.user, 800, 0, white)
  pygame.display.update()

def drawSelectEsc(): #select screen
  screen.fill(black)
  screen.blit(titleLogo, (250, 30))
  screen.blit(sescButton, (20,20))
  screen.blit(pingLogo, (143,270))
  screen.blit(aimLogo, (143,400))
  screen.blit(pastryLogo, (572,270))
  screen.blit(wormLogo, (572,400))
  showHubCoin(vars.user, 800, 0, white)
  pygame.display.update()

def countDownScreen(): #count down
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
  show_text_size("GO", 300, 100, white, 400)
  pygame.display.update()
  time.sleep(1)

def banscreen():
  screen.fill(black)
  screen.blit(cheaterdetected, (0,0))
  pygame.display.update()
