from ast import Pass
from msilib.schema import Font
import pygame
from dino_runner.components.dinosaur import Dinosaur
from dino_runner.components.obstacles.obstacle_manager import ObtacleManager
from dino_runner.utils.constants import BG, ICON, RUNNING, SCREEN_HEIGHT, SCREEN_WIDTH, TITLE, FPS

FONT_STYLE = "freesansbold.ttf"

class Game:
    def __init__(self):
        pygame.init()
        pygame.display.set_caption(TITLE)
        pygame.display.set_icon(ICON)
        self.screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))
        self.clock = pygame.time.Clock()
        self.playing = False
        self.player=Dinosaur() #aca muestra el dinosaurio
        self.running = False
        self.obstacle_manager= ObtacleManager()
        self.game_speed = 20
        self.x_pos_bg = 0
        self.y_pos_bg = 380

        self.points = 0
        self.death_count = 0

    def execute(self):
        self.running = True
        while self.running:
            if not self.playing:
                self.show_menu() 

        pygame.display.quit()
        pygame.quit()

    def run(self):
        # Game loop: events - update - draw
        self.obstacle_manager.reset_obstacles()
        self.playing = True
        while self.playing:
            self.events()
            self.update()
            self.draw()

    def events(self):
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                self.playing = False
                self.playing = False

    # How to update points

    def update(self):
        self.update_score()
        user_input=pygame.key.get_pressed()
        self.player.update(user_input)
        self.obstacle_manager.update(self)

    def update_score(self):
        # incrementar puntos
        #incrementar la velocidad de juego cada 100 puntos en 1
        self.points +=1
        if self.points % 100 == 0:
            self.game_speed += 20

    def draw(self):
        self.clock.tick(FPS)
        self.screen.fill((255, 255, 255))
        self.draw_score()
        self.draw_background()
        self.player.draw(self.screen)
        self.obstacle_manager.draw(self.screen)
        pygame.display.update()
        pygame.display.flip()

    def draw_background(self):
        image_width = BG.get_width()
        self.screen.blit(BG, (self.x_pos_bg, self.y_pos_bg))
        self.screen.blit(BG, (image_width + self.x_pos_bg, self.y_pos_bg))
        if self.x_pos_bg <= -image_width:
            self.screen.blit(BG, (image_width + self.x_pos_bg, self.y_pos_bg))
            self.x_pos_bg = 0
        self.x_pos_bg -= self.game_speed

    def draw_score(self):
        font = pygame.font.Font(FONT_STYLE, 22)
        text = font.render(f"Points: {self.points}", True, (0,0,0)) #change color
        text_rect = text.get_rect()
        text_rect.center = (1000, 50)
        self.screen.blit(text, text_rect)

    def handle_key_events_on_menu(self):
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                self.playing = False
                self.running = False
                pygame.display.quit()
                pygame.quit()
                exit()

            if event.type == pygame.KEYDOWN:
                 #Tarea
                 #REINCIAR PUNTOS Y VELOCIDAD
                self.points=0
                self.game_speed = 20
                self.run()
                

    def show_menu(self):
        self.screen.fill((255, 255, 255)) #chage color
        half_screen_height = SCREEN_HEIGHT //2
        half_screen_width = SCREEN_WIDTH //2

        if self.death_count == 0:
            font = pygame.font.Font(FONT_STYLE, 30)
            text = font.render("Press any key to start", True, (0,0,0)) #chage color
            text_rect = text.get_rect()
            text_rect.center = (half_screen_width, half_screen_height)
            self.screen.blit(text, text_rect)
        elif self.death_count > 0:
             #Tarea
            #MOSTRAR PUNTOS ACTUALES | puntos riniciados
            font = pygame.font.Font(FONT_STYLE, 30)
            text_score= font.render(f"YOUR SCORE IS: {self.points}",True,(0,0,0) )
            text_rect=text_score.get_rect()
            text_rect.center=(half_screen_width, half_screen_height)
            self.screen.blit(text_score,text_rect)
            #numero de muertes
            text_numero_de_Muertes= font.render(f"YOU DIED {self.death_count} TIMES",True,(0,0,0) )
            text_rect=text_numero_de_Muertes.get_rect()
            text_rect.center=(half_screen_width, half_screen_height+30)
            self.screen.blit(text_numero_de_Muertes,text_rect)
            #MOSTRAR UN MENSAJE PARA REINICIAR
            text_reinciar= font.render(f"Presiona cualquier tecla para reiniciar.",True,(0,0,0) )
            text_rect=text_reinciar.get_rect()
            text_rect.center=(half_screen_width, half_screen_height+60)
            self.screen.blit(text_reinciar,text_rect)
            

         
        # aca muestra el final
        self.screen.blit(RUNNING[0], (half_screen_width - 20, half_screen_height - 140))
       

        pygame.display.update()
        self.handle_key_events_on_menu()
