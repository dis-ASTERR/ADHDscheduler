from database import Database
from user import User
from task import Task


import datetime as dt



#KIVY STUFF
from kivy.clock import Clock
from kivy.lang import Builder
from kivy.uix.screenmanager import ScreenManager, Screen
import kivy.properties as kp



from kivymd.app import MDApp
from kivymd.uix.pickers import MDDockedDatePicker
from kivymd.uix.pickers import MDTimePickerDialVertical
#from kivymd.uix.button import MDButton
#from kivymd.uix.textfield import MDTextField
from kivymd.uix.boxlayout import MDBoxLayout
from kivymd.uix.screen import MDScreen
from kivymd.uix.screenmanager import MDScreenManager
from kivymd.uix.scrollview import MDScrollView
from kivy.uix.checkbox import CheckBox


# from kivymd.uix.screen import MDScreen
# from kivymd.uix.button import MDRaisedButton, MDButtonC




# class SearchAddQuery(MDScreen):
#     def __init__(self, *args, **kwargs):
#        super().__init__(*args, **kwargs)
    
#     def submit(self):
#         #energy = int(self.ids.energy.text)
#         #etc
#         self.manager.current = "Home"

user_name = 'Todd'

class SearchQuery(MDScreen):
    return_Val = kp.DictProperty()
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)


    def submit(self):
        print("Submit function was called!!")
        query_result = dict()
        
        child = self.children[0]
        print(child.name)
        query_result['name'] = child.name.text
        query_result['description'] = child.description.text


        #category
        query_result['category_name'] = child.category_name.text
        query_result['category_priority'] = child.category_priority.text

        query_result['category_ID'] = [child.category_ID.text]
        query_result['energy'] = [child.energy.text, child.energy.text]
        query_result['difficulty'] = [child.difficulty.text, child.difficulty.text]
        query_result['importance'] = [child.importance.text, child.importance.text]

        query_result['energy'] = child.energy.text
        query_result['difficulty'] = child.difficulty.text
        query_result['importance'] = child.importance.text


        query_result['complete'] = str(child.complete.active)
        
        query_result['deadline'] = ''
        query_result['time_to_complete'] = ''
        
        




        return_Val = query_result


        app = MDApp.get_running_app()
        if app is not None:
            app.handle_add_and_query(return_Val, is_new_task= False)
        else:
            raise ValueError("Unable to find app!")


class AddTask(MDScreen):
    return_Val = kp.DictProperty()
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs) 


    def submit(self):
        print("Submit function was called!!")
        query_result = dict()
        
        child = self.children[0]
        print(child.name)
        query_result['name'] = child.name.text
        query_result['description'] = child.description.text


        tags = child.tags.text
        if ',' in tags:
            tags = tags.split(',')
        query_result['tags'] = tags


        #category
        query_result['category_name'] = child.category_name.text
    
        #could raise error if user isn't perfect :)
        query_result['category_ID'] = child.category_ID.text


        query_result['category_priority'] = child.category_priority.value
        query_result['energy'] = child.energy.value
        query_result['difficulty'] = child.difficulty.value
        query_result['importance'] = child.importance.value


        query_result['complete'] = bool(child.complete.active)
        
        query_result['deadline'] = ''
        query_result['time_to_complete'] = ''
        
        




        return_Val = query_result


        app = MDApp.get_running_app()
        if app is not None:
            app.handle_add_and_query(return_Val, is_new_task= True)
        else:
            raise ValueError("Unable to find app!")

     



# class User:
#     def __init__(self, name:str ='debug') -> None:
#         self.name = name

class TimePicker(MDBoxLayout):
    def __init__(self, **kwargs):
        super(TimePicker, self).__init__(**kwargs)


    def show_time_picker(self, hour, minute):
        self.time_picker= MDTimePickerDialVertical()
        self.time_picker.bind(on_cancel=self.cancel_time_picker)
        self.time_picker.bind(on_ok=self.time_picker_ok)
        self.time_picker.open()


    def cancel_time_picker(self, time_picker:MDTimePickerDialVertical):
        self.timereturn = None
        time_picker.dismiss()


    def time_picker_ok(self, time_picker:MDTimePickerDialVertical):
        minute = time_picker.minute
        hour = time_picker.hour
        self.timereturn = dt.timedelta(hours=int(hour), minutes=int(minute))
        time_picker.dismiss()


class LabelSlider(MDBoxLayout):
   def __init__(self, **kwargs):
       super(LabelSlider, self).__init__(**kwargs)
   title = kp.StringProperty("")
   value = kp.NumericProperty(0)


class Home(MDScreen):
    def __init__(self, **kwargs):
        super(Home, self).__init__(**kwargs)
    points = kp.NumericProperty(0)


class DatePicker(MDBoxLayout):
    def __init__(self, **kwargs):
        super(DatePicker, self).__init__(**kwargs)
        # Call super first to initialize parent class logic
        


    def show_date_picker(self, focus,text_id):
        if not focus:
            return
        date_dialog = MDDockedDatePicker(
            min_date = dt.date.today()
        )
        # date_dialog.pos = [
        #     self.ids.field.center_x - date_dialog.width / 2,
        #     self.ids.field.y - (0.5*date_dialog.height),
        # ]
        date_dialog.bind(on_cancel=self.cancel_date_picker)
        date_dialog.bind(on_ok=self.date_picker_ok)
        #date_dialog.bind(on_select_day=self.date_picker_update(date_dialog,text_id))
        date_dialog.open()
        


    def cancel_date_picker(self, date_picker:MDDockedDatePicker):
        self.datereturn = None
        date_picker.dismiss()




    def date_picker_ok(self, date_picker:MDDockedDatePicker):
        day = date_picker.sel_day
        month = date_picker.sel_month
        year = date_picker.sel_year
        self.datereturn = dt.datetime(year=year, month=month, day=day)
        date_picker.dismiss()


class Intro_Q(MDScreen):
    energyVal= kp.NumericProperty()
    def __init__(self, **kwargs):
        super(Intro_Q, self).__init__(**kwargs)
    def submit(self):
        energyVal = int(self.ids.energy.value)
        hours = int(self.ids.time.hours)
        minutes = int(self.ids.time.minutes)
        self.manager.current = 'Home'
        app = MDApp.get_running_app()
        app.update_user(energyVal, hours, minutes,0)
        
       # minutes = int(self.ids.minutes.value)

class GetTimeDelta(MDBoxLayout):
    def __init__(self, **kwargs):
        super(GetTimeDelta, self).__init__(**kwargs)
    hours = kp.NumericProperty()
    minutes = kp.NumericProperty()
    


class ADHDScheduler(MDApp):
    user = kp.ObjectProperty(User(name=user_name))
    def build(self):
       self.theme_cls.theme_style="Light"
       self.theme_cls.primary_palette = "Blue"
       sm = MDScreenManager()
       sm.md_bg_color = self.theme_cls.backgroundColor
       sm.add_widget(Intro_Q(name='Intro_Q'))
       sm.add_widget(Home(name='Home'))
       sm.add_widget(AddTask(name='AddTask'))
       sm.add_widget(SearchQuery(name='SearchQuery'))
       return sm
       #return Builder.load_file("adhdscheduler.kv")
    
  
   ########### APP FUNCTIONS#########
    def make_task(self):
        #generate page (widget tree)
        #name
        #call add deadline (opt)
        #add prerequisite or requisite task with search_tasks
        # 3 sliders: energy, difficulty, importance
        #send to database
        pass
    def add_deadline(self):
        #return datetime object
        #show date picker, then time picker. store values.
        pass
    def handle_add_and_query(self, query_info:dict, is_new_task:bool):
        if is_new_task:
            
            new_task = Task(
                name = query_info['name'],
                description = query_info['description'],
                tags = query_info['tags'],
                energy = query_info['energy'],
                difficulty = query_info['difficulty'],
                importance = query_info['importance'],
                complete = query_info['complete'],


                category_name = query_info['category_name'],
                category_priority = query_info['category_priority'],
                category_ID = query_info['category_ID'],
            )

        if new_task is not None:
            Database().add_task_to_database(task=new_task, user=self.user.name)
        else:
            print("Unable to create task!")
        #show list of tasks. be able to search via name, category, and tag, and select a task.
        pass

    def update_user(self, energy, hours, minutes, points):
        self.user.current_energy = energy
        self.user.time = dt.timedelta(hours=hours,minutes=minutes)
        pass








   ########### UI FUNCTIONS #########
   ### TIME PICKER###
   # def show_time_picker(self, hour, minute):
   #     self.time_picker= MDTimePickerDialVertical()
   #     self.time_picker.bind(on_cancel=self.cancel_time_picker)
   #     self.time_picker.bind(on_ok=self.time_picker_ok)
   #     self.time_picker.open()


   # def cancel_time_picker(self, time_picker:MDTimePickerDialVertical):
   #     self.timereturn = None
   #     time_picker.dismiss()


   # def time_picker_ok(self, time_picker:MDTimePickerDialVertical):
   #     minute = time_picker.minute
   #     hour = time_picker.hour
   #     self.timereturn = dt.timedelta(hours=int(minute), minutes=int(minute))
   #     time_picker.dismiss()


   # ### DATE PICKER ###
   # def show_date_picker(self, focus,text_id):
   #     if not focus:
   #         return
   #     date_dialog = MDDockedDatePicker(
   #         min_date = dt.date.today()
   #     )
   #     date_dialog.pos = [
   #         self.root.ids.field.center_x - date_dialog.width / 2,
   #         self.root.ids.field.y - (date_dialog.height),
   #     ]
   #     date_dialog.bind(on_cancel=self.cancel_date_picker)
   #     date_dialog.bind(on_ok=self.date_picker_ok)
   #     #date_dialog.bind(on_select_day=self.date_picker_update(date_dialog,text_id))
   #     date_dialog.open()
      


   # def cancel_date_picker(self, date_picker:MDDockedDatePicker):
   #     self.datereturn = None
   #     date_picker.dismiss()




   # def date_picker_ok(self, date_picker:MDDockedDatePicker):
   #     day = date_picker.sel_day
   #     month = date_picker.sel_month
   #     year = date_picker.sel_year
   #     self.datereturn = dt.datetime(year=year, month=month, day=day)
   #     date_picker.dismiss()
  
   # def date_picker_update(self, date_picker:MDDockedDatePicker, textid):
   #     day = date_picker.sel_day
   #     month = date_picker.sel_month
   #     year = date_picker.sel_year
   ### ISSUE HERE: accessing text field
   #     self.root.ids.field.ids.textid.text = f"{month}/{day}/{year}"


   ###
  











#def main():
   #db = Database()
   #collection = db.get_collection_from_user()


   # print("wowow")
   # test_task = Task()
   # test_task.name = "Test Task"
   # test_task.description = "This is a test task designed to make me suffer! :3"
   # test_task.category = Category()
   # test_task.tags = ["Apple", "Banana", "Debug"]
   # test_task.points = 10
   # test_task.deadline = dt.datetime(2026, 4, 18)
   # test_task.time = dt.timedelta(hours=5)
   # test_task.energy = 6
   # test_task.difficulty = 3
   # test_task.prerequisite = None
   # test_task.requisite = None
   # test_task.complete = False
   # test_task.priority = test_task.update_priority()
   # test_task.ID = hash(test_task)


   # print(test_task.convert_task_data_to_json())
  # pass
  
  




#make_task
#open_app/questionnaire
#user_setup
#get_tasks
  


if __name__ == '__main__':
   print("GUH")
   ADHDScheduler().run()
   print("GUH2")





