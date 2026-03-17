import pygame,random,time,math

number=2000

pygame.init()
SCREEN_WIDTH, SCREEN_HEIGHT = 1920, 1080
screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))
pygame.display.set_caption("Evolution 2.0")
clock = pygame.time.Clock()


def colourer(value,lower,upper):
    return int(((value-lower)*255)/(upper-lower))

class Dot:
    def __init__(self,x,y,xv,yv,rgb):
        self.x = x
        self.y = y
        self.xv = xv
        self.yv = yv
        self.rgb = rgb
        
    def update(self):
        if (self.x + self.xv < 1910) and (self.x + self.xv >10):
            self.x += self.xv
        if (self.y + self.yv < 1070) and (self.y + self.yv >10):
            self.y += self.yv
    

           
def spawn(number):
    dots=[]
    for i in range (number):
        x=random.randint(10,1910)
        y=random.randint(10,1070)
        xv=random.uniform(-5,5)
        yv=random.uniform(-5,5)
        rgb=colourer(xv,-5,5),colourer(yv,-5,5),random.randint(0,255)
        
        dots.append(Dot(x,y,xv,yv,rgb))
    return dots
      
def move(dots):
    for i in range(len(dots)):
        dots[i].update
    return dots

def kill(dots):
    suvivors=[]
    for dot in dots:
        if dot.y>540:
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
    

def breed(dots,number):
    grid=makeGrid(dots)
    nextGen=[]
    attempts=0
    while attempts<=number:
        i=random.randint(0,len(dots)-1)
        mother=dots[i]
        cell=(int(mother.x//50)),(int(mother.y)//50)
        neighbours=grid[cell]
        if len(neighbours)==0:
            pass
        distances=[]
        for neighbour in neighbours:
            distances.append(int((((mother.x-neighbour.x)**2) + ((mother.y-neighbour.y)**2))**0.5))
        distances.sort()
        lowest=distances[0]
        index=distances.index(lowest)
        x=random.randint(10,1910)
        y=random.randint(10,1070)
        nxv=(mother.xv+neighbours[index].xv)/2
        nyv=(mother.yv+neighbours[index].yv)/2
        rgb=colourer(nxv,5,-5),colourer(nyv,-5,5),random.randint(0,255)
        nextGen.append(Dot(x,y,nxv,nyv,rgb))
        attempts+=1
    return nextGen
        
                
dots=spawn(number)

running = True
survivors=[]
count=0
times=[]
while running:
    for event in pygame.event.get():
        if event.type==pygame.QUIT:
            running=False
    for simulations in range(10):
        for length in range(600):
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