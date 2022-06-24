from kivy.lang import Builder
from kivy.uix.boxlayout import BoxLayout
from kivy.uix.anchorlayout import AnchorLayout
from kivy.uix.textinput import TextInput
from kivy.properties import ObjectProperty, StringProperty
# from utils import add_activity_util
from kivy.uix.popup import Popup
# from utils import current_time_util
from kivy.uix.label import Label
from kivy.uix.widget import Widget
from kivy.graphics import Color, Rectangle
from kivy.clock import Clock

from size_dict import size_dict

Builder.load_file('mainbox/mainbox.kv')

class MainBoxLayout(BoxLayout):
  ps1_base_width=ObjectProperty(0)
  ps1_base_height=ObjectProperty(0)
  toolbar_height=ObjectProperty(0)

  def __init__(self,**kwargs):
    super(MainBoxLayout, self).__init__(**kwargs)
    self.on_size_count=0
    self.sc=3#size coefficient
    self.bind(size=self.on_size)


  def on_size(self,*args):
    print('MainBox on_size')
    self.input_act_note.sc=self.sc
    if self.on_size_count==1:
      print('MainBox on_size - made changes ****')
      self.label_email.text="nickapeed@yahoo.com"

      self.label_act_name.text="Add Activity Name"
      self.label_act_note.text="Add Acitivty Note"

      self.label_date.text="Date"
      self.input_date.text = "6/20/2022"
      self.label_time.text="Time"
      self.input_time.text= "17:20"

      self.btn_submit_act.text="Submit Activity"
    self.on_size_count+=1

  def size_kids(self):
    base_screen_manager = self.parent.parent.parent.parent

  # Act Screen Name / Email
    self.label_email.size_hint=(None,None)
    self.label_email.font_size=self.ps1_base_height * size_dict['label_email']['font_size'][self.sc]
    self.label_email.size= self.label_email.texture_size

    self.anchor_screen_name.anchor_x="right"
    self.anchor_screen_name.size_hint=(1,None)
    self.anchor_screen_name.padding=(0,self.ps1_base_height * size_dict['anchor_screen_name']['padding-top'][self.sc],
      self.ps1_base_width * size_dict['anchor_screen_name']['padding-right'][self.sc],0)
    self.anchor_screen_name.height=self.label_email.height + self.ps1_base_height * size_dict['anchor_screen_name']['padding-top'][self.sc]

    Clock.schedule_once(self.get_size, .01)
    # print('Note: Anything after this line will run concurrently, so just put everything in get_size from now on...')

  def get_size(self,*args):
    self.label_email.size= self.label_email.texture_size

  #Add Act Name
    self.label_act_name.size_hint=(None,None)
    self.label_act_name.font_size = self.ps1_base_width * size_dict['label_act_name']['font_size'][self.sc]
    self.anchor_screen_name.size_hint_y=None
    Clock.schedule_once(self.get_size_2, .01)
    # print('Note: Anything after this line will run concurrently, so just put everything in get_size_2 from now on...')

  def get_size_2(self,*args):
    self.label_act_name.size = self.label_act_name.texture_size

    self.anchor_screen_name.height=self.label_email.texture_size[1]

    # with self.label_act_name.canvas.before:
    #   print('does canves get set?????????')
    #   Color(1, 0, 0, 1)
    #   Rectangle(pos=self.label_email.pos, size=self.label_email.size)

    self.input_act_name.font_size=self.ps1_base_width * size_dict['input_act_name']['font_size'][self.sc]
    self.input_act_name.height = self.label_act_name.height

    self.anchor_act_name_label.anchor_x="left"
    self.anchor_act_name_label.size_hint=(1,None)
    self.anchor_act_name_label.height=self.label_act_name.height

    self.box_act_name.size_hint=(1,None)
    self.box_act_name.height = self.anchor_act_name_label.height + self.input_act_name.height + \
      self.ps1_base_height * size_dict['box_act_name']['padding-top'][self.sc]
    self.box_act_name.padding =(self.ps1_base_width*size_dict['box_act_name']['padding-left'][self.sc],
      self.ps1_base_height * size_dict['box_act_name']['padding-top'][self.sc],
      self.ps1_base_width*size_dict['box_act_name']['padding-right'][self.sc],0)

  #Add Act Note
    self.label_act_note.size_hint=(None,None)
    self.label_act_note.font_size = self.ps1_base_width * size_dict['label_act_note']['font_size'][self.sc]
    Clock.schedule_once(self.get_size_3,.01)

  def get_size_3(self,*args):
    self.label_act_note.size=self.label_act_note.texture_size

    self.input_act_note.font_size=self.ps1_base_width * size_dict['input_act_note']['font_size'][self.sc]
    self.input_act_note.size_hint=(1,None)
    self.input_act_note.height=self.label_act_note.height *len(self.input_act_note._lines)

    self.anchor_act_note_label.anchor_x="left"
    self.anchor_act_note_label.size_hint=(1,None)
    self.anchor_act_note_label.height = self.label_act_note.height

    self.box_act_note.size_hint=(1,None)
    self.box_act_note.padding=(self.ps1_base_width*size_dict['box_act_note']['padding-left'][self.sc],
      self.ps1_base_height * size_dict['box_act_note']['padding-top'][self.sc],
      self.ps1_base_width*size_dict['box_act_note']['padding-right'][self.sc],0)

  #Add Date Time
    self.label_time.font_size = self.ps1_base_width * size_dict['label_time']['font_size'][self.sc]
    self.label_date.font_size = self.ps1_base_width * size_dict['label_date']['font_size'][self.sc]

    self.label_time.size_hint = (None,None)
    self.label_date.size_hint = (None,None)

    Clock.schedule_once(self.get_size_4,.01)

  def get_size_4(self,*args):
    self.label_date.size = self.label_date.texture_size
    self.label_time.size = self.label_time.texture_size

    self.input_time.font_size = self.ps1_base_width * size_dict['input_time']['font_size'][self.sc]
    self.input_date.font_size = self.ps1_base_width * size_dict['input_date']['font_size'][self.sc]
    self.input_time.size_hint=(1,None)
    self.input_date.size_hint=(1,None)

    self.input_time.height=self.label_time.height
    self.input_date.height=self.label_date.texture_size[1]


    Clock.schedule_once(self.get_size_5,.01)
  def get_size_5(self,*args):

    self.anchor_date_time.size_hint=(1,None)
    self.anchor_date_time.height = self.input_date.height + self.label_date.height + \
      self.ps1_base_height * size_dict['anchor_date_time']['padding-top'][self.sc]
    self.anchor_date_time.padding =(self.ps1_base_width * size_dict['anchor_date_time']['padding-left'][self.sc],
      self.ps1_base_height * size_dict['anchor_date_time']['padding-top'][self.sc],
      self.ps1_base_width * size_dict['anchor_date_time']['padding-right'][self.sc],0)

    self.btn_submit_act.font_size = self.ps1_base_width * size_dict['btn_submit_act']['font_size'][self.sc]

    self.anchor_submit.anchor_x = "right"
    self.anchor_submit.padding = (0,0,self.ps1_base_width * size_dict['anchor_submit']['padding-right'][self.sc],0)


  def wonder_button(self):
    print('---mainbox wonder_button---')
    print('self.box_act_name.height:', self.box_act_name.height)
    print('self.anchor_act_name_label.height:', self.anchor_act_name_label.height)
    print('self.label_act_name.height:', self.label_act_name.height)
    print('self.input_act_name.height:', self.input_act_name.height)


# class CanvasWidget(Widget):
#   def __init__(self,**kwargs):
#     super().__init__(**kwargs)
#     with self.canvas:
#       Color(200/255,160/255,100/255,1)
#       self.rect=Rectangle(pos=self.pos,size=self.size)
#       self.bind(pos=self.update_rect,
#                     size=self.update_rect)
#   def update_rect(self, *args):
#     self.rect.pos = self.pos
#     self.rect.size = self.size


class TextInputAddName(TextInput):
  def on_focus(instance, instance_twice, value):#I'm not sure why i'm passing instance twice
    print('***TextInputAddName***')
    main_box =instance.parent.parent#different hiearchey than TextInputDynamicActNote
    if value:
      main_box.label_act_name.color=(0,0,0,1)
    else:
      main_box.label_act_name.color=(.3,.3,.3,1)



class TextInputDynamicActNote(TextInput):
  def __init__(self,**kwargs):
    super().__init__(**kwargs)
    self.on_size_count=0
    self.old_line_count=1
    self.bind(_lines=self.change_height_util)

  def change_height_util(self,*args):
    self.main_box=self.parent.parent
    self.height=len(self._lines) * self.main_box.label_act_note.height
    self.main_box.box_act_note.height=self.main_box.input_act_note.height + self.main_box.anchor_act_note_label.height + \
      self.main_box.ps1_base_height * size_dict['box_act_note']['padding-top'][self.sc]


  def on_focus(self, instance_twice, value):
    self.main_box=self.parent.parent
    if value:
      self.main_box.label_act_note.color=(0,0,0,1)
    else:
      self.main_box.label_act_note.color=(.3,.3,.3,1)
