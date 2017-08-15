from pygame.locals import *
import pygame
import time

class Player:
    #x=10
    #y=10
    x=[]
    y=[]
    step=44
    direction=0
    #speed=1
    length=3
    updatecountmax=2
    updatecount=0
    def __init__(self,length):
        self.length=length
        for i in range(0,length):
            self.x.append(0)
            self.y.append(0)
    def update(self):
        self.updatecount+=1
        if  self.updatecount > self.updatecountmax:
            for i in range(self.length-1,0,-1):
                print ("self.x["+ str(i)+"]=self.x["+setr(i-1)+"]")
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
        #self.x+=self.speed
        self.direction=0
    def moveleft(self):
        #self.x-=self.speed
        self.direction=1
    def moveup(self):
        #self.y-=self.speed
        self.direction=2
    def movedown(self):
        #self.y+=self.speed
        self.direction=3
    def draw(self,surface,image):
        for i in range(0,self.length):
            surface.blit(image,(self.x[i],self.y[i]))
class SnakeGame:
    window_width=800
    window_height=600
    player=0

    def __init__(self):
        self.runningG=True
        self.displayG=None
        self.imageG=None
        self.player=Player(10)
    def on_init(self):
        pygame.init()
        self.displayG=pygame.display.set_mode((self.window_width,self.window_height),pygame.HWSURFACE)
        pygame.display.set_caption('Snake Game for you') #pyagamedisplay
        self.runningG=True
        self.imageG=pygame.image.load("pygame.png").convert()
    def on_event(self,event):
        if event.type==QUIT:
            self.runningG=False
    def on_loop(self):
        pass
    def on_render(self):
        self.displayG.fill((0,0,0))
        #self.displayG.blit(self.imageG,(self.player.x,self.player.y))
        self.player.draw(self.displayG,self.imageG)
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
        time.sleep(50.0/1000.0)
        self.on_cleanup()

if __name__=="__main__":
    snake=SnakeGame()
    snake.on_execute()
    