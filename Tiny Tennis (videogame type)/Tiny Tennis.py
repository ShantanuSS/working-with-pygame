import pygame
import random
import time
pygame.init() #initializes pygame

red=(255,0,0)
green=(0,255,0)
blue=(0,0,255)
yellow=(255,255,0)
black=(0,0,0)
white=(255,255,255)
orange=(255,127,0)
violet=(127,0,255)
brown=(102,51,0)
screen_width=600
screen_height=400
game_screen=pygame.display.set_mode((screen_width,screen_height))
pygame.display.set_caption("Created for you")
font=pygame.font.SysFont("monospace",75) #or can be any other font too
ballx=int(screen_width/2)
bally=int(screen_height/2)
ball_xv=3
ball_yv=3
ballr=20

paddle1x=10  #creating paddle 1
paddle1y=10
paddle1w=25
paddle1h=100
paddle2x=screen_width-35     #creating paddle 2
paddle2y=10
paddle2w=25
paddle2h=100
scorep1=0
scorep2=0
#logic starts here-
pygame.mouse.set_visible(0)  #make
do=True
while do:
    pressed=pygame.key.get_pressed()
    pygame.key.set_repeat
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            do=False
    if pressed[pygame.K_ESCAPE]:
        do=False
    if pressed[pygame.K_w]:
        paddle1y -=5;
    elif pressed[pygame.K_s]:
        paddle1y +=5
    if pressed[pygame.K_UP]:
        paddle2y -=5
    elif pressed[pygame.K_DOWN]:
        paddle2y +=5


    
    if bally-ballr <=0 or bally+ballr >=screen_height:  #collision of ball with top down of screen
        ball_yv*=-1
    if paddle1y<0:    #collision of paddle 1 with edges of screen
        paddle1y=0
    elif paddle1y+paddle1h >screen_height:
        paddle1y=screen_height-paddle1h
    if paddle2y<0:    #collision of paddle 2 with edges of screen
        paddle2y=0
    elif paddle2y+paddle2h >screen_height:
        paddle2y=screen_height-paddle2h

    if ballx<paddle1x + paddle1w and bally>=paddle1y and bally<=paddle1y+paddle1h: #collision of ball and left paddle
        ball_xv*=-1
    if ballx>paddle2x and bally>=paddle2y and bally<=paddle2y+paddle2h: 
        ball_xv*=-1

    if ballx<=0:                    
        scorep2 +=1
        ballx=int(screen_width/2)
        bally=int(screen_height/2)
    elif ballx>=screen_width:
        scorep1+=1
        ballx=int(screen_width/2)
        bally=int(screen_height/2)
    game_screen.fill(black)
    paddle1=pygame.draw.rect(game_screen,white,(paddle1x,paddle1y,paddle1w,paddle1h),0)
    paddle2=pygame.draw.rect(game_screen,white,(paddle2x,paddle2y,paddle2w,paddle2h),0)
    net=pygame.draw.line(game_screen,yellow,(300,5),(300,400))
    ball=pygame.draw.circle(game_screen,red,(ballx,bally),ballr,0)
    score=font.render(str(scorep1) +" "+str(scorep2),1,white)
    game_screen.blit(score,(screen_width/2-score.get_width()/2,10))
    pygame.display.update()
    time.sleep(0.0179557)
pygame.quit()
