from pygame import *



clock = time.Clock()
FPS = 60
width = 800
high = 800
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
        if keys[K_LEFT] and self.rect.x > 5:
            self.rect.x -= self.speed
        if keys[K_RIGHT] and self.rect.x < 630:
            self.rect.x += self.speed

game = True
while game:
    for e in event.get():
        if e.type == QUIT:
            game = False
    display.update()

    clock.tick(FPS)
    