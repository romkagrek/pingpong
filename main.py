from pygame import *



clock = time.Clock()
FPS = 60
width = 1000
high = 500
window = display.set_mode((width, high))
display.set_caption("Пинг - понг")
window.fill((255,255,255))

class GameSprite(sprite.Sprite): 
    def __init__(self, img, speed, x, y, w, h):
        super().__init__()
        self.image = transform.scale(image.load(img), (w, h))
        self.speed = speed
        self.rect = self.image.get_rect()
        self.rect.x = x
        self.rect.y = y
    def reset(self):
        window.blit(self.image, (self.rect.x, self.rect.y))

class Player(GameSprite):
    def update(self):
        keys = key.get_pressed()
        if keys[K_UP] and self.rect.y > 0:
            self.rect.y -= self.speed
        if keys[K_DOWN] and self.rect.y < width - 500:
            self.rect.y += self.speed
    def update2(self):
        keys = key.get_pressed()
        if keys[K_w] and self.rect.y > 0:
            self.rect.y -= self.speed
        if keys[K_s] and self.rect.y < width - 500:
            self.rect.y += self.speed
a = Player("walltwo.png", 10, 10, 100, 30, 173)
b = Player("walltwo.png", 10, 950, 100, 30, 173)
ball = GameSprite("ball.png", 5, 400, 100, 50, 50) 
font.init()
font = font.Font(None, 35)
lose1 = font.render('PLAYER 1 LOSE!', True, (188,0,0))
lose2 = font.render('PLAYER 2 LOSE!', True, (188,0,0))   
speed_x = 3
speed_y = 3
game = True
finish = False
while game:
    for e in event.get():
        if e.type == QUIT:
            game = False
    window.fill((255,255,255))
    if finish != True:
        a.update()
        b.update2()
        a.reset()
        a.update()
        b.reset()
        b.update2()
        ball.reset()
        ball.rect.x += speed_x
        ball.rect.y += speed_y
        
        if sprite.collide_rect(a, ball) or sprite.collide_rect(b, ball):
            speed_x *= -1.01
            speed_y *= 1.01
        
        if ball.rect.y > high-50 or ball.rect.y < 0:
            speed_y *= -1
        if ball.rect.x < 0:
            finish = True
            window.blit(lose1, (400,200))
        if ball.rect.x > width:
            finish = True
            window.blit(lose2, (400,200))
        display.update()
    clock.tick(FPS)
    