#Trolin Group Backend, Software Design Spring 2012

#Gui: user hits enter, calls class Backend.goto(rawinput)
locations={'west hall':1,'wh':1, 'westhall':1,'east hall':2,'eh':2,'ac':3,'academic center':3,'the academic center':3,'campus center':4,'cc':4,'the campus center':4,'milas hall':5,'mh':5,'o':6,'the o':6,'olin o':6,'great lawn':7,'the great lawn':7,'franks':8,'mailroom':8,'mail room':8}
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
		return 'westhall.JPG'
	elif value==2:
		return 'easthall_standin.jpg'
	elif value==3:
		return 'ac_standin.jpg'
	elif value==8:
		return 'franks_standin.jpg'
	elif value==4:
		return 'cc_standin.jpg'
	elif value==5:
		return 'milas_hall.JPG'
	elif value==6:
		return 'the_o.JPG'
	elif value==7:
		return 'GreatLawn.jpg'
	elif value==9:
		return 'large proj image'
