#Trolin Group Backend, Software Design Spring 2012

#Gui: user hits enter, calls class backend_email.email(input)
import pygame
import os, sys

words={'email':1, 'mail':1, 'miniquests':1, 'quests':1, 'tasks':1, 'quest list':1, 'miniquest list':1, 'email list':1}
emailmenu = pygame.display.set_mode((900,560))###&&&

#needed variables
headerpic = pygame.image.load(os.path.join('EmailDisplay', 'Header.png'))

#Reads the input; returns none or runs display
#also input David's thing
def email(input):		
	value=words.get(input,0)
	if value==0:
		return None
	elif value==1:
		return display()	#put in David's list/dict thing in later
		
	#self.miniquesturl = 'blankminiquests.png'		###
	#self.emailpic = pygame.image.load(os.path.join('EmailDisplay', self.emailurl))	###
	#self.miniquestspic = pygame.image.load(os.path.join('EmailDisplay', self.miniquesturl))	###
	
def display():
	emailmenu.blit(headerpic, (10,10))
	
	
	
	emailpic = pygame.image.save(emailmenu,os.path.join('EmailDisplay','emailimage.png'))
	return 'emailimage.png'
	#self.background.blit(self.image, (10,10))

	#return [self.emailpic, self.emailRect]
