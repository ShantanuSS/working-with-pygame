#here we have to add a Computer Player
from pygame.locals import *
from random import randint
import pygame
import time

class Food:  #same as snakegame.py
    x=0
    y=0
    step=44
    def __init__(self,x,y):
        self.x=x*self.step
        self.y=y*self.step
    def draw(self,surface,image):
        surface.blit(image,(self.x,self.y))

class Player: #same as snakegame.py
    x=[0]
    y=[0]
    step=44
    direction=0
    length=3
    updatecountmax=2
    updatecount=0
    def __init__(self,length):
        self.length=length
        for i in range(0,2000):
            self.x.append(-100)
            self.y.append(-100)
        self.x[1]=1*44
        self.x[2]=2*44
    def update(self):
        self.updatecount+=1
        if  self.updatecount > self.updatecountmax:  
            for i in range(self.length-1,0,-1):
                self.x[i]=self.x[i-1]
                self.y[i]=self.y[i-1]
            if self.direction==0:
                self.x[0]+=self.step
            if self.direction==1:
                self.x[0]-=self.step
            if self.direction==2:
                self.y[0]-=self.step
            if self.direction==3:
                self.y[0]+=self.step
            self.updatecount=0
    def moveright(self):
        self.direction=0
    def moveleft(self):
        self.direction=1
    def moveup(self):
        self.direction=2
    def movedown(self):
        self.direction=3
    def draw(self,surface,image):
        for i in range(0,self.length):
            surface.blit(image,(self.x[i],self.y[i]))

class Computer:
    x=[0]
    y=[0]
    step=44
    direction=0
    length=3
    updatecountmax=2
    updatecount=0
    def __init__(self,length):
        self.length=length
        for i in range(0,2000):
            self.x.append(-100)
            self.y.append(-100)
        self.x[0]=1*44
        self.y[0]=4*44  #we changed this
    def update(self):
        self.updatecount+=1
        if  self.updatecount > self.updatecountmax:     
            for i in range(self.length-1,0,-1):
                self.x[i]=self.x[i-1]
                self.y[i]=self.y[i-1]
            if self.direction==0:
                self.x[0]+=self.step
            if self.direction==1:
                self.x[0]-=self.step
            if self.direction==2:
                self.y[0]-=self.step
            if self.direction==3:
                self.y[0]+=self.step
            self.updatecount=0
    def moveright(self):
        self.direction=0
    def moveleft(self):
        self.direction=1
    def moveup(self):
        self.direction=2
    def movedown(self):
        self.direction=3

    def target(self,dx,dy):   #this func will go to destintion and neglect any obstacles
        if self.x[0] >dx:
            self.moveleft()
        if self.x[0] <dx:
            self.moveright()
        if self.x[0] ==dx:
            if self.y[0] <dy:
                self.movedown()
            if self.y[0]>dy:
                self.moveup()
    
    def draw(self,surface,image):
        for i in range(0,self.length):
            surface.blit(image,(self.x[i],self.y[i]))

class Game:                                         #handling collision with snake's food
    def isCollision(self,x1,y1,x2,y2,bsize):
        if x1>=x2 and x1<=x2+bsize:
            if y1>=y2 and y1<=y2+bsize:
                return True
        return False

class SnakeGame:
    window_width=800
    window_height=600
    player=0
    apple=0

    def __init__(self):
        self.runningG=True
        self.displayG=None
        self.imageG=None
        self.appleG=None
        self.game=Game()
        self.player=Player(5)
        self.apple=Food(8,5)
        self.computer=Computer(5)
        self.im1=None
        
    def on_init(self):
        pygame.init()
        self.displayG=pygame.display.set_mode((self.window_width,self.window_height),pygame.HWSURFACE)
        pygame.display.set_caption('Snake Game for you') 
        self.runningG=True
        self.imageG=pygame.image.load("pygame.png").convert()
        self.appleG=pygame.image.load("foodie.png").convert()
        self.im1=pygame.image.load("im1.png").convert()
    def on_event(self,event):
        if event.type==QUIT:
            self.runningG=False
    def on_loop(self):
        self.computer.target(self.apple.x,self.apple.y) #this line also added
        self.player.update()
        self.computer.update() 
        #pass
        for i in range(0,self.player.length): 
            if self.game.isCollision(self.apple.x,self.apple.y,self.player.x[i],self.player.y[i],44):
                self.apple.x=randint(2,9)*44
                self.apple.y=randint(2,9)*44
                self.player.length+=1
        for i in range(0,self.player.length):  #new loop for computer
            if self.game.isCollision(self.apple.x,self.apple.y,self.computer.x[i],self.computer.y[i],44):
                self.apple.x=randint(2,9)*44
                self.apple.y=randint(2,9)*44
                #self.computer.length+=1    ;using this line computer's snake size also increases after eating ;so for simplicity don't use it
        for i in range(2,self.player.length):  
            if self.game.isCollision(self.player.x[0],self.player.y[0],self.player.x[i],self.player.y[i],40):
                print("You lose! Collision")
                print("x[0]("+ str(self.player.x[0]) +","+str(self.player.y[0])+")")
                print("x["+str(i)+"]("+str(self.player.x[i])+","+str(self.player.y[i])+")")
                exit(0)
        pass                
    def on_render(self):
        self.displayG.fill((0,0,0))
        self.player.draw(self.displayG,self.imageG)
        self.apple.draw(self.displayG,self.appleG)
        self.computer.draw(self.displayG,self.im1)
        pygame.display.flip()
    def on_cleanup(self):
        pygame.quit()
    def on_execute(self):
        if self.on_init()==False:
            self.runningG=False
        while (self.runningG):
            pygame.event.pump()
            keys=pygame.key.get_pressed()
            if(keys[K_RIGHT]):
                self.player.moveright()
            if(keys[K_LEFT]):
                self.player.moveleft()
            if(keys[K_UP]):
                self.player.moveup()
            if(keys[K_DOWN]):
                self.player.movedown()
            if(keys[K_ESCAPE]):
                self.runningG=False
            self.on_loop()
            self.on_render()
            time.sleep(50.0/1000.0);
        self.on_cleanup()

if __name__=="__main__":
    snake=SnakeGame()
    snake.on_execute()
    
