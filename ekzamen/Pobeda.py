import pygame, Buttons, ekzamen
from pygame.locals import *
import sys
pygame.init()

class Background(pygame.sprite.Sprite):
        def __init__(self, image_file, location):
                pygame.sprite.Sprite.__init__(self)
                self.image = pygame.image.load(image_file)
                self.rect = self.image.get_rect()
                self.rect.left, self.rect.top = location

BackGround = Background('background_image_2.jpg', [0,0])
        
class Button_Example:
        def __init__(self):
                self.main()
    
        #Create a display
        def display(self):
                self.screen = pygame.display.set_mode((1920,1080),0,32)
                pygame.display.set_caption("Buttons.py - example")

        #Update the display and show the button
        def update_display(self):
                #Parameters:               surface,      color,       x,   y,   length, height, width,    text,      text_color
                self.screen.blit(BackGround.image, BackGround.rect)
                self.Button1.create_button(self.screen, (0,0,0), 689, 515, 200,    100,    0,        "Restart", (255,255,255))
                self.Button2.create_button(self.screen, (0,0,0), 689, 625, 200,    100,    0,        "Exit", (255,255,255))
                myfont=pygame.font.Font(None,60)
                GameOverText=myfont.render("You Win! :)",True,'red')
                self.screen.blit(GameOverText,(700,400))
                pygame.display.update()

        #Run the loop
        def main(self):
                self.Button1 = Buttons.Button()
                self.Button2 = Buttons.Button()
                self.display()
                while True:
                        self.update_display()
                        for event in pygame.event.get():
                                if event.type == pygame.QUIT:
                                        pygame.quit()
                                elif event.type == MOUSEBUTTONDOWN:
                                        if self.Button1.pressed(pygame.mouse.get_pos()):
                                                ekzamen.game1()
                                        if self.Button2.pressed(pygame.mouse.get_pos()):
                                                pygame.quit()


if __name__ == '__main__':
        obj = Button_Example()

