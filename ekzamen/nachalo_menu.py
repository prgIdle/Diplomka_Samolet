import pygame, Buttons,Level_switch 
from pygame.locals import *

#Initialize pygame
pygame.init()
class Background(pygame.sprite.Sprite):
    def __init__(self, image_file, location):
        pygame.sprite.Sprite.__init__(self)
        self.image = pygame.image.load(image_file)
        self.rect = self.image.get_rect()
        self.rect.left, self.rect.top = location


BackGround = Background('background_image_1.jpg', [0,0])
class Button_Example:
    def __init__(self):
        self.main()
    
    #Create a display
    def display(self):
        self.screen = pygame.display.set_mode((1920,1080),0,32)
        pygame.display.set_caption("Buttons.py - example")

    #Update the display and show the button
    def update_display(self):
        self.screen.fill((30,144,255))
        #Parameters:               surface,      color,       x,   y,   length, height, width,    text,      text_color
        self.Button1.create_button(self.screen, (107,142,35), 830, 280, 200,    100,    0,        "Start", (255,255,255))
        pygame.display.flip()


    #Run the loop
    def main(self):
        self.Button1 = Buttons.Button()
        self.display()
        while True:
            self.update_display()
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    pygame.quit()
                elif event.type == MOUSEBUTTONDOWN:
                    if self.Button1.pressed(pygame.mouse.get_pos()):
                        Level_switch.Level_Vibor()

if __name__ == '__main__':
    obj = Button_Example()
