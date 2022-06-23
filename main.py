from kivymd.app import MDApp
from kivy.core.window import Window
from myscreencontroller import MyScreenController
import os;import platform
from kivy.metrics import MetricsBase

if platform in ['ios','android']:
  print('kivy.utils.platform:::', platform)
  print('window size NOT set by application. Set by device')
else:
  # Window.size = (640, 1136)#iphone demensions
  Window.size = (960, 1704)#iphone mini
  # Window.size = (2560, 1440)
  print('window size set by application')


class MainApp(MDApp):
  def __init__(self,**kwargs):
    super().__init__(**kwargs)
    self.mycontroller=MyScreenController()

  def build(self):
    print('return build method')
    return self.mycontroller.get_screen()

if __name__=='__main__':
  MainApp().run()
