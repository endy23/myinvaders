import pygame
from pygame.locals import *
from sys import exit

class Craft(object):
	def __init__(self,imagefile,coord):
		self.shape = pygame.image.load(imagefile)
		self.ship_width = self.shape.get_width()
		self.ship_height = self.shape.get_height()
		self.rect = pygame.Rect(coord, (self.ship_width, self.ship_height))
		
	def Show(self, surface):
		surface.blit(self.shape,(self.rect[0], self.rect[1]))
		
	def Move(self, speed_x, speed_y, time):
		distance_x = speed_x * time
		distance_y = speed_y * time
		self.rect.move_ip(distance_x, distance_y)
		
	def Fire(self):
		pass
		
class SpaceCraft(Craft):
	def __init__(self, imagefile, coord, min_coord, max_coord):
		super(SpaceCraft, self).__init__(imagefile, coord)
		self.min_coord = min_coord
		self.max_coord = (max_coord[0] - self.ship_width, max_coord[1] - self.ship_height)
	
	def Move(self, speed_x, speed_y, time):
		super(SpaceCraft, self).Move(speed_x, speed_y, time)
		for i in (0,1):
			if self.rect[i] < self.min_coord[i]:
				self.rect[i] = self.min_coord[i]
			if self.rect[i] > self.max_coord[i]:
				self.rect[i] = self.max_coord[i]
	
class SpaceBackground:
	def __init__(self,coord, imagefile):
		self.shape = pygame.image.load(imagefile)
		self.coord = coord
		
	def Show(self, surface):
		surface.blit(self.shape, self.coord)
		
	def Scroll(self, speed_y, time):
		pass
		
	
def getQuit():
	for event in pygame.event.get():
		if event.type==QUIT:
			return True
	return False
	
def PlayMusic(soundfile):
	pygame.mixer.music.load(soundfile)
	pygame.mixer.music.play(-1)
			
def main():
	
	pygame.init()
	screenwidth, screenheight = (480, 640)
	spaceship_pos = (240,540)
	screen = pygame.display.set_mode((screenwidth, screenheight), DOUBLEBUF, 32)
	pygame.display.set_caption("Pygame Invaders")
	pygame.key.set_repeat(1,1)
	StarField = SpaceBackground((480, 640),"stars.jpg")
	spaceship_low = (0,0)
	spaceship_high = (screenwidth, screenheight)
	SpaceShip = SpaceCraft("spaceship2.png", spaceship_pos, spaceship_low, spaceship_high)
	clock = pygame.time.Clock()
	framerate = 60
	laser = pygame.mixer.Sound("laser.wav")
	laser.play()
	PlayMusic("spaceinvaders.ogg")
	while True:
		time = clock.tick(framerate)/1000.0
		shipspeed_x = 0
		shipspeed_y = 0
		for event in pygame.event.get():
			if event.type == QUIT:
				pygame.quit()
				exit()
			if event.type == KEYDOWN:
				key = pygame.key.get_pressed()
				if key[K_q]:
					pygame.quit()
					exit()
				if key[K_LEFT]:
					shipspeed_x = -300
				if key[K_RIGHT]:
					shipspeed_x = 300 
				if key[K_UP]:
					shipspeed_y = -300
				if key[K_DOWN]:
					shipspeed_y = 300 

		SpaceShip.Move(shipspeed_x, shipspeed_y, time)
		StarField.Show(screen)
		SpaceShip.Show(screen)
		pygame.display.update()
	

if __name__ == "__main__":
	main()
	
