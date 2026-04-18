#Store Task & related Classes
import datetime as dt
import json

class Task:
    def __init__(self):
        self.name:str = ""
        self.description:str = ""
        self.category:Category = Category() #Add category class?
        self.tags = [] #"Can listen to audiobook", "Fun", "Menial", "Project.." etc
        self.points:int = 0 #implement later. from 0 to 200 probably.
        self.deadline:dt.datetime = dt.datetime(year=2026, month=4, day= 18, hour=23, minute=59) #BY DEFAULT, SET TO END OF DAY
        self.time:dt.timedelta =  dt.timedelta(hours=1)#time commitment 
        self.energy:int = 0 #0-10
        self.difficulty:int = 0 #0-10
        self.importance:int = 0 #user given, 0-10
        self.prerequisite = None
        self.requisite = None
        self.ID:int = 0
        self.complete:bool = False
        self.priority:int = self.update_priority() #range from 0 to 1000

    def convert_task_data_to_json(self):
        res = json.dumps(self.__dict__, default=custom_serializer)
        return res
    
    def update_priority(self): #assign self a priority value
        #calculate priority
        priority = 8*self.importance
        if self.deadline is not None:
            time_to_deadline = dt.timedelta()
            time_to_deadline = self.deadline - dt.datetime.now() 
            hours_to_deadline = time_to_deadline/dt.timedelta(hours=1)
            priority += (self.time.seconds/(60^2))/hours_to_deadline #ex: task that takes 1 hour will have priority 40 24 hours before deadline
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
        self.name = ""
        self.current_energy = 0
        self.avg_energy = 0


def custom_serializer(obj):
    "custom serializer for objects that don't traditionally format with JSON"
    if obj is None:
        return 'None'
    elif isinstance(obj, dt.datetime):
        return obj.isoformat()
    elif isinstance(obj, dt.timedelta):
        return str(obj)
    elif isinstance(obj, Category):
        return obj.__dict__
    

    raise TypeError(f'Type {type(obj)} not serializable')