from email.mime import image
from multiprocessing.pool import RUN
from operator import truediv
from pickle import TRUE
from sre_constants import JUMP
from time import time
from tkinter import font
import pygame
from dino_runner.components.power_ups.hammer import Hammer
from dino_runner.utils.constants import BG, DUCKING, DUCKING_HAMMER, DUCKING_SHIELD, FPS, JUMPING, JUMPING_SHIELD, RUNNING, DEFAULT_TYPE, RUNNING_SHIELD, SHIELD_TYPE,HAMMER_TYPE,JUMPING_HAMMER,RUNNING_HAMMER
from pygame.sprite import Sprite

from dino_runner.utils.text_utils import draw_message_component




DUCK_ING = {DEFAULT_TYPE: DUCKING, SHIELD_TYPE: DUCKING_SHIELD, HAMMER_TYPE:DUCKING_HAMMER}
JUMP_ING = {DEFAULT_TYPE: JUMPING, SHIELD_TYPE: JUMPING_SHIELD, HAMMER_TYPE:JUMPING_HAMMER}
RUN_ING = {DEFAULT_TYPE: RUNNING, SHIELD_TYPE: RUNNING_SHIELD, HAMMER_TYPE:RUNNING_HAMMER}

class Dinosaur(Sprite):
    X_POS=80
    Y_POS=310
    Y_POS_DUCK = 340
    JUMP_VEL=8.5
    
    def __init__(self):
        self.type = DEFAULT_TYPE
        self.image=RUN_ING[self.type][0]
        self.dino_rect=self.image.get_rect()
        self.dino_rect.x=self.X_POS
        self.dino_rect.y=self.Y_POS
        self.step_index=0
        self.dino_run=True
        self.dino_jump=False
        self.dino_duck=False
        self.jump_vel=self.JUMP_VEL
        self.setup_state()

    def setup_state(self):
        self.has_power_up = False
        self.show_text = False

        self.shield = False
        self.hammer = False 
        self.shield_time_up = 0

    def update(self,user_input):
        if self.dino_run:
            self.run()
        elif self.dino_jump:
            self.jump()
        elif self.dino_duck:
            self.duck()

        if user_input[pygame.K_UP] and not self.dino_jump:
            self.dino_jump=True
            self.dino_run=False
            self.dino_duck=False

        elif user_input[pygame.K_DOWN] and not self.dino_duck:
            self.dino_jump=False
            self.dino_run=False
            self.dino_duck=True

        elif not self.dino_jump and not self.dino_duck:

            self.dino_jump=False
            self.dino_duck=False
            self.dino_run=True
        

        if self.step_index>=9:
            self.step_index=0

    def duck(self):
        self.image=DUCK_ING[self.type][self.step_index // 5]
        self.dino_rect =self.image.get_rect()
        self.dino_rect.x = self.X_POS
        self.dino_rect.y = self.Y_POS_DUCK
        self.step_index += 1 
        
            

    def run(self):
        
        self.image=RUN_ING[self.type][self.step_index // 5] 
        self.dino_rect=self.image.get_rect()
        self.dino_rect.x=self.X_POS
        self.dino_rect.y=self.Y_POS
        self.step_index+=1

    def jump(self):
        self.image=JUMP_ING[self.type]
        if self.dino_jump:
            self.dino_rect.y-=self.jump_vel*4
            self.jump_vel-=0.8
        
        if self.jump_vel<-self.JUMP_VEL:
            self.dino_rect.y=self.Y_POS
            self.dino_jump=False
            self.jump_vel=self.JUMP_VEL

    def check_invincibility(self, screen):
        if self.shield or self.hammer:
            time_to_show = round((self.shield_time_up - pygame.time.get_ticks()) / 1000, 2)
            if time_to_show >= 0 and self.show_text:
                if self.shield:
                    self.mensaje="Shield"
                else:
                    self.mensaje="Hammer"

                draw_message_component(f"" + self.mensaje + " enabled for {time_to_show}",
                                    screen,
                                    font_size=18, 
                                    pos_x_center=500,
                    pos_y_center=40
                )
            else:
                self.shield = False
                self.hammer=False
                self.type = DEFAULT_TYPE
        

    def draw(self, screen:pygame.Surface):
        screen.blit(self.image,(self.dino_rect.x,self.dino_rect.y))
        

    def draw_background(self):
        image_width=BG.get_width()
        self.screen.blit(BG,(self.x_pos_bg,self.y_pos_bg))
        self.screen.blit(BG,(image_width+self.x_pos_bg,self.y_pos_bg))
        if self.x_pos_bg<=-image_width:
            self.screen.blit(BG,(image_width+self.x_pos_bg,self.y_po_bg))


