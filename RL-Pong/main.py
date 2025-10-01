import pygame as pg 
import sys

pg.init()
WIDTH, HEIGHT = 1200, 800

#color
BLUE = (0, 0, 121)
PALE_YELLOW = (255, 255, 150)
WHITE = (255, 255, 255)
RED = (255, 10, 15)

screen = pg.display.set_mode((WIDTH, HEIGHT))
clock = pg.time.Clock()
FPS = 50
running = True

dx, dy = 100, HEIGHT//2      # for paddle one
ax, ay = 1050, HEIGHT//2     # for paddle two
ball_x, ball_y = WIDTH//2, HEIGHT//2-15 # ball

# ball
velocity_x = 5
velocity_y = 5

while running:
    screen.fill(BLUE)
    pg.draw.rect(screen, WHITE, (WIDTH//2, 0, 5, HEIGHT))
    for event in pg.event.get():
        if event.type == pg.QUIT:
            running = False
            sys.exit()

    paddle1 = pg.Rect(dx, dy, 50, 120)
    paddle2 = pg.Rect(ax, ay, 50, 120)
    
    pg.draw.rect(screen, PALE_YELLOW, paddle1)
    pg.draw.rect(screen, PALE_YELLOW, paddle2)

    # ball
    ball_x += velocity_x
    ball_y += velocity_y

    if ball_y-15 < 0 or ball_y+15 >= HEIGHT:
        velocity_y *= -1
    if ball_x-15 <= 0 or ball_x+15 >= WIDTH:
        velocity_x *= -1

    ball = pg.Rect(ball_x-15, ball_y-15, 30, 30)

    # handling collision
    if ball.colliderect(paddle1):
        velocity_x = abs(velocity_x)  # push ball at right
        offset = (ball_y - (dy+60))/60 # relative hit pos (-1 to 1)
        velocity_y += offset*5

    if ball.colliderect(paddle2):
        velocity_x = -abs(velocity_x)  # push ball at right
        offset = (ball_y - (ay+60))/60 # relative hit pos (-1 to 1)
        velocity_y += offset*5

    key = pg.key.get_pressed()
    if key[pg.K_w]:
        dy -= 8
        if dy<0:
            dy = 0
    if key[pg.K_s]:
        dy += 8
        if dy>HEIGHT-120:
            dy=HEIGHT-120

    if key[pg.K_UP]:
        ay -= 8
        if ay<0:
            ay = 0
    if key[pg.K_DOWN]:
        ay += 8
        if ay>HEIGHT-120:
            ay=HEIGHT-120
    
    #draw ball 
    pg.draw.circle(screen, RED, (ball_x, ball_y), radius=15)

    pg.display.flip()
    pg.display.set_caption("Pong")
    clock.tick(FPS)
    
pg.quit()
