import datetime as dt
class User:
    def __init__(self):
        self.name = ""
        self.current_energy = 0
        #self.avg_energy = 0
        self.points = 0
        self.time:dt.timedelta = 0