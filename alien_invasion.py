import pygame

from pygame.sprite import Group
from settings import Settings
from game_stats import GameStats
from scoreboard import Scoreboard
from button import Button
from ship import Ship
from alien import Alien
import game_functions as gf 

def run_game():
	#Inicializa o pygame, as configurações e o objeo screen
	pygame.init()
	ai_settings = Settings()
	screen = pygame.display.set_mode(
	(ai_settings.screen_width, ai_settings.screen_height))
	pygame.display.set_caption("alien ivasion")
	
	#Cria o botão play
	play_button = Button(ai_settings, screen, "Play")
	
	#Cria uma instância para armazenar dados estatísticos do jogo
	stats = GameStats(ai_settings)
	sb = Scoreboard(ai_settings, screen, stats)
	
	#Cria uma espaçonave, um grupo de projéteiss e um grupo de alienígenas
	ship = Ship(ai_settings,screen)
	bullets = Group()
	aliens = Group()
	
	#Cria uma frota de alienígenas
	gf.create_fleet(ai_settings, screen, ship, aliens)
	
	#Inicia o laço principal do jogo
	while True:
		gf.check_events(ai_settings, screen, stats, sb, play_button, ship,
			aliens, bullets)
		if stats.game_active:
			ship.update() 
			gf.update_bullets(ai_settings, screen, stats, sb, ship, aliens, bullets)
			gf.update_aliens(ai_settings, stats, sb, screen, ship, aliens, bullets)
		gf.update_screen(ai_settings, screen, stats, sb, ship, aliens, bullets, play_button)
			
run_game() 
		
