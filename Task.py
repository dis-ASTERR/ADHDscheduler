#Store Task & related Classes
import datetime as dt

class Task:
    def __init__(self):
        self.name:str = ""
        self.description:str = ""
        self.category = None #Add category class?
        self.tags = [] #"Can listen to audiobook", "Fun", "Menial", "Project.." etc
        self.points:int = 0 #implement later. from 0 to 200 probably.
        self.deadline:dt.datetime = None 
        self.time:dt.timedelta = 0 #time commitment 
        self.energy:int = 0 #0-10
        self.difficulty:int = 0 #0-10
        self.prerequisite = None
        self.requisite = None
        self.ID = 0
        self.complete = False
        self.priority = self.update_priority() #range from 0 to 1000
    
    def update_priority(self): #assign self a priority value
        #calculate priority
        priority = 1
        if self.deadline is not None:
            time_to_deadline = dt.timedelta()
            time_to_deadline = self.deadline - dt.datetime.now() 
            priority += time_to_deadline.days*5
        #if this task is a prerequisite and its requisite task has higher priority, assume the requisite's priority
        if self.requisite is not None and self.requisite.priority > self.priority:
            self.priority = self.requisite.priority


    def __repr__(self):
        return f"Name='{self.name}', Desc={self.description}, Category={self.category.name}, Category.priority={self.category.priority}, Tags={self.tags}, Points={self.points}, Deadline={self.deadline}, Energy={self.energy}, Difficulty={self.difficulty}, Prerequisite={self.prerequisite}, Requisite={self.requisite}, ID={self.ID}, Complete={self.complete}, Priority={self.priority}"

class Category: #?????
    def __init__(self):
        self.name:str = ""
        self.priority:int = 0
        self.ID = 0

class User:
    def __init__(self):
        self.name = ""
        self.current_energy = 0
        self.avg_energy = 0