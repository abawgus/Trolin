import pygame
import os, sys
from pygame.locals import *
#from backend import *
import backend_david as backend

class GUI(object):
	def __init__(self):
		#letter takes the user's input letters and makes a string...
		#until enter is pressed
		def letter(self, thekey, userinput):
			self.theletter = thekey
			#theletter = theletter.strip()
			self.userinput.append(self.theletter)
			return ''.join(self.userinput)

		pygame.init()

		#makes the GUI screen & sets the top caption
		self.background = pygame.display.set_mode((920,800))
		#self.character = pygame.display.set_mode()
		pygame.display.set_caption('TrOlin')
		
		#needed variables
		self.userinput = []
		text = 'Welcome to Olin!'
		global theword
		theword = ''
		global thefinalword
		thefinalword = ''
		global image
		image = pygame.image.load(os.path.join('Backgrounds', 'BirdsEye.jpg'))
		global person
		person = pygame.image.load(os.path.join('Characters', 'StickFig1.png'))
		
		 
		#establishing colors
		GREEN = (0,255,0)
		BLUE = (0,0,128) 
		BLACK = (0,0,0)
		WHITE = (255,255,255)
		
		#The Font and the text box
		self.fontObj = pygame.font.Font('freesansbold.ttf', 24)
		self.inputthings = self.fontObj.render('>>', True, WHITE)
		self.inputrect = self.inputthings.get_rect()
		self.inputrect.center = (35, 768)

		while True:	#main game loop
			self.background.fill(BLUE)		#makes white bg
			pygame.draw.rect(self.background, BLACK, (10, 580, 900, 160))	#makes dialogue box
			pygame.draw.rect(self.background, BLACK, (10, 750, 900, 40))	#makes black textbar
			self.background.blit(self.inputthings, self.inputrect)		#inputs '>>'
			
			
			#The main event loop; reads and uses the user's input events
			for event in pygame.event.get():
			#event = pygame.event.poll()
				if event.type == QUIT:	#enables program to quit
					pygame.quit()
					sys.exit()
				elif event.type == KEYDOWN:	#reads when & what key is pressed
					theword = letter(self, event.dict['unicode'], self.userinput)	#the growing string
					if event.type == KEYDOWN and event.key == K_RETURN:
						thefinalword = theword		#the final string
						thefinalword = thefinalword.lower()
						thefinalword = thefinalword.strip()
						
						#identifying the string & running backend
						thefinalstring = thefinalword.split()
						j = len(thefinalstring)
						if j == 0:
							pass
						else:
							firstword = thefinalstring[0]
							lastword = thefinalstring[1:j]	
							k = len(lastword)
							delimiter = ' '
							lastword = delimiter.join(lastword)
							
							"""#GOTO identifier
							if firstword == 'goto' or firstword == 'go':
								if k == 0:
									print 'Go where?'
								elif lastword[0] == 'to':
									lastword = lastword[1:k]
								else:
									url = backend.goto(lastword)
									print url"""
							
							image = pygame.image.load(os.path.join('Backgrounds','GreatLawn.jpg'))
							person = pygame.image.load(os.path.join('Characters', 'StickFig2.png'))
							self.userinput = []
							theword = ''
					if event.type == KEYDOWN and event.key == K_BACKSPACE:	#backspace!
						i = len(theword)
						self.userinput = self.userinput[0:i-2]
						theword = theword[0:i-2]
			
			#Prints the current bg and character onto GUI				
			self.background.blit(image, (10,10))
			self.background.blit(person, (10,10))
			
			#Prints the current string onto the GUI
			self.thestringSurface = self.fontObj.render(theword, True, WHITE)
			self.thestringRect = self.thestringSurface.get_rect()
			self.thestringRect.midleft = (58, 771)
			self.background.blit(self.thestringSurface, self.thestringRect)
			
			#Prints the current text/dialogue onto the GUI
			self.thedialogueSurface = self.fontObj.render(text, True, WHITE)
			self.thedialogueRect = self.thedialogueSurface.get_rect()
			#self.thedialogueRect = Rect(10, 580, 900, 160)
			self.thedialogueRect.topleft = (20, 588)
			self.background.blit(self.thedialogueSurface, self.thedialogueRect)
					
			#changes the display
			pygame.display.flip()		

#runs the GUI!	
theGUI = GUI()
