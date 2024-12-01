import pygame
from utils import *

game_config = load_game_config()

pygame.init()
screen = pygame.display.set_mode((game_config['dimensions']['window-width'], game_config['dimensions']['window-height']))

pygame.display.set_caption(game_config['info']['game-name'])

character_image, character_rect = load_character_image(game_config)

clock = pygame.time.Clock()
running = True

while running:

    keys = pygame.key.get_pressed()
    if keys[pygame.K_UP] and character_rect.y >0 :character_rect.y -= 5
    if keys[pygame.K_DOWN] and character_rect.y < game_config['dimensions']['window-height'] - game_config['dimensions']['character-height'] : character_rect.y += 5
    if keys[pygame.K_LEFT] and character_rect.x > 0: character_rect.x -= 5
    if keys[pygame.K_RIGHT] and character_rect.x < game_config['dimensions']['window-width'] - game_config['dimensions']['character-width'] : character_rect.x += 5

    screen.fill(tuple(game_config['colors']['background-color']))
    screen.blit(character_image, character_rect)

    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

    pygame.display.flip()

    clock.tick(game_config['parameters']['fps'])

pygame.quit()