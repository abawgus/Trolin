import pygame
import os, sys
from pygame.locals import *
#from backend import *
#import backend_david as backend
import textwrap
import backend_email	###
import backend_naomi	###
import backend_david2 as backend

class GUI(object):
	def __init__(self):
		pygame.init()

		#makes the GUI screen & sets the top caption
		self.background = pygame.display.set_mode((920,800))
		#self.character = pygame.display.set_mode()
		pygame.display.set_caption('TrOlin')
		
		#makes the miniquest Class (David's)	###@@@
		self.quest_manager = backend.quest_manager()
		
		#needed variables
		self.userinput = []
		self.text = 'Welcome to Olin!'
		self.text2 = ''
		self.text3 = ''
		self.text4 = ''
		self.text5 = ''
		self.url = 'BirdsEye.jpg'
		self.personurl = 'StickFig1.png'				###@@@
		self.emailurl = 'blankemail.png'		###
		#self.miniquesturl = 'blankminiquests.png'		###
		self.theword = ''
		self.thefinalword = ''
		self.image = pygame.image.load(os.path.join('Backgrounds', self.url))
		self.person = pygame.image.load(os.path.join('Characters', self.personurl))
		self.emailpic = pygame.image.load(os.path.join('EmailDisplay', self.emailurl))	###
		#self.miniquestspic = pygame.image.load(os.path.join('EmailDisplay', self.miniquesturl))	###
		
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
			for self.event in pygame.event.get():
			#event = pygame.event.poll()
				if self.event.type == QUIT:	#enables program to quit
					pygame.quit()
					sys.exit()
				elif self.event.type == KEYDOWN:	#reads when & what key is pressed
					self.thetyped = self.event.dict['unicode']
					self.keysdown(self.thetyped)
			
			#Prints the current bg and character onto GUI				
			self.background.blit(self.image, (10,10))
			self.background.blit(self.person, (10,10))
			self.background.blit(self.emailpic, (0,0))
			#self.background.blit(self.miniquestspic, (610,10))
			
			#Prints the current string onto the GUI
			self.thestringSurface = self.fontObj.render(self.theword, True, WHITE)
			self.thestringRect = self.thestringSurface.get_rect()
			self.thestringRect.midleft = (58, 771)
			self.background.blit(self.thestringSurface, self.thestringRect)
			
			#Wraps the current text/dialogue
			textlist = textwrap.wrapline(self.text, self.fontObj, 880)
			try:
				self.text = textlist[0]
				self.text2 = textlist[1]
				self.text3 = textlist[2]
				self.text4 = textlist[3]
				self.text5 = textlist[4]
			except: 
				pass
				
			#Prints the current text/dialogue onto the GUI
			self.thedialogueSurface = self.fontObj.render(self.text, True, WHITE)
			self.thedialogueRect = self.thedialogueSurface.get_rect()
			self.thedialogueRect.topleft = (20, 588)
			self.background.blit(self.thedialogueSurface, self.thedialogueRect)
					
			#Prints the current text/dialogue onto the GUI
			self.thedialogueSurface2 = self.fontObj.render(self.text2, True, WHITE)
			self.thedialogueRect2 = self.thedialogueSurface2.get_rect()
			self.thedialogueRect2.topleft = (20, 614)
			self.background.blit(self.thedialogueSurface2, self.thedialogueRect2)
			
			#Prints the current text/dialogue onto the GUI
			self.thedialogueSurface3 = self.fontObj.render(self.text3, True, WHITE)
			self.thedialogueRect3 = self.thedialogueSurface3.get_rect()
			self.thedialogueRect3.topleft = (20, 640)
			self.background.blit(self.thedialogueSurface3, self.thedialogueRect3)
			
			#Prints the current text/dialogue onto the GUI
			self.thedialogueSurface4 = self.fontObj.render(self.text4, True, WHITE)
			self.thedialogueRect4 = self.thedialogueSurface4.get_rect()
			self.thedialogueRect4.topleft = (20, 666)
			self.background.blit(self.thedialogueSurface4, self.thedialogueRect4)
			
			#Prints the current text/dialogue onto the GUI
			self.thedialogueSurface5 = self.fontObj.render(self.text5, True, WHITE)
			self.thedialogueRect5 = self.thedialogueSurface5.get_rect()
			self.thedialogueRect5.topleft = (20, 692)
			self.background.blit(self.thedialogueSurface5, self.thedialogueRect5)
			
			#changes the display
			pygame.display.flip()		
			
	#letter takes the user's input letters and makes a string...
	#until enter is pressed
	def letter(self, thekey, userinput):
		self.theletter = thekey
		#theletter = theletter.strip()
		self.userinput.append(self.theletter)
		return ''.join(self.userinput)
		
	#identifies what is typed, outputs it to blits to display on GUI
	def keysdown(self, thetyped):
		self.theword = self.letter(thetyped, self.userinput)	#the growing string
		if self.event.type == KEYDOWN and self.event.key == K_RETURN:
			self.thefinalword = self.theword		#the final string
			self.thefinalword = self.thefinalword.lower()
			self.thefinalword = self.thefinalword.strip()
			
			#identifying the string & running backend
			self.thefinalstring = self.thefinalword.split()
			j = len(self.thefinalstring)
			if j == 0:
				pass	#later turn into "continue" for conversation?
			else:
				firstword = self.thefinalstring[0]
				self.lastword = self.thefinalstring[1:j]	
				self.lastwordlength = len(self.lastword)
				
				#GOTO identifier
				if firstword == 'goto' or firstword == 'go':
					self.goto()
					
				#EMAIL identifier	###
				if firstword == 'check':
					self.emailfunc()

				#EXIT identifier	###
				if firstword == 'exit' or firstword == 'quit':
					self.emailurl = 'blankemail.png'
					#self.miniquesturl = 'blankminiquests.png'
								
				#loading the bg and person images
				self.image = pygame.image.load(os.path.join('Backgrounds',self.url))
				self.person = pygame.image.load(os.path.join('Characters', 'StickFig2.png'))
				self.emailpic = pygame.image.load(os.path.join('EmailDisplay', self.emailurl))	###
				#self.miniquestspic = pygame.image.load(os.path.join('EmailDisplay', self.miniquesturl))	###
				self.userinput = []		#resetting the userinput
				self.theword = ''		#resetting the displayed text
				
		if self.event.type == KEYDOWN and self.event.key == K_BACKSPACE:	#backspace!
			i = len(self.theword)
			self.userinput = self.userinput[0:i-2]
			self.theword = self.theword[0:i-2]
			
	def emailfunc(self):
		if self.lastwordlength == 0:
			if self.emailurl == 'blankemail.png':
				self.text = 'Check what?'
			else:
				self.text = "You've refreshed the page. Congratulations, nothing has changed."
		else:
			self.changelastwordtostring()
			self.newurl = backend_email.email(self.lastword)
			if self.newurl == None:
				"Sorry, it may have a nice ass, but you probably shouldn't be checking it out."
			else:
				self.emailurl = self.newurl
				#self.emailurl = self.newurl[0]
				#self.miniquesturl = self.newurl[1]
				
	def goto(self):
		if self.lastwordlength == 0:
			self.text = 'Go where?'
		elif self.lastword[0] == 'to':
			self.lastword = self.lastword[1:self.lastwordlength]
			self.run_goto()
		else:
			self.run_goto()
				
	def run_goto(self):
		self.changelastwordtostring()
		self.questlist = self.quest_manager.goto(self.lastword)	###@@@ and below
		if self.questlist[1] == None:
			self.text = 'Sorry, you have to stay in the bubble.'
		else:
			self.url = self.questlist[1]
			self.personurl = self.questlist[2]
			self.text = self.questlist[3]
			
	#changes lastword to string so backend can read it
	#note: this change happens later rather than sooner so analysis on the list can still occur
	def changelastwordtostring(self):
		delimiter = ' '
		self.lastword = delimiter.join(self.lastword)
		
#runs the GUI by making it into a class
theGUI = GUI()
