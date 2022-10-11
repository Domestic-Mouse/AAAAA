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
  running = True
  Orbit_moon = ((3600*24)/14)
  clock = pygame.time.Clock()
  Pause = False
  # initalises the class for the bodies
  class body(): 
    #class Earth(body):
    def __init__(self,mass,radius,xposition,yposition,colour,xvelocity,yvelocity):
      self.mass = mass
      self.rad = radius
      self.xpos = xposition #coordinates of the planet
      self.ypos = yposition
      self.colour = colour
      self.xvel = xvelocity # determines the x and y velocity of the planet
      self.yvel = yvelocity
      self.Gravconst = 6.68*10**-11
      self.MU = 384400000
      self.AU = 1.49*10**9
      self.scale = 300/self.MU

    def positionUpdate(self,window):
      y = (self.ypos * self.scale + 375)
      x = (self.xpos * self.scale + 625)
      print(x,y)
      pygame.draw.circle(window,self.colour,(x,y),self.rad)
      pygame.draw.line(window,((255,255,255)),(planet1.xpos,planet1.ypos),(x,y))
    
    def calculation(self,other):
      forceX=forceY=0
      xdistance =  (self.xpos - other.xpos)
      ydistance =  (self.ypos - other.ypos)
      distance = math.sqrt(xdistance**2 + ydistance**2)
      force = ((self.Gravconst*self.mass*other.mass)/distance**2)
      angle = math.atan2(xdistance,ydistance)
      forceX = math.cos(angle) * force
      forceY = math.sin(angle) * force
      planet2.xvel += forceX/planet2.mass*Orbit_moon 
      planet2.yvel += forceY/planet2.mass*Orbit_moon 
      angVel = (planet2.xvel**2+planet2.yvel**2)/self.MU
      planet2.yvel += angVel*math.cos(angle+pi/2)
      planet2.xvel += angVel*math.sin(angle+pi/2)
      x = planet2.xvel
      y = planet2.yvel
      return x, y

  #defines 2 bodies
  planet1 = body(5.9*10**24,6,625,375,((0,0,255)),0,0)
  planet2 = body(7.3*10**22,4,-1*384400000,0,((255,255,255)),100,-10)
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
    planet2.xpos, planet2.ypos = planet2.calculation(planet1)
    
    planet2.xpos *= Orbit_moon
    planet2.ypos *= Orbit_moon
    planet2.positionUpdate(window)
    
    

    #draws bodies based on qualities and a line connecting bodies (temp)
    
    pygame.draw.circle(window,((planet1.colour)),(planet1.xpos,planet1.ypos),30,0)
    pygame.draw.circle(window,((planet2.colour)),(planet2.xpos, planet2.ypos),7.5,0)
    #time.sleep(0.038)
core()