import pygame, sys, random
from settings import *
from entities import Player, Obstacle, Power_up


b_mouse = pygame.sprite.GroupSingle(Mouse())

pygame.mixer.music.load('pacman_beginning.wav')
pygame.mixer.music.play(-1)

#player section

score = 0
highscore = open('highscore.txt', 'r').read()

spawn_points = [(40,20),(80,20),(120,20),(160,0),(200,20),(240,20),(280,20),(320,20),(360,0)]
size_proportion = [(20,20), (20, 20), (30,30), (35,35), (40,40), (45,45), (50,50)]
obstacle_group = []
power_up_group = []
time_conter = 0

highscore_text = text_font.render(f'highscore: {highscore}', False, 'black')
highscore_text_rect = highscore_text.get_rect(topleft = (50, 250))

heart = pygame.Surface((10,20))
heart.fill('red')

game_on = False
options_on = False
credits_on = False

pygame.mouse.set_visible(False)

while True:
	highscore = open('highscore.txt', 'r').read()
	player = Player(10, (200,200), player_sprite_path)

	screen.fill((180,180,200))
	for event in pygame.event.get():
		if event.type == pygame.QUIT:
			pygame.quit()
			exit()
		if event.type == pygame.MOUSEBUTTONDOWN:
			
			if play_button_rect.collidepoint(event.pos): 
				if pygame.mouse.get_pressed():
					pygame.mixer.music.load('pacman_ringtone.mp3')
					pygame.mixer.music.play(-1)
					game_on = True
			if options_button_rect.collidepoint(event.pos): 
				if pygame.mouse.get_pressed():
					options_on = True
					print('open options')
			if credit_button_rect.collidepoint(event.pos): 
				if pygame.mouse.get_pressed():
					credits_on = True

	screen.blit(title_surf, (150,50))
	screen.blit(play_button_surf,play_button_rect)
	screen.blit(options_button_surf,options_button_rect)
	screen.blit(credit_button_surf,credit_button_rect)
	screen.blit(highscore_text, highscore_text_rect)

	b_mouse.draw(screen)
	b_mouse.update()

	while options_on:
		screen.fill((180,180,200))
		
		for event in pygame.event.get():
			if event.type == pygame.QUIT:
				pygame.quit()
				exit()
			if event.type == pygame.MOUSEBUTTONDOWN:
				if back_button_rect.collidepoint(event.pos): 
					if pygame.mouse.get_pressed():
						options_on = False
				if sd2_button_rect.collidepoint(event.pos): 
					if pygame.mouse.get_pressed():
						player_sprite_path = 'dino2.png'
				if sd1_button_rect.collidepoint(event.pos): 
					if pygame.mouse.get_pressed():
						player_sprite_path = 'dino1.png'

		screen.blit(back_button_surf, back_button_rect)	

		screen.blit(options_text, options_text_rect)
		screen.blit(options_text2, options_text2_rect)	
		screen.blit(options_text3, options_text3_rect)

		screen.blit(select_dino1_button_surf, sd1_button_rect)
		screen.blit(select_dino2_button_surf, sd2_button_rect)

		b_mouse.draw(screen)
		b_mouse.update()	

		pygame.display.update()
		clock.tick(60)

	while credits_on:
		screen.fill((180,180,200))

		for event in pygame.event.get():
			if event.type == pygame.QUIT:
				pygame.quit()
				exit()
			if event.type == pygame.MOUSEBUTTONDOWN:
				if back_button_rect.collidepoint(event.pos): 
					if pygame.mouse.get_pressed():
						credits_on = False

		screen.blit(back_button_surf, back_button_rect)

		screen.blit(credits_text2, credits_text2_rect)
		screen.blit(credits_text, credits_text_rect)
		screen.blit(credits_text3, credits_text3_rect)	
		screen.blit(credits_text4, credits_text4_rect)
		screen.blit(credits_text5, credits_text5_rect)

		b_mouse.draw(screen)
		b_mouse.update()

		pygame.display.update()
		clock.tick(60)
		


	while game_on:

		score += 1

		display.blit(bg,(0,0))

		for event in pygame.event.get():
			if event.type == pygame.QUIT:
				pygame.quit()
				exit()
			if event.type == pygame.KEYDOWN:
				if event.key == pygame.K_w:
					obstacle_group.append(Obstacle(random.choice(size_proportion),random.choice(spawn_points)))


		display.blit(player.image, player.rect)

		if time_conter == 0:
			for sp in spawn_points:
				if random.choice([0,1]):
					obstacle_group.append(Obstacle(random.choice(size_proportion), sp))
			if random.choice([0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,1]):
				power_up_group.append(Power_up((20,20), random.choice(spawn_points)))
			time_conter = 50
		else:
			time_conter -= 1

		x, y = 20, 20
		for hp in range(player.health):
			display.blit(heart, (x,y))	
			x += 20

		player.update()
		for ob in obstacle_group:
			display.blit(ob.image, ob.rect)
			ob.update()

			if ob.rect.colliderect(player.rect):
				player.health -= 1
				obstacle_group.pop(obstacle_group.index(ob))
		for ob in power_up_group:
			display.blit(ob.image, ob.rect)
			ob.update()
			if ob.rect.colliderect(player.rect):
				print('power up')
				player.health += 1
				power_up_group.pop(power_up_group.index(ob))

		if player.health == 0:
			print(int(score/100))
			f = open('highscore.txt', 'r')
			value = f.read()
			if int(score/100) > int(value):
				f = open('highscore.txt', 'w')
				f.write(f'{int(score/100)}')
			game_on = False

		screen.blit(pygame.transform.scale(display, (600, 600)), (0,0))
		pygame.display.update()
		clock.tick(60)

	
	pygame.display.update()
	clock.tick(60)