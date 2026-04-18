from database import Database
from task import Task, Category
import datetime as dt
import json

class User:
    def __init__(self, name:str ='debug') -> None:
        self.name = name


def main():
    db = Database()
    tasks = db.query_database(deadline=dt.datetime(year=2026, month=4, day= 18, hour=23, minute=59, tzinfo=dt.UTC))
    for task in tasks:
        task.print_out_task()




    #result = db.database.cursor_comand()
    """col = db.get_collection_from_user()
    if col is not None:
        result = col.find({'name': 'Test', 'category.name': '', 'points':10})
        for entry in result:
            task = db.convert_entry_to_task(entry)
            task.print_out_task()

    else:
        print("Error! - could not find collection")"""
    
    

if __name__ == '__main__':
    main()

def task_example_collapsable():
    """test_task = Task()
    test_task.name = "Test Task"
    test_task.description = "This is a test task designed to make me suffer! :3"
    test_task.category = Category()
    test_task.tags = ["Apple", "Banana", "Debug"]
    test_task.points = 10
    test_task.deadline = dt.datetime(2026, 4, 18)
    test_task.time = dt.timedelta(hours=5)
    test_task.energy = 6
    test_task.difficulty = 3
    test_task.importance = 9
    test_task.prerequisite = None
    test_task.requisite = None
    test_task.complete = False
    test_task.priority = test_task.update_priority()
    test_task.ID = hash(test_task)"""
    #db.add_task_to_database(task=test_task)
    pass
