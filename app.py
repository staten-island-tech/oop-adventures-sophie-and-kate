
class Fhair:
    Straight=150
    Curly=70
    Layered=100
    Wavy=100
    Braids=120 


def add(x,y):
        return x + y
##class human

##class male companion
##class female companion

##desired woman class
create_dream_woman=[]

def get_female_hair(female_hair):
        question=input('choose your dream hairstyle:(a:straight, b:curly, c:layered, d:wavy, e:braids)')
        if question==('a'):
                create_dream_woman.append('Straight=150')
        if question==('b'):
                create_dream_woman.append('Curly=70')
        if question==('c'):
                create_dream_woman.append('Layered=100')
        if question==('d'):
                create_dream_woman.append('Wavy=100')
        if question==('e'):
                create_dream_woman.append('Braids=120')


def get_female_physique(female_physique):
        question=input('choose your dream physique:(a:curvy, b:skinny, c:muscular, d:slim thick, e:average)')
        if question==('a'):
                create_dream_woman.append('Curvy=120')
        if question==('b'):
                create_dream_woman.append('Skinny=100')
        if question==('c'):
                create_dream_woman.append('Muscular=150')
        if question==('d'):
                create_dream_woman.append('Slim Thick=200')
        if question==('e'):
                create_dream_woman.append('Average=75')


def get_female_personality(female_personality):
        question=input('choose your dream personality:(a:submissive, b:independent, c:baddie, d:wifey, e:angry)')
        if question==('a'):
                create_dream_woman.append('Submissive=60')
        if question==('b'):
                create_dream_woman.append('Independent=80 ')
        if question==('c'):
                create_dream_woman.append('Baddie=200')
        if question==('d'):
                create_dream_woman.append('Wifey=215')
        if question==('e'):
                create_dream_woman.append('Angry=20')


def get_female_hair_color(female_hair_color):
        question=input('choose your dream hair color:(a:dirty blond, b:blond, c:black, d:brunette, e:ginger)')
        if question==('a'):
                create_dream_woman.append('Dirty Blond=50')
        if question==('b'):
                create_dream_woman.append('Blond=70')
        if question==('c'):
                create_dream_woman.append('Black=30')
        if question==('d'):
                create_dream_woman.append('Brunette=70')
        if question==('e'):
                create_dream_woman.append('Ginger=20')
get_female_hair(1)
get_female_physique(1)
get_female_personality(1)
get_female_hair_color(1)
print(create_dream_woman)


##desired man person class
create_dream_man=[]

def get_male_hair(male_hair):
        question=input('choose your dream hairstyle:(a:fade, b:edgar, c:buzz, d:fluffy, e:dreads)')
        if question==('a'):
                 create_dream_man.append('Fade=200')
        if question==('b'):
                 create_dream_man.append('Edgar=100')
        if question==('c'):
                 create_dream_man.append('Buzz=70')
        if question==('d'):
                 create_dream_man.append('Fluffy=80')
        if question==('e'):
                create_dream_man.append('Dreads=70')


def get_male_physique(male_physique):
        question=input('choose your dream physique:(a:muscular, b:dad bod, c:skinny, d:overweight, e:body builder)')
        if question==('a'):
                create_dream_man.append('Muscular=200')
        if question==('b'):
                create_dream_man.append('DadBod=40')
        if question==('c'):
                create_dream_man.append('Skinny=150')
        if question==('d'):
                create_dream_man.append('Overweight=20')
        if question==('e'):
                create_dream_man.append('BodyBuilder=150')


def get_male_personality(male_personality):
        question=input('choose your dream personality:(a:sigma, b:alpha, c:omega, d:npc, e:sassy)')
        if question==('a'):
                create_dream_man.append('Sigma=200')
        if question==('b'):
                create_dream_man.append('Alpha=215 ')
        if question==('c'):
                create_dream_man.append('Omega=50')
        if question==('d'):
                create_dream_man.append('NPC=3')
        if question==('e'):
                create_dream_man.append('Sassy=25')


def get_male_hair_color(male_hair_color):
        question=input('choose your dream hair color:(a:dirty blond, b:blond, c:black, d:brunette, e:ginger)')
        if question==('a'):
                create_dream_man.append('Dirty Blond=50')
        if question==('b'):
                create_dream_man.append('Blond=70')
        if question==('c'):
                create_dream_man.append('Black=30')
        if question==('d'):
                create_dream_man.append('Brunette=70')
        if question==('e'):
                create_dream_man.append('Ginger=20')

get_male_hair(1)
get_male_physique(1)
get_male_personality(1)
get_male_hair_color(1)
print(create_dream_man)
##compare person to pre-created companions  