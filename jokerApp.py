from typing import List, Any

import kivy

from kivy.app import App
from kivy.lang import Builder
from kivy.uix.widget import Widget
from kivy.uix.floatlayout import FloatLayout
from kivy.uix.label import Label
from kivy.properties import ObjectProperty
from kivy.uix.button import Button
from kivy.uix.popup import Popup
from kivy.uix.screenmanager import ScreenManager, Screen

nums = set()
myset = set()
set_click= set()
joker: List[Any] = []

files = {'2009':'Joker_2009.xlsx','2010': 'Joker_2010.xlsx', '2011':'Joker_2011.xlsx', '2012':'Joker_2012.xlsx', '2013':'Joker_2013.xlsx',
         '2014':'Joker_2014.xlsx', '2015':'Joker_2015.xlsx', '2016': 'Joker_2016.xlsx', '2017':'Joker_2017.xlsx', '2018':'Joker_2018.xlsx',
         '2019':'Joker_2019.xlsx','2020': 'Joker_2020.xlsx', '2021': 'Joker_2021.xlsx'}

class Widgets(Widget):
    def btn(self):
        show_popup()

class P(FloatLayout):
    def set_text(self, text):
        self.ids['label'].text = text
    pass

class MyGrid(Widget):
    def __init__(self, **kwargs):
        super(MyGrid, self).__init__(**kwargs)

class IntroScreen(Screen):
    pass

class SelectScreen(Screen):
    pass

class SelectbScreen(Screen):
    pass

class InputScreen(Screen):
   pass

class InputbScreen(Screen):
    pass
    '''final_check_button = ObjectProperty()

    def disablebtn(self):
        if self.final_check_button.disabled == "Disabled":
            self.final_check_button.text = "Enabled"
        else:
            self.final_check_button.text = "Disabled"

    def validate(self):
        if len(nums) != 5:
            print('NO')
            self.final_check_button.disabled == True
        else:
            self.final_check_button.disabled == False'''

class FinalScreen(Screen):
    pass

class ScreenManagment(ScreenManager):
    pass

kv = Builder.load_file('multiples.kv')

def show_popup():
    show = P()
    popupWindow = Popup(title="Popup Window", content=show, size_hint=(None, None), size=(400, 400),auto_dismiss=True)
    popupWindow.open()

class MyJokerApp(App):
    def __init__(self, **kwargs):
        super().__init__(**kwargs)
        self.value = None

    def build(self):
        Builder.load_file('multiples.kv')
        sm = ScreenManager()
        sm.add_widget(IntroScreen(name='Intro'))
        sm.add_widget(SelectScreen(name='Select'))
        sm.add_widget(SelectbScreen(name='Selectb'))
        sm.add_widget(InputScreen(name='Input'))
        sm.add_widget(InputbScreen(name='Inputb'))
        sm.add_widget(FinalScreen(name='Final'))
        return sm
        #return MyGrid()


    def btn_press(self, button):
        myset.add(button.text)
        if len(nums) < 5:
            nums.add(int(button.text))
        else:
            show_popup()
            pass
        print(nums)
        print(len(myset))
        return nums

    def btn_press_joker(self, button):
        ''' get the joker number '''
        joker.append(button.text)
        if len(joker) > 1:
            joker.pop()
            popup = Popup(title='Test popup',
                          content=Label(text='You have entered a valid joker number already!!!'),
                          size_hint=(None, None), size=(400, 400))
            popup.open()
            # print(joker)
        else:
            print(f'joker number is {button.text}')
        return button.text

    def call(self, button):
        '''return the value of the selected YEAR'''
        print(files[button.text])
        return button.text

    '''def validate(self):
        if len(nums) != 5:
            print('NO')
            #self.final_check_button.disabled == True
            return False
        else:
            print('YES')
            #self.final_check_button.disabled == False
            return True    '''

    def erase(self):
        if len(nums) > 1:
            nums.pop()
        else:
            pass
        print(nums)
        return nums

    def disable_btn(self):
        if self.validate() == True:
            self.ids.final_check_button.disabled = False
        else:
            self.ids.final_check_button.disabled = True



label = MyJokerApp()

label.run()