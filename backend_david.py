#Trolin Group Backend, Software Design Spring 2012

sleep=1

#Gui: user hits enter, calls class Backend.goto(rawinput)
locations={'west hall':1,'wh':1, 'westhall':1,'east hall':2,'eh':2,'ac':3,'academic center':3,'campus center':4,'cc':4,'the campus center':4,'milas hall':5,'mh':5,'o':6,'the o':6,'olin o':6,'great lawn':7,'the great lawn':7,'franks':8,'mailroom':8,'mail room':8}
input1='west hall'

def process(word):
	word1=word.strip()
	word2=word1.lower()
	return goto(word2)

def goto(input1):
	value=locations.get(input1,0)
	if value==0:
		return None
	elif value==1:
		return 'WHedit.png'
	elif value==2:
		return 'eh.png'
	elif value==3:
		return 'ac_standin.jpg'
	elif value==8:
		return 'franks.png'
	elif value==4:
		return 'CC.png'
	elif value==5:
		return 'milas_halledit.png'
	elif value==6:
		return 'the_o.png'
	elif value==7:
		return 'GreatLawnedit.png'

ls_nosleep=["Today's lesson will be... As the lecture begins you feel the fatigue of the previous day weighing on you. You thought 4 hours of sleep would be enough to keep yourself together for at least one lecture. But the chairs... now so soft, your eyes heavy... What do you do? (1) Keep yourself awake by taking notes rigorously (2) Drift off into a bliss-filled nap", True]

ls_options=["You try to keep attentive, but as the lecture briefly driftes into topics of theories you couldn't hope to understand this fatigued you become increasingly more interested in your artistic abilities. Soon, you look up, happy with your character from who-knows-what and lost as to how all the complex notations got there. You attempt to recover, but now the lecture has ended.", "You awaken an hour and 40 mins later to the sound of awkward applause your class has made mandatory at the end of each sentence. Now you feel well rested enough for your next class which is at... 3:20, fuck."]

ls_sleep=["Today's lesson will be... As the lecture begins you stay attentive as the transitions flow effortlessly through your brain. Yes yes it makes sense that e^jwt is the same as expressing this with sin and cos! You leave the class triumphant, with only a twinge of regret that you sacrificed so much of your evening yesterday", False]

oie1="You attend the first lecture which seems like a nice warm feelings-jam, which in retrospect was not what you wanted to do with all the work you should be doing. You decide that maybe you can miss these classes without consequences, but as a complete and utter nerd could you even DREAM of such a thing?"

def modconlec(sleep):
	if sleep==True:
		return ls_sleep, ls_options
	if sleep==False: 
		return ls_nosleep, ls_options

def oielec():
	return oie1
