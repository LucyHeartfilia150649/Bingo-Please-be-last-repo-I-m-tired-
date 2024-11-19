from Start import *
from Button import Button


class Menu:
    def __init__(self):
        pass

    def draw(self):
        title = font(100).render("BinGo Go!", True, yellow)
        plays = Button(
            yellow_button,
            glow_button,
            (640, 450),
            "Play",
            font(40),
            black,
            light_blue,
            0.5,
        )
        exits = Button(
            yellow_button,
            glow_button,
            (640, 600),
            "Exit",
            font(40),
            black,
            light_blue,
            0.5,
        )
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
            screen.blit(blue_screen, (0, 0))
            screen.blit(sand, (0, 0))
            screen.blit(chest, (800, 400))
            screen.blit(seaweed, (995, 400))
            screen.blit(seaweed2, (0, 400))
            screen.blit(crab, (300, 400))
            screen.blit(seahorse, (1000, 100))
            screen.blit(fish, (100, 50))

            screen.blit(
                title, (screen_width // 2 - title.get_width() // 2, screen_height // 5)
            )
            plays.changeColor(mouse)
            plays.update(screen)
            exits.changeColor(mouse)
            exits.update(screen)
            pygame.display.update()

    def option_draw(self):
        select_option = font(100).render("Select Game Mode", True, yellow)
        enemy_game = Button(
            yellow_button,
            glow_button,
            (640, 450),
            "Multiplayer",
            font(40),
            black,
            light_blue,
            0.5,
        )
        solo = Button(
            yellow_button,
            glow_button,
            (640, 600),
            "Single Player",
            font(40),
            black,
            light_blue,
            0.5,
        )
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
            screen.blit(blue_screen, (0, 0))
            screen.blit(
                select_option,
                (
                    screen_width // 2 - select_option.get_width() // 2,
                    screen_height // 4,
                ),
            )
            screen.blit(sand, (0, 0))
            screen.blit(chest, (800, 400))
            screen.blit(seaweed, (995, 400))
            screen.blit(seaweed2, (0, 400))
            screen.blit(crab, (300, 400))
            screen.blit(seahorse, (1050, 100))
            screen.blit(fish, (30, 50))
            enemy_game.changeColor(mouse)
            enemy_game.update(screen)
            solo.changeColor(mouse)
            solo.update(screen)
            pygame.display.update()
