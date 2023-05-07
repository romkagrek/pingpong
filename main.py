from pygame import *



clock = time.Clock()
FPS = 60
width = 800
high = 600
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
        if keys[K_DOWN] and self.rect.y < width - 80:
            self.rect.y += self.speed
    def update2(self):
        keys = key.get_pressed()
        if keys[K_W] and self.rect.y > 0:
            self.rect.y -= self.speed
        if keys[K_S] and self.rect.y < width - 80:
            self.rect.y += self.speed
a = Player("wall.png", 25, 0, 200, 150, 300)
game = True
while game:
    for e in event.get():
        if e.type == QUIT:
            game = False
    a.reset()
    a.update()
    display.update()

    clock.tick(FPS)
    