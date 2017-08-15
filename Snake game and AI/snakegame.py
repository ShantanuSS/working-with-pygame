from pygame.locals import *
import pygame
class Player:
    x=10
    y=10
    speed=1
    def moveright(self):
        self.x+=self.speed
    def moveleft(self):
        self.x-=self.speed
    def moveup(self):
        self.y-=self.speed
    def movedown(self):
        self.y+=self.speed
class SnakeGame:
    window_width=800
    window_height=600
    player=0

    def __init__(self):
        self.runningG=True
        self.displayG=None
        self.imageG=None
        self.player=Player()
    def on_init(self):
        pygameinit()
        self.displayG=pygame.display.set_mode((self.window_width,self.window_height),pygame.HWSURFACE)
        pygame.display.set_caption('Snake Game for you') #pyagamedisplay
        self.runningG=True
        self.imageG=pygame.image.load("abc.png").convert()
    def on_event(self,event):
        if event.type==QUIT:
            self.runningG=False
    def on_loop(self):
        pass
    def on_render(self):
        self.displayG.fill(0,0,0)
        self.displayG.blit(self.image,(self.player.x,self.player.y))
        pygame.display.flip()
    def on_cleanup(self):
        pygamequit()
    def on_execute(self):
        if self.on_init()==False:
            self.runningG=False
        while (self.running):
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
            self.on_cleanup()

if __name__=="__main__":
    snake=SnakeGame()
    snake.on_execute()
    
    
