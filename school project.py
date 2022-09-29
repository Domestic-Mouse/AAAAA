from cmath import pi
import math
import pygame
from pygame.locals import *
import time

#intialises pygame 

pygame.init



#acts as a fucntion for the main part of the pprogram after everything has been imported and intialised
def core(): 
  #Creates key variables
  window = pygame.display.set_mode([1250,750])
  totalFX = 0
  totalFY = 0
  AU = 384400000 # distance from moon to Earth in M
  scale = (300/AU)
  running = True
  Orbit_moon = ((3600*24)/14)
  clock = pygame.time.Clock()
  Pause = False
  # initalises the class for the bodies
  class body(): 
    def __init__(self,mass,radius,xposition,yposition,colour,xvelocity,yvelocity):
      self.mass = mass
      self.rad = radius
      self.xpos = xposition #coordinates of the planet
      self.ypos = yposition
      self.colour = colour
      self.xvel = xvelocity # determines the x and y velocity of the planet
      self.yvel = yvelocity
      self.Gravconst = 6.68*10**-11

    def positionUpdate(self,window):
      y = self.ypos * scale + 375
      x = self.xpos * scale + 625
      print(x,y)
      pygame.draw.circle(window,self.colour,(x,y),self.rad)
      pygame.draw.line(window,((255,255,255)),(planet1.xpos,planet1.ypos),(x,y))
    
    def calculation(self,other):
      xdistance =  (self.xpos - other.xpos)
      ydistance =  (self.ypos - other.ypos)
      distance = math.sqrt(xdistance**2 + ydistance**2)
      force = ((self.Gravconst*self.mass*other.mass)/distance**2)
      angle = math.atan2(xdistance,ydistance)
      forceX = math.cos(angle) * force
      forceY = math.sin(angle) * force
      return forceX, forceY
    
    #page 66 kerboodle for keplar


  #defines 2 bodies
  planet1 = body(5.9*10**24,6,625,375,((0,0,255)),0,0)
  planet2 = body(7.3*10**22,4,-1*AU,0,((255,255,255)),0,0)
  pygame.display.set_caption("Orbit Simulation")
  
  while running:
    #updates window after every change
    mousePos = pygame.mouse.get_pos()
    pygame.draw.rect(window,((200,200,200)),[1000,100,100,50])
    if 1000 <= mousePos[0] <= 1100 and 100<= mousePos[1] <= 150:
      pygame.draw.rect(window,((150,150,150)),[1000,100,100,50])

    clock.tick(60)
    pygame.display.update()
    
    for event in pygame.event.get():
      if event.type == pygame.QUIT:
       running = False
      #pausing
      if event.type == pygame.MOUSEBUTTONDOWN: # checking for pause/unpause
        if 1000 <= mousePos[0] <= 1100 and 100<= mousePos[1] <= 150:
          Pause = not Pause
    
    while Pause:
      for event in pygame.event.get():
        #unpausing    
        if event.type == pygame.QUIT:
          Pause = False
          running = False
          break
        if event.type == pygame.MOUSEBUTTONDOWN: # checking for pause/unpause
          if 1000 <= mousePos[0] <= 1100 and 100<= mousePos[1] <= 150:
            Pause = not Pause
      
    #resets frame
    window.fill((0,0,0))

    
    #bulk of calculations
    forceX, forceY = planet2.calculation(planet1)
    totalFX += forceX
    totalFY += forceY
    planet2.xvel += totalFX/planet2.mass*Orbit_moon
    planet2.yvel += totalFY/planet2.mass*Orbit_moon
    print(math.sqrt(planet2.xvel**2+planet2.yvel**2))
    planet2.xpos += (planet2.xvel * Orbit_moon)
    planet2.ypos += (planet2.yvel * Orbit_moon)
    planet2.positionUpdate(window)
    
    

    #draws bodies based on qualities and a line connecting bodies (temp)
    
    pygame.draw.circle(window,((planet1.colour)),(planet1.xpos,planet1.ypos),30,0)
    pygame.draw.circle(window,((planet2.colour)),(planet2.xpos, planet2.ypos),7.5,0)
    time.sleep(0.038)
core()
