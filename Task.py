from datetime import datetime

class Task:
    def __init__(self):
        self.name:str = ""
        self.description:str = ""
        self.category = None #Add category class?
        self.tags = [] #"Can listen to audiobook", "Fun", "Menial", "Project.." etc
        self.points:int = 0 #later
        self.deadline:datetime = None 
        self.time:datetime = 0 #time commitment 
        self.energy:int = 0
        self.difficulty:int = 0
        self.prerequisite = None
        self.ID = 0

class Category:
    def __init(self):
        self.name:str = ""
        self.priority:int = 0
        self.ID = 0