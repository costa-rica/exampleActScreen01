from kivy.lang import Builder
from kivy.uix.screenmanager import ScreenManager, Screen
from kivy.properties import ObjectProperty, ColorProperty, StringProperty
from kivymd.uix.navigationdrawer import MDNavigationDrawer, MDNavigationLayout
from kivymd.uix.toolbar import MDToolbar
from kivy.uix.boxlayout import BoxLayout
from kivy.uix.textinput import TextInput
from kivy.uix.label import Label

import mainbox.mainbox

Builder.load_file('ps2.kv')


class NavMenu(BoxLayout):...
# class Toolbar(MDToolbar):...

class ParentScreen2(Screen):
  def __init__(self,**kwargs):
    super().__init__(**kwargs)
    print('ParentScreen2 __init__')
    self.on_enter_count=0
    self.sc_tracker=2

  def on_enter(self):
    print('ParentScreen2 on_enter: ', self.on_enter_count)
    act_screen = self.children[0].children[1].children[0]
    self.main_box = act_screen.children[0].children[0].children[1]
    extra_box = act_screen.children[0].children[0].children[0]
    self.main_box.ps1_base_width=self.parent.ps1_base_width
    self.main_box.ps1_base_height=self.parent.ps1_base_height
    self.main_box.size_kids()
    self.on_enter_count+=1
    print('self.main_box.sc:::', self.main_box.sc)

  def change_app_size(self,*args):
    print('shcange app size')
    print(self.sc_tracker % 3)

    self.main_box.sc=self.sc_tracker % 3 +1
    if self.main_box.sc == 3:
      self.btn_font_size.text="Font size: Large"
      self.btn_font_size.background_color=(.1,.1,.3)
      print('large print')
    elif self.main_box.sc ==2:
      self.btn_font_size.text="Font size: Medium"
      self.btn_font_size.background_color=(.3,.3,.3)
      print('medium font')
    else:
      self.btn_font_size.text="Font size: Small"
      self.btn_font_size.background_color=(.6,.6,.9)
      print('small font')
    self.sc_tracker+=1
    self.main_box.size_kids()
    # main_box.sc =





class ExtraBoxLayout(BoxLayout):
  ps1_base_height=ObjectProperty(0)
  def __init__(self,**kwargs):
    super().__init__(**kwargs)
    print('ExtraBoxLayout __init__')
