import yaml
import pygame

def load_game_config():
    with open("game_config.yaml", "r") as file:
        game_config = yaml.safe_load(file)
    return game_config

def load_character_image(config_file):
    original_image = pygame.image.load(config_file['info']['character-image-path']).convert_alpha()
    scaled_width, scaled_height = config_file['dimensions']['character-width'], config_file['dimensions']['character-height']
    character_image = pygame.transform.scale(original_image, (scaled_width, scaled_height))
    character_rect = character_image.get_rect()
    character_rect.topleft = (600, 300)
    return character_image, character_rect