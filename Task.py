#Store Task & related Classes
import datetime as dt
import json

class Task:
    def __init__(self):
        self.name:str = ""
        self.description:str = ""
        self.category:Category = None #Add category class?
        self.tags = [] #"Can listen to audiobook", "Fun", "Menial", "Project.." etc
        self.points:int = 0 #implement later. from 0 to 200 probably.
        self.deadline:dt.datetime = None #BY DEFAULT, SET TO END OF DAY
        self.time:dt.timedelta = 0 #time commitment 
        self.energy:int = 0 #0-10
        self.difficulty:int = 0 #0-10
        self.importance:int = 0 #user given, 0-10
        self.prerequisite = None
        self.requisite = None
        self.ID:int = 0
        self.complete:bool = False
        self.priority:int = self.update_priority() #range from 0 to 1000

    def convert_task_data_to_json(self):
        res = json.dumps(self.__dict__)
        return res
    
    def update_priority(self): #assign self a priority value
        #calculate priority
        priority = 8*self.importance
        if self.deadline is not None:
            time_to_deadline = dt.timedelta()
            time_to_deadline = self.deadline - dt.datetime.now() 
            hours_to_deadline = time_to_deadline/dt.timedelta(hours=1)
            priority += int(800*(self.time.hours)/hours_to_deadline) #ex: task that takes 1 hour will have priority 40 24 hours before deadline
        #tasks with important categories will have more priority
        priority = priority * self.category.priority 
        #if this task is a prerequisite and its requisite task has higher priority, assume the requisite's priority
        if self.requisite is not None and self.requisite.priority > self.priority:
            self.priority = self.requisite.priority
        return priority

    def __repr__(self):
        return f"Name='{self.name}', Desc={self.description}, Category={self.category.name}, Category.priority={self.category.priority}, Tags={self.tags}, Points={self.points}, Deadline={self.deadline}, Energy={self.energy}, Difficulty={self.difficulty}, Prerequisite={self.prerequisite}, Requisite={self.requisite}, ID={self.ID}, Complete={self.complete}, Priority={self.priority}"

class Category: #?????
    def __init__(self, name: str='', priority:int = 0, ID:int = 0):
        self.name:str = name
        self.priority:int = priority
        self.ID = ID

    def __repr__(self):
        repr_str = str(self.__dict__)
        return repr_str

class User:
    def __init__(self):
        self.name:str = ""
        self.current_energy:int = 0
        self.avg_energy:float = 0
        self.current_time:dt.timedelta = 0
        self.ID:int = 0
        #each user has its own task database