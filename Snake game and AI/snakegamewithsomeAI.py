#here we have to add a Computer Player

class Computer:
    x=[0]
    y=[0]
    step=44
    direction=0
    #speed=1
    length=3
    updatecountmax=2
    updatecount=0
    def __init__(self,length):
        self.length=length
        for i in range(0,2000):
            self.x.append(-100)
            self.y.append(-100)
            #initial pos ;no collisions
        self.x[1]=1*44
        self.x[2]=2*44
    def update(self):
        self.updatecount+=1
        if  self.updatecount > self.updatecountmax:  #update prev position   
            for i in range(self.length-1,0,-1):
                #print ("self.x["+ str(i)+"]=self.x["+str(i-1)+"]")
                self.x[i]=self.x[i-1]
                self.y[i]=self.y[i-1]
            #update head of snake
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











    def on_loop(self):
        self.player.update()
        self.computer.update #this
        #pass
        for i in range(0,self.player.length): 
            if self.game.isCollision(self.apple.x,self.apple.y,self.player.x[i],self.player.y[i],44):
                self.apple.x=randint(2,9)*44
                self.apple.y=randint(2,9)*44
                self.player.length+=1
        for i in range(2,self.player.length):  
            if self.game.isCollision(self.player.x[0],self.player.y[0],self.player.x[i],self.player.y[i],40):
                print("You lose! Collision")
                print("x[0]("+ str(self.player.x[0]) +","+str(self.player.y[0])+")")
                print("x["+str(i)+"]("+str(self.player.x[i])+","+str(self.player.y[i])+")")
                exit(0)

        pass                
    
    def target(Self,dx,dy):   #this func will go to destintion and neglect any obstacles
        if self.x[0] >dx:
            self.moveleft()
        if self.x[0] <dx:
            self.moveright()
        if self.x[0] ==dx:
            if self.y[0] <dy:
                self.movedown()
            if self.y[0]>dy:
                self.moveup()

        
                
        
        

    
