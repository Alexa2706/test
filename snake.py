import pygame
import random
from queue import Queue

width, height = 1280, 720
size_rectangle = 40
size_fruit = 20
move = 40
pygame.init()
screen = pygame.display.set_mode((width, height))
pygame.display.set_caption('Snake game')
x, y = 0, 0
dx, dy = 0, 0
qs = Queue()
#x, y -> predstavlaju kordinate gornjeg levog coska glave
class Snake:
    data = []
    def __init__(self, x, y):
        self.x = x
        self.y = y
        Snake.data.append(self)

    def move(self, dx, dy):
        self.x += dx
        self.y += dy
        if self.y < 0: #gornji zid
            self.y = height - size_rectangle
        elif self.y > height: #donji zid
            self.y = 0
        elif self.x < 0: #levi zid
            self.x = width - size_rectangle
        elif self.x > width: #desni zid
            self.x = 0

    def collides(self, x, y):
        return self.x <= x and self.y <= y and self.x + size_rectangle >= x and self.y + size_rectangle >= y

head = Snake(x, y)
frx, fry = random.randint(0, int(width / move) - 1) * move + size_fruit, random.randint(0, int(height / move) - 1) * move + size_fruit

while True:
    clock = pygame.time.Clock()
    clock.tick(12)
    x += dx
    y += dy
    screen.fill((0, 0, 0))
    pygame.display.flip()
    cnt = 0
    for snk in Snake.data:
        snk.move(dx, dy)
        pygame.draw.rect(screen, (0, 255, 0), (snk.x, snk.y, size_rectangle, size_rectangle))
        if snk.collides(frx, fry):
            cnt += 1

    assert cnt <= 1
    if cnt == 1:
        if dx != 0 or dy != 0:
            frx, fry = random.randint(0, int(width / move) - 1) * move + size_fruit, random.randint(0, int(height / move) - 1) * move + size_fruit
            if dx == -move:
                Snake(Snake.data[-1].x + size_rectangle, Snake.data[-1].y)
            elif dx == +move:
                Snake(Snake.data[-1].x - size_rectangle, Snake.data[-1].y)
            elif dy == -move:
                Snake(Snake.data[-1].x, Snake.data[-1].y + size_rectangle)
            else:
                assert dy == +move
                Snake(Snake.data[-1].x, Snake.data[-1].y - size_rectangle)

    pygame.draw.circle(screen, (255, 0, 0), (frx, fry), size_fruit)
    pygame.display.update()
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
        elif event.type == pygame.KEYDOWN:
            if event.key == pygame.K_LEFT:
                dx, dy = -move, 0
            elif event.key == pygame.K_RIGHT:
                dx, dy = move, 0
            elif event.key == pygame.K_UP:
                dx, dy = 0, -move
            elif event.key == pygame.K_DOWN:
                dx, dy = 0, +move