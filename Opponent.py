from Start import *
from Card import Card


class Bot:
    def __init__(self, name, y_offset):
        self.name = name
        self.card = Card()
        self.y_offset = y_offset
        self.has_bingo = False

    def mark_automatically(self, announced_number):
        for col in range(size_card):
            for row in range(size_card):
                if self.card.card_numbers[col][row] in announced_number:
                    self.card.clicked_cells.add((col, row))

    def check_bingo(self):
        self.has_bingo = self.card.check_bingo(self.card.clicked_cells)
        return self.has_bingo

    def draw_bot_card(self, screen):
        for col in range(size_card):
            for row in range(size_card):
                x = (
                    screen_width // 4 - (5 * bot_size_block) // 2 + col * bot_size_block
                ) - 100
                y = self.y_offset + row * bot_size_block
                pygame.draw.rect(screen, orange, (x, y, bot_size_block, bot_size_block))
                pygame.draw.rect(
                    screen, navy_blue, (x, y, bot_size_block, bot_size_block), 1
                )

                if (col, row) in self.card.clicked_cells:
                    if self.name == "octopus":
                        screen.blit(bot_mark("octopus_mark"), (x, y))
                    elif self.name == "seahorse":
                        screen.blit(bot_mark("seahorse_mark"), (x, y))
                    else:
                        screen.blit(bot_mark("crab_mark"), (x, y))
                else:
                    number_text = (
                        font(8).render(
                            str(self.card.card_numbers[col][row]), True, black
                        )
                        if self.card.card_numbers[col][row] == "FREE"
                        else font(12).render(
                            str(self.card.card_numbers[col][row]), True, black
                        )
                    )
                    screen.blit(
                        number_text,
                        (
                            x + bot_size_block // 2 - number_text.get_width() // 2,
                            y + bot_size_block // 2 - number_text.get_height() // 2,
                        ),
                    )

    def draw_for_winner(self, screen):
        for col in range(size_card):
            for row in range(size_card):
                x = screen_width // 2 - (5 * size_block) // 2 + col * size_block
                y = screen_height // 2 - (5 * size_block) // 2 + row * size_block + 50
                pygame.draw.rect(screen, orange, (x, y, size_block, size_block))
                pygame.draw.rect(screen, navy_blue, (x, y, size_block, size_block), 2)

                number_text = (
                    font(18).render(str(self.card.card_numbers[col][row]), True, black)
                    if self.card.card_numbers[col][row] == "FREE"
                    else font(30).render(
                        str(self.card.card_numbers[col][row]), True, black
                    )
                )
                screen.blit(
                    number_text,
                    (
                        x + size_block // 2 - number_text.get_width() // 2,
                        y + size_block // 2 - number_text.get_height() // 2,
                    ),
                )
                if self.name == "octopus":
                    screen.blit(octopus2, (290, 200))
                elif self.name == "seahorse":
                    screen.blit(seahorse2, (115, 400))
                else:
                    screen.blit(crab2, (285, 600))
                if (col, row) in self.card.clicked_cells:
                    if self.name == "octopus":
                        screen.blit(bot_mark_winner("octopus_mark"), (x, y))
                    elif self.name == "seahorse":
                        screen.blit(bot_mark_winner("seahorse_mark"), (x, y))
                    else:
                        screen.blit(bot_mark_winner("crab_mark"), (x, y))
