import pygame
from pygame.locals import*
import random
import time

pink = (255,200,200)
blue = (0,0,255)
green = (0,255,0)
black = (0,0,0)
white = (255,255,255)
orange = (255, 165, 0)

x=0
y=0
colors=[pink,blue,green,white]
pygame.init()
screen = pygame.display.set_mode((1000,600))
pygame.display.set_caption("window")
titleLogo = pygame.image.load("Logo/titleLogo.png")
playButton = pygame.image.load("Logo/play.png")
nftButton = pygame.image.load("Logo/nft.png")
escButton = pygame.image.load("Logo/esc.png")

pingLogo = pygame.image.load("Logo/ping.png")
aimLogo = pygame.image.load("Logo/aim.png")
wormLogo = pygame.image.load("Logo/worm.png")
pastryLogo = pygame.image.load("Logo/pastry.png")


def show_text(msg, xp, yp, color):
  fontobj = pygame.font.SysFont("comicsans", 32)
  msgobj = fontobj.render(msg, False, color)
  screen.blit(msgobj, (xp, yp))




def drawTitle():
  screen.fill(black)
  pygame.display.set_caption("window")
  screen.blit(playButton, (333,266))
  screen.blit(nftButton, (333,430))
  screen.blit(titleLogo, (250, 30))
  pygame.display.update()

def titlePlay():
  pygame.display.set_caption("window")
  screen.blit(playButton, (338, 271))
  screen.blit(nftButton, (333, 430))
  screen.blit(titleLogo, (250, 30))
  pygame.display.update()

def titleNFT():
  screen.fill(black)
  pygame.display.set_caption("window")
  screen.blit(playButton, (333, 266))
  screen.blit(nftButton, (338, 435))
  screen.blit(titleLogo, (250, 30))
  pygame.display.update()


def drawSelect():
  screen.fill(black)
  screen.blit(titleLogo, (250, 30))
  screen.blit(escButton,(20,20))
  screen.blit(pingLogo, (143,270))
  screen.blit(aimLogo, (143,400))
  screen.blit(pastryLogo, (572,270))
  screen.blit(wormLogo, (572,400))
  pygame.display.update()


def pingSelect():
  screen.fill(black)
  screen.blit(titleLogo, (250, 30))
  screen.blit(escButton,(20,20))
  screen.blit(pingLogo, (148,275))
  screen.blit(aimLogo, (143,400))
  screen.blit(pastryLogo, (572,270))
  screen.blit(wormLogo, (572,400))
  pygame.display.update()
  time.sleep(0.25)
  drawSelect()
  pygame.display.update()
  time.sleep(0.25)


def pastrySelect():
  screen.fill(black)
  screen.blit(titleLogo, (250, 30))
  screen.blit(escButton,(20,20))
  screen.blit(pingLogo, (143,270))
  screen.blit(aimLogo, (143,400))
  screen.blit(pastryLogo, (577,275))
  screen.blit(wormLogo, (572,400))
  pygame.display.update()
  time.sleep(0.25)
  drawSelect()
  pygame.display.update()
  time.sleep(0.25)

def aimSelect():
  screen.fill(black)
  screen.blit(titleLogo, (250, 30))
  screen.blit(escButton,(20,20))
  screen.blit(pingLogo, (143,270))
  screen.blit(aimLogo, (148,405))
  screen.blit(pastryLogo, (572,270))
  screen.blit(wormLogo, (572,400))
  pygame.display.update()
  time.sleep(0.25)
  drawSelect()
  pygame.display.update()
  time.sleep(0.25)

def wormSelect():
  screen.fill(black)
  screen.blit(titleLogo, (250, 30))
  screen.blit(escButton,(20,20))
  screen.blit(pingLogo, (143,270))
  screen.blit(aimLogo, (143,400))
  screen.blit(pastryLogo, (572,270))
  screen.blit(wormLogo, (577,405))
  pygame.display.update()
  time.sleep(0.25)
  drawSelect()
  pygame.display.update()
  time.sleep(0.25)