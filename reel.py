import pygame
import random
import math

def cos_intrp(a, b, t):
    t2 = (1 - math.cos(t * math.pi)) / 2
    return a * (1 - t2) + b * t2

class reel:
    def __init__(self, elements, x, y, start_speed=-1, end_speed=0, min_duration=10000, max_duration=15000, width=200, height=50, case_height=20, draw_border=True, border_width=2, current_offset=100):
        self.elements = elements
        self.x = x
        self.y = y
        self.start_speed = start_speed
        self.end_speed = end_speed
        self.min_duration = min_duration
        self.max_duration = max_duration
        self.width = width
        self.height = height
        self.case_height = case_height
        self.draw_border = draw_border
        self.border_width = border_width
        self.current_offset = current_offset
        self.rolling = False
        self.duration = 0
        self.time = 0

        self.font = pygame.font.SysFont('Arial', 20)

    def draw(self, screen):
        for i in range(len(self.elements)):
            element = self.elements[i]
            y_offset = (i * self.case_height + self.current_offset) % (len(self.elements) * self.case_height) - len(self.elements) * self.case_height // 2
            text = self.font.render(element, True, (0, 0, 0))
            y_pos = (self.y - text.get_height() // 2) + y_offset

            if y_pos <= self.y + self.height // 2 - self.case_height // 2 and y_pos + text.get_height() >= self.y - self.height // 2 + self.case_height // 2:
                screen.blit(text, (self.x - text.get_width() // 2, y_pos))

        if self.draw_border:
            pygame.draw.rect(screen, (0, 0, 0), (self.x - self.width // 2 - self.border_width, self.y - self.height // 2 - self.border_width, self.width + 2 * self.border_width, self.height + 2 * self.border_width), self.border_width)

        #pygame.draw.circle(screen, (255, 0, 0), (self.x, self.y), 2)
        #pygame.draw.circle(screen, (255, 0, 0), (self.x, self.y + self.height // 2), 2)
        #pygame.draw.circle(screen, (255, 0, 0), (self.x, self.y - self.height // 2), 2)
        #pygame.draw.circle(screen, (255, 0, 0), (self.x - self.width // 2, self.y), 2)
        #pygame.draw.circle(screen, (255, 0, 0), (self.x + self.width // 2, self.y), 2)

    def start_spin(self):
        if self.rolling:
            return
        self.rolling = True
        self.time = 0
        self.duration = random.randint(self.min_duration, self.max_duration)

    def stop_spin(self):
        self.rolling = False

    def update(self, dt):
        if self.rolling:
            self.time += dt
            if self.time >= self.duration:
                self.stop_spin()
                self.time = 0
            else:
                t = self.time / self.duration
                speed = cos_intrp(self.start_speed, self.end_speed, t)
                self.current_offset += speed * dt


if __name__ == "__main__":
    pygame.init()
    #font = pygame.font.SysFont('Arial', 20)
    screen = pygame.display.set_mode((400, 400))
    pygame.display.set_caption("Test Reel")

    numbers = [str(i) for i in range(10)]
    r = reel(numbers, 200, 200)

    last_time = pygame.time.get_ticks()
    deltatime = 0

    running = True
    while running:
        current_time = pygame.time.get_ticks()
        deltatime = current_time - last_time
        last_time = current_time

        screen.fill((255, 255, 255))

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                running = False

            if event.type == pygame.KEYDOWN:
                r.start_spin()

        r.update(deltatime)
        r.draw(screen)
        pygame.display.flip()

    pygame.quit()