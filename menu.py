from Start import *
from Button import Button

class Menu:
    def __init__(self):
        pass
    def draw(self):
        title = font(100).render("BinGo Go!",True,yellow)
        plays = Button(yellow_button,glow_button, (640, 450), 'Play', font(40), black, light_blue,0.5)
        exits = Button(yellow_button,glow_button, (640, 600), 'Exit', font(40), black, light_blue,0.5)
        while True:
            mouse = pygame.mouse.get_pos()
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    pygame.quit()
                    sys.exit()
                elif event.type == pygame.MOUSEBUTTONDOWN:
                    if plays.checkForInput(mouse):
                        return False
                    elif exits.checkForInput(mouse):
                        pygame.quit()
                        sys.exit()
            screen.blit(blue_screen,(0,0))
            #แปะภาพตกแต่ง
            
            screen.blit(title,(screen_width // 2 - title.get_width() // 2, screen_height // 5))
            plays.changeColor(mouse)
            plays.update(screen)
            exits.changeColor(mouse)
            exits.update(screen)
            pygame.display.update()
    
    def option_draw(self):
        select_option = font(100).render("Select Gameplay",True,yellow)
        enemy_game = Button(yellow_button,glow_button, (640, 450), 'bot', font(40), black, light_blue,0.5)
        solo = Button(yellow_button,glow_button, (640, 600), 'solo', font(40), black, light_blue,0.5)
        while True:
            mouse = pygame.mouse.get_pos()
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    pygame.quit()
                    sys.exit()
                elif event.type == pygame.MOUSEBUTTONDOWN:
                    if enemy_game.checkForInput(mouse):
                        return 0
                    elif solo.checkForInput(mouse):
                        return 1
            screen.blit(blue_screen,(0,0))
            screen.blit(select_option,(screen_width // 2 - select_option.get_width() // 2, screen_height // 4))
            enemy_game.changeColor(mouse)
            enemy_game.update(screen)
            solo.changeColor(mouse)
            solo.update(screen)
            pygame.display.update()