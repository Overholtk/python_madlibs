
def displayMenu():
    print('Welcome to the game of Copypasta Mad Libs!')
    print('Please enter the number corresponding with your choice and hit enter:')
    print('1. Play Mad Lib number one')
    print('2. Play Mad Lib number two')
    print('3. Exit')
    choice = input('')
    if choice == '1':
        madlibOne()
    elif choice == '2':
        madlibTwo()
    elif choice == '3':
        quit()

def madlibOne():
    greeting = input('give me a greeting: ').capitalize()
    color1 = input('give me a color: ').capitalize()
    illness = input('give me an illness: ').capitalize()
    animal = input('give me an animal: ').capitalize()
    noun = input('give me a noun: ').lower()
    color2 = input('give me a color: ').lower()
    color3 = input('give me a color again: ').lower()
    body = input('give me a part of the body: ').lower()
    adj = input('give me an adjective: ').lower()
    color4 = input('give me one more color: ').lower()
    plurNoun = input('give me a plural noun: ').lower()
    propNoun = input('give me a proper noun: ').capitalize()
    explative = input('give me an explative!: ').lower()

    print(greeting + ' my namne is ' + color1 + ' Dark\'ness ' + illness + ' ' + animal + ' Way and I have long ebony black hair (that\'s how I got my ' + noun + ') with ' + color2 + ' streaks and ' + color3 + ' tips that reaches my ' + body + ' and ' + adj + ' ' + color4 + ' eyes like limpid ' + plurNoun + ' and a lot of people tell me I look like ' + propNoun + ' (AN: if u don\'t know who she is get da ' + explative + ' out of here!)')
    choice = input('Play Again? y/n' ).lower()
    if choice == 'y' or choice == 'yes':
        displayMenu()
    else:
        quit()

def madlibTwo():
    cuss = input('give me an explative!: ')
    verb1 = input('give me a verb: ')
    num1 = input('give me a number: ')
    adj = input('give me an adjective: ')
    place = input('give me a place: ')
    noun1 = input('give me a noun: ')
    job = input('give me a job: ')
    verb2 = input('give me a verb: ')
    weather = input('give me a type of weather: ')
    body = input('give me a part of the body: ')

    print('What the ' + cuss + ' did you just ' + cuss + 'ing say about me, you little bitch? I\'ll have you know I ' + verb1 + 'ed top of my class in the Navy Seals, and I\'ve been involved in numerous secret raids on Al-Quaeda, and I have over ' + num1 + ' confirmed kills. I am trained in gorilla warfare and I\'m the top sniper in the entire ' + place + ' armed forces. You are nothing to me but just another ' + noun1 + '. I will wipe you the fuck out with ' + adj + ' the likes of which has never been seen before on this Earth, mark my fucking words. You think you can get away with saying that shit to me over the Internet? Think again, fucker. As we speak I am contacting my secret network of ' + job + 's across the USA and your IP is being ' + verb2 + 'ed right now so you better prepare for the ' + weather + ', maggot. The storm that wipes out the pathetic little thing you call your life. You\'re fucking dead, kid. I can be anywhere, anytime, and I can kill you in over seven hundred ways, and that\'s just with my bare ' + body + '. Not only am I extensively trained in unarmed combat, but I have access to the entire arsenal of the United States Marine Corps and I will use it to its full extent to wipe your miserable ass off the face of the continent, you little shit. If only you could have known what unholy retribution your little "clever" comment was about to bring down upon you, maybe you would have held your fucking tongue. But you couldn\'t, you didn\'t, and now you\'re paying the price, you goddamn idiot. I will shit fury all over you and you will drown in it. You\'re fucking dead, kiddo.')

    choice = input('Play Again? y/n' ).lower()
    if choice == 'y' or choice == 'yes':
        displayMenu()
    else:
        quit()

displayMenu()