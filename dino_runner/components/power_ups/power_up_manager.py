from time import time
import pygame
import random
from dino_runner.components.power_ups.hammer import Hammer

from dino_runner.components.power_ups.shield import Sheild

class PowerUpManager:
    def __init__(self):
        self.power_ups = []
        self.when_appears = 0

    def generate_power_up(self, points,player):
        
        if len(self.power_ups) == 0:
            if self.when_appears == points:
                self.when_appears == random.randint(self.when_appears + 50, self.when_appears + 300)
                self.power_type= random.randint(0,1)
                if self.power_type==0:
                    
                    self.power_ups.append(Sheild())
                else:
                    print("HAMER")
                    self.power_ups.append(Hammer())

    def update(self, points, game_speed, player):
        self.generate_power_up(points,player)
        for power_up in self.power_ups:
            power_up.update(game_speed, self.power_ups)
            if player.dino_rect.colliderect(power_up.rect):
                power_up.start_time = pygame.time.get_ticks()
                if (power_up.type=="shield"):
                    player.shield = True
                    player.hammer = False
                else:
                    player.hammer = True
                    player.shield = False
               
                player.show_text = True
                player.type = power_up.type
                time_random = random.randint(5, 8)
                player.shield_time_up=power_up.start_time+(time_random*1000)
                self.power_ups.remove(power_up)
                

    def draw(self, screen):
        for power_up in self.power_ups:
            power_up.draw(screen)

    def reset_power_ups(self):
        self.power_ups = []
        self.when_appears = random.randint(50,300)