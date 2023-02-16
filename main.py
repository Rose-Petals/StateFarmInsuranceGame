import random, time
import pygame
import unicodedata
from pygame.constants import K_BACKSPACE, K_KP_ENTER, KEYDOWN, K_ESCAPE

pygame.init()
clock = pygame.time.Clock()

win = pygame.display.set_mode((900,600))
pygame.display.set_caption("CONfident")
noteRectange = pygame.Rect(200,300,300,50)
font = pygame.font.SysFont(None, 200)

#importing all the photos
submit = pygame.image.load('submit.png').convert_alpha()
uncheck = pygame.image.load('box.png').convert_alpha()
check = pygame.image.load('check.png').convert_alpha()
info = pygame.image.load('info.png').convert_alpha()
compScreen= pygame.image.load('compScreen.png').convert_alpha()
open1 = pygame.image.load('1.png').convert_alpha()
open2 = pygame.image.load('2.png').convert_alpha()
open3 = pygame.image.load('3.png').convert_alpha()
open4 = pygame.image.load('4.png').convert_alpha()
open5 = pygame.image.load('5.png').convert_alpha()
open6 = pygame.image.load('6.png').convert_alpha()
open7 = pygame.image.load('7.png').convert_alpha()
open8 = pygame.image.load('8.png').convert_alpha()
open9 = pygame.image.load('9.png').convert_alpha()
open10 = pygame.image.load('10.png').convert_alpha()
open11 = pygame.image.load('messUp.png').convert_alpha()
open12 = pygame.image.load('11.png').convert_alpha()
open13 = pygame.image.load('12.png').convert_alpha()
open14 = pygame.image.load('13.png').convert_alpha()
open15 = pygame.image.load('14.png').convert_alpha()
open16 = pygame.image.load('15.png').convert_alpha()
open17 = pygame.image.load('10.png').convert_alpha()
open18 = pygame.image.load('16.png').convert_alpha()
open19 = pygame.image.load('17.png').convert_alpha()
open20 = pygame.image.load('messUp3.png').convert_alpha()
open21 = pygame.image.load('18.png').convert_alpha()
open22 = pygame.image.load('19.png').convert_alpha()
open23 = pygame.image.load('20.png').convert_alpha()
open24 = pygame.image.load('21.png').convert_alpha()
open25 = pygame.image.load('22.png').convert_alpha()
open26 = pygame.image.load('23.png').convert_alpha()
open27 = pygame.image.load('10.png').convert_alpha()
open28 = pygame.image.load('24.png').convert_alpha()
open29 = pygame.image.load('26.png').convert_alpha()
open30 = pygame.image.load('27.png').convert_alpha()
open31 = pygame.image.load('28.png').convert_alpha()
open32 = pygame.image.load('29.png').convert_alpha()
open33 = pygame.image.load('10.png').convert_alpha()
open34 = pygame.image.load('31.png').convert_alpha()
open35 = pygame.image.load('messUp5.png').convert_alpha()
open36 = pygame.image.load('32.png').convert_alpha()
open37 = pygame.image.load('33.png').convert_alpha()
open38 = pygame.image.load('35.png').convert_alpha()
open39 = pygame.image.load('36.png').convert_alpha()
open40 = pygame.image.load('messUp4.png').convert_alpha()
open41 = pygame.image.load('39.png').convert_alpha()
open42 = pygame.image.load('38.png').convert_alpha()
card1 = pygame.image.load('Liability.png').convert_alpha()
card2 = pygame.image.load('Collision_Insurance.png').convert_alpha()
card3 = pygame.image.load('Rental_Car.png').convert_alpha()
card4 = pygame.image.load('Emergency_Road.png').convert_alpha()
card5 = pygame.image.load('Rideshare_Driver.png').convert_alpha()
card6 = pygame.image.load('Medical_Payments.png').convert_alpha()
arrow = pygame.image.load('backArrow.png').convert_alpha()
name =[open1, open2, open3, open4, open5, open6, open7,open8, open9,open10, open11, open12, open13, open14, open15, open16, open17,
open18, open19, open20, open21, open22, open23, open24, open25, open26, open27, open28, open29, open30, open31, open31, open32, open33,
open34, open35, open36, open37, open38, open39, open40, open41, open42, compScreen]

check = [uncheck, check, submit,info]
formation=[card1, card2, card3, card4, card5, card6]



class Button():
    def __init__(self, x, y, image):
        self.image = image
        self.rect = self.image.get_rect()
        self.rect.topleft = (x, y)
        self.clicked = False
    def draw(self):
        action = False
        pos = pygame.mouse.get_pos()

        if self.rect.collidepoint(pos):
            if pygame.mouse.get_pressed()[0] == 1 and self.clicked == False:
                self.clicked = True
                time.sleep(0.2)
                action = True

        if pygame.mouse.get_pressed()[0] == 0:
            self.clicked = False


        win.blit(self.image, (self.rect.x, self.rect.y))

        return action



#clickScreen = Button(0, 0, open1)



def draw_text(text, font, color, surface, x, y):
    textobj = font.render(text, 1, color)
    textrect = textobj.get_rect()
    textrect.topleft = (x, y)
    surface.blit(textobj, textrect)


#menu screen funtion
def main():
    run = True
    n=0 

    while run:
        clickScreen = Button(0, 0, open1)
      
        win.fill((189, 189, 189))
        
        if clickScreen.draw():
            n+= 1
            if n ==10:
                player()
            if n ==17:
                player()
            if n ==27:
                player()
            if n==33:
                player()
            
                
        win.blit((name[n]),(0,0))


        pygame.time.delay(100)

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                run = False

        pygame.display.update()

    pygame.quit()

def infocard(x):
    
    backArrow= Button(700,500, arrow)
    running = True
    while running:
        win.blit((formation[x]),(0,0))
        if backArrow.draw():
            running = False



        pygame.display.update()

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
            

        pygame.display.update()


def player():
    running = True
    cb1= 0
    cb2=0
    cb3=0
    cb4=0
    cb5=0
    cb6=0
    base=0
    pygame.time.set_timer(pygame.USEREVENT, 1000)
    cash=font.render((str(base)), True, (0,0,0))
    y=43
    while running:
        win.fill((189, 189, 189))
        win.blit((name[y]),(0,0))
        checkBox1= Button(20,70, check[cb1])
        checkBox2= Button(20,130, check[cb2])
        checkBox3= Button(20,200, check[cb3])
        checkBox4= Button(20,270, check[cb4])
        checkBox5= Button(20,340, check[cb5])
        checkBox6= Button(20,400, check[cb6])
        submitIt= Button(60, 500, check[2])
        info1 = Button(800,70, check[3])
        info2 = Button(800,130, check[3])
        info3 = Button(800,200, check[3])
        info4 = Button(800,270, check[3])
        info5 = Button(800,340, check[3])
        info6 = Button(800,400, check[3])
        if info1.draw():
            infocard(0)
        if info2.draw():
            infocard(1)
        if info3.draw():
            infocard(2)
        if info4.draw():
            infocard(3)
        if info5.draw():
            infocard(4)
        if info6.draw():
            infocard(5)

        if submitIt.draw():
            running= False
        if checkBox1.draw():
            if cb1 ==0:
                base+150
                cb1=1
            else:
                base-150
                cb1=0
        if checkBox2.draw():
            if cb2 ==0:
                base+150
                cb2=1
            else:
                base-150
                cb2=0
        if checkBox3.draw():
            if cb3 ==0:
                base+150
                cb3=1
            else:
                base-150
                cb3=0
        if checkBox4.draw():
            if cb4 ==0:
                base+150
                cb4=1
            else:
                base-150
                cb4=0
        if checkBox5.draw():
            if cb5 ==0:
                base+150
                cb5=1
            else:
                base-150
                cb5=0
        if checkBox6.draw():
            if cb6 ==0:
                base+150
                cb6=1
            else:
                base-150
                cb6=0
        
                
            


        
        pygame.display.update()

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
            

        pygame.display.update()


main()