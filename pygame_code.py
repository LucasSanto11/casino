import pygame

pygame.init()

screen=pygame.display.set_mode([1600, 900])
pygame.display.set_caption('Demo')
clock = pygame.time.Clock()
IPS=60


#charger images boutons
image_jouer = pygame.image.load('placeholderG.png').convert_alpha()
image_quitter = pygame.image.load('placeholderR.png').convert_alpha()

#bouton class
class button():
    def __init__(self, x, y, image):
        self.image=image
        self.rect= self.image.get_rect()
        self.rect.topleft = (x, y)

    def draw(self):
        screen.blit(self.image, (self.rect.x, self.rect.y))

#afficher boutons
bouton_jouer = button(500, 0, image_jouer)
bouton_quitter = button(-500, 0, image_quitter)


#Partie active
run= True

while run:
    screen.fill((0, 0, 50))

    bouton_jouer.draw()
    bouton_quitter.draw()

    for event in pygame.event.get():
        #quitter
        if event.type == pygame.QUIT:
            run = False
    pygame.event.get()
    pygame.display.update()
