import os
import pygame

from reel import reel

WHITE = (255, 255, 255)
BLACK = (0, 0, 0)
ORANGE = (255, 165, 0)


class window:
    def __init__(self, width, height, config):
        self.width = width
        self.height = height
        self.config = os.path.join(os.path.dirname(__file__), config)

        with open(self.config, 'r') as f:
            self.data_file = self.get_next_line(f).strip()
            self.title = self.get_next_line(f).strip()
            self.second_title = self.get_next_line(f).strip()
            self.categories = []
            category = self.get_next_line(f).strip()
            while category:
                self.categories.append(category)
                category = self.get_next_line(f).strip()
            f.close()

        self.data = []
        with open(self.data_file, 'r') as f:
            for line in f:
                self.data.append(line.strip())
            f.close()

        self.reels = []
        for i, category in enumerate(self.categories):
            self.reels.append(reel(self.data, 300 + (300 * i), 500))

        self.screen = pygame.display.set_mode((self.width, self.height))
        pygame.display.set_caption(self.title)
        self.titl_font = pygame.font.SysFont('Arial', 24)
        self.font = pygame.font.SysFont('Arial', 20)
        self.small_font = pygame.font.SysFont('Arial', 16)
        self.running = True

        self.last_time = pygame.time.get_ticks()
        self.deltatime = 0

        self.loop()

    def loop(self):
        while self.running:
            current_time = pygame.time.get_ticks()
            self.deltatime = current_time - self.last_time
            self.last_time = current_time

            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    self.running = False

            self.screen.fill((255, 255, 255))
            self.draw()
            pygame.display.flip()

        pygame.quit()

    def draw(self):
        self.screen.fill((255, 255, 255))
        self.draw_text(self.title, 0, 250, self.titl_font, ORANGE)

        #self.draw_button("Start", 0, 175, 75, 30, BLACK, WHITE, self.font, ORANGE, action=lambda: print("interact"))
        self.draw_button("Start", 0, 175, 75, 30, BLACK, WHITE, self.font, ORANGE, action=self.start_spin)

        for i, category in enumerate(self.categories):
            self.draw_text(category, 0 + (300 * (i - len(self.categories) // 2)), 0, self.font, BLACK)

        for reel in self.reels:
            reel.update(self.deltatime)
            reel.draw(self.screen)

        #pygame.draw.circle(self.screen, (255, 0, 0), (self.width // 2, self.height // 2), 2)

    def draw_text(self, text, x, y, font, color, x_align=0.5, y_align=0.5):
        x = self.width // 2 - (self.font.size(text)[0] * x_align) + x
        y = self.height // 2 - (self.font.size(text)[1] * y_align) - y
        self.screen.blit(font.render(text, True, color), (x, y))

    def draw_button(self, text, x, y, width, height, color, hover_color, font, text_color, action=None):
        mouse = pygame.mouse.get_pos()
        click = pygame.mouse.get_pressed()
        mouse_x = mouse[0] - self.width // 2 + width // 2
        mouse_y = self.height // 2 - mouse[1] + height // 2

        if x < mouse_x < x + width and y < mouse_y < y + height:
            pygame.draw.rect(self.screen, hover_color, (x + self.width // 2 - width // 2, self.height // 2 - y - height // 2, width, height))
            if click[0] == 1 and action:
                action()
        else:
            pygame.draw.rect(self.screen, color, (x + self.width // 2 - width // 2, self.height // 2 - y - height // 2, width, height))

        self.draw_text(text, x, y, font, text_color, 0.5, 0.5)

    def get_next_line(self, f):
        line = f.readline()
        while line and (line[0] == '#' or line == '\n'):
            if not line:
                return None
            line = f.readline()
        return line

    def start_spin(self):
        for reel in self.reels:
            reel.start_spin()

if __name__ == "__main__":
    pygame.init()
    window(1280, 720, 'config.txt')