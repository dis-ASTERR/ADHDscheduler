import datetime

class Task:
    def __init__(self):
        self.name:str = ""
        self.description:str = ""
        self.category = None #Add category class?
        self.tags = [] #"Can listen to audiobook", "Fun", "Menial", "Project.." etc
        self.points:int = 0 #later
        self.deadline:datetime = None 
        self.energy:int = 0
        self.difficulty:int = 0
        self.prerequisite = None
        self.ID = 000
