import pygame
from pygame import mixer
import random
import os

#Setup ****************
pygame.init()
pygame.mixer.init()
dis = width,height=720,1600
screen=pygame.display.set_mode(dis,pygame.FULLSCREEN)
pygame.display.set_caption('Snake Game')
pygame.display.update()
clock= pygame.time.Clock()



# Colors ****************
white = ((255,255,255))
black= ((0,0,0))
game_ground=((0,0,0))
border_color = ((97,57,30))
red =((255,0,0,0))
snake_img = pygame.image.load('snakeblock.png')
snake_img= pygame.transform.scale(snake_img,(40,40))


	




# Game Setup ***************
def setup(x,y):
	pygame.draw.rect(screen,border_color,(0,0,720,1040))
	pygame.draw.rect(screen,game_ground,(15,15,690,1000))
	pygame.draw.rect(screen,red,(x,y,20,20))

	
			
# Snake Ploting  ***************
def plot_snake(l,a,b):
	for x,y in l:
		pygame.draw.rect(screen,(0,255,0),(x,y,a,b),2,0,0,0)
		screen.blit(snake_img,(x-10,y-9))
	
	

# Text On Screen ***************
def text_screen(font,txt,x,y):
	screen_txt=font.render(txt,True,red)
	screen.blit(screen_txt,(x,y))
	



# Infine Loop ***************
def gameloop():
	# If high Score file does not exists
	if not os.path.isfile('highscore.txt'):
		open('highscore.txt','x') 
		with open ('highscore.txt','w') as f:
			f.write(str(1))

# Game Loop Variables ***************
	game_over= False
	exit_game= False
	
	mixer.music.load('backgroundmusic.mp3')
	mixer.music.play(-1)
	
# Snake Variables ***************
	snake_x_size=20
	snake_y_size=20
	snake_list=[]
	snake_length=1
	velocity_x = 0
	velocity_y=0
	
	# Speed Of  Snake *******************
	snake_speed = 8
	
	
	snake_x=200
	snake_y=300
	
# High Score 
	with open('highscore.txt','r') as f:
		highscore = f.read()
	
# Food ****************
	food_x=random.randint(20,690)
	food_y=random.randint(20,1000)


# Font ****************
	font=pygame.font.Font('freesansbold.ttf',40)
	font1=pygame.font.Font('freesansbold.ttf',80)
	
	
# Arrow *****************
	arrow_x=300
	arrow_y=1100
	
	
	fps=40
	
# Images *********************
	cursor_img = pygame.image.load('arrows.png')
	cursor_img = pygame.transform.scale(cursor_img,(390,260))
	replay_img = pygame.image.load('replay.png')
	replay_img= pygame.transform.scale(replay_img,(400,150))

	
	
# Score *********************
	score =0
	
	while not exit_game:
		
		
		# Game Over *****************
		if game_over:
# Writing High Score in high score file
			with open('highscore.txt','w') as f:
				f.write(str(highscore))
				
				
			pygame.draw.rect(screen,white,(130,100,500,400))
			text_screen(font1,'Game Over',150,200)
			screen.blit(replay_img,(150,300))
			for event in pygame.event.get():
				
				if event.type == pygame.MOUSEBUTTONDOWN:
					(pos_x,pos_y)= (pygame.mouse.get_pos())
					
		#  Replay ********************************************
					if pos_x>=150 and pos_x<=550:
						if pos_y>=300 and pos_y <= 450:
							gameloop()
		
			
# If game not over	***************************************
		else:
			screen.fill((0,0,0))
			
			setup(food_x,food_y)
			
# Arrow **************************************************
			screen.blit(cursor_img,(arrow_x,arrow_y))
			
			
# Snake Movement Controll ********************************
			for event in pygame.event.get():
				
				
# Quit Event 
				if event.type == pygame.QUIT:
					game_over = True
					exit_game = True
				
				
# IF MOVEMENT BY ARROWS
				if event.type == pygame.MOUSEBUTTONDOWN:
					(pos_x,pos_y)= (pygame.mouse.get_pos())										
		#  Down **********************************************
					if pos_x>=440 and pos_x<=570:
						if pos_y>=1100 and pos_y <= 1230:
							velocity_y= -snake_speed
							velocity_x=0		
							
							
		# Up *************************************************
					if pos_x>=440 and pos_x<=570:
						if pos_y>=1240 and pos_y <= 1460:
							velocity_y=snake_speed
							velocity_x=0
		
					
											
		# Right **********************************************
					if pos_x>= 580 and pos_x<=700:
						if pos_y>=1240 and pos_y <= 1360:
							velocity_x=snake_speed
							velocity_y=0
		
							
																	
		# Left  ***********************************************
					if pos_x>=440-140 and pos_x<=570-140:
						if pos_y>=1240 and pos_y <= 1360:
							velocity_x=-snake_speed
							velocity_y=0			
							
		
 # If snake eat food ***********************************
			if abs((snake_x+10)-(food_x+10)) <=12 and abs((snake_y+10)-(food_y+10)) <=12:
							score+=10
							snake_length+=8
							eating_sound = mixer.Sound('applecrunch.wav')
							eating_sound.play()
							food_x=random.randint(20,690)
							food_y=random.randint(20,1000)
							
					
			snake_x+=velocity_x
			snake_y+=velocity_y	
			
# High Score Updation
			if score > int(highscore):
				highscore=score
			

# Score On screen
			text_screen(font,'Score = '+str(score),20,1050)
			text_screen(font,'High Score = '+str(highscore),20,1100)
							
							
# Snake head ********************************************
			head=[]
			head.append(snake_x)
			head.append(snake_y)
			snake_list.append(head)
			
			
			if len(snake_list) > snake_length:
				del snake_list[0]
			
			
# Snake Collide	*****************************************
			if head in snake_list[:-1]:
				mixer.music.load('explosion.mp3')
				mixer.music.play()
				game_over=True
				
			
#  Calling Function For ploting Snake ***********************
			plot_snake(snake_list,snake_x_size,snake_y_size)
			
			
# If Snake touch boudry ***********************************
			if snake_x<=15 or snake_x >=690 or snake_y<=15 or snake_y>=1000:
				mixer.music.load('explosion.mp3')
				mixer.music.play()
				game_over=True
		
						
		
						
		
# fps ****************************************************
		clock.tick(fps)
		
# Update Statement **************************************
		pygame.display.update()
	
		
# Quit	**************************************************
	pygame.quit()
	quit()
	
	
# Calling Function Gameloop *******************************
gameloop()






