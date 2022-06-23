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

  def on_enter(self):
    print('ParentScreen2 on_enter: ', self.on_enter_count)
    act_screen = self.children[0].children[1].children[0]
    main_box = act_screen.children[0].children[0].children[1]
    extra_box = act_screen.children[0].children[0].children[0]
    main_box.ps1_base_width=self.parent.ps1_base_width
    main_box.ps1_base_height=self.parent.ps1_base_height
    main_box.size_kids()
    self.on_enter_count+=1




class ExtraBoxLayout(BoxLayout):
  ps1_base_height=ObjectProperty(0)
  def __init__(self,**kwargs):
    super().__init__(**kwargs)
    print('ExtraBoxLayout __init__')