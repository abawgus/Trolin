#Trolin Group Backend, Software Design Spring 2012

#Gui: user hits enter, calls class Backend.goto(rawinput)
locations={'west hall':1,'wh':1, 'westhall':1,'east hall':2,'eh':2,'ac':3,'academic center':3,'the academic center':3,'campus center':4,'cc':4,'the campus center':4,'milas hall':5,'mh':5,'o':6,'the o':6,'olin o':6,'great lawn':7,'the great lawn':7,'franks':8,'mailroom':8,'mail room':8,'large project building':9,'lpb':9,'the large project builing':9,'lounge':10,'the lounge':10,'a lounge':10,'bike room':11,'br':11,'the bike room':11,'wood shop':12,'minishop':12,'mini shop':12,'the woodshop':12,'dh':13,'dining hall':13,'cafe':13,'cafeteria':13,'dinner':13,'pool room':14,'billiards room':14,'pr':14}
input1='west hall'


def process(word):
	word1=word.strip()
	word2=word1.lower()
	return goto(word2)

class quest_manager(object):
	"makes shit work"
	def goto(self,input1):
		self.value=locations.get(input1,0)
		list1=[]
		if self.value==0:
			return None
		elif self.value==1:
			list1=['WHedit.png',None,None]
			if self.day==2:
				if self.haircut==1 and self.water_plants!=2:
					list1=['WHedit.png','StickFig1.jpg','Hey come back with buzzers!']
				elif self.haircut==1 and self.water_plants==2:
					list1=['WHedit.png','SketchFig2.jpg','Thanks for the buzz!']	
			return list1
		elif self.value==2:
			list1=['eh.png',None,None]
			return list1
		elif self.value==3:
			list1=['ac.jpg',None,None]
			if self.day==3 and self.ac_couch==1:
				if self.mh_couch==2 or self.gl_couch==2:
					list1=['ac.jpg','StickFig1.jpg','you found one couch! One more to go!']
					self.ac_couch=2
				elif self.mh_couch==1 and self.gl_couch==1:
					list1=['ac.jpg','StickFig1.jpg','you found one couch! Two to go!']
					self.ac_couch=2
				elif self.mh_couch==2 and self.gl_couch==2:
					list1=['ac.jpg','StickFig1.jpg','you found one couch! congrats you found them all!']
					self.ac_couch=2
			return list1
		elif self.value==8:
			list1=['franks.png',None,None]
			if self.value==8 and self.day==1 and self.lost_prox==1:
				self.lost_prox=2
				lists1=['franks.png',None,'congrats you found a p-card']
			return list1
		elif self.value==4:
			list1=['CC.png',None,None]
			if self.day==5:
				if self.find_crawford==2 and self.charles_vest==1:
					self.charles_vest=2
					list1=['CC.png','CharlieNolanNoVest.png','Thanks for my vest!']
				elif self.find_crawford!=2 and self.charles_vest==1:
					list1=['CC.png','CharlieNolanWithVest.png','have you seen my partners vest?']
			return list1
		elif self.value==5:
			list1=['milas_halledit.png',None,None]
			if self.day==3 and self.mh_couch==1:
				if self.ac_couch==2 or self.gl_couch==2:
					list1=['milas_halledit.png','StickFig1.jpg','you found one couch! One more to go!']
					self.mh_couch=2
				elif self.ac_couch==1 and self.gl_couch==1:
					list1=['milas_halledit.png','StickFig1.jpg','you found one couch! Two to go!']
					self.mh_couch=2
				elif self.ac_couch==2 and self.gl_couch==2:
					list1=['milas_halledit.png','StickFig1.jpg','you found one couch! congrats you found them all!']
					self.mh_couch=2
			return list1
		elif self.value==6:
			list1=['the_o.png',None,None]
			if self.day==4:
				if self.babby==1:
					self.babby=2
					list1=['the_o.png','StickFig1.jpg','What no money? Ill take your shoes!']
			return list1
		elif self.value==7:
			list1=['GreatLawnedit.png',None,None]
			if self.day==6 and self.no_trees==1:
				list1=['GreatLawnwdit.png','Cypress.psd','kill the tree']
				self.no_trees=2
			elif self.day==3 and self.gl_couch==1:
				if self.ac_couch==2 or self.mh_couch==2:
					list1=['GreatLawnwdit.png','StickFig1.jpg','you found one couch! One more to go!']
					self.gl_couch=2
				elif self.ac_couch==1 and self.mh_couch==1:
					list1=['GreatLawnwdit.png','StickFig1.jpg','you found one couch! Two to go!']
					self.gl_couch=2
				elif self.ac_couch==2 and self.mh_couch==2:
					list1=['GreatLawnwdit.png','StickFig1.jpg','you found one couch! congrats you found them all!']
					self.gl_couch=2
			return list1
		elif self.value==9:
			list1=['lpb.png',None,None]
			if self.day==1:
				if self.lost_prox==2:
					self.lost_prox=3
					list1=['lpb.png','Jazmin.psd','Yay you found it! Have a bike tire!']
				elif self.lost_prox==1:
					list1=['lpb.png','Jazmin.psd','hey have you seen my prox?']
			return list1
		elif self.value==10:
			list1=['lounge.png',None,None]
			if self.day==2 and self.water_plants==1:
				list1=['lounge.png','plant.jpg','you water plants and recieve buzzers']
			if self.day==6 and sef.ohman==1:
				self.ohman=2
				list1=['lounge.png','ZachBrass.psd','secrets of the modcon bear']
			return list1
		elif self.value==11:
			list1=['bikeroom.jpg',None,None]
			if self.day==1:
				if self.fix_bike==1 and self.lost_prox==3:
					self.fix_bike=2
					list1=['bikeroom.jpg','StickFig1.jpg','thanks for the tire']
				elif self.bike==1 and self.lost_prox!=3:
					list1=['bikeroom.jpg','StickFig1.jpg','hey bud bring me tire']
			return list1
		elif self.value==12:
			list1=['minishop.jpg',None,None]
			if self.day==4:
				if self.shop_buddy==1:
					self.shop_buddy=2
					list1=['minishop.jpg','StickFig1.jpg','Thanks for coming!']
					if self.babby==2:
						list1=['minishop.jpg','StickFig1.jpg','hey you need shoes to be in here!']
			return list1
		elif self.value==13:
			list1=['dininghall.png',None,None]
			if self.day==5 and self.find_crawford==1:
				self.find_crawford=2
				list1=['dininghall.png','Crawford.psd','i think this vest belongs to Charles']
			return list1
		elif self.value==14:
			list1=['poolroom.jpg',None,None]
			if self.day==3 and self.missing_person==1:
				self.missing_person=2
				list1=['poolroom.jpg','StickFig1.jpg','oh Ill get over there right away']
			return list1
