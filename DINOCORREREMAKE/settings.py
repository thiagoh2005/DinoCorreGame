import pygame
pygame.init()

screen = pygame.display.set_mode((600,600))
display = pygame.Surface((400,400))
clock = pygame.time.Clock()


pygame.mixer.pre_init(44100, -16, 2, 512)


#menu 
title_surf = pygame.transform.scale(pygame.image.load('title.png'), (303,48))

text_font = pygame.font.Font('pixeltype-regular.ttf', 35)

player_sprite_path = 'dino1.png'



play_button_surf = pygame.transform.scale(pygame.image.load('play_button.png'), (150,40))
play_button_rect = play_button_surf.get_rect(center = (300, 400))

options_button_surf = pygame.transform.scale(pygame.image.load('options_button.png'), (150,40))
options_button_rect = options_button_surf.get_rect(center = (300, 460))
options_text = text_font.render('its already 01:30 am,', False, (80,80,100))
options_text_rect = options_text.get_rect(topleft =(150,160))
options_text2 = text_font.render('Im not doing the options menu,', False, (80,80,100))
options_text2_rect = options_text2.get_rect(topleft =(150,200))
options_text3 = text_font.render('I want to sleep', False, (80,80,100))
options_text3_rect = options_text3.get_rect(topleft =(150,240))

select_dino1_button_surf = pygame.transform.scale(pygame.image.load('select_dino1.png'), (36,75))
sd1_button_rect =select_dino1_button_surf.get_rect(center = (450, 460))
select_dino2_button_surf = pygame.transform.scale(pygame.image.load('select_dino2.png'), (78,78))
sd2_button_rect =select_dino2_button_surf.get_rect(center = (150, 460))




credit_button_surf = pygame.transform.scale(pygame.image.load('credits_button.png'), (150,40))
credit_button_rect = credit_button_surf.get_rect(center = (300, 520))
credits_text = text_font.render('Game made by thiagoh2005', False, (80,80,100))
credits_text_rect = credits_text.get_rect(topleft =(130,380))
credits_text2 = text_font.render('Thanks for playing my game,', False, (80,80,100))
credits_text2_rect = credits_text2.get_rect(topleft =(130,200))
credits_text3 = text_font.render('check out thiagoh2005 on youtube!!!', False, (80,80,100))
credits_text3_rect = credits_text3.get_rect(topleft =(130,240))
credits_text4 = text_font.render('sfx downloaded at:', False, (80,80,100))
credits_text4_rect = credits_text4.get_rect(topleft =(50,280))
credits_text5 = text_font.render('www.classicgaming.cc/classics/pac-man/sounds', False, (80,80,100))
credits_text5_rect = credits_text4.get_rect(topleft =(50,320))

back_button_surf = pygame.transform.scale(pygame.image.load('back_button.png'), (150,40))
back_button_rect = credit_button_surf.get_rect(center = (300, 520))

bg = pygame.image.load('field.png')

#sounds


class Mouse(pygame.sprite.Sprite):

	def __init__(self):
		super().__init__()
		self.image = pygame.transform.scale(pygame.image.load('cursor.png'), (24,28))
	
		self.rect = self.image.get_rect(center = (300,300))

	def update(self):
		if pygame.mouse.get_pos():
			self.rect.center = pygame.mouse.get_pos()