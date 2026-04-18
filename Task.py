#Store Task & related Classes
import datetime as dt
import json
from typing import Optional

class Task:
    def __init__(self, 
                 
                name:str = '', 
                description:str = '', 
                tags:list[str] = [],
                points:int = 0,
                energy:int = 0,
                difficulty:int = 0,
                importance:int = 0,
                prerequisites:list[int] = [],
                requisites:list[int] = [],
                ID:int = 0,
                complete:bool = False,

                category_name:str = '',
                category_priority:int = 0,
                category_ID:int = 0,

                deadline = dt.datetime(year=2026, month=4, day= 18, hour=23, minute=59, tzinfo=dt.UTC), 
                time_to_complete = dt.timedelta(hours=1),
        ):
        self.name:str = name
        self.description:str = description
        self.category:Category = Category(name=category_name, priority=category_priority, ID=category_ID) #Add category class?
        self.tags:list[str] = tags #"Can listen to audiobook", "Fun", "Menial", "Project.." etc
        self.points:int = points #implement later. from 0 to 200 probably.
        self.deadline:dt.datetime = deadline #BY DEFAULT, SET TO END OF DAY
        self.time_to_complete:dt.timedelta =  time_to_complete #time commitment 
        self.energy:int = energy #0-10
        self.difficulty:int = difficulty #0-10
        self.importance:int = importance #user given, 0-10
        self.prerequisite:list[int] = prerequisites     #should be the id of the task
        self.requisite:list[int] = requisites
        self.ID:int = ID
        self.complete:bool = complete
        self.priority = 0
        #self.priority:int = self.update_priority() #range from 0 to 1000

    def convert_task_data_to_json(self):
        res = json.dumps(self.__dict__, default=custom_serializer)
        return res
    
    def update_priority(self): #assign self a priority value
        
        #calculate priority
        priority = 8*self.importance
        if self.deadline is not None:
            time_to_deadline:dt.timedelta = self.deadline - dt.datetime.now() 
            hours_to_deadline = time_to_deadline/dt.timedelta(hours=1)
            priority += int(800*(self.time_to_complete.seconds/(60^2))/hours_to_deadline) #ex: task that takes 1 hour will have priority 40 24 hours before deadline
        #tasks with important categories will have more priority
        priority *= self.category.priority 
        #if this task is a prerequisite and its requisite task has higher priority, assume the requisite's priority
        return int(priority)
        # if self.requisite is not None and self.requisite.priority > self.priority:
        #     self.priority = self.requisite.priority
        
    def print_out_task(self):
        for k, v in self.__dict__.items():
            print(k, v)

    def __repr__(self):
        return str(self.__dict__)
        return f"Name='{self.name}', Desc={self.description}, Category={self.category}, Tags={self.tags}, Points={self.points}, Deadline={self.deadline}, time_to_complete={self.time_to_complete}, Energy={self.energy}, Difficulty={self.difficulty}, Prerequisite={self.prerequisite}, Requisite={self.requisite}, ID={self.ID}, Complete={self.complete}, Priority={self.priority}"

class Category: #?????
    def __init__(self, name: str='', priority:int = 0, ID:int = 0):
        self.name:str = name
        self.priority:int = priority
        self.ID = ID

  

    def __repr__(self):
        repr_str = str(self.__dict__)
        return repr_str




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
