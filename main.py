from kivy.app import App
from kivy.uix.screenmanager import ScreenManager
from screens import HomeScreen, Registro1Screen, LoginScreen, SplashScreen, Registro2Screen

class MyScreenManager(ScreenManager):
    def __init__(self, **kwargs):
        super(MyScreenManager, self).__init__(**kwargs)
        self.add_widget(SplashScreen(name='splash'))
        self.add_widget(HomeScreen(name='home'))
        self.add_widget(Registro1Screen(name='registro1'))
        self.add_widget(Registro2Screen(name='registro2'))
        self.add_widget(LoginScreen(name='login'))


class MyApp(App):
    def build(self):
        return MyScreenManager()


if __name__ == '__main__':
    MyApp().run()
