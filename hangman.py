import pygame
import math
import random

pygame.init()
WIDTH, HEIGHT = 1000, 700
win = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption("HANGMAN")
FPS = 60
clock = pygame.time.Clock()
run = True

radius = 24
space = 20
letters = []
x_start = round((WIDTH - (radius * 2 + space) * 13) / 2)
y_start = 540
A = 65

for i in range(26):
    x = x_start + space * 2 + ((radius * 2 + space) * (i % 13))
    y = y_start + ((i // 13) * (space + radius * 2))
    letters.append([x, y, chr(A + i), True])

font = pygame.font.SysFont("comicsans", 45)
WORD = pygame.font.SysFont("comicsans", 40)
TITLE = pygame.font.SysFont("comicsans", 70)

hangman = 0
lists = ["GEEKS", "GFG", "DOCKER", "DEVELOPER", "RUST", "GITHUB", "R", "PYTHON", "BASH"]
words = random.choice(lists)
guessed = []

def draw_hangman_stage(surface, stage):
    pygame.draw.line(surface, (0, 0, 0), (150, 500), (300, 500), 5)
    pygame.draw.line(surface, (0, 0, 0), (225, 500), (225, 100), 5)
    pygame.draw.line(surface, (0, 0, 0), (225, 100), (375, 100), 5)
    pygame.draw.line(surface, (0, 0, 0), (375, 100), (375, 150), 5)

    if stage > 0:
        pygame.draw.circle(surface, (0, 0, 0), (375, 180), 30, 4)
    if stage > 1:
        pygame.draw.line(surface, (0, 0, 0), (375, 210), (375, 320), 4)
    if stage > 2:
        pygame.draw.line(surface, (0, 0, 0), (375, 240), (340, 280), 4)
    if stage > 3:
        pygame.draw.line(surface, (0, 0, 0), (375, 240), (410, 280), 4)
    if stage > 4:
        pygame.draw.line(surface, (0, 0, 0), (375, 320), (340, 380), 4)
    if stage > 5:
        pygame.draw.line(surface, (0, 0, 0), (375, 320), (410, 380), 4)

def draw():
    win.fill((255, 255, 255))

    title = TITLE.render("HangMan", 1, (0, 0, 0))
    win.blit(title, (WIDTH // 2 - title.get_width() // 2, 10))

    disp_word = ""
    for letter in words:
        if letter in guessed:
            disp_word += letter + " "
        else:
            disp_word += "_ "

    text = WORD.render(disp_word, 1, (0, 0, 0))
    win.blit(text, (500, 250))

    for btn_pos in letters:
        x, y, ltr, visible = btn_pos
        if visible:
            pygame.draw.circle(win, (0, 0, 0), (x, y), radius, 4)
            txt = font.render(ltr, 1, (0, 0, 0))
            win.blit(txt, (x - txt.get_width() / 2, y - txt.get_height() / 2))

    draw_hangman_stage(win, hangman)
    pygame.display.update()

while run:
    clock.tick(FPS)
    draw()

    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            run = False

        if event.type == pygame.MOUSEBUTTONDOWN:
            x_mouse, y_mouse = pygame.mouse.get_pos()

            for letter in letters:
                x, y, ltr, visible = letter

                if visible:
                    dist = math.sqrt((x - x_mouse) ** 2 + (y - y_mouse) ** 2)

                    if dist <= radius:
                        letter[3] = False
                        guessed.append(ltr)
                        if ltr not in words:
                            hangman += 1

    won = True
    for letter in words:
        if letter not in guessed:
            won = False
            break

    if won:
        draw()
        pygame.time.delay(1000)
        win.fill((0, 0, 0))
        text = WORD.render("YOU WON", 1, (129, 255, 0))
        win.blit(text, (WIDTH // 2 - text.get_width() // 2, HEIGHT // 2 - text.get_height() // 2))
        pygame.display.update()
        pygame.time.delay(4000)
        print("WON")
        break

    if hangman == 6:
        draw()
        pygame.time.delay(1000)
        win.fill((0, 0, 0))
        text = WORD.render("YOU LOST", 1, (255, 0, 5))
        answer = WORD.render("The answer is " + words, 1, (129, 255, 0))
        win.blit(text, (WIDTH // 2 - text.get_width() // 2, HEIGHT // 2 - text.get_height() // 2))
        win.blit(answer, (WIDTH // 2 - answer.get_width() // 2,
                          HEIGHT // 2 - text.get_height() // 2 + 70))

        pygame.display.update()
        pygame.time.delay(4000)
        print("LOST")
        break

pygame.quit()