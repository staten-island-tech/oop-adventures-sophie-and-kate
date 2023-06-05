class man:
    def __init__(self,Hcolor,Hstyle,personaility,physique):
        self.Hcolor=Hcolor
        self.Hstyle=Hstyle
        self.personaility=personaility
        self.physique=physique
        self.score = 0
    def get_score(self):
        return self.score
    def set_score(self):
        self.score += 1
    

class woman:
    def __init__(self,Hcolor,Hstyle,personaility,physique):
        self.Hcolor=Hcolor
        self.Hstyle=Hstyle
        self.personaility=personaility
        self.physique=physique
        self.score = 0
    def get_score(self):
        return self.score
    def set_score(self,x):
        self.score += 1
