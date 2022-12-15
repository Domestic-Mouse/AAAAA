from cmath import pi
import math
import pygame
from pygame.locals import *
import time
import tkinter as tk
from tkinter import *
from PIL import Image, ImageTk
#imports all necassary modules
#intialises pygame 
pygame.init()

# initalises the class for the bodies
class body(): #B for OOP
    #class Earth(body):
    def __init__(self,mass,radius,xposition,yposition,colour,xvelocity,yvelocity):
      self.mass = mass #Mass of the planet
      self.rad = radius #Radius of the planet
      self.xpos = xposition #coordinates of the planet
      self.ypos = yposition
      self.colour = colour #Colour of the planet
      self.xvel = xvelocity # determines the x and y velocity of the planet
      self.yvel = yvelocity
      self.Gravconst = 6.68*10**-11 #Constant values from here
      self.MU = 384400000
      self.AU = 1.49*10**9
      self.scale1 = 3/self.MU
      self.scale2 = 12/self.AU
      self.scale3 = 1.5/(self.AU +self.MU)
      self.Orbit_moon = ((3600*24/(365/28))) # time scale for moon
      self.Orbit_Sun = ((3600*24))# time scale for Sun

    def positionUpdate(self,window,core,scale): #Updates the postion of an orbiting object
      y = (self.ypos * scale + 375) # finds scaled postions for x and y
      x = (self.xpos * scale + 625)
      temp1 = core.xpos
      temp2 = core.ypos

      #print(x,y)
      pygame.draw.circle(window,self.colour,(x,y),self.rad)
      pygame.draw.line(window,((255,255,255)),(temp1,temp2),(x,y))
      
    def positionUpdateS(self,window,core,scale,X,Y): #Special position Update for Sun Earth and Moon
      if X == 0:
        temp1 = core.xpos
        temp2 = core.ypos
      else:
        temp1 = X
        temp2 = Y
      y = (self.ypos * scale + Y) #Used for saving coordinates
      x = (self.xpos * scale + X)
     
      #print(x,y)
      pygame.draw.circle(window,self.colour,(x,y),self.rad)
      pygame.draw.line(window,((255,255,255)),(temp1,temp2),(x,y))
      return x,y
    
    def calculation(self,core,window,scale):
      #runs calculation to find actual values through use of Gravitational force, trigonometry and circular motion as well as displays values for velocity and force of each orbiter
      pygame.font.init()
      Font = pygame.font.SysFont('timesnewroman',20)
      forceX=0 #resets force
      forceY=0
      xdistance =  (self.xpos - core.xpos) #finds distance vectors
      ydistance =  (self.ypos - core.ypos)
      distance = math.sqrt(xdistance**2 + ydistance**2) # finds the distance 
      force = ((self.Gravconst*self.mass*core.mass)/distance**2) #A catagory for physics simualtions (Calculations)
      angle = math.atan2(xdistance,ydistance) #Finds the angle
      forceX = math.cos(angle) * force #Finds the force vectors
      forceY = math.sin(angle) * force

      self.xvel += forceX/self.mass*self.Orbit_moon #Finds the velocity vectors
      self.yvel += forceY/self.mass*self.Orbit_moon 
      print(self.xvel,self.yvel)
      angVel = (self.xvel**2+self.yvel**2)/self.AU #Finds the angular velocity
      self.yvel += angVel*math.cos(angle+pi/2) #vecocity vectors
      self.xvel += angVel*math.sin(angle+pi/2)
      xvel = self.xvel
      yvel = self.yvel
      if self.mass == planet2a.mass:
        text1 = Font.render(("Moon X velocity"),True,((255,255,255)))
        text1a = Font.render((str(self.xvel)),True,((255,255,255)))
        text2 = Font.render(("Moon Y velocity"),True,((255,255,255)))
        text2a = Font.render((str(self.yvel)),True,((255,255,255)))
        text3 = Font.render(("Magnitude of Force on Moon"),True,((255,255,255)))
        text3a = Font.render((str(force)),True,((255,255,255)))
        textbox1 = text1.get_rect()
        textbox1a = text1a.get_rect()
        textbox2 = text2.get_rect()
        textbox2a = text2a.get_rect()
        textbox3 = text3.get_rect()
        textbox3a = text3a.get_rect()
        textbox1.center =(625-300,375-50)
        textbox1a.center =(625-300,375-20)
        textbox2.center = (625-300,375 +20)
        textbox2a.center =(625-300,375+50)
        textbox3.center = (625-300,375-100)
        textbox3a.center = (625-300,375-80)
        window.blit(text1,textbox1)
        window.blit(text1a,textbox1a)
        window.blit(text2,textbox2)
        window.blit(text2a,textbox2a)
        window.blit(text3,textbox3)
        window.blit(text3a,textbox3a)
      elif self.mass == planet1a.mass:
        text1 = Font.render(("Earth X velocity"),True,((255,255,255)))
        text1a = Font.render((str(self.xvel)),True,((255,255,255)))
        text2 = Font.render(("Earth Y velocity"),True,((255,255,255)))
        text2a = Font.render((str(self.yvel)),True,((255,255,255)))
        text3 = Font.render(("Magnitude of Force on Earth"),True,((255,255,255)))
        text3a = Font.render((str(force)),True,((255,255,255)))
        textbox1 = text1.get_rect()
        textbox1a = text1a.get_rect()
        textbox2 = text2.get_rect()
        textbox2a = text2a.get_rect()
        textbox3 = text3.get_rect()
        textbox3a = text3a.get_rect()
        textbox1.center =(625+300,375-50)
        textbox1a.center =(625+300,375-20)
        textbox2.center = (625+300,375 +20)
        textbox2a.center =(625+300,375 +50)
        textbox3.center = (625+300,375-100)
        textbox3a.center = (625+300,375-80)
        window.blit(text1,textbox1)
        window.blit(text1a,textbox1a)
        window.blit(text2,textbox2)
        window.blit(text2a,textbox2a)
        window.blit(text3,textbox3)
        window.blit(text3a,textbox3a)
     
      return xvel, yvel

#creates menu
class OrbitSim(tk.Tk):
  def __init__(self,*args,**KeyArgs): 
    tk.Tk.__init__(self,*args,**KeyArgs)
    self.title("Orbit Simulation")
    self.geometry("1000x400")
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
    #Sets intial values
    self.MoonMass = 1.0
    self.SunMass = 1.0
    self.EarthMass = 1.0
    self.rate = 1
    #each button corrosponds to a different simulation
    button_Sim1 = tk.Button(self, text="Earth and Moon", command = lambda: self.runSim1(parent, controller))
    button_Sim1.grid(column = 0, row =0)
    button_Sim2 = tk.Button(self, text="Earth and Sun", command = lambda: self.runSim2(parent, controller))
    button_Sim2.grid(column = 1, row =0)
    button_Sim3 = tk.Button(self, text="Earth, Sun and Moon", command = lambda: self.runSim3(parent, controller))
    button_Sim3.grid(column = 2, row =0)
    button_Sim4 = tk.Button(self, text="Sun and Moon", command = lambda: self.runSim4(parent, controller))
    button_Sim4.grid(column = 3, row =0)
    #runs a get fucntion for each value
    Enter = tk.Button(self,text = "Enter values", command=lambda: self.getV(MoonMass,EarthMass,SunMass))
    Enter.grid(row= 4, column = 1)
    
    
    #Displays small images for each Simulation
    self.img1 = ImageTk.PhotoImage(Image.open("Sun and Earth.png"))
    tk.Label(self, image= self.img1).grid(row = 1, column = 1)
    self.img2 = ImageTk.PhotoImage(Image.open("Moon and Earth.png"))
    tk.Label(self, image= self.img2).grid(row = 1, column = 0)
    self.img3 = ImageTk.PhotoImage(Image.open("Moon and Sun.png"))
    tk.Label(self, image= self.img3).grid(row = 1, column = 3)
    self.img4 = ImageTk.PhotoImage(Image.open("Three body.png"))
    tk.Label(self, image= self.img4).grid(row = 1, column = 2)
    
  #Creates entry boxes for the user to change the Mass of each obejct
    tk.Label(self, text="Mass of Sun (Multiplicative)").grid(row=2)
    SunMass = tk.Entry(self)
    SunMass.insert(0,"1.0") #inserts a default value to avoid errors
    SunMass.grid(row=3,column=0)

    tk.Label(self, text="Mass of Moon (Multiplicative)").grid(row=4)
    MoonMass = tk.Entry(self)
    MoonMass.insert(0,"1.0")
    MoonMass.grid(row=5,column=0) 

    tk.Label(self, text="Mass of Earth (Multiplicative)").grid(row=6)
    EarthMass = tk.Entry(self)
    EarthMass.insert(0,"1.0")
    EarthMass.grid(row=7,column=0)

    tk.Label(self, text="Speed of simulation").grid(row=5, column =3)
    Slow = tk.Button(self,text = "Slow", command=lambda: self.SetSpeed("Slow"))
    Slow.grid(row= 4, column = 2)
    Normal = tk.Button(self,text = "Normal", command=lambda: self.SetSpeed("Normal")) #Creates buttons for Sim speed
    Normal.grid(row= 4, column = 3)
    Fast = tk.Button(self,text = "Fast", command=lambda: self.SetSpeed("Fast"))
    Fast.grid(row= 4, column = 4)
    
    End = tk.Button(self,text="Quit",command=quit)
    End.grid(row =6 , column = 2) # closes the program
    
  def SetSpeed(self,Speed):
    if Speed == "Slow":
      self.rate = 2
    elif Speed =="Normal": #Allows the user to change the simulation speed to predefiend speeds
      self.rate = 1
    elif Speed =="Fast":
      self.rate = 0.5

  def getV(self,MoonMass,EarthMass,SunMass): #Gets the changed mass values each object and has exception handeling for incorrect data types
    try:
      self.MoonMass = float(MoonMass.get())
      if self.MoonMass <0.3 or self.MoonMass > 10:
        tk.Label(self,text="Please enter a deciamal value between 0.3 and 10").grid(row = 10, column = 0)
        self.MoonMass = 1.0
    except:
      tk.Label(self,text="Please enter a deciamal value between 0.3 and 10").grid(row=10, column = 0 )
    try:
      self.EarthMass = float(EarthMass.get())
      if self.EarthMass <0.3 or self.EarthMass > 10:
        tk.Label(self,text="Please enter a deciamal value between 0.3 and 10").grid(row = 10, column = 0)
        self.EarthMass = 1.0
    except:
      tk.Label(self,text="Please enter a deciamal value between 0.3 and 10").grid(row=10, column = 0 )
    try:
      self.SunMass = float(SunMass.get())
      if self.SunMass <0.3 or self.SunMass > 10:
        tk.Label(self,text="Please enter a deciamal value between 0.3 and 10").grid(row = 10, column = 0)
        self.SunMass = 1.0
    except:
      tk.Label(self,text="Please enter a deciamal value between 0.3 and 10").grid(row=10, column = 0 )

#Defines function for button presses for simulations
  def runSim1(self,parent, controller):
    EM(self.EarthMass,self.MoonMass,self.rate)
  def runSim2(self,parent,controller):
    SE(self.SunMass,self.EarthMass,self.rate)
  def runSim3(self,parent,controller):
    SEM(self.SunMass,self.EarthMass,self.MoonMass,self.rate)
  def runSim4(self,parent,controller):
    SM(self.SunMass,self.MoonMass,self.rate)
    


   
#Creates each planet and changes them based on different simulation
planet1a = body(5.9*10**24,6,625,375,((0,0,255)),0,0)
planet1b = body(5.9*10**24,6,-1.49*10**9,0,((0,0,255)),0,0)
planet2a = body(7.3*10**22,4,-1*384400000,0,((255,255,255)),100,-10)
planet2b = body(7.3*10**22,4,-1*384400000-1.49*10**9,0,((255,255,255)),100,-10)
planet3 = body(1.989*10**30,4,625,375,((221,110,15)),0,0)

def SM(SunM,Moon,rate): #Simulation of the Sun and Moon
  pygame.font.init()
  planet2b = body(7.3*10**22,4,-1*384400000,0,((255,255,255)),100,-10)
  planet3 = body(1.989*10**30,4,625,375,((221,110,15)),0,0) #Resests values
  window = pygame.display.set_mode([1250,750]) #Creates window
  running = True #used to keep the window open
  core_planet = planet3 # Sets what planet will not movw
  scale = planet3.scale3 #Sets the scale that will be used
  clock = pygame.time.Clock() #Used to set framerate
  Pause = False #Used for pausing
  planet3.mass *= SunM #Adjusts masses based on user input
  planet2b.mass *= Moon
  
  pygame.display.set_caption("Orbit Simulation")
  
  while running:
    #updates window after every change
    mousePos = pygame.mouse.get_pos()
    pygame.draw.rect(window,((200,200,200)),[1000,100,100,50])
    pygame.draw.rect(window,((200,200,200)),[100,100,100,50]) #Creates buttons for qutting and pausing
    Font = pygame.font.SysFont('timesnewroman',15)
    text1 = Font.render("Pause/Unpause",True,((0,0,0)))
    text2 = Font.render("Quit",True,((0,0,0)))
    textbox1 = text1.get_rect()
    textbox2 = text2.get_rect()
    textbox1.center =(1050,125) #Places text on the buttons
    textbox2.center = (150,125)
    window.blit(text1,textbox1)
    window.blit(text2,textbox2)
    if 100 <= mousePos[0] <= 200 and 100<= mousePos[1] <= 150:
      pygame.draw.rect(window,((150,150,150)),[100,100,100,50])
      window.blit(text1,textbox1)
      window.blit(text2,textbox2)
    if 1000 <= mousePos[0] <= 1100 and 100<= mousePos[1] <= 150:
      pygame.draw.rect(window,((150,150,150)),[1000,100,100,50]) #Compares the mouse position to the buttons
      window.blit(text1,textbox1)
      window.blit(text2,textbox2)
    clock.tick(60)
    pygame.display.update()
    
    for event in pygame.event.get():
      if event.type == pygame.QUIT:
       running = False
       pygame.quit()
      #pausing
      if event.type == pygame.MOUSEBUTTONDOWN: # checking for pause/unpause and Quitting
        if 100 <= mousePos[0] <= 200 and 100<= mousePos[1] <= 150:
          running = False
          pygame.quit()
        if 1000 <= mousePos[0] <= 1100 and 100<= mousePos[1] <= 150: 
          Pause = not Pause
    
    while Pause: 
      for event in pygame.event.get():
        #unpausing    
        if event.type == pygame.QUIT:
          Pause = False
          running = False
          break
        if event.type == pygame.MOUSEBUTTONDOWN: # checking for unpause
          if 1000 <= mousePos[0] <= 1100 and 100<= mousePos[1] <= 150:
            Pause = not Pause
      
    #resets frame
    window.fill((0,0,0))
    #bulk of calculations
    planet2b.xpos, planet2b.ypos = planet2b.calculation(core_planet,window,scale)    
    planet2b.xpos *= planet2b.Orbit_Sun
    planet2b.ypos *= planet2b.Orbit_Sun #Updates the actual postion with a time scale
    planet2b.positionUpdate(window,core_planet,scale)#Creates a scaled postion which is then dispalyed

    pygame.draw.circle(window,((core_planet.colour)),(core_planet.xpos,core_planet.ypos),30,0) #Draws the center planet
    time.sleep(0.038*rate)

def EM(Earth,Moon,rate): 

  #Creates and resets key variables
  pygame.font.init()
  planet1a = body(5.9*10**24,6,625,375,((0,0,255)),0,0)
  planet2 = body(7.3*10**22,4,-1*384400000,0,((255,255,255)),100,-10)
  Sun = False
  window = pygame.display.set_mode([1250,750])
  running = True
  core_planet = planet1a
  if not Sun: #Changes the scale based on whether or not the Sun is present
    scale = planet2.scale1
  else:
    scale = planet2.scale2
  clock = pygame.time.Clock()
  Pause = False
  planet1a.mass *= Earth
  planet2.mass *= Moon
  
  pygame.display.set_caption("Orbit Simulation")
  
  while running:
    mousePos = pygame.mouse.get_pos()
    pygame.draw.rect(window,((200,200,200)),[1000,100,100,50])
    pygame.draw.rect(window,((200,200,200)),[100,100,100,50])
    Font = pygame.font.SysFont('timesnewroman',15)
    text1 = Font.render("Pause/Unpause",True,((0,0,0)))
    text2 = Font.render("Quit",True,((0,0,0)))
    textbox1 = text1.get_rect()
    textbox2 = text2.get_rect()
    textbox1.center =(1050,125)
    textbox2.center = (150,125)
    window.blit(text1,textbox1)
    window.blit(text2,textbox2)
    if 100 <= mousePos[0] <= 200 and 100<= mousePos[1] <= 150:
      pygame.draw.rect(window,((150,150,150)),[100,100,100,50])
      window.blit(text1,textbox1)
      window.blit(text2,textbox2)
    if 1000 <= mousePos[0] <= 1100 and 100<= mousePos[1] <= 150:
      pygame.draw.rect(window,((150,150,150)),[1000,100,100,50])
      window.blit(text1,textbox1)
      window.blit(text2,textbox2)

    clock.tick(60)
    pygame.display.update()
    
    for event in pygame.event.get():
      if event.type == pygame.QUIT:
       running = False
       pygame.quit()
      #pausing
      if event.type == pygame.MOUSEBUTTONDOWN: # checking for pause or Quit
        if 100 <= mousePos[0] <= 200 and 100<= mousePos[1] <= 150:
          Pause = False
          running = False
          pygame.quit()
        if 1000 <= mousePos[0] <= 1100 and 100<= mousePos[1] <= 150:
          Pause = not Pause
    
    while Pause: # allows unpausing
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
    planet2.xpos, planet2.ypos = planet2.calculation(core_planet,window,scale)    
    planet2.xpos *= planet2.Orbit_moon
    planet2.ypos *= planet2.Orbit_moon
    planet2.positionUpdate(window,core_planet,scale)
    #draws bodies based on qualities and a line connecting bodies (temp)
    pygame.draw.circle(window,((core_planet.colour)),(core_planet.xpos,core_planet.ypos),30,0)
    #pygame.draw.circle(window,((planet2.colour)),(planet2.xpos, planet2.ypos),7.5,0)
    time.sleep(0.038*rate)

def SEM(SunM,Earth,Moon,rate): 
  #Creates key variables
  pygame.font.init() # initialises font
  planet1b = body(5.9*10**24,6,-1.49*10**9,0,((0,0,255)),0,0)
  planet2b = body(7.3*10**22,4,-1*384400000,0,((255,255,255)),100,-100)
  planet3 = body(1.989*10**30,4,625,375,((221,110,15)),0,0)
  planet1b.mass *= Earth
  planet2b.mass *= Moon
  planet3.mass *= SunM
  window = pygame.display.set_mode([1250,750])
  running = True
  core_planet = planet3
  scale1 = planet2b.scale1
  scale2 = planet2b.scale2
  clock = pygame.time.Clock()
  Pause = False
  pygame.display.set_caption("Orbit Simulation")
  
  while running:
    mousePos = pygame.mouse.get_pos()
    
    pygame.font.init()
    pygame.draw.rect(window,((200,200,200)),[1000,100,100,50])
    pygame.draw.rect(window,((200,200,200)),[100,100,100,50])
    Font = pygame.font.SysFont('timesnewroman',15)
    text1 = Font.render("Pause/Unpause",True,((0,0,0)))
    text2 = Font.render("Quit",True,((0,0,0)))
    textbox1 = text1.get_rect()
    textbox2 = text2.get_rect()
    textbox1.center =(1050,125) #Creates boxes and text to indicate buttons for pausing/unpausing and quitting the sinulation
    textbox2.center = (150,125)
    window.blit(text1,textbox1)
    window.blit(text2,textbox2)
    if 100 <= mousePos[0] <= 200 and 100<= mousePos[1] <= 150:
      pygame.draw.rect(window,((150,150,150)),[100,100,100,50])
      window.blit(text1,textbox1)
      window.blit(text2,textbox2)
    if 1000 <= mousePos[0] <= 1100 and 100<= mousePos[1] <= 150:
      pygame.draw.rect(window,((150,150,150)),[1000,100,100,50])
      window.blit(text1,textbox1)
      window.blit(text2,textbox2)

    clock.tick(60)
    pygame.display.update()
    
    for event in pygame.event.get():
      if event.type == pygame.QUIT:
       running = False
       pygame.quit()
      #pausing
      if event.type == pygame.MOUSEBUTTONDOWN: # checking for pause/unpause
        if 100 <= mousePos[0] <= 200 and 100<= mousePos[1] <= 150:
          running = False
          pygame.quit()
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
    planet1b.xpos, planet1b.ypos = planet1b.calculation(core_planet,window,scale2)
    planet1b.xpos *= planet1b.Orbit_Sun
    planet1b.ypos *= planet1b.Orbit_Sun
    x,y = planet1b.positionUpdateS(window,core_planet,scale2,625,375)

    planet2b.xpos,planet2b.ypos = planet2b.calculation(planet1b,window,scale1)
    planet2b.ypos *= planet2b.Orbit_moon
    planet2b.xpos *= planet2b.Orbit_moon

    planet2b.positionUpdateS(window,planet1b,scale1,x,y)

    #draws bodies based on qualities and a line connecting bodies (temp)
    pygame.draw.circle(window,((core_planet.colour)),(core_planet.xpos,core_planet.ypos),30,0)
    #pygame.draw.circle(window,((planet2.colour)),(planet2.xpos, planet2.ypos),7.5,0)
    time.sleep(0.038*rate)

def SE(SunM,Earth,rate): 
  #Creates key variables
  pygame.font.init()
  planet1b = body(5.9*10**24,6,-1.49*10**9,0,((0,0,255)),0,0)
  planet3 = body(1.989*10**30,4,625,375,((221,110,15)),0,0)
  planet1b.mass *= Earth
  planet3.mass *= SunM
  Sun = True
  window = pygame.display.set_mode([1250,750])
  running = True
  core_planet = planet3
  if not Sun:
    scale = planet2a.scale1
  else:
    scale = planet2a.scale2
  clock = pygame.time.Clock()
  Pause = False

  

  #defines 2 bodies

  pygame.display.set_caption("Orbit Simulation")
  
  while running:
    mousePos = pygame.mouse.get_pos()
    pygame.draw.rect(window,((200,200,200)),[1000,100,100,50])
    pygame.draw.rect(window,((200,200,200)),[100,100,100,50])
    Font = pygame.font.SysFont('timesnewroman',15)
    text1 = Font.render("Pause/Unpause",True,((0,0,0)))
    text2 = Font.render("Quit",True,((0,0,0)))
    textbox1 = text1.get_rect()
    textbox2 = text2.get_rect()
    textbox1.center =(1050,125)# Draws text on each box for Pausing/Unpausing and Quitting
    textbox2.center = (150,125)
    window.blit(text1,textbox1)
    window.blit(text2,textbox2)
    if 100 <= mousePos[0] <= 200 and 100<= mousePos[1] <= 150:
      pygame.draw.rect(window,((150,150,150)),[100,100,100,50])
      window.blit(text1,textbox1)
      window.blit(text2,textbox2)
    if 1000 <= mousePos[0] <= 1100 and 100<= mousePos[1] <= 150:
      pygame.draw.rect(window,((150,150,150)),[1000,100,100,50])
      window.blit(text1,textbox1)
      window.blit(text2,textbox2)

    clock.tick(60)
    pygame.display.update()
    
    for event in pygame.event.get():
      if event.type == pygame.QUIT:
       running = False
       pygame.quit()
      #pausing
      if event.type == pygame.MOUSEBUTTONDOWN: # checking for pause/unpause
        if 100 <= mousePos[0] <= 200 and 100<= mousePos[1] <= 150:
          running = False
          pygame.quit()
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

    
    #extra Calculations
    planet1b.xpos, planet1b.ypos = planet1b.calculation(core_planet,window,scale)
    planet1b.xpos *= planet1b.Orbit_Sun
    planet1b.ypos *= planet1b.Orbit_Sun
    planet1b.positionUpdate(window,core_planet,scale)
    
    pygame.draw.circle(window,((core_planet.colour)),(core_planet.xpos,core_planet.ypos),30,0)
  
    time.sleep(0.038*rate)

      
Sim = OrbitSim() # Opens the main menu
Sim.mainloop() # Runs the program