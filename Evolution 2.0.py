import pygame,random,time,math

number=2000

pygame.init()
SCREEN_WIDTH, SCREEN_HEIGHT = 1920, 1080
screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))
pygame.display.set_caption("Evolution 2.0")
clock = pygame.time.Clock()

class Brain:
    def __init__(self):
        self.w1=[[random.uniform(-1,1) for _ in range (3)] for _ in range (4)]
        self.b1=[random.uniform(-1,1) for _ in range (4)]
        
        self.w2=[[random.uniform(-1,1) for _ in range (4)] for _ in range (2)]
        self.b2=[random.uniform(-1,1) for _ in range (2)]
        
    def activate(self,x):
        return math.tanh(x)
    
    def think(self,inputs):
        hidden = []
        for i in range (4):
            total=self.b1[i]
            for j in range (3):
                total+=self.w1[i][j]*inputs[j]
            hidden.append(self.activate(total))
            
        output = []
        for i in range (2):
            total=self.b2[i]
            for j in range (4):
                total+=self.w2[i][j]*hidden[j]
            output.append(self.activate(total))
        return output
        
        
           
def colourer(value,lower,upper):
    return int(((value-lower)*255)/(upper-lower))

class Dot:
    def __init__(self,x,y,xv,yv,rgb,brain):
        self.x = x
        self.y = y
        self.xv = xv
        self.yv = yv
        self.rgb = rgb
        self.brain = Brain()
        self.fitness = 960-self.x
        
    def update(self):
        xv_change,yv_change=self.brain.think([self.xv,self.yv,int(self.x//1920),int(self.y//1080)])
        self.xv+=(xv_change)
        self.yv+=(yv_change)
        if self.xv**2>100:
            self.xv=int(self.xv/int(((self.xv/10)**2)**0.5))
        if self.yv**2>100:
            self.yv=int(self.yv/int(((self.yv/10)**2)**0.5))
        if (self.x + self.xv < 1910) and (self.x + self.xv >10):
            self.x += self.xv
        if (self.y + self.yv < 1070) and (self.y + self.yv >10):
            self.y += self.yv
    

def mutate(x, rate=0.1,strength=0.3):
    if random.random()<rate:
        return x+random.uniform(-strength,strength)
    return x






          

def spawn(number):
    dots=[]
    for i in range (number):
        x=random.randint(960,1910)
        y=random.randint(10,1070)
        xv=random.uniform(-5,5)
        yv=random.uniform(-5,5)
        rgb=colourer(xv,-5,5),colourer(yv,-5,5),random.randint(0,255)
        
        dots.append(Dot(x,y,xv,yv,rgb,Brain))
    return dots
      
def move(dots):
    for i in range(len(dots)):
        dots[i].update
    return dots

def kill(dots):
    suvivors=[]
    for dot in dots:
        if dot.x>960:
            suvivors.append(dot)
    print(len(suvivors))
    return suvivors

def makeGrid(dots):
    grid={}
    for dot in dots:
        cx=int(dot.x//50)
        cy=int(dot.y//50)
        grid.setdefault((cx,cy), []).append(dot)
    return grid
    

def brainBreeder(mother,neighbour):
    mBrain=mother.brain
    nBrain=neighbour.brain
    ow1=[]
    ob1=[]
    ow2=[]
    ob2=[]
    for i in range(4):
        chance=random.randint(0,1)
        if chance==0:
            ob1.append(mutate(mBrain.b1[i]))
        if chance==1:
            ob1.append(mutate(nBrain.b1[i]))
        temp=[]
        for j in range(3):
            if chance==0:
                temp.append(mutate(mBrain.w1[i][j]))
            if chance ==1:
                temp.append(mutate(nBrain.w1[i][j]))
        ow1.append(temp)
        
    
    for i in range(2):
        chance=random.randint(0,1)
        if chance==0:
            ob2.append(mutate(mBrain.b2[i])) 
        if chance==1:
            ob2.append(mutate(nBrain.b2[i]))
        temp=[]
        for j in range(4):
            if chance==0:
                temp.append(mutate(mBrain.w2[i][j]))
            if chance ==1:
                temp.append(mutate(nBrain.w2[i][j]))
        ow2.append(temp)
    
    return ow1,ob1,ow2,ob2

def breed(dots,number):
    nextGen=[]
    attempts=0
    while attempts<=number:
        i=random.randint(0,len(dots)-1)
        j=random.randint(0,len(dots)-1)
        mother=dots[i]
        father=dots[j]
        x=random.randint(10,1910)
        y=random.randint(10,1070)
        nxv=(mother.xv+father.xv)/2
        nyv=(mother.yv+father.yv)/2
        rgb=random.randint(0,255),0,random.randint(0,255)
        obrain=brainBreeder(mother,father)
        nextGen.append(Dot(x,y,nxv,nyv,rgb,obrain))
        attempts+=1
    return nextGen
        
                
dots=spawn(number)

running = True
survivors=[]
count=0
times=[]

for simulations in range(300):
    for length in range(100):
        screen.fill((0,0,0))
        for dot in dots:
            dot.update()
            pygame.draw.circle(screen,dot.rgb, (dot.x, dot.y), 5)
        pygame.display.flip()
        clock.tick(60)
    dots=kill(dots)
    survivors.append(len(dots))
    count+=1
    times.append(count)
    dots=breed(dots,number)
print(survivors)
print(times)
        
        
        
            
        
    
        

        
        
        
       
        