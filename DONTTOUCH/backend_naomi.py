#Trolin Group Backend, Software Design Spring 2012

#Gui: user hits enter, calls class Backend.goto(rawinput)


def process(word):
	word3=str(word)
	word1=word3.strip()
	word2=word1.lower()
	return ask(word2)

def ask(thing):
	if thing == 'o':
		return "The O is the central area between the Campus Center, Academic Center, and Milas Hall. The sidewalks cut through the grass forming the Olin 'O'. In nice weather, you may find students out here studying, napping, eating, or just hanging out."
	if thing == 'great lawn':
		return "The vast expanse of grass in front of the dorms is known as The Great Lawn. In winter, the great lawn becomes host to an assortment of snow people and forts, while in warmer weather it is the stadium of the brutal competition known as lap-tag."
	if thing == 'west hall' or thing == 'wh':
		return "West Hall houses all first year students and the majority of the sophomores. This is also where Nick Tatar lives."
	if thing == 'laundry room' or thing == 'laundry':
		return "West Hall has laundry rooms on the second, third, and fourth floors, and East Hall has one laundry room in the basement. Since Olin students are not smart enough to know how to do their own laundry, not to mention forgetful and impatient, you will find both wet and dry clothes all over the laundry room. While the LaundryView website attempts to inform students of which washers and dryers are currently in use, it is hardly ever accurate since we just love to open up washers and dryers, you know, just for funsies."
	if thing == 'fire alarms' or thing == 'alarms' or thing == 'fire':
		return "Don't set these off. Seriously, just don't. Don't touch them. Don't go near them. They're very sensitive, so don't hurt their feelings by taking a steamy shower or making root beer, popcorn, tea, fire, etc. in your room, because it will make them scream at you until public safety can get to you and shut them off. You will regret it."
	if thing == 'kitchen':
		return "Each residence hall has a kitchen on the first floor. None of us really know how to wash dishes or clean up after ourselves, so make sure you don't knock over the huge piles of dishes, and watch out for unidentified food objects lying around. They say to not set the kitchens on fire, but who knows, you just might get a new microwave and stove that actually work!"
	if thing == 'lounges' or thing == 'lounge':
		return "Each residence hall has one lounge per floor. West Hall lounges are generally more active than East Hall lounges, because first years like to amass in the lounges pretending to do homework, or getting checked off for ModSim."
	if thing == 'east hall' or thing == 'eh':
		return "East Hall houses all the cool kids -- I mean, most of the juniors and seniors, as well as some sophomores. AJ and Mark Chang both have apartments on the first floor of East Hall. East Hall has lots of suites, so make sure you have upperclass friends who can share their suite lounges with you."
	if thing == 'bike room' or thing == 'bike' or thing == 'bikes':
		return "In the bike room you will find... wait for it... GO! bikes! These are somewhat functional bikes that you can borrow at any time. You are also allowed to store your own bike there, in which case you are guaranteed a bike that works and fits you at all times."
	if thing == 'man hall' or thing == 'mann hall' or thing == 'manhall' or thing == 'mannhall':
		return "Well you see, there are some men... and they live in a hall... the EH north wing, specifically... sometimes some women live there too... they always keep to the most legal of practices -- just watch out where you step."
	if thing == 'practice room' or thing == 'practice rooms' or thing == 'music' or thing == 'music rooms' or thing == 'music room':
		return "There are two practice rooms in the basement of EH. One of them has a piano. The other one does not. The one with the piano is also the home of drum club's drums, and some sheet music for the piano."
	if thing == 'public safety':
		return "Public Safety is apparently located in East Hall. Since we're such a small school though, officers generally come over from Babson when we need them. This is who you call in any emergency."
	if thing == 'ac' or thing == 'academic center':
		return "Somewhat self-explanatory, this is where most of your classes will take place. In this building you will also find all of the labs and machine shops."
	if thing == 'mh' or thing == 'milas hall':
		return "Milas Hall is home to the library, the auditorium, the computer lab, IT, admissions, and many other offices. We technically also have an Olin store in this building, but I don't think it's ever open."
	if thing == 'cc' or thing == 'campus center':
		return "The Campus Center contains the mail room, the pool room, the jam room (not the kind you put on toast), the dining hall, the crescent room, and lots of administrative offices for StAR, OSL, and PGP, mostly. Also provides nice cover for you to avoid rain on the way to class."
	if thing == 'dining hall' or thing == 'dh':
		return "Delicious Sodexo food! This food is apparently much better than at most schools, but here inside the bubble we don't really know what the food at other schools actually tastes like, so who really knows? You'll be required to pay for the unlimited Olin meal plan, so you don't really have a choice anyway."
	if thing == 'jam room':
		return "The Jam Room has all sort of musical instruments, including many old, out of tune pianos. People like to, well, 'jam' in here."
	if thing == 'pool room':
		return "What used to be a completely white empty area outside of the mail room has been transformed into a classy space with two pool tables. It also has some awesome window seats."
	if thing == 'wooden waterfall' or thing == 'waterfall':
		return "Oliners are too cool for real waterfalls, so instead we have one made out of wood. Located in the Campus Center, this is where class photos are taken and where you will find plaques hanging on the wall with the names of all past and present R2s. This would be a cool place to hang out too, but it's ridiculously echo-y, so it doesn't really have any other practical purposes."
	if thing == 'mail room' or thing == 'mailroom' or thing == 'mail':
		return "Package Receipt Notification are some of the most exciting words you'll get in an email. When you do head right down to the mail room to get your stuff. For other mail, you will have to manually check your own mailbox on the lower level of the CC. Since remembering extraneous things like lock combinations takes up precious memory space, and turning knobs takes up too much time, most mailboxes are open all the time."
	if thing == 'franks':
		return "Franks is Olin's general supply store. Here you can buy your basic toiletries, some snacks, mailing supplies (like stamps and boxes), and some other random things. Frank will be your best friend come the end of the school year when you need those blue bins..."
	if thing == 'small project building' or thing == 'spb':
		return "Oh that... Yeah we don't talk much about the Small Project Building... Not since... Well... Yeah just don't worry about that one."
	if thing == 'large project building' or thing == 'lpb':
		return "Pretty self explanatory... this building is where you can work on large projects. Things like Sailbot and HPV take place here."
	if thing == 'mark somerville' or thing == 'mark' or thing == 'somerville':
		return "Due to his immense height, nobody knows what he truly looks like, nor how he gets into buildings. He is also constantly busy, so you may need to employ your stalking skills if you ever need to meet with him. Nevertheless this colossus has managed to squeeze his way into a list of the top 300 professors in the country."
	if thing == 'crawford' or thing == 'crawf' or thing == 'the crawf':
		return "Legend has it that long ago a mythical creature known as the Crawford roamed the halls of Olin. Those days are long since past, but even today, if you are truly fortunate, you may catch a glimpse of this creature returning to his old hunting grounds. Be on the lookout for an enormous red beard."
	if thing == 'hoho' or thing == 'ho ho':
		return "Hoho, a visiting professor from MIT, teaches some of the math classes at Olin. She's a tiny old Asian woman who's a genius in mathematics, coaches Olympic Martial Arts, and loves throwing knives."
	if thing == 'R2s' or thing == 'R2' or thing == 'resident resource' or thing == 'resident resources' or thing == 'RA' or thing == 'resident adviser':
		return "Your Resident Resources are excellent, um, resources for your life at Olin. With at least one on every floor, you can always go to any of them for help with anything. The R2 on-call is always there to save the day, when there's an emergency or, more often, when you get locked out of your room."
	if thing == 'tree' or thing == 'trees':
		return "Sorry, Olin has no trees."
	













