import pygame, sys ,random,time
from pygame.locals import QUIT

creNum=500

pygame.init()
SCREEN_WIDTH, SCREEN_HEIGHT = 1920, 1080
screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))
pygame.display.set_caption("Evolution 2.0")
clock = pygame.time.Clock()
running = True

def colourer(value,lower,upper):
    return int(((value-lower)*255)/(upper-lower))
def spawn(creNum):
    creatures=[]
    for i in range (creNum):
        creature={}
        creature["xVel"]=random.randint(-10,10)
        creature["yVel"]=random.randint(-10,10)
        creature["spontenuity"]=random.randint(0,2000)
        creature["x"]=random.randint(0,1920)
        creature["y"]=random.randint(0,1080)
        rgb=(colourer(creature["xVel"],-10,10),colourer(creature["yVel"],-10,10),colourer(creature["spontenuity"],0,2000))
        #rgb=(colourer(creature["xVel"],-5,5),colourer(creature["yVel"],-5,5),random.randint(0,255))
        creature["colour"]=rgb
        creatures.append(creature)
        pygame.draw.circle(screen, creature["colour"], (creature["x"],creature["y"]), 5)
    pygame.display.flip()
    return creatures


def move(creatures):
    for n in range (150):
        #time.sleep(0.005)
        for i in range (len(creatures)):
            pygame.draw.circle(screen, (0,0,0), (creatures[i]["x"],creatures[i]["y"]), 5)
            if (creatures[i]["x"] + creatures[i]["xVel"] < 1910) and (creatures[i]["x"] + creatures[i]["xVel"] >10):
                creatures[i]["x"]+=creatures[i]["xVel"]
            if (creatures[i]["y"] + creatures[i]["yVel"] < 1070) and (creatures[i]["y"] + creatures[i]["yVel"] >10):
                creatures[i]["y"]+=creatures[i]["yVel"]
            if creatures[i]["spontenuity"]>0:
                chance=random.randint(1,creatures[i]["spontenuity"])
                if chance==1:
                    creatures[i]["xVel"]=random.randint(-10,10)
                    creatures[i]["yVel"]=random.randint(-10,10)
                        
            pygame.draw.circle(screen, creatures[i]["colour"], (creatures[i]["x"],creatures[i]["y"]), 5)
            pygame.display.flip()
    return creatures

def breed(creatures,creNum):
    creature={}
    newCreatures=[]
    for i in range(creNum):
        mother=random.randint(0,(len(creatures)-1))
        father=random.randint(0,(len(creatures)-1))
        creature["xVel"]=int((creatures[mother]["xVel"]+creatures[father]["xVel"])/2)
        creature["yVel"]=int((creatures[mother]["yVel"]+creatures[father]["yVel"])/2)
        creature["spontenuity"]=int((creatures[mother]["spontenuity"]+creatures[father]["spontenuity"])/2)
        creature["x"]=random.randint(0,1910)
        creature["y"]=random.randint(0,1070)
        rgb=(colourer(creature["xVel"],-10,10),colourer(creature["yVel"],-10,10),colourer(creature["spontenuity"],0,2000))
        #rgb=(colourer(creature["xVel"],-5,5),colourer(creature["yVel"],-5,5),random.randint(0,255))
        creature["colour"]=rgb
        newCreatures.append(creature)
        pygame.draw.circle(screen, creature["colour"], (creature["x"],creature["y"]), 5)
        creature={}
    pygame.display.flip()
    return newCreatures
        
def killLeft(creatures):
    for i in range(len(creatures)-1,-1,-1):
        if creatures[i]["x"]<960:
            pygame.draw.circle(screen, (0,0,0), (creatures[i]["x"],creatures[i]["y"]), 5)
            pygame.display.flip()
            creatures.pop(i)
    print(len(creatures))
    time.sleep(2)
    for i in range (len(creatures)):
        pygame.draw.circle(screen, (0,0,0), (creatures[i]["x"],creatures[i]["y"]), 5)
    pygame.display.flip()
    #time.sleep(1)
    return creatures

def killTop(creatures):
    for i in range(len(creatures)-1,-1,-1):
        if creatures[i]["y"]>540:
            pygame.draw.circle(screen, (0,0,0), (creatures[i]["x"],creatures[i]["y"]), 5)
            pygame.display.flip()
            creatures.pop(i)
            pygame.display.flip()
    #print(len(creatures))
    time.sleep(2)
    for i in range (len(creatures)):
        pygame.draw.circle(screen, (0,0,0), (creatures[i]["x"],creatures[i]["y"]), 5)
    pygame.display.flip()
    time.sleep(1)
    return creatures


def run(creatures,creNum):
    creatures=move(creatures)
    creatures=killLeft(creatures)
    #creatures=killTop(creatures)
    creatures=breed(creatures,creNum)
    return creatures

            

def simulate(creNum):
    creatures=spawn(creNum)
    for i in range(500):
        creatures=run(creatures,creNum)
        
        
    
simulate(creNum)
pygame.display.flip()



while running:
    for event in pygame.event.get():
        if event.type == QUIT:
            running = False

pygame.quit()
sys.exit()
    
