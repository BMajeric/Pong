import pygame
import random
pygame.init()

scrwid = 700
scrlen = 500
win = pygame.display.set_mode((scrwid, scrlen))
pygame.display.set_caption('Pong')


scoreL = 0
scoreR = 0

counter = 0

neg = 1

Music = ['africa.mp3', 'all_star.mp3','believer.mp3', 'deja_vu.mp3','havana.mp3',
         'im_a_mess.mp3','livin_on_a_prayer.mp3', 'moves_like_jagger.mp3',
         'pumped_up_kicks.mp3', 'rick_roll.mp3','sans.mp3', 'telephone.mp3',
         'thunder.mp3', 'watt_is_love.mp3','young_blood.mp3']

playing = random.choice(Music)
music = pygame.mixer.music.load(playing)

pygame.mixer.music.play(-1)
pygame.mixer.music.set_volume(0.125)

hit = pygame.mixer.Sound('oof.wav')
print(pygame.mixer.music.get_volume())

class paddle(object):
    def __init__(self, x, y, width, height):
        self.x = x
        self.y = y
        self.width = width
        self.height = height
        self.vel = 8
    def draw(self, win):
        pygame.draw.rect(win, (255, 255, 255), (self.x, self.y, self.width, self.height))

class ball(object):
    def __init__(self, x, y, radius):
        self.x = x
        self.y = y
        self.radius = radius
        self.velx = -4
        self.vely = 4
    def draw(self, win):
        pygame.draw.circle(win, (255, 255, 255), (self.x, self.y), self.radius)

class end(object):
    def __init__(self, x, y, width, height):
        self.x = x
        self.y = y
        self.width = width
        self.height = height
    def draw(self, win):
        pygame.draw.rect(win, (0, 0, 0), (self.x, self.y, self.width, self.height))

def windowRedraw():
    win.fill((0, 0, 0))
    
    textL = font.render(str(scoreL), 1, (255, 255, 255))
    win.blit(textL, ((scrwid // 2) - 50 - textL.get_width(), 10))

    textR = font.render(str(scoreR), 1, (255, 255, 255))
    win.blit(textR, ((scrwid // 2) + 50, 10))
    
    padL.draw(win)
    padR.draw(win)
    lopta.draw(win)
    krajL.draw(win)
    krajR.draw(win)
    mid.draw(win)
    pygame.display.update()

def reset():
    global neg
    global counter
    #padL.x = 50
    #padL.y = (scrlen // 2) - 40
    #padR.x = scrwid - 50 - 10
    #padR.y = (scrlen // 2) - 40
    lopta.x = scrwid // 2
    lopta.y = scrlen // 2
    neg *= -1
    lopta.velx = -4 * neg
    lopta. vely = 4 * neg
    counter = 0
    

#Mainloop
font = pygame.font.SysFont('OCR A Extended', 100)
run = True

padL = paddle(50, (scrlen // 2) - 40, 10, 80)
padR = paddle(scrwid - 50 - 10, (scrlen // 2) - 40, 10, 80)
lopta = ball(scrwid // 2, scrlen // 2, 5)
krajL = end(0, 0, 40, scrlen)
krajR = end(scrwid - 40, 0, 50, scrlen)
mid = paddle((scrwid // 2) - 3, 0, 6, scrlen)

while run:
    pygame.time.delay(20)
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            run = False
    
    if lopta.y + lopta.radius < 500 and lopta.y - lopta.radius > 0:
        lopta.x += lopta.velx
        lopta.y += lopta.vely
        if lopta.y <= padL.y + 5 + padL.height and lopta.y >= padL.y - 5:
            if lopta.x - lopta.radius <= padL.x + padL.width and lopta.x + lopta.radius >= padL.x:
                hit.play()
                neg *= -1
                counter += 1
                lopta.velx *= -1
                lopta.x += lopta.velx
                lopta.y += lopta.vely
                if counter % 3 == 2:
                    lopta.velx += 1 * neg * -1
                    lopta.vely += 1 * neg
        if lopta.y <= padR.y + 5 + padR.height and lopta.y >= padR.y - 5:
            if lopta.x + lopta.radius >= padR.x and lopta.x - lopta.radius <= padR.x + padR.width:
                hit.play()
                neg *= -1
                counter += 1
                lopta.velx *= -1
                lopta.x += lopta.velx
                lopta.y += lopta.vely
                if counter % 3 == 2:
                    lopta.velx += 1 * neg * -1
                    lopta.vely += 1 * neg
        if lopta.x - lopta.radius < krajL.x + krajL.width:
                reset()
                scoreR += 1
                
        if lopta.x + lopta.radius > krajR.x:
                reset()
                scoreL += 1      
    else:
        lopta.vely *= -1
        lopta.x += lopta.velx
        lopta.y += lopta.vely
    
    keys = pygame.key.get_pressed()
    
    if keys[pygame.K_w] and padL.y > 5:
        padL.y -= padL.vel
    if keys[pygame.K_s] and padL.y < scrlen - padL.height - 5:
        padL.y += padL.vel

    if keys[pygame.K_UP] and padR.y > 5:
        padR.y -= padR.vel
    if keys[pygame.K_DOWN] and padR.y < scrlen - padR.height - 5:
        padR.y += padR.vel

    if scoreL == 10 or scoreR == 10:
        break
    

    windowRedraw()
    
    if scoreL == 7 or scoreR == 7:
        if playing == 'sans.mp3':
            continue
        else:
            playing = 'sans.mp3'
            music = pygame.mixer.music.load(playing)
            pygame.mixer.music.play(-1)
            pygame.mixer.music.set_volume(0.125)


    

pygame.quit()
