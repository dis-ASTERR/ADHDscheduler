from database import Database
from task import Task, Category
import datetime as dt
import json
from user import User


def main():
    new_user = User("Todd")
    
    db = Database()
    col = db.get_collection_from_user(new_user.name)
    l_o_t = db.get_all_entries_and_put_them_in_a_list_of_tasks(new_user.name)
    print(l_o_t)
    




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
