import datetime as dt
class User:
    def __init__(self, name:str = 'Jeff'):
        self.name:str = name
        self.current_energy:int = 0
        #self.avg_energy = 0
        self.time:dt.timedelta = 0
        self.current_points:int = 0
