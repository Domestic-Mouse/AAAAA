from cmath import pi
import math
import pygame
from pygame.locals import *
import time
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
      self.scale1 = 3/self.MU
      self.scale2 = 12/self.AU
      self.Orbit_moon = ((3600*24)/14)
      self.Orbit_Sun = ((3600*24))

    def positionUpdate(self,window,core,scale):
      y = (self.ypos * scale + 375)
      x = (self.xpos * scale + 625)
      print(x,y)
      pygame.draw.circle(window,self.colour,(x,y),self.rad)
      pygame.draw.line(window,((255,255,255)),(core.xpos,core.ypos),(x,y))
    
    def calculation(self,core):
      forceX=0
      forceY=0
      xdistance =  (self.xpos - core.xpos)
      ydistance =  (self.ypos - core.ypos)
      distance = math.sqrt(xdistance**2 + ydistance**2)
      force = ((self.Gravconst*self.mass*core.mass)/distance**2)
      angle = math.atan2(xdistance,ydistance)
      forceX = math.cos(angle) * force
      forceY = math.sin(angle) * force
      self.xvel += forceX/self.mass*self.Orbit_moon 
      self.yvel += forceY/self.mass*self.Orbit_moon 
      angVel = (self.xvel**2+self.yvel**2)/self.MU
      self.yvel += angVel*math.cos(angle+pi/2)
      self.xvel += angVel*math.sin(angle+pi/2)
      xvel = self.xvel
      yvel = self.yvel
      return xvel, yvel
class OrbitSim(tk.Tk):
  def __init__(self,*args,**KeyArgs): #Args = arguements
    tk.Tk.__init__(self,*args,**KeyArgs)
    self.title("Orbit Simulation")
    self.geometry("400x400")
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
    button_Sim2 = tk.Button(self, text="Earth and Sun", command = lambda: self.runSim2(parent, controller))
    button_Sim2.grid(column = 1, row =0)
    button_Sim3 = tk.Button(self, text="Earth, Sun and Moon", command = lambda: self.runSim3(parent, controller))
    button_Sim3.grid(column = 2, row =0)
    master = tk.Tk()
    tk.Label(master, text="Mass of Sun (Multiplicative)").grid(row=0)
    button_getSun = tk.Button(master, text="Enter",command = lambda: self.get(SunMass))
    button_getSun.grid(column = 0, row = 1)
    SunMass = tk.Entry(master)
    SunMass.grid(row=0,column=1)
    
  def get(self,SunMass):
    print(SunMass)
    return int(SunMass.get())

    
  def runSim1(self,parent, controller,SunMass,):
    EM()
  def runSim2(self,parent,controller):
    SE()
  def runSim3(self,parent,controller):
    SEM()
    
   

planet1a = body(5.9*10**24,6,625,375,((0,0,255)),0,0)
planet1b = body(5.9*10**24,6,-1.49*10**9,0,((0,0,255)),0,0)
planet2 = body(7.3*10**22,4,-1*384400000,0,((255,255,255)),100,-10)
planet3 = body(1.989*10**30,4,625,375,((221,110,15)),0,0)

#acts as a fucntion for the main part of the pprogram after everything has been imported and intialised
def EM(): 
  #Creates key variables
  Sun = False
  window = pygame.display.set_mode([1250,750])
  running = True
  core_planet = planet1a
  if not Sun:
    scale = planet2.scale1
  else:
    scale = planet2.scale2
  clock = pygame.time.Clock()
  Pause = False
  
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
    planet2.xpos, planet2.ypos = planet2.calculation(core_planet)    
    planet2.xpos *= planet2.Orbit_moon
    planet2.ypos *= planet2.Orbit_moon
    planet2.positionUpdate(window,core_planet,scale)
    #draws bodies based on qualities and a line connecting bodies (temp)
    pygame.draw.circle(window,((core_planet.colour)),(core_planet.xpos,core_planet.ypos),30,0)
    #pygame.draw.circle(window,((planet2.colour)),(planet2.xpos, planet2.ypos),7.5,0)
    time.sleep(0.038)

def SEM(): 
  #Creates key variables
  Sun = True
  window = pygame.display.set_mode([1250,750])
  running = True
  core_planet = planet3
  scale1 = planet2.scale1
  scale2 = planet2.scale2
  clock = pygame.time.Clock()
  Pause = False
  
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
    planet1b.xpos, planet1b.ypos = planet1b.calculation(core_planet)
    planet1b.xpos *= planet1b.Orbit_Sun
    planet1b.ypos *= planet1b.Orbit_Sun
    planet1b.positionUpdate(window,core_planet,scale2)

    planet2.xpos,planet2.ypos = planet2.calculation(planet1b)
    planet2.ypos *= planet2.Orbit_moon
    planet2.xpos *= planet2.Orbit_moon
    print(planet2.xpos,planet2.ypos)
    planet2.positionUpdate(window,planet1b,scale1)

    #draws bodies based on qualities and a line connecting bodies (temp)
    pygame.draw.circle(window,((core_planet.colour)),(core_planet.xpos,core_planet.ypos),30,0)
    #pygame.draw.circle(window,((planet2.colour)),(planet2.xpos, planet2.ypos),7.5,0)
    time.sleep(0.038)

def SE(): 
  #Creates key variables
  Sun = True
  window = pygame.display.set_mode([1250,750])
  running = True
  core_planet = planet3
  if not Sun:
    scale = planet2.scale1
  else:
    scale = planet2.scale2
  clock = pygame.time.Clock()
  Pause = False
  print(scale)
  

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
    planet1b.xpos, planet1b.ypos = planet1b.calculation(core_planet)
    planet1b.xpos *= planet1b.Orbit_Sun
    planet1b.ypos *= planet1b.Orbit_Sun
    planet1b.positionUpdate(window,core_planet,scale)
   
    
    

    #draws bodies based on qualities and a line connecting bodies (temp)
    
    pygame.draw.circle(window,((core_planet.colour)),(core_planet.xpos,core_planet.ypos),30,0)
    #pygame.draw.circle(window,((planet2.colour)),(planet2.xpos, planet2.ypos),7.5,0)
    time.sleep(0.0002)

Sim = OrbitSim()
Sim.mainloop()