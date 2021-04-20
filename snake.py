import math,random,sys,pygame
pygame.init()
size=width,height=600,600
Window=pygame.display.set_mode(size)
class redblock:
    def __init__(self,x,y,speed,width,height):
        self.x=x;
        self.y=y;
        self.speed=speed
        self.width=width
        self.height=height
blocks=[redblock(39,39,[20,0],22,22)]
blocks+=[redblock(blocks[0].x+2,blocks[0].y-18,[0,20],18,18)]
blocks+=[redblock(blocks[1].x,blocks[1].y-20,[0,20],18,18)]
isfood=0
time=100
curlen=len(blocks)
coord=[]
for x in range(0,width,20):
    for y in range(0,height,20):
        coord+=[(x,y)]
flag=0
x1=10
y1=50
size1=36
music=pygame.mixer.music.load("music.mp3")
pygame.mixer.music.set_volume(0.25)
pygame.mixer.music.play(loops=-1,start=0.0)
while 1:
    pygame.time.delay(time)
    for event in pygame.event.get():
        if event.type == pygame.QUIT: sys.exit()
    font1=pygame.font.SysFont('arial', 36)
    if flag:
        flag=0
        blocks=[redblock(39,39,[20,0],22,22)];blocks+=[redblock(blocks[0].x+2,blocks[0].y-18,[0,20],18,18)];blocks+=[redblock(blocks[1].x,blocks[1].y-20,[0,20],18,18)]
        time=100
        size1=36
        x1=10
        y1=50
        pygame.mixer.music.unpause( )
    if time==1500:
        size1=100
        font1=pygame.font.SysFont('arial', size1)
        x1=width/2-225
        y1=height/2-95
        text1=font1.render("Game Over!!",0,(255,255,255))
        flag=1
        Window.blit(text1,(x1,y1))
        pygame.display.flip()
    else:
        text1=font1.render('Points:'+str(len(blocks)),0,(255,255,255))
    keys=pygame.key.get_pressed()
    if blocks[0].speed[0]!=0:
        if keys[pygame.K_DOWN]:
                if blocks[1].speed!=[0,-20]: blocks[0].speed=[0,20]
        if keys[pygame.K_UP]:
                if blocks[1].speed!=[0,20]: blocks[0].speed=[0,-20]
    else:
        if keys[pygame.K_RIGHT]:
                if blocks[1].speed!=[-20,0]: blocks[0].speed=[20,0]
        if keys[pygame.K_LEFT]:
                if blocks[1].speed!=[20,0]: blocks[0].speed=[-20,0]
    if (len(blocks)>curlen):
        time-=1
    curlen=len(blocks)
    if not isfood:
        rand=coord[:]
        for crd in blocks:
            if (crd.x-1,crd.y-1) in rand or (crd.x+1,crd.y+1) in rand:
                try:
                    rand.remove((crd.x-1,crd.y-1))
                except:
                    try:
                        rand.remove((crd.x+1,crd.y+1))
                    except:
                        "Nothing"
        rand1=random.randint(0,len(rand))
        pos=[rand[rand1][0],rand[rand1][1]]
        isfood=1
    for crd in blocks:
        if crd!=blocks[0]:
            if (crd.x-1,crd.y-1)==(blocks[0].x+1,blocks[0].y+1):
                time=1500
                pygame.mixer.music.pause( )
    if blocks[0].x+1==0 and blocks[0].speed[0]==-20 or blocks[0].x+21==width and blocks[0].speed[0]==20 or blocks[0].y+1==0 and blocks[0].speed[1]==-20 or blocks[0].y+21==height and blocks[0].speed[1]==20:
        time=1500
        pygame.mixer.music.pause( )
    if time==1500: continue
    if blocks[0].x+1==pos[0] and blocks[0].y+1==pos[1]:
            if blocks[len(blocks)-1].speed==[0,20]:
                blocks+=[redblock(blocks[len(blocks)-1].x,blocks[len(blocks)-1].y-20,[0,20],18,18)]
            if blocks[len(blocks)-1].speed==[0,-20]:
                blocks+=[redblock(blocks[len(blocks)-1].x,blocks[len(blocks)-1].y+20,[0,-20],18,18)]
            if blocks[len(blocks)-1].speed==[20,0]:
                blocks+=[redblock(blocks[len(blocks)-1].x-20,blocks[len(blocks)-1].y,[20,0],18,18)]
            if blocks[len(blocks)-1].speed==[-20,0]:
                blocks+=[redblock(blocks[len(blocks)-1].x+20,blocks[len(blocks)-1].y,[-20,0],18,18)]
            isfood=0
    for i in range(len(blocks)):
        blocks[i].x+=blocks[i].speed[0]
        blocks[i].y+=blocks[i].speed[1]
    for i in range(1,len(blocks)):
        if abs(blocks[i].speed[0]):
            if (abs(blocks[i].x-blocks[i-1].x)<=2):
                if blocks[i].y<blocks[i-1].y:
                    blocks[i].speed=[0,20]
                else:
                    blocks[i].speed=[0,-20]
        if abs(blocks[i].speed[1]):
            if abs(blocks[i].y-blocks[i-1].y)<=2:
                if blocks[i].x<blocks[i-1].x:
                    blocks[i].speed=[20,0]
                else:
                    blocks[i].speed=[-20,0]
    '''for i in range(len(blocks)):
        if blocks[i].x+blocks[i].width<0:
            blocks[i].x=width;
        if blocks[i].x>width:
            blocks[i].x=0-blocks[i].width
        if blocks[i].y+blocks[i].height<0:
            blocks[i].y=height
        if blocks[i].y>height:
            blocks[i].y=0-blocks[i].height
    '''
    Window.fill((50,25,50))
    for x in range(0,width,20):
        for y in range(0,height,20):
            pygame.draw.rect(Window,(100,50,100),(x+0.1,y+0.1,20-0.2,20-0.2))
    pygame.draw.rect(Window,(0,200,0),(pos[0],pos[1],20,20))
    pygame.draw.rect(Window,(160,0,0),(blocks[0].x,blocks[0].y,blocks[0].width,blocks[0].height))
    for i in range(1,len(blocks)):
        pygame.draw.rect(Window,(200,0,0),(blocks[i].x,blocks[i].y,blocks[i].width,blocks[i].height))
    if (blocks[0].speed==[20,0]):
        pygame.draw.rect(Window,(255,255,255),(blocks[0].x+10,blocks[0].y+3.5,5,5))
        pygame.draw.rect(Window,(255,255,255),(blocks[0].x+10,blocks[0].y+13.5,5,5))
    if (blocks[0].speed==[-20,0]):
        pygame.draw.rect(Window,(255,255,255),(blocks[0].x+blocks[0].width-15,blocks[0].y+3.5,5,5))
        pygame.draw.rect(Window,(255,255,255),(blocks[0].x+blocks[0].width-15,blocks[0].y+13.5,5,5))
    if (blocks[0].speed==[0,20]):
        pygame.draw.rect(Window,(255,255,255),(blocks[0].x+3.5,blocks[0].y+10,5,5))
        pygame.draw.rect(Window,(255,255,255),(blocks[0].x+13.5,blocks[0].y+10,5,5))
    if (blocks[0].speed==[0,-20]):
        pygame.draw.rect(Window,(255,255,255),(blocks[0].x+3.5,blocks[0].y+blocks[0].height-15,5,5))
        pygame.draw.rect(Window,(255,255,255),(blocks[0].x+13.5,blocks[0].y+blocks[0].height-15,5,5))
    Window.blit(text1,(x1,y1))
    pygame.display.flip()
