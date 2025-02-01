import pygame
import random

class Pipe:

    def __init__(self, X, Y, H):
        self.posX = X
        self.posY = Y
        self.height = H
        self.width = 10

    def collides(self, ball):
        return self.posX <= ball.posX <= self.posX + self.width and \
               self.posY <= ball.posY <= self.posY + self.height

    def updatePipeUp1(self):
        self.posX = round(random.randint(280, 320))
        self.height = round(random.randint(210, 270))

    def updatePipeUp2(self):
        self.posX = round(random.randint(510, 560))
        self.height = round(random.randint(210, 270))

    def updatePipeDown1(self):
        self.posX = round(random.randint(140, 170))
        posY = round(random.randint(100, 360))
        self.posY = posY
        self.height = 500-posY

    def updatePipeDown2(self):
        self.posX = round(random.randint(430, 460))
        posY = round(random.randint(150, 300))
        self.posY = posY
        self.height = 500-posY

    def updatePipeDown3(self):
        self.posX = round(random.randint(670, 690))
        posY = round(random.randint(200, 350))
        self.posY = posY
        self.height = 500-posY

    def render(self, screen):
        pygame.draw.line(screen, pygame.Color(0,100,0), [self.posX, self.posY],
                         [self.posX, self.posY + self.height], self.width)


class Ball:
    def __init__(self, X, Y, R):
        self.posX = X
        self.posY = Y
        self.radius = R
        self.speed = 0
        self.speedX = 2
        self.img = pygame.image.load("bird.png").convert_alpha()
        self.img = pygame.transform.rotozoom(self.img, 0, 0.25)

    def update(self):
        # Jump
        self.posY -= self.speed
        self.posX += self.speedX
        self.speed -= 0.8

    def render(self, screen):
        w, h = self.img.get_rect().size
        screen.blit(self.img, (self.posX - w / 2, self.posY - h / 2))


class App:

    def __init__(self):
        self.running = False
        self.clock = None
        self.screen = None
        self.ball = None

    def run(self):
        self.init()
        while self.running:
            self.update()
            self.render()
        self.cleanUp()

    def init(self):
        self.screen = pygame.display.set_mode((700, 500))
        pygame.display.set_caption("Flappy-bird")
        self.clock = pygame.time.Clock()
        self.running = True

        self.ball = Ball(50, 250, 10)

        self.pipeUp1 = Pipe(300, 0, 250)
        self.pipeUp2 = Pipe(555, 0, 256)
        self.pipeDown1 = Pipe(150, 350, 150)
        self.pipeDown2 = Pipe(450, 280, 220)
        self.pipeDown3 = Pipe(670, 200, 300)

    def update(self):
        self.events()

        if self.pipeUp1.collides(self.ball) or self.pipeUp2.collides(self.ball) or self.pipeDown1.collides(self.ball) or \
           self.pipeDown2.collides(self.ball) or self.pipeDown3.collides(self.ball):
            self.running = False

        if self.ball.posY >= 500:
            self.running = False

        if self.ball.posY <= 0:
            self.running = False

        if self.ball.posX >= 700:
            self.ball.posX = 0
            self.pipeUp1.updatePipeUp1()
            self.pipeUp2.updatePipeUp2()
            self.pipeDown1.updatePipeDown1()
            self.pipeDown2.updatePipeDown2()
            self.pipeDown3.updatePipeDown3()

        self.ball.update()

    def events(self):
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                self.running = False

            if event.type == pygame.MOUSEBUTTONDOWN and event.button == 1:
                self.ball.speed = 12

        # Keyboard
        keys = pygame.key.get_pressed()
        if keys[pygame.K_SPACE]:
            self.ball.speed = 7

    def render(self):
        self.screen.fill((0, 0, 0))
        bg = pygame.image.load("background.png")
        self.screen.blit(bg, (0, 0))

        self.ball.render(self.screen)
        self.pipeUp1.render(self.screen)
        self.pipeUp2.render(self.screen)
        # self.pipeDown1.render(self.screen)
        self.pipeDown1.render(self.screen)
        self.pipeDown2.render(self.screen)
        self.pipeDown3.render(self.screen)

        pygame.display.flip()
        self.clock.tick(60)

    def cleanUp(self):
        pass


if __name__ == "__main__":
    app = App()
    app.run()