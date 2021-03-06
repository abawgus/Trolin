import pygame
import os, sys
from pygame.locals import *
import backend_david as backend
import textwrapS as textwrap

class GUI(object):
	def __init__(self):
		pygame.init()
		self.endPrompt = False #if the day has ended, prompt with sleep option
		self.l = False #if in a lecture or not
		self.sleep=True #moniters if character has slept the previous night
		
		#Lecture numbers for each class
		self.oie=1
		self.oielec1=0
		self.oielec2=0
		self.oielec3=0
		
		self.dn=1
		self.dnlec1=0
		self.dnlec2=0
		self.dnlec3=0
		
		self.modcon=1
		self.modconlec1=0
		self.modconlec2=0
		self.modconlec3=0
		
		self.modsim=1
		self.modsimlec1=0
		self.modsimlec2=0
		self.modsimlec3=0
		
		self.classnum=0  #number of classes you've had today
		self.day=1 #the day of the week

		#makes the GUI screen & sets the top caption
		self.background = pygame.display.set_mode((920,800))
		#self.character = pygame.display.set_mode()
		pygame.display.set_caption('TrOlin')
		
		#needed variables
		self.userinput = []
		self.text = 'Welcome to Olin!' #Intro Screen Settings
		self.text2 = ''
		self.text3 = ''
		self.text4 = ''
		self.text5 = ''
		self.url = 'BirdsEye.jpg'
		self.personurl=None
		self.theword = ''
		self.thefinalword = ''
		self.image = pygame.image.load(os.path.join('Backgrounds', 'BirdsEye.jpg'))
		self.person = pygame.image.load(os.path.join('Characters', 'none.png'))
		
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
			self.background.fill((47,79,79))		#makes white bg
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
			self.background.blit(self.person, (300,10))
			
			#Prints the current string onto the GUI
			self.thestringSurface = self.fontObj.render(self.theword, True, WHITE)
			self.thestringRect = self.thestringSurface.get_rect()
			self.thestringRect.midleft = (58, 771)
			self.background.blit(self.thestringSurface, self.thestringRect)
			
			#Wraps the current text/dialogue
			self.text=str(self.text)
			
			textlist = textwrap.wrapline(self.text,self.fontObj,880)
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
			#self.thedialogueRect = Rect(10, 580, 900, 160)
			self.thedialogueRect.topleft = (20, 588)
			self.background.blit(self.thedialogueSurface, self.thedialogueRect)
					
			#Prints the current text/dialogue onto the GUI
			self.thedialogueSurface2 = self.fontObj.render(self.text2, True, WHITE)
			self.thedialogueRect2 = self.thedialogueSurface2.get_rect()
			#self.thedialogueRect = Rect(10, 580, 900, 160)
			self.thedialogueRect2.topleft = (20, 614)
			self.background.blit(self.thedialogueSurface2, self.thedialogueRect2)
			
			#Prints the current text/dialogue onto the GUI
			self.thedialogueSurface3 = self.fontObj.render(self.text3, True, WHITE)
			self.thedialogueRect3 = self.thedialogueSurface3.get_rect()
			#self.thedialogueRect = Rect(10, 580, 900, 160)
			self.thedialogueRect3.topleft = (20, 640)
			self.background.blit(self.thedialogueSurface3, self.thedialogueRect3)
			
			#Prints the current text/dialogue onto the GUI
			self.thedialogueSurface4 = self.fontObj.render(self.text4, True, WHITE)
			self.thedialogueRect4 = self.thedialogueSurface4.get_rect()
			#self.thedialogueRect = Rect(10, 580, 900, 160)
			self.thedialogueRect4.topleft = (20, 666)
			self.background.blit(self.thedialogueSurface4, self.thedialogueRect4)
			
			#Prints the current text/dialogue onto the GUI
			self.thedialogueSurface5 = self.fontObj.render(self.text5, True, WHITE)
			self.thedialogueRect5 = self.thedialogueSurface5.get_rect()
			#self.thedialogueRect = Rect(10, 580, 900, 160)
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
				
			
			firstword = self.thefinalstring[0]
			#self.lastword = self.thefinalstring[1:j]	
			#self.k = len(self.lastword)
			
			self.personurl='none.png'
			self.text = ''
			self.text2 = ''
			self.text3 = ''
			self.text4 = ''
			self.text5 = ''
			
			if self.endPrompt:
				print firstword
				if firstword =='1':
					self.sleep = True
					self.endPrompt = False
					self.url='dorm.jpg'
					self.classnum=0
					self.day=self.day+1
				elif firstword == '2':
					self.sleep = False
					self.endPrompt = False
					self.url='lounge.jpg'
					self.classnum = 0
					self.day=self.day+1
				else:
					self.text="Answer the goddamn question"
			print self.endPrompt, self.classnum		
			if self.l and self.modconlec2 != 0 and j !=0: #if you are in the second modcon lecture
				self.url='lecture.jpg'
			
				ls1,lsop = backend.modconlec(self.sleep)
										
				if ls1[len(ls1)-1] and self.modconlec2 < len(ls1)-1: #
					self.text=ls1[self.modconlec2]
				elif ls1[len(ls1)-1] and self.modconlec2< len(ls1): # if there are options in the prompt
					choise= int(firstword)
					self.text=lsop[choise-1]
					if choise == 1:			
						self.url='notes.jpg'
						self.personurl='none.png'
				if ls1[len(ls1)-1]:
					if self.modconlec2 == len(ls1):
						self.l=False
						self.personurl == 'none.png'
						self.modconlec2 =0
						self.classnum=self.classnum+1
				elif ls1[len(ls1)-1] == False:
					if self.modconlec2 == len(ls1)-1:
						#print 'met condit lesson over'
						self.l=False
						self.classnum=self.classnum+1
						self.personurl='none.png'
						self.modconlec2 =0
				else: self.personurl='tempStorey.png'
				self.modconlec2=self.modconlec2+1
			else:
				pass
				
							
			if j == 0:
				pass	#later turn into "continue" for conversation?
			else:
				if self.classnum ==2:
					self.text="Well that was an event-filled day. What do you want to do? (1) Go to bed and get some rest before your classes (2) Stay up, you're at college for fucks sake"
					self.endPrompt = True
				firstword = self.thefinalstring[0]
				self.lastword = self.thefinalstring[1:j]	
				self.k = len(self.lastword)

				#classList=['modcon','modsim','design','' ]


				#GOTO identifier
				if self.l==False and firstword == 'goto' or firstword == 'go':
					if self.lastword[0] != 'modcon': #change to if lastword is not in list of classes
						self.goto()	
					elif self.lastword[0] == 'modcon' or self.lastword[1] == 'con': 
						ls1,lsop = backend.modconlec(self.sleep)
						self.text=ls1[self.modconlec2]
						
						self.url='lecture.jpg'
						self.personurl='tempStorey.png'
						self.l=True
						self.modconlec2=self.modconlec2+1
					elif self.lastword[0] == 'oie':
						




				#loading the bg and person images
				self.image = pygame.image.load(os.path.join('Backgrounds',self.url))
				if self.personurl != None:
					self.person = pygame.image.load(os.path.join('Characters', self.personurl))
				self.userinput = []		#resetting the userinput
				self.theword = ''		#resetting the displayed text
				
		if self.event.type == KEYDOWN and self.event.key == K_BACKSPACE:	#backspace!
			i = len(self.theword)
			self.userinput = self.userinput[0:i-2]
			self.theword = self.theword[0:i-2]
			
	def goto(self):
		if self.k == 0:
			self.text = 'Go where?'
		elif self.lastword[0] == 'to':
			self.lastword = self.lastword[1:self.k]
			self.run_goto()
		else:
			self.run_goto()
				
	def run_goto(self):
		self.changelastwordtostring()
		self.newurl = backend.goto(self.lastword)
		if self.newurl == None:
			self.text = 'Sorry, you have to stay in the bubble.'
		else:
			self.url = self.newurl
			
	#changes lastword to string so backend can read it
	#note: this change happens later rather than sooner so analysis on the list can still occur
	def changelastwordtostring(self):
		delimiter = ' '
		self.lastword = delimiter.join(self.lastword)
		
#runs the GUI by making it into a class
theGUI = GUI()
