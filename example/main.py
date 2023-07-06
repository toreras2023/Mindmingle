from kivy.app import App
from kivy.uix.floatlayout import FloatLayout
from kivy.uix.button import Button
from kivy.uix.screenmanager import ScreenManager, Screen, SlideTransition

class FirstPage(FloatLayout):

    def switch_screen(self):
        myapp.screen_manager.transition = SlideTransition(direction='left', duration=.25)
        myapp.screen_manager.current = 'SecondPage'

class SecondPage(FloatLayout):

    def switch_back(self):
        myapp.screen_manager.transition = SlideTransition(direction='right', duration=.25)
        myapp.screen_manager.current = 'FirstPage'

class MyApp(MDApp):

    def build(self):
        self.screen_manager = ScreenManager()

        self.firstpage = FirstPage()
        screen = Screen(name='FirstPage')
        screen.add_widget(self.firstpage)
        self.screen_manager.add_widget(screen)

        self.secondpage = SecondPage()
        screen = Screen(name='SecondPage')
        screen.add_widget(self.secondpage)
        self.screen_manager.add_widget(screen)

        return self.screen_manager

myapp = MyApp()
myapp.run()
