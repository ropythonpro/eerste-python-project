import pygame
import random

pygame.init()

score_x = 0
score_y = 600
width, height = 800, 600
score = 0
window = pygame.display.set_mode((width, height))
pygame.display.set_caption("the diving chef")
white = (255, 255, 255)
blue = (0, 0, 255)
yellow = (255, 255, 0)
black = (0, 0, 0)
font = pygame.font.SysFont('algarian', 40)

imp = pygame.image.load().convert_alpha()
imp2 = pygame.image.load().convert_alpha()
imp = pygame.transform.scale(imp, [130, 70])
imp2 = pygame.transform.scale(imp2, [175, 100])
impduiker = pygame.image.load().convert_alpha()
impduiker = pygame.transform.scale(impduiker, [175, 100])
immpplantjes = pygame.image.load().convert_alpha()
impachtergrond = pygame.image.load().convert_alpha()

shark_x = 500
shark_y = 4000

circle_radius = 20
player_x = width // 2
player_y = height // 2
circle_speed = 0.75

coin_radius = 10


def spawn_coin():
    return random.randint(coin_radius, width - coin_radius), random.randint(coin_radius, height - coin_radius)


coin_x, coin_y = spawn_coin()

running = True
while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

    keys = pygame.key.get_pressed()

    if keys[pygame.K_LEFT]:
        player_x -= circle_speed
    if keys[pygame.K_RIGHT]:
        player_x += circle_speed
    if keys[pygame.K_UP]:
        player_y -= circle_speed
    if keys[pygame.K_DOWN]:
        player_y += circle_speed

    distance = ((player_x - coin_x) ** 2 + (player_y - coin_y) ** 2) ** 0.5
    if distance < circle_radius + coin_radius:
        coin_x, coin_y = spawn_coin()
        score = score + 1

    if shark_x < player_x:
        shark_x = shark_x + 0.1
    if player_x < shark_x:
        shark_x = shark_x + -0.1
    if shark_y < player_y:
        shark_y = shark_y + 0.1
    if player_y < shark_y:
        shark_y = shark_y + -0.1

    window.fill(blue)
    distance = ((player_x - shark_x) ** 2 + (player_y - shark_y) ** 2) ** 0.5
    if distance < circle_radius + 25:
        running = False

    pygame.draw.circle(window, white, (player_x, player_y), circle_radius)
    pygame.draw.circle(window, yellow, (coin_x, coin_y), coin_radius)
    pygame.draw.rect(window, blue, (shark_x, shark_y, 50, 50))
    window.blit(impachtergrond, (0, 0))
    text_surface = font.render('score: ' + str(score), True, (0, 255, 0))
    window.blit(text_surface, (0, 0))
    window.blit(imp, (coin_x - 70, coin_y - 30))
    window.blit(imp2, (shark_x - 150, shark_y - 20))
    window.blit(impduiker, (player_x - 77, player_y - 48))
    window.blit(impplantjes, (100, 999))

    pygame.display.flip()

pygame.quit()