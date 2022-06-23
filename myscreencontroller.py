from kivy.lang import Builder
from kivy.uix.screenmanager import Screen, ScreenManager
from kivy.properties import ObjectProperty
import ps2

KV='''
<BaseScreenManger>:
  login_screen:login_screen
  ps2:ps2
  canvas.before:
    Color:
      rgb: [127/255,160/255,189/255]
    Rectangle:
      pos: self.pos
      size: self.size
  Screen:
    id:login_screen
    name:"parent_screen_1"
    BoxLayout:
      orientation:"vertical"
      Label:
        text:"Login Screen"
      Button:
        text:"Login Button"
        on_press: root.current="parent_screen_2"
  ParentScreen2:
    id:ps2
    name:"parent_screen_2"

'''

Builder.load_string(KV)


class BaseScreenManger(ScreenManager):
  controller = ObjectProperty()
  def __init__(self,**kwargs):
    super().__init__(**kwargs)
    print('BaseScreenManger __init__')
    self.bind(children=self.on_children)

  def on_children(self,*args):
    # print('self.children:::', self.children)
    children_names_dict={i.name:i for i in self.children}
    if 'parent_screen_1' in children_names_dict.keys():
      self.ps1_base_height=children_names_dict['parent_screen_1'].height
      self.ps1_base_width=children_names_dict['parent_screen_1'].width
      print(self.ps1_base_height)



class MyScreenController():
  def __init__(self):
    self.view=BaseScreenManger(controller=self)
    print('MyScreenController __init__')

  def get_screen(self):
    return self.view
