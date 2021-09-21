def HelloWorld():
    print("Hellow!")
def CreditWhereCreditIsDue():
    print('This text adventure is heavily based off of the "Oasis" side quest from Fallout 3')
    print("I did not come up with the plot, characters, decisions, or anything else displayed in this text adventure")
    print("All credit for the plot goes to Bethesda (the original developers of Fallout 3), the Fallout 3 fandom website, and the YouTube videos (by Oxhorn) which I used as reference material")
    print("Reference material here ---> https://fallout.fandom.com/wiki/Oasis_(quest)")
    print("")
    print("")
    print("")
CreditWhereCreditIsDue()
asked=0
def AskRitual():
    print('')
    print('Tree Father Birch says that in order to meet "Him" you must go through the "Ceremony of Purification" and that once its complete youll be able to speak to "Him"')
def FurtherExplinationBirch():
    print('"I would have prefered that he made the introduction but i understand your hesitation"')
    print('"The great one is a God-Tree. A living, breathing, speaking God-Tree"')
    print('"the treeminders are blessed to have this being watch over us"')
    AskRitual()
def ExplinationBeforeEncounter():
    print('"He is the one who grows, he is the one who gives, and he is the one who guides"')
    print('"No one speaks his name out of reverence for his magesty"')
    print('"Thanks to him, The Treeminders have a home" Birch says.')
    answer = input('Type 1 and press enter to pressure further about it. Type 2 let it slide and just go with it.')
    if answer=="1":
        print ('')
        asked=1
        FurtherExplinationBirch()
    else:
        if answer=="2":
            print('')
            AskRitual()
        else:
            print('')
            print ("INVALID ANSWER")
    
def PressureOportunity():
    answer = input('Type 1 and press enter to ask who "he" is and why they are being so vague about it. Type 2 let it slide and just go with it.')
    if answer=="1":
        print('')
        ExplinationBeforeEncounter()
    else:
        if answer=="2":
            print('')
            AskRitual()
        else:
            print('')
            print ("INVALID ANSWER")
def DecisionFollow():
    print('While leading you to their village hidden inside of an abandoned salt mine, Birch explains that he is the leader of "The Treeminders"')
    print('Birch explains that The Treeminders are a group of people who worship "him" and treasure every bit of life he brings to their village.')
    PressureOportunity()
def DecisionBurn():
    print('You refuse and end the side quest')
def GameStart():
    print('When exploring the map of Fallout 3 you encounter a strange place called "Oasis".')
    print('On aproaching Oasis, you encounter a strange man by the name of "Tree Father Birch" who asks you to follow him.')
    print('Birch explains that "He" has summoned you, but doesent say exactly who or what "He" is.')
    answer = input('Type 1 and press enter to go with Birch. Type 2 and press enter to say no and end the quest imediately.')
    #If/then/else starement for a different response depending on the answer
    if answer=="1":
        print('')
        DecisionFollow()
    else:
        if answer=="2":
            print('')
            DecisionBurn()
        else:
            print('')
            print ("INVALID ANSWER")

def Action1():
    print('***ACTION 1 ERROR***')
def Action2():
    print('***ACTION 2 ERROR***')
def UnusedSoFar():

    
    answer = input('Type 1 to _____. Type 2 to _____.')
    if answer=="1":
        print('')
        Action1()
    else:
        if answer=="2":
            print('')
            Action2()
        else:
            print('')
            print ("INVALID ANSWER")

            
    print('')
    print('On arival to their village The Treeminders lead you into the Grove, where they introduce you to a tree named Harold.')
    print('Birch informs you that harrold is the one who asked for you to be brought in')
    print('They all await to see what you chose to say to harrold')

GameStart()
