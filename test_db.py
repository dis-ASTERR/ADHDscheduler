from database import Database
from user import User
user = User(name='debug')
user.current_energy = 5
user_2 = User(name='Todd')
user_2.current_energy = 5


def main():
    task = Database().pick_task_for_user(user=user.name, current_energy=user.current_energy)
    print(task)

    user.current_energy = 3

    task = Database().pick_task_for_user(user=user.name, current_energy=user.current_energy)
    print(task)


    task = Database().pick_task_for_user(user=user_2.name, current_energy=user_2.current_energy)
    print(task)

main()