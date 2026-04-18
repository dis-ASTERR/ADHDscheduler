from database import Database

class User:
    def __init__(self, name:str ='debug') -> None:
        self.name = name




def main():
    db = Database()
    collection = db.get_collection_from_user()
    

if __name__ != '__main__':
    main()
