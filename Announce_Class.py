from Start import *

class NumberAnnouncer:
    def __init__(self):
        self.number_pool = list(range(1, 51))
        random.shuffle(self.number_pool)
        self.announced_number = None
        self.announcement_time = time.time()
        self.history = []

    def announce(self):
        if time.time() - self.announcement_time > announce_time:
            if len(self.history) != 51:
                if 'FREE' not in self.history:
                    self.history.append('FREE')
                else:
                    self.announced_number = self.number_pool.pop(0)
                    self.history.append(self.announced_number)
                    self.announcement_time = time.time()
            else:
                return False
        return self.announced_number

    def draw_number(self, screen):
        if self.announced_number is None:
            ready_text = font(50).render('Ready?', True, yellow)
            screen.blit(ready_text, ready_text.get_rect(center=((screen_width / 2)+20, 60)))
        else:
            current_number_text = font(50).render(str(self.announced_number), True, navy_blue)
            if len(str(self.announced_number)) == 1:
                screen.blit(current_number_text, ((screen_width // 2)-25, 60))
            else:
                screen.blit(current_number_text, ((screen_width // 2)-40, 60))

        if len(self.history) > 1:
            previous_text = font(25).render("Previous Numbers", True, yellow)
            screen.blit(previous_text, (screen_width - 325, 200))
            free_history = [num for num in self.history[-6:-1] if num != 'FREE']
            for i, number in enumerate(free_history):
                past_number_text = font(24).render(str(number), True, white)
                if len(str(number)) == 1:
                    screen.blit(past_number_text, (screen_width - 200, 280 + (i * 60)))
                else:
                    screen.blit(past_number_text, (screen_width - 215, 280 + (i * 60)))