import pygame
import random

from dino_runner.components.obstacles.captus import Cactus
from dino_runner.utils.constants import SMALL_CACTUS,LARGE_CACTUS

class ObtacleManager:
    def __init__(self):
        self.obstacles = []
        self.tipoCactus= 0

    def update(self, game):

        if len(self.obstacles) == 0:
            self.tipoCactus= random.randint(1, 2)
            if self.tipoCactus==1:
                self. obstacles.append(Cactus(SMALL_CACTUS))
            else:
                self. obstacles.append(Cactus(LARGE_CACTUS))
        

        for obstacle in self.obstacles:
            obstacle.update(game.game_speed, self.obstacles)
            if game.player.dino_rect.colliderect(obstacle.rect):
                pygame.time.delay(500)
                game.playing = False
                break

    def draw(self, screen):
      
        for obstacle in self. obstacles:
            obstacle.draw(screen)