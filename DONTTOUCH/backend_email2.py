import pygame
import os, sys

class email(object):
	def __init__(self, menu):
		self.emailmenu = menu

		#needed variables
		self.emailurl = 'Header.png'		###
		self.miniquesturl = 'blankminiquests.png'		###
		self.emailpic = pygame.image.load(os.path.join('EmailDisplay', self.emailurl))	###
		self.miniquestspic = pygame.image.load(os.path.join('EmailDisplay', self.miniquesturl))	###
		
	def display(self):
		self.emailRect = pygame.Rect(10,10,600,560)
		#self.emailRect = self.emailpic.get_rect()
		self.emailnewRect = self.emailRect.clamp(self.emailRect)
		self.emailRect.topleft = (10,10)
		
		self.emailmenu.blit(self.emailpic, self.emailRect)
		emailpic = pygame.image.save(self.emailmenu, 'email.png')
		return emailpic
		#self.background.blit(self.image, (10,10))

		#return [self.emailpic, self.emailRect]
