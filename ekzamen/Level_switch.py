import pygame, Buttons, ekzamen , nachalo_menu
from pygame.locals import *
import sys
pygame.init()

class Level_Vibor:
    def __init__(self):
        self.main()
    
    #Create a display
    def display(self):
        self.screen = pygame.display.set_mode((1920,1080),0,32)
        pygame.display.set_caption("Buttons.py - example")

    #Update the display and show the button
    def update_display(self):
        self.screen.fill(('black'))
        #Parameters:               surface,      color,       x,   y,   length, height, width,    text,      text_color
        self.Button1.create_button(self.screen, (107,142,35), 400, 135, 80,    80,    0,        "1", (255,255,255))
        myfont=pygame.font.Font(None,100)
        GameOverText=myfont.render("Level",True,'red')
        self.screen.blit(GameOverText,(850,50))
        pygame.display.update()


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
                        ekzamen.game1()

if __name__ == '__main__':
    obj = Button_Example()
