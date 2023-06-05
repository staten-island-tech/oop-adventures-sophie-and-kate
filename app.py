from classes_man import woman, man

create_dream_woman=[]
def get_female_hair(female_hair):
        question=input('choose your dream hairstyle:(a:straight, b:curly, c:layered, d:wavy, e:braids)')
        if question==('a'):
                create_dream_woman.append('Straight')
        elif question==('b'):
                create_dream_woman.append('Curly')
        elif question==('c'):
                create_dream_woman.append('Layered')
        elif question==('d'):
                create_dream_woman.append('Wavy')
        elif question==('e'):
                create_dream_woman.append('Braids')
        elif question != ('a','b','c','d', 'e'):
              print('you made an error!')
              get_female_hair(female_hair)   

def get_female_physique(female_physique):
        question=input('choose your dream physique:(a:curvy, b:skinny, c:muscular, d:slim thick, e:average)')
        if question==('a'):
                create_dream_woman.append('Curvy')
        elif question==('b'):
                create_dream_woman.append('Skinny')
        elif question==('c'):
                create_dream_woman.append('Muscular')
        elif question==('d'):
                create_dream_woman.append('Slim Thick')
        elif question==('e'):
                create_dream_woman.append('Average')
        elif question != ('a','b','c','d', 'e'):
              print('you made an error!')
              get_female_physique(female_physique)   


def get_female_personality(female_personality):
        question=input('choose your dream personality:(a:submissive, b:independent, c:baddie, d:wifey, e:angry)')
        if question==('a'):
                create_dream_woman.append('Submissive')
        elif question==('b'):
                create_dream_woman.append('Independent')
        elif question==('c'):
                create_dream_woman.append('Baddie')
        elif question==('d'):
                create_dream_woman.append('Wifey')
        elif question==('e'):
                create_dream_woman.append('Angry')
        elif question != ('a','b','c','d', 'e'):
              print('you made an error!')
              get_female_personality(female_personality)   

def get_female_hair_color(female_hair_color):
        question=input('choose your dream hair color:(a:dirty blond, b:blond, c:black, d:brunette, e:ginger)')
        if question==('a'):
                create_dream_woman.append('Dirty Blond')
        elif question==('b'):
                create_dream_woman.append('Blond')
        elif question==('c'):
                create_dream_woman.append('Black')
        elif question==('d'):
                create_dream_woman.append('Brunette')
        elif question==('e'):
                create_dream_woman.append('Ginger')
        elif question != ('a','b','c','d', 'e'):
              print('you made an error!')
              get_female_hair_color(female_hair_color)   


##desired man person class
create_dream_man=[]

def get_male_hair(male_hair):
        question=input('choose your dream hairstyle:(a:fade, b:edgar, c:buzz, d:fluffy, e:dreads)')
        if question==('a'):
                 create_dream_man.append('Fade')
        elif question==('b'):
                 create_dream_man.append('Edgar')
        elif question==('c'):
                 create_dream_man.append('Buzz')
        elif question==('d'):
                 create_dream_man.append('Fluffy')
        elif question==('e'):
                create_dream_man.append('Dreads')
        elif question != ('a','b','c','d', 'e'):
              print('you made an error!')
              get_male_hair(male_hair)   

def get_male_physique(male_physique):
        question=input('choose your dream physique:(a:muscular, b:dad bod, c:skinny, d:overweight, e:body builder)')
        if question==('a'):
                create_dream_man.append('Muscular')
        elif question==('b'):
                create_dream_man.append('DadBod')
        elif question==('c'):
                create_dream_man.append('Skinny')
        elif question==('d'):
                create_dream_man.append('Overweight')
        elif question==('e'):
                create_dream_man.append('BodyBuilder')
        elif question != ('a','b','c','d', 'e'):
              print('you made an error!')
              get_male_physique(male_physique) 

def get_male_personality(male_personality):
        question=input('choose your dream personality:(a:sigma, b:alpha, c:omega, d:npc, e:sassy)')
        if question==('a'):
                create_dream_man.append('Sigma')
        elif question==('b'):
                create_dream_man.append('Alpha')
        elif question==('c'):
                create_dream_man.append('Omega')
        elif question==('d'):
                create_dream_man.append('NPC')
        elif question==('e'):
                create_dream_man.append('Sassy')
        elif question != ('a','b','c','d', 'e'):
              print('you made an error!')
              get_male_personality(male_personality) 


def get_male_hair_color(male_hair_color):
        question=input('choose your dream hair color:(a:dirty blond, b:blond, c:black, d:brunette, e:ginger)')
        if question==('a'):
                create_dream_man.append('Dirty Blond')
        elif question==('b'):
                create_dream_man.append('Blond')
        elif question==('c'):
                create_dream_man.append('Black')
        elif question==('d'):
                create_dream_man.append('Brunette')
        elif question==('e'):
                create_dream_man.append('Ginger')
        elif question != ('a','b','c','d', 'e'):
              print('you made an error!')
              get_male_hair_color(male_hair_color) 
def make_woman():
        get_female_hair(1)
        get_female_physique(1)
        get_female_personality(1)
        get_female_hair_color(1)
def make_man():
        get_male_hair(1)
        get_male_physique(1)
        get_male_personality(1)
        get_male_hair_color(1)

def choose_gender():
        question=input("what is your prefered gender?(male or female)")
        if question==('female'):
                make_woman()
                print(create_dream_woman)
                return "female"
        elif question==('male'):
                make_man()
                print(create_dream_man)
                return "male"
        else:
                print('you made an error!')
                choose_gender()
x = choose_gender()
##woman options
Ella=woman('dirty blond','straight','baddie','muscular')
Anna=woman('ginger','braids','submissive','curvy')
Layla=woman('brunette','wavy','wifey','skinny')
Chanel=woman('black','layered','angry','slim thick')
Olivia=woman('blond','curly','independant','average')
women=[Ella, Anna, Layla, Chanel, Olivia]
##men options
Xavier=man('Dreads','BodyBuilder','Alpha','Black')
Phil=man('Buzz','DadBod','Omega','Ginger')
John=man('Fulffy', 'Muscular','Sigma','DirtyBlond')
Eric=man('Fade','OverWeight','NPC','Brunette')
Juan=man('Edgar','Skinny','Sassy','Blond')
men=[Xavier, Phil, John, Eric, Juan]
##compare person to pre-created companions  

#score
#current_top_candidate
score = 0
def compare_candidates(x):
        top_cand = {}
        current_cand = {}
        for man in men: 
                if man.Hstyle == create_dream_man[0]: 
                        man.set_score()
                if man.physique == create_dream_man[1]:
                         man.set_score()
                if man.personaility == create_dream_man[2]:
                         man.set_score()
                if man.Hcolor == create_dream_man[3]:
                         man.set_score()
                                
compare_candidates(x)



                                       #call class function to increase character score 
                                      
                                        

                                ## compare
                                ## track the score and current score
                                ## create a global variable for current top comparison
                                ## change comparison based on score
                                ## compare current candidate with top
                                ## if score > current score, replace
"""        elif choose_gender==('female'):
                for x in women:
                        for y in create_dream_woman:
                                ## compare
                                ## track the score and current score
                                ## create a global variable for current top comparison
                                ## change comparison based on score
                                ## compare current candidate with top
                                ## if score > current score, replace
        else:
                print('you made an error!')
                compare_candidates()
 """