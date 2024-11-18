from Start import *

class Card:
    def __init__(self):
        self.card_numbers = self.random_number() #store num
        self.bingo_word = ['B','I','N','G','O']
        self.clicked_cells = set()
        self.sound = pygame.mixer.Sound('sounds/click.mp3')
           
    def random_number(self): # generate number ^-^
        card = [] # [[1-10],[11-20],[21-30],[31-40],[41-50]]
        for col in range(size_card):  
            start = col * (range_number//5) + 1
            end = start + (range_number//5)
            column_numbers = random.sample(range(start, end), size_card)
            card.append(column_numbers)
        card[2][2] = 'FREE'
        return card
    
    def check_bingo(self , clicked_cells):
        for row in range(size_card): #check row
            count_row = 0  
            for column in range(size_card):
                if (column, row) in clicked_cells: #use clicked_cells because the action is in it
                    count_row += 1  
            if count_row == 5:
                return True

        for column in range(size_card): #check column
            count_column = 0
            for row in range(size_card):
                if (column,row) in clicked_cells:
                    count_column += 1
            if count_column == 5:
                return True

        if ((0,0) in clicked_cells) and ((1,1) in clicked_cells) and ((2,2) in clicked_cells) and ((3,3) in clicked_cells) and ((4,4) in clicked_cells):
            return True
        if ((0,4) in clicked_cells) and ((1,3) in clicked_cells) and ((2,2) in clicked_cells) and ((3,1) in clicked_cells) and ((4,0) in clicked_cells):
            return True
        if ((0,0) in clicked_cells) and ((0,4) in clicked_cells) and ((2,2) in clicked_cells) and ((4,0) in clicked_cells) and ((4,4) in clicked_cells):
            return True
        
        return False

    def draw_grid(self, click_cells): # create table . if the table is error , fix this function 
        for col in range(size_card):
            for row in range(size_card):
                x = screen_width // 2 - (5 * size_block) // 2 + col * size_block
                y = screen_height // 2 - (5 * size_block) // 2 + row * size_block + 80
                x_bingo = screen_width // 2 - (5 * size_block) // 2 + row * size_block
                y_bingo = screen_height // 2 - (5 * size_block) // 2 + -1 * size_block + 80
                pygame.draw.rect(screen, light_blue, (x, y, size_block, size_block))
                pygame.draw.rect(screen, black, (x, y, size_block, size_block), 2)
                pygame.draw.rect(screen, navy_blue, (x_bingo, y_bingo, size_block, size_block))
                pygame.draw.rect(screen, black, (x_bingo, y_bingo, size_block, size_block),2)
                number_text = font(18).render(str(self.card_numbers[col][row]), True, black) if self.card_numbers[col][row] == 'FREE' else font(30).render(str(self.card_numbers[col][row]), True, black)
                screen.blit(number_text, (x + size_block // 2 - number_text.get_width() // 2, y + size_block // 2 - number_text.get_height() // 2))

                if (col, row) in click_cells:
                    screen.blit(mark_pic, (x, y))
                
                bingo_text = font(40).render(str(self.bingo_word[row]), True, yellow)
                screen.blit(bingo_text, (x_bingo + size_block // 2 - bingo_text.get_width() // 2, y_bingo + size_block // 2 - bingo_text.get_height() // 2))
 
    def mark_number(self, pos, announced_number, card_numbers):
        for col in range(size_card):
            for row in range(size_card):
                x = screen_width // 2 - (5 * size_block) // 2 + col * size_block
                y = screen_height // 2 - (5 * size_block) // 2 + row * size_block + 80
                rect = pygame.Rect(x, y, size_block, size_block)
                if rect.collidepoint(pos) and (col, row) not in self.clicked_cells:
                    if card_numbers[col][row] in announced_number:
                        self.clicked_cells.add((col, row))
                        
