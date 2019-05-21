#Iris Ku & Jessie Liang PD 10
#Escape
#3/26

#for final version hashtag lvl2 while game not over
#pepper needs to repeatly shoot
#Mrs.Margolin we would like to repeatedly shoot in our game before waiting for the other pepper to be off the screen 




from gamelib import*
game = Game(1000,700, "Escape")
bk = Image("cafeteria.jpg",game)
player2 = Animation("Sheet1.png",16,game,128/4,128/4) #pink
player1 = Animation("sheet2.png",12,game,96/3,128/4)    #blue 
teacher = Animation("sheet3.png",12,game,108/3,144/4)
logo = Image("logo.png",game)
start = Image("lft2.png",game)
cloud = Image("cloud.jpg",game)
htpp = Image("htpp.png", game)

#sound
shoot = Sound("shoot.wav",1)
bgm = Sound("222.wav",2)
collision = Sound("111.wav",3)
bubble = Sound("bbbubble.wav",4)


player1.visible = True
player2.visible = True 
carrot = []

pineapple = []
orange = []
avocado = []
pepper = []
pepper2 = []
pepper3 = []

bk.resizeTo(1000,700)
player1.resizeBy(380)
player2.resizeBy(380)
teacher.resizeBy(380)
logo.resizeBy(80)
cloud.resizeTo(1000,200)

teacher.setSpeed(14,149)

#teacher.moveTo(500,100)


#start screen
while not game.over:
    game.processInput()
    bgm.play()
    bk.draw()
    logo.draw()
    logo.y = 200
    start.draw()
    #if keys.Pressed[K_SPACE]:
        #game.over = True

    if mouse.LeftClick:
        bubble.play()
        game.over = True

        
    
    
    game.update(30)
game.over = False



#How To Play Screen
while not game.over:
    game.processInput()
    
    
    htpp.resizeTo(900,600)
    htpp.draw()
    if keys.Pressed[K_SPACE]:
        bubble.play()
        game.over = True

    

    game.update(30)
game.over = False





#level 1
player1.moveTo(200,600)
player2.moveTo(800,600)

player1.health = 100
player2.health = 100
key = 0

for index in range(5):
    carrot.append(Image("carrot.png",game))
for index in range(5):
    orange.append(Image("orange.png",game))
for index in range(5):
    pineapple.append(Image("pineapple.png",game))
for index in range(5):
    avocado.append(Image("avocado.png",game))
for index in range(50):
    pepper.append(Image("pepper.png",game))


for index in range(50):
    x = randint(100,900)
    y = -randint(100,2000)
    s = randint(2,3)
    a = -randint(1,180)
    pepper[index].moveTo(x,y)
    pepper[index].setSpeed(s,180)
    pepper[index].resizeBy(-90)
    #x+=200

for index in range(5):
    x = randint(100,900)
    y = -randint(100,2000)
    s = randint(2,3)
    carrot[index].moveTo(x,y)
    carrot[index].setSpeed(s,180)
    carrot[index].resizeBy(-70)

for index in range(5):
    x = randint(100,900)
    y = -randint(100,2000)
    s = randint(2,3)
    pineapple[index].moveTo(x,y)
    pineapple[index].setSpeed(s,180)
    pineapple[index].resizeBy(-70)
    
for index in range(5):
    x = randint(100,900)
    y = -randint(100,2000)
    s = randint(2,3)
    avocado[index].moveTo(x,y)
    avocado[index].setSpeed(s,180)
    avocado[index].resizeBy(-75)

for index in range(5):
    x = randint(100,900)
    y = -randint(100,2000)
    s = randint(2,3)
    orange[index].moveTo(x,y)
    orange[index].setSpeed(s,180)
    orange[index].resizeBy(-75)

    

    
    
while not game.over:
    game.processInput()
    bk.draw()
    
    player1.draw()
    player2.draw()
    cloud.y = 0
    #move player1
    if keys.Pressed[K_LEFT]:
        player2.x-=6
    if keys.Pressed[K_RIGHT]:
        player2.x+=6
    if keys.Pressed[K_UP]:
        player2.y-=6
    if keys.Pressed[K_DOWN]:
        player2.y+=6
    #move player2
    if keys.Pressed[K_a]:
        player1.x-=6
    if keys.Pressed[K_d]:
        player1.x+=6
    if keys.Pressed[K_w]:
        player1.y-=6
    if keys.Pressed[K_s]:
        player1.y+=6
    #pepper
    for index in range(50):
        pepper[index].move()
    #food
    for index in range(5):
        carrot[index].move()
    for index in range(5):
        pineapple[index].move()
    for index in range(5):
        avocado[index].move()
    for index in range(5):
        orange[index].move()
        
    #pepper disapear & minus health    
    for index in range(50):
        if pepper[index].collidedWith(player1,"rectangle"):
            pepper[index].visible = False
            player1.health-=5
        
            
        if pepper[index].collidedWith(player2,"rectangle"):
            pepper[index].visible = False
            player2.health-=5



    #carrot disapear 
    for index in range(5):
        if carrot[index].collidedWith(player1,"circle") or carrot[index].collidedWith(player2,"circle"):
            key+=1
            carrot[index].visible = False
            collision.play()
            
    #pineapple disapear
    for index in range(5):
        if pineapple[index].collidedWith(player1,"circle") or pineapple[index].collidedWith(player2,"circle"):
            key+=1
            pineapple[index].visible = False
            collision.play()

    #orange disapear
    for index in range(5):
        if orange[index].collidedWith(player1, "circle") or orange[index].collidedWith(player2, "circle"):
            key+=1
            orange[index].visible= False
            collision.play()
            

    #avocado
    for index in range(5):
        if avocado[index].collidedWith(player1, "circle") or avocado[index].collidedWith(player2, "circle"):
            key +=1
            avocado[index].visible= False
            collision.play()
    
    #health
    if player1.health == 0:
        player1.visible = False

    if player2.health == 0:
        player2.visible = False

    if player1.health == 0 and player2.health == 0:
        game.over= True 

    if key == 15:
        game.over = True        
        

        
    cloud.draw()
    game.drawText("Player1.health:"+str(player1.health),10,10)
    game.drawText("Player2.health:"+str(player2.health),10,30)
    game.drawText("key:"+str(key),10,50)



    if player1.health<0 and player2.health<0:
        game.over=True 
    game.update(30)

game.over = False


#level 2

player1.moveTo(200,600)
player2.moveTo(800,600)

for index in range(50):
    pepper2.append(Image("pepper.png",game))
    

for index in range(50): 
    pepper2[index].resizeBy(-90)
    pepper2[index].setSpeed(10,0)
    pepper2[index].visible = False


for index in range(50):
    pepper3.append(Image("pepper.png",game))
    

for index in range(50): 
    pepper3[index].resizeBy(-90)
    pepper3[index].setSpeed(10,0)
    pepper3[index].visible = False

teacher.health = 100

egg = []
cegg = []
for index in range(10):
    egg.append(Image("egg.png", game))
for index in range(10):
    cegg.append(Animation("ceggg.png",16,game,144/4,144/4))

for index in range(10):
    e = randint(0,360)
    s = randint(1,8)
    egg[index].setSpeed(s,e)
    egg[index].moveTo(teacher.x, teacher.y)
    #cegg[index].moveTo(egg[index].x, egg[index].y)
    cegg[index].resizeBy(50)
    egg[index].resizeBy(50)



      
while not game.over: #and key == 15:
    game.processInput()
    bgm.play()
    bk.draw()
    player1.draw()
    player2.draw()
    x = randint(100,900)
    y = randint(100,600)
    for index in range(10):
        egg[index].move()
        cegg[index].draw()
    teacher.move(True)


    
    #move player2
    if keys.Pressed[K_LEFT]:
        player2.x-=6
    if keys.Pressed[K_RIGHT]:
        player2.x+=6
    if keys.Pressed[K_UP]:
        player2.y-=6
    if keys.Pressed[K_DOWN]:
        player2.y+=6
    #move player1
    if keys.Pressed[K_a]:
        player1.x-=6
    if keys.Pressed[K_d]:
        player1.x+=6
    if keys.Pressed[K_w]:
        player1.y-=6
    if keys.Pressed[K_s]:
        player1.y+=6
    #teacher.moveTo(x,y)
    #if teacher.collidedWith(player1, "rectangle"):
        #player1.health-= 5
    #if teacher.collidedWith(player2, "rectangle"):
        #player2.health-=5


    #egg move behine the teacher

    for index in range(10):
        #cegg[index].moveTo(egg[index].x, egg[index].y)
        egg[index].visible = True
        cegg[index].visible = False 
   
        if egg[index].collidedWith(player1):
            cegg[index].moveTo(player1.x,player1.y-20)
            egg[index].visible = False
            cegg[index].visible = True
            egg[index].moveTo(teacher.x,teacher.y)
            player1.health-=2
            
        
        if egg[index].collidedWith(player2):
            cegg[index].moveTo(player2.x,player2.y-20)
            egg[index].moveTo(teacher.x,teacher.y)
            egg[index].visible = False
            cegg[index].visible = True
            player2.health-=2

    for index in range(10):
        if egg[index].isOffScreen():
            egg[index].moveTo(teacher.x,teacher.y)
            egg[index].move()
    

    #for index in range(50):
        #pepper[index].setSpeed(10,180)

    if pepper2[index].collidedWith(teacher,"rectangle"):
        pepper2[index].visible=False
        teacher.health-=5
        
    if pepper3[index].collidedWith(teacher,"rectangle"):
        pepper3[index].visible=False
        teacher.health-=5

        
    for index in range(50):
        pepper2[index].move()
        if keys.Pressed[K_SPACE]:
            shoot.play()
            pepper2[index].moveTo(player1.x, player1.y)
            pepper2[index]. visible = True
            
                    
            
    for index in range(50):
        pepper3[index].move()
        if keys.Pressed[K_KP_ENTER]:
            shoot.play()
            pepper3[index].moveTo(player2.x, player2.y)
            pepper3[index].visible = True
        
    '''if pepper2[index].collidedWith(teacher,"rectangle"):
        pepper2[index].visible=False
        teacher.health-=5
    if pepper3[index].collidedWith(teacher,"rectangle"):
        pepper3[index].visible7=False
        teacher.health-=5'''
        
    if teacher.health < 0:
        game.over = True

    if player2.health < 0:
        player2.visible = False

    if player1.health < 0:
        player1.visible = False


    if player1.health < 0 and player2.health < 0:
        game.over = True

    game.drawText("teacher.health:"+str(teacher.health),10,10)
    game.drawText("Player1.health:"+str(player1.health),10,30)
    game.drawText("Player2.health:"+str(player2.health),10,50)


                
    game.update(30)
game.over = False

#winning end screen

win = Animation("win.png",12,game,138/3,184/4)
win.resizeBy(1500)
hg = Image("hg.png",game)
hg2 = Image("hg.png",game)
hg.resizeBy(50)
hg2.resizeBy(50)
while not game.over and teacher.health<0:
    game.processInput()

    bk.draw()
    player1.draw()
    player2.draw()
    player1.visible=True
    player2.visible=True
    player1.moveTo(200,600)
    player2.moveTo(800,600)
    hg.draw()
    hg2.draw()
    hg.moveTo(200,550)
    hg2.moveTo(800,550)
    win.draw()



    game.update(30)
    
#losing end screen

lose = Animation("Lose.png",8,game,96/3,96/3)
lose.resizeBy(1500)

while not game.over:
    game.processInput()
    bk.draw()
    player1.draw()
    player2.draw()
    player1.moveTo(200,600)
    player2.moveTo(800,600)
    #game.displayTime(60)
    lose.draw()
    lose.moveTo(500,250)
    
    game.update(30)
    
game.quit()
