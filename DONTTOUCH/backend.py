#Trolin Group Backend, Software Design Spring 2012

#Gui: user hits enter, calls class Backend.goto(rawinput)

class Backend(rawinput):
	sleep=1 #1 means they've slept, 0 means they haven't
	numEven=0 #number of things they've done today, used to trigger sleep
	inp=rawinp.split(' ')	
	def goto(local):
		if inp[1] == 'AC':
			bg='AC'
			return 'url'
		elif inp[1] == 'WEST' or inp[1] == 'WH':
			bg='WH'
			return 'url'
		elif inp[1] == 'CLASS':
			classList = 'MODCON, MODSIM, DESNAT, OIE'
			return "Which class? You have like 80 or something: %s" %classList
		elif inp[1] =='MODCON':
			Events.modconlec1()

	def check(thing):
		if thing=='EMAIL':
			#bg='computer'
			pass
            #return email screen and var of messages
		elif thing=='INV':
			pass
			#return inv screen and list of items
						
	def talk(person):
		if person =='Storey':
			Person.Storey()
		elif person =='SIBB':
			Person.SIBB()



class Events1():
	c=0
	def tutorial(self):
		Person.SIBB()
		return "Hey welcome to your freshman year! I'm your sibb! It's my job to teach you the ropes here at Olin. You can ask me what like about Olin. Just type ASK WEST HALL to ask me about west hall. When you're ready to enter Olin, say EXIT", 'url'
	def modconlec1_1(self):
		Person.Storey()
		return "Welcome to Modcon! This class will cover a ton of stuff you'll never understand (not official dialog, don't let this into the final code!)", 'url', 'storey,url'
	def modconlec2(self, sleep):
		Person.Storey()
		return "Today's lesson will be...", 'url, storey,url'
		if sleep==1:
			return "As the lecture begins you stay attentive as the transitions flow effortlessly through your brain. Yes yes it makes sense that e^jwt is the same as expressing this with sin and cos! You leave the class triumphant, with only a twinge of regret that you sacrificed so much of your evening yesterday"
		if sleep==0:
			return "As the lecture begins you feel the fatigue of the previous day weighing on you. You thought 4 hours of sleep would be enough to keep yourself together for at least one lecture. But the chairs... now so soft, your eyes heavy... What do you do? (1) Keep yourself awake by taking notes rigorously (2) Drift off into a bliss-filled nap"
			

class Person():
	def SIBB():
		PersonUrl = 'url'
		if inp[0]=='ASK':
			if inp[1] == 'WEST':
				return "West Hall is where most First Years and Sophmores live.It has a pretty good Lounge culture, with four Lounges that are frequenctly occupied. All of the rooms are doubles; you'll be in one of them. West Hall also has Laundry Room and a Kitchen "
        	if inp[1] == 'EAST':
				return "East Hall is where most of the Juniors and Seniors live. It has doubles as well as suites. East Hall also has the Piano Room, Bike Room, and Public Saftey. Man Hall is also in East Hall."
			if inp[1] == 'MILAS':
				return "Milas Hall is blahbalh blah insert whatever"
			if inp[1] =='GREAT':
				return "The vast expanse of grass in front of the dorms is known as The Great Lawn.  In Winter The Great Lawn becomes host to an assortment of snow people and forts, while in warmer weather it is the stadium of the brutal competition known as lap-tag."
	def Storey():
		

