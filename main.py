import sys, pygame
import time

pygame.init()
pygame.font.init()

size = width, height = 320, 240
speed = [2, 2]
black = 0, 0, 0


ball = pygame.image.load("intro_ball.gif")
ballrect = ball.get_rect()

class View:
    def __init__(self, matrix):
        self.screen = pygame.display.set_mode((matrix.width, matrix.height))
        self.matrix = matrix

    def step(self):
        self.matrix.step(self.screen)


class Matrix:
    def __init__(self, width, height):
        self.width = width
        self.height = height
        self.contents = []
        
    def step(self, screen):
        global ball
        global ballrect
        for event in pygame.event.get():
            if event.type == pygame.QUIT: sys.exit()

        ballrect = ballrect.move(speed)
        if ballrect.left < 0 or ballrect.right > width:
            speed[0] = -speed[0]
        if ballrect.top < 0 or ballrect.bottom > height:
            speed[1] = -speed[1]

        screen.fill(black)
        screen.blit(ball, ballrect)
        pygame.display.flip()


matrix = Matrix(480,480)
view = View(matrix)
while 1:
    view.step()
    time.sleep(0.05)

