#from database import Database
# from Task import Task, Category
import datetime as dt


#KIVY STUFF
from kivy.clock import Clock
from kivy.lang import Builder
import kivy.properties as kp


from kivymd.app import MDApp
from kivymd.uix.pickers import MDDockedDatePicker
from kivymd.uix.pickers import MDTimePickerDialVertical
from kivymd.uix.button import MDButton
from kivymd.uix.textfield import MDTextField
from kivymd.uix.boxlayout import MDBoxLayout
from kivymd.uix.scrollview import MDScrollView
from kivy.uix.checkbox import CheckBox


# from kivymd.uix.screen import MDScreen
# from kivymd.uix.button import MDRaisedButton, MDButtonC




class SearchAddQuery(MDScrollView):
   def __init__(self, *args, **kwargs):
       super().__init__(*args, **kwargs)


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
  
   # def date_picker_update(self, date_picker:MDDockedDatePicker, textid):
   #     day = date_picker.sel_day
   #     month = date_picker.sel_month
   #     year = date_picker.sel_year
   ### ISSUE HERE: accessing text field
   #     self.root.ids.field.ids.textid.text = f"{month}/{day}/{year}"
   pass


class ADHDScheduler(MDApp):
   def build(self):
       self.theme_cls.theme_style="Light"
       self.theme_cls.primary_palette = "Blue"
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
   def search_tasks(self):
       #show list of tasks. be able to search via name, category, and tag, and select a task.
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
  








# class Intro_Questionnaire(BoxLayout):






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





