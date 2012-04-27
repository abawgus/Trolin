import pygame
import os, sys
from pygame.locals import *
import backend_david as backend
import textwrapS as textwrap

class GUI(object):
	def __init__(self):
		pygame.init()
		#pygame.mixer.music.load('bgmusic.mp3')
		#pygame.mixer.music.set_volume(1)
		#pygame.mixer.music.play(-1,0.0)
		self.endPrompt = False #if the day has ended, prompt with sleep option
		self.l = False #if in a lecture or not
		self.sleep=True #moniters if character has slept the previous night
		self.p=0

		#Lecture numbers for each class
		self.oie=1
		self.desnat=1
		self.modcon=1
		self.modconlec2=0 #needed for any lecture with options, currently only mc2
		self.modsim=1

		#if work for each class is done
		self.modconhw=False
		self.modsimhw=False
		self.desnathw=False 
		self.oiehw=False

		self.classnum=0  #number of classes you've had today
		self.day=1 #the day of the week

		#makes the GUI screen & sets the top caption
		self.background = pygame.display.set_mode((920,800))
		#self.character = pygame.display.set_mode()
		pygame.display.set_caption('TrOlin')
		
		#needed variables
		self.userinput = []
		self.text = 'Hello! I`m you`re Sibb! You should go to one of your classes: MODSIM MODCON DESNAT or OIE. You`ll be assigned work for each class, so make sure you get that done! If you want to know about anything, just ASK me.' #Intro Screen Settings
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
		self.fontObj = pygame.font.Font('8bit.TTF', 18)
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
			self.background.blit(self.person, (200,70))
			
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
				
			
			if len(self.thefinalstring)>0:
				firstword = self.thefinalstring[0]
			#self.lastword = self.thefinalstring[1:j]	
			#self.k = len(self.lastword)
			
			self.personurl='none.png'
			self.text = ''
			self.text2 = ''
			self.text3 = ''
			self.text4 = ''
			self.text5 = ''
			
			if self.day == 7:
				self.text="Today is the day of your finals. Chose which to go to first. MODCON DESNAT OIE or MODSIM"
				
			if self.day ==7 and firstword == 'modcon':
				if self.modconhw ==True:
					self.text="You present your working modcon project, a beautiful piece of circuitry if you do say so yourself. Everyone is shocked and amazed at your prowess and you complete the course with a lovely PASS"
				if self.modconhw ==False:
					self.text="You present a horrific nightmare of circuits shooting sparks every which-way. One of these loose embers catches the neighboring project on the efficiency of lighterfluid. The building go up in flames. Needless to say you are leave with a weighty FAIL on your record."
			
			if self.day ==7 and firstword == 'modsim':
				if self.modsimhw ==True:
					self.text="The model you lovingly created excutes magnificently. With a palette swap or two, you MATLAB animation could be mistaken for reality! A stunning success, you leave with a PASS!"
				if self.modsimhw ==False:
					self.text="Your model is so horribly abuses the law of earth and man that it makes the audience sick to view. In the mass chaos, you see this abomination of physics begin to tear a whole in reality. You and your audience are sent hurling into the sun as the universe tries to correct this creation you made. As you burn for eternity, you still make note of the new fail on your record."
					
			if self.day ==7 and firstword == 'desnat':
				if self.desnathw ==True:
					self.text="When it comes your time to present, you squeeze together the suction cups that active your hopper and stand back. With a second, it leaps. Higher and higer it climbs, through the cieling tiles, past the roof of the ac and further upwards. After watching for 5 min, it descends, perfectly in-tact as the applause of the class wafts over you. You comemorate this day celebrating a PASS on your record."
				if self.desnathw ==False:
					self.text="The unholy monstrosity you made is set on the stage. Nervously, you activate the trigger. Instead of Hopper, it further deforms. This 'hopper' you created repeats 'HUNT KILL DESTROY swag' over its rampage. The tragedy is one you hope to never think of again. You leave with a FAIL, but an impressive body-count"
					
			if self.day ==7 and firstword == 'oie':
				if self.oiehw ==True:
					self.text="You turn in your essay, and proceed to never think about it again. A week later you get an email that says what a wonderful job you did, and a note that you passes the class."
				if self.oiehw ==False:
					self.text="You fail to turn in your essasy and a week later you recieve an email about how disappointed your professer is. When you check your class status, you note that  you still passed. lol ok"
			
			
			
			if self.endPrompt:
				if firstword =='1':
					self.sleep = True
					self.endPrompt = False
					self.url='dorm.jpg'	
					self.classnum=0
					self.day=self.day+1
					self.p=1
				elif firstword == '2':
					self.sleep = False
					self.endPrompt = False
					self.url='lounge.png'
					self.classnum = 0
					self.day=self.day+1
					self.p=1
				elif self.p==1:
					self.text="Answer the question already!"

		
			if self.l and self.modconlec2 != 0 and j !=0: #if you are in the second modcon lecture
				self.url='lecture.png'
			
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
						self.modcon=3
						self.personurl == 'none.png'
						self.modconlec2 =0
						self.classnum=self.classnum+1
				elif ls1[len(ls1)-1] == False:
					if self.modconlec2 == len(ls1)-1:
						#print 'met condit lesson over'
						self.l=False
						self.modcon=3
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
					self.text="Wait! It's getting late. It's too late to do that! Although you are tired, there are still people up in the lounge. Do you (1) Go to sleep (2) Stay up and have some fun in your life."
					self.endPrompt = True
				firstword = self.thefinalstring[0]
				self.lastword = self.thefinalstring[1:j]	
				self.k = len(self.lastword)

				classList=['modcon','modsim','desnat','oie', 'design' ]

				if len(self.lastword)!=0 and self.lastword[0]=='to':
					self.lastword = self.lastword[1:self.k]

				if firstword == 'kill' or firstword == 'die':
					if firstword == 'kill' and self.lastword[0]=='self':
						self.url='death.png'
					elif firstword== 'die':
						self.url = 'death.png'
					else:
						self.text="Stop trying to kill things, this is a happy environment."

				if firstword =='do':
					if 'home'and 'work' or'hw' or 'homework' in self.lastword:
						if 'mod' and 'con' or 'modcon' in self.lastword:
							self.modconhw=True
							self.text="Well it's nice to get that out of the way!"
						if 'mod' and 'sim' or 'modsim' in self.lastword:
							self.modsimhw=True
							self.text="Well it's nice to get that out of the way!"
						if 'design' and 'nature' or 'desnat' in self.lastword:
							self.desnathw=True
							self.text="Well it's nice to get that out of the way!"					
						if 'oie' in self.lastword:
							self.oiehw=True
							self.text="Well it's nice to get that out of the way!"							
							
				#GOTO identifier
				if not self.endPrompt and self.day <7 and self.l==False and firstword == 'goto' or firstword == 'go':
					if self.lastword[0] not in classList: #change to if lastword is not in list of classes
						self.goto()
					elif self.lastword[0] == 'modcon': 
						if self.lastword[0]=='to':
							self.lastword = self.lastword[1:self.k]
						
						if self.modcon ==1:
							self.text="Welcome to Modeling and  Control! I'm Brian Storey and you're in for a world of pain and depression. Have fun with simulink!"
							self.classnum=self.classnum+1
							self.url='lecture.png'
							self.personurl='tempStorey.png'
							self.modcon =2
						elif self.modcon ==2:
							ls1,lsop = backend.modconlec(self.sleep)
							self.text=ls1[self.modconlec2]
							self.url='lecture.jpg'
							self.personurl='tempStorey.png'
							self.l=True
							self.modconlec2=self.modconlec2+1
						elif self.modcon==3:
							self.text="For your final project make sure it is AWESOME and you'll do fine. Or do this lab or whatever, the ninja's will deal with you then"
							self.personurl="tempStorey.png"
							self.url='lecture.png'
							self.classnum=self.classnum+1
							self.modcon=4
					elif self.lastword[0] == 'oie':
						if self.oie ==1:
							self.text= backend.oielec()
							self.url='lecture.png'	
							self.classnum= self.classnum+1
							self.oie =2
						elif self.oie==2:
							self.text= "Well that was very informative about... dating culture or something. Fun times! (Did he mention an essay or something?)"
							self.oie=3
							self.url='lecture.png'
							self.classnum=self.classnum+1
						elif self.oie==3:
							self.text="Well friends, it looks like we're coming to the end of your first semester. You only need to finish your essay, and then you're experienced and entire introduction to Olin"
							self.classnum=self.classnum+1
							self.url='lecture.png'
							self.oie=4
					elif self.lastword[0] =='modsim':
						if self.modsim ==1:
							self.text="Hello. I'm John Geddes. We're going to be doing some physics and, everybody's favorite, MATLAB! (No Mathematica. Ever.)"
							self.url='lecture.png'
							self.classnum=self.classnum+1
							self.modsim=2
						elif self.modsim ==2:
							self.text="You better get to work on your simulation. -You are a bit unsure what to do for your project, so you decide yo wait for John to get to your group. Unfortunately after an hour, he is only at the second table and you lose hope-"
							self.classnum=self.classnum+1
							self.modsim=3
							self.url='lecture.png'
						elif self.modsim ==3:
							self.text="Remember that you're project is do soon!If you don't keep your model accurate to real-world physics, who knows what's going to happen"
							self.classnum=self.classnum+1
							self.modsim=4
							self.url='lecture.png'
					elif self.lastword[0]=='desnat' or self.lastword[0]=='design':
						if self.desnat==1:
							self.classnum=self.classnum+1
							self.desnat=2
							self.url='lecture.png'
							self.text="Hello and welcome to Design Nature! Now go in the woods and draw bugs. Trust us this is `important`"
						elif self.desnat ==2:			
							self.classnum=self.classnum+1
							self.desnat=3
							self.url='lecture.png'
							self.text="Well now that you have some bug pictures and thoroughly studied that scientific paper on jumping, make a Hopper that moves! Only with this one crappy motor, rubber tubbing and all of the delrim. Also learn solidworks"
						elif self.desnat==3:	
							self.classnum=self.classnum+1
							self.desnat=4
							self.url='lecture.png'
							self.text="So you're hopper doesn't.... quite... work... Well, as long as it's done by finals!"
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
		elif self.lastword[0] == 'on':
			if self.lastword[1] =='skype':
				self.url = 'skype.png'
				self.text='What are you doing on skype? Everyone you could possibly want to talk to is within 50 ft!'
			elif self.lastword[1]=='steam':
				self.url = 'steam.png'
				self.text="Hmm... That game of TF2 looks tempting... But you really do have more pressing mattters."
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
