
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
def get_female_hair(female_hair):
        question=input('choose your dream hairstyle:(a:straight, b:curly, c:layered, d:wavy, e:braids)')
        if question==('a'):
                print('Straight=150')
        if question==('b'):
                print('Curly=70')
        if question==('c'):
                print('Layered=100')
        if question==('d'):
                print('Wavy=100')
        if question==('e'):
                print('Braids=120')


def get_female_physique(female_physique):
        question=input('choose your dream physique:(a:curvy, b:skinny, c:muscular, d:slim thick, e:average)')
        if question==('a'):
                print('Curvy=120')
        if question==('b'):
                print('Skinny=100')
        if question==('c'):
                print('Muscular=150')
        if question==('d'):
                print('Slim Thick=200')
        if question==('e'):
                print('Average=75')


def get_female_personality(female_personality):
        question=input('choose your dream personality:(a:submissive, b:independent, c:baddie, d:wifey, e:angry)')
        if question==('a'):
                print('Submissive=60')
        if question==('b'):
                print('Independent=80 ')
        if question==('c'):
                print('Baddie=200')
        if question==('d'):
                print('Wifey=215')
        if question==('e'):
                print('Angry=20')


def get_female_hair_color(female_hair_color):
        question=input('choose your dream hair color:(a:dirty blond, b:blond, c:black, d:brunette, e:ginger)')
        if question==('a'):
                print('Dirty Blond=50')
        if question==('b'):
                print('Blond=70')
        if question==('c'):
                print('Black=30')
        if question==('d'):
                print('Brunette=70')
        if question==('e'):
                print('Ginger=20')


##desired man person class
def get_male_hair(male_hair):
        question=input('choose your dream hairstyle:(a:fade, b:edgar, c:buzz, d:fluffy, e:dreads)')
        if question==('a'):
                print('Fade=200')
        if question==('b'):
                print('Edgar=100')
        if question==('c'):
                print('Buzz=70')
        if question==('d'):
                print('Fluffy=80')
        if question==('e'):
                print('Dreads=70')


def get_male_physique(male_physique):
        question=input('choose your dream physique:(a:muscular, b:dad bod, c:skinny, d:overweight, e:body builder)')
        if question==('a'):
                print('Muscular=200')
        if question==('b'):
                print('DadBod=40')
        if question==('c'):
                print('Skinny=150')
        if question==('d'):
                print('Overweight=20')
        if question==('e'):
                print('BodyBuilder=150')


def get_male_personality(male_personality):
        question=input('choose your dream personality:(a:sigma, b:alpha, c:omega, d:npc, e:sassy)')
        if question==('a'):
                print('Sigma=200')
        if question==('b'):
                print('Alpha=215 ')
        if question==('c'):
                print('Omega=50')
        if question==('d'):
                print('NPC=3')
        if question==('e'):
                print('Sassy=25')


def get_male_hair_color(male_hair_color):
        question=input('choose your dream hair color:(a:dirty blond, b:blond, c:black, d:brunette, e:ginger)')
        if question==('a'):
                print('Dirty Blond=50')
        if question==('b'):
                print('Blond=70')
        if question==('c'):
                print('Black=30')
        if question==('d'):
                print('Brunette=70')
        if question==('e'):
                print('Ginger=20')


get_male_hair(1)
get_male_physique(1)
get_male_personality(1)
get_male_hair_color(1)
##compare person to pre-created companions  