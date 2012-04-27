c=0
#class bg(self):
 #   def f(self):
 #       if bg =='AC':
 #           pass
            #loc='url'

#class Person(name):
#    """who the player is interacting with"""
#    if name=='Storey':
#        pass


while c is 0:
    var=raw_input("Hey welcome to your freshman year! I'm your sibb! It's my job to teach you the ropes here at Olin. You can ask me what like about Olin. Just type ASK WEST HALL to ask me about west hall. When you're ready to enter Olin, say EXIT ")

    inp=var.split(' ')

    if inp[0]=='ASK':
        if inp[1] == 'WEST':
            var=raw_input("West Hall is where most First Years and Sophmores live.It has a pretty good Lounge culture, with four Lounges that are frequenctly occupied. All of the rooms are doubles; you'll be in one of them. West Hall also has Laundry Room and a Kitchen ")
        if inp[1] == 'EAST':
            var=raw_input("East Hall is where most of the Juniors and Seniors live. It has doubles as well as suites. East Hall also has the Piano Room, Bike Room, and Public Saftey. Man Hall is also in East Hall. ")
        if inp[1] == 'MILAS':
            var=raw_input("Milas Hall is blahbalh blah insert whatever")


    if inp[0]=='EXIT':
        c=1


