from Card import Card
from Button import Button
from Announce_Class import NumberAnnouncer
from Start import *
from menu import Menu
from Opponent import Bot


class BingoGame:
    def __init__(self):
        pygame.init()
        pygame.display.set_caption("BingoGo")

    def main(self):
        while True:
            pygame.mixer_music.stop()
            pygame.mixer.music.load("sounds/main_sound/adventure.mp3")
            pygame.mixer.music.play(loops=-1)
            menu = Menu()
            menu.draw()
            if menu.option_draw() == 0:
                pygame.mixer.music.stop()
                pygame.mixer.music.load("sounds/main_sound/battle.mp3")
                pygame.mixer.music.play(loops=-1)
                self.run_bot(
                    NumberAnnouncer(),
                    Card(),
                    [Bot("octopus", 100), Bot("seahorse", 300), Bot("crab", 500)],
                )
            else:
                pygame.mixer.music.stop()
                pygame.mixer.music.load("sounds/main_sound/battle.mp3")
                pygame.mixer.music.play(loops=-1)
                self.run_single(NumberAnnouncer(), Card())

    def run_bot(self, announce, card, bots):
        bingo_detected = False
        paused = Button(
            yellow_button,
            glow_button,
            (1150, 60),
            "PAUSE",
            font(20),
            black,
            light_blue,
            0.3,
        )

        while not bingo_detected:
            announced_number = announce.history
            position_mouse = pygame.mouse.get_pos()
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    pygame.quit()
                    sys.exit()
                elif event.type == pygame.MOUSEBUTTONDOWN:
                    if paused.checkForInput(position_mouse):
                        if self.pause():
                            return
                    card.mark_number(event.pos, announced_number, card.card_numbers)
            screen.blit(blue_screen, (0, 0))
            card.draw_grid(card.clicked_cells)
            paused.changeColor(position_mouse)
            paused.update(screen)

            for bot in bots:
                bot.draw_bot_card(screen)
            announce.draw_number(screen)
            pygame.display.update()

            if card.check_bingo(card.clicked_cells):
                if self.display_bingo_message(card):
                    pygame.time.delay(1000)
                    bingo_detected = True
            elif announce.announce() == False:
                if self.game_over():
                    bingo_detected = True
            for bot in bots:
                bot.mark_automatically(announced_number)
                if bot.check_bingo():
                    if self.opponent_game_over(bot, bot.name):
                        bingo_detected = True

    def run_single(self, announce, card):
        bingo_detected = False
        paused = Button(
            yellow_button,
            glow_button,
            (1150, 60),
            "PAUSE",
            font(20),
            black,
            light_blue,
            0.3,
        )
        start = time.time()
        start_time = time.time()
        while not bingo_detected:
            position_mouse = pygame.mouse.get_pos()
            announced_number = announce.history
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    pygame.quit()
                    sys.exit()
                elif event.type == pygame.MOUSEBUTTONDOWN:
                    if paused.checkForInput(position_mouse):
                        if self.pause():
                            return
                    card.mark_number(event.pos, announced_number, card.card_numbers)
            screen.blit(blue_screen, (0, 0))
            card.draw_grid(card.clicked_cells)
            screen.blit(shark2, (0, 100))
            screen.blit(octopus, (1050, 510))
            announce.draw_number(screen)
            paused.changeColor(position_mouse)
            paused.update(screen)
            if time.time() - start > announce_time:
                elapsed_time = int(time.time() - start_time)
                timer_text = font(30).render(f"Time: {elapsed_time}s", True, yellow)
                screen.blit(timer_text, (10, 10))
            else:
                start_time = time.time()
            pygame.display.update()

            if card.check_bingo(card.clicked_cells):
                if self.display_bingo_message(card):
                    pygame.time.delay(1000)
                    bingo_detected = True
            elif announce.announce() == False:
                if elapsed_time == 5:
                    pass

    def pause(self):
        game_background = screen.copy()
        overlay = pygame.Surface((screen_width, screen_height))
        overlay.set_alpha(150)
        overlay.fill((0, 0, 0))
        game_background.blit(overlay, (0, 0))

        pause_text = font(80).render("PAUSED?", True, yellow)
        resume = Button(
            yellow_button,
            glow_button,
            (520, 450),
            "Resume",
            font(20),
            black,
            light_blue,
            0.25,
        )
        menu = Button(
            yellow_button,
            glow_button,
            (760, 450),
            "Main Menu",
            font(20),
            black,
            light_blue,
            0.25,
        )
        times = time.time()

        while True:
            mouse = pygame.mouse.get_pos()
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    pygame.quit()
                    sys.exit()
                elif event.type == pygame.MOUSEBUTTONDOWN:
                    if resume.checkForInput(mouse):
                        return
                    elif menu.checkForInput(mouse):
                        return True

                if time.time() - times > 0.5 and event.type == pygame.KEYDOWN:
                    if event.key == pygame.K_p:
                        return

            screen.blit(game_background, (0, 0))
            menu_box = pygame.Rect(300, 150, 700, 500)
            pygame.draw.rect(screen, (50, 50, 50), menu_box)
            pygame.draw.rect(screen, yellow, menu_box, 5)
            screen.blit(pause_screen, (305, 155))

            screen.blit(
                pause_text, (screen_width // 2 - pause_text.get_width() // 2, 200)
            )
            resume.changeColor(mouse)
            resume.update(screen)
            menu.changeColor(mouse)
            menu.update(screen)

            pygame.display.update()

    def opponent_game_over(self, opponent_card, name):
        pygame.mixer_music.stop()
        game_over_sound = pygame.mixer.Sound("sounds/losing/game_over.mp3")
        game_over_sound.play()
        restart = Button(
            yellow_button,
            glow_button,
            (1090, 545),
            "main menu",
            font(40),
            black,
            light_blue,
            0.5,
        )
        exits = Button(
            yellow_button,
            glow_button,
            (1090, 650),
            "exit",
            font(40),
            black,
            light_blue,
            0.5,
        )
        game_over_text = font(100).render(f"{name} is winner", True, yellow)
        while True:
            mouse = pygame.mouse.get_pos()
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    pygame.quit()
                    sys.exit()
                elif event.type == pygame.MOUSEBUTTONDOWN:
                    if restart.checkForInput(mouse):
                        pygame.mixer.stop()
                        return True
                    elif exits.checkForInput(mouse):
                        pygame.quit()
                        sys.exit()
            screen.blit(blue_screen, (0, 0))
            screen.blit(sad_octopus, (30, 400))
            screen.blit(sad_shark, (900, 200))
            screen.blit(
                game_over_text,
                (
                    screen_width // 2 - game_over_text.get_width() // 2,
                    screen_height // 2 - game_over_text.get_height() // 2 - 270,
                ),
            )
            opponent_card.draw_for_winner(screen)
            restart.changeColor(mouse)
            restart.update(screen)
            exits.changeColor(mouse)
            exits.update(screen)
            pygame.display.update()

    def display_bingo_message(self, card):
        pygame.mixer_music.stop()
        sound1 = pygame.mixer.Sound("sounds/winning/win.mp3")
        sound2 = pygame.mixer.Sound("sounds/winning/bingo.mp3")
        sound_check = False
        bingo_button = Button(
            yellow_button,
            glow_button,
            (1100, 600),
            "BINGO!",
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
                    if bingo_button.checkForInput(mouse):
                        sound_check = True
                        screen.blit(blue_screen, (0, 0))
                        screen.blit(
                            BINGO,
                            (
                                screen_width // 2 - BINGO.get_width() // 2,
                                screen_height // 2 - BINGO.get_height() // 2,
                            ),
                        )
                        screen.blit(shark3, (50, 50))
                        screen.blit(octopus3, (100, 500))
                        screen.blit(g_of_fish,(900,100))
                        screen.blit(cloral,(1020,450))
                        pygame.display.update()
                        if sound_check == True:
                            sound1.play()
                            while pygame.mixer.get_busy():
                                time.sleep(0.1)
                            sound2.play()
                        return True
            screen.blit(blue_screen, (0, 0))
            card.draw_grid(card.clicked_cells)
            bingo_button.changeColor(mouse)
            bingo_button.update(screen)
            pygame.display.update()


if __name__ == "__main__":
    game = BingoGame()
    game.main()
