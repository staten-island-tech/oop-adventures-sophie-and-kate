class man:
    def __init__(self,Hstyle,physique,personality,Hcolor,name):
        self.Hcolor=Hcolor
        self.Hstyle=Hstyle
        self.personality=personality
        self.physique=physique
        self.score = 0
        self.name = name
    def get_score(self):
        return self.score
    def set_score(self):
        self.score += 1
    
class woman:
    def __init__(self,Hstyle,physique,personality,Hcolor):
        self.Hcolor=Hcolor
        self.Hstyle=Hstyle
        self.personality=personality
        self.physique=physique
        self.score = 0
    def get_score(self):
        return self.score
    def set_score(self):
        self.score += 1

