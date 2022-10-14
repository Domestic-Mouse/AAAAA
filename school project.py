from cmath import pi
import math
import pygame
from pygame.locals import *
import time
import GUI
import tkinter as tk
#intialises pygame 
pygame.init()


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
      self.scale = 3/self.MU
      self.Orbit_moon = ((3600*24)/14)

    def positionUpdate(self,window):
      y = (self.ypos * self.scale + 375)
      x = (self.xpos * self.scale + 625)
      print(x,y)
      pygame.draw.circle(window,self.colour,(x,y),self.rad)
      pygame.draw.line(window,((255,255,255)),(planet1.xpos,planet1.ypos),(x,y))
    
    def calculation(self,core):
      forceX=0
      forceY=0
      xdistance =  (self.xpos - core.xpos)
      ydistance =  (self.ypos - core.ypos)
      distance = math.sqrt(xdistance**2 + ydistance**2)
      print(distance)
      force = ((self.Gravconst*self.mass*core.mass)/distance**2)
      angle = math.atan2(xdistance,ydistance)
      forceX = math.cos(angle) * force
      forceY = math.sin(angle) * force
      planet2.xvel += forceX/planet2.mass*self.Orbit_moon 
      planet2.yvel += forceY/planet2.mass*self.Orbit_moon 
      angVel = (planet2.xvel**2+planet2.yvel**2)/self.MU
      planet2.yvel += angVel*math.cos(angle+pi/2)
      planet2.xvel += angVel*math.sin(angle+pi/2)
      xvel = planet2.xvel
      yvel = planet2.yvel
      return xvel, yvel

class OrbitSim(tk.Tk):
  def __init__(self,*args,**KeyArgs): #Args = arguements
    tk.Tk.__init__(self,*args,**KeyArgs)
    self.title("Orbit Simulation")
    self.geometry("500x500")
    container =tk.Frame(self)
    container.pack(side ="top",fill="both",)
    container.grid_rowconfigure(0, weight =0)
    container.grid_columnconfigure(0, weight = 0)

    self.frames ={}
    frame = MainMenu(container,self)
    self.frames[MainMenu] = frame
    frame.grid(row=0,column=0)
    self.show(MainMenu)

  def show(self,container):
    frame = self.frames[container]
    self.active_frame = frame
    frame.tkraise()

class MainMenu(tk.Frame):
  def __init__(self,parent,controller):
    tk.Frame.__init__(self, parent)

    #label_Sim1 = tk.Label(self, text="Simulation of Earth and Moon")
    #label_Sim1.grid(column=0, row=0, padx=5, pady=5) (example just in case)
    #entry_(variable name) = tk.Entry(self,textvariable = input(variable), show="(used to hide characters behind symbol)", width =Int value)
    
    button_Sim1 = tk.Button(self, text="Earth and Moon", command = lambda: self.runSim1(parent, controller))
    button_Sim1.grid(column = 0, row =0)
  def runSim1(self,parent, controller):
    core()

class Slider(tk.Tk):
  pass
    
   

planet1 = body(5.9*10**24,6,625,375,((0,0,255)),0,0)
planet2 = body(7.3*10**22,4,-1*384400000,0,((255,255,255)),100,-10)


 

#acts as a fucntion for the main part of the pprogram after everything has been imported and intialised
def core(): 
  #Creates key variables
  window = pygame.display.set_mode([1250,750])
  running = True
  
  clock = pygame.time.Clock()
  Pause = False
  

  #defines 2 bodies

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
       pygame.quit()
      #pausing
      if event.type == pygame.MOUSEBUTTONDOWN: # checking for pause/unpause
        if 1000 <= mousePos[0] <= 1100 and 100<= mousePos[1] <= 150:
          Pause = not Pause
    
    while Pause: #Make seperate window for GUI
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
    
    planet2.xpos *= planet2.Orbit_moon
    planet2.ypos *= planet2.Orbit_moon
    planet2.positionUpdate(window)
    
    

    #draws bodies based on qualities and a line connecting bodies (temp)
    
    pygame.draw.circle(window,((planet1.colour)),(planet1.xpos,planet1.ypos),30,0)
    #pygame.draw.circle(window,((planet2.colour)),(planet2.xpos, planet2.ypos),7.5,0)
    time.sleep(0.038)


Sim = OrbitSim()
Sim.mainloop()