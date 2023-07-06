import time
from kivy.app import App
from kivy.uix.boxlayout import BoxLayout
from kivy.uix.button import Button
from kivy.uix.image import Image
from kivy.uix.label import Label
from kivy.animation import Animation
from kivy.uix.screenmanager import ScreenManager, Screen
from kivy.uix.screenmanager import SlideTransition
from kivy.clock import Clock
import sqlite3
from kivy.app import App
from kivy.uix.boxlayout import BoxLayout
from kivy.uix.button import Button
from kivy.uix.label import Label
from kivy.uix.screenmanager import ScreenManager, Screen
from kivy.uix.textinput import TextInput

# Conexión a la base de datos SQLite3
conn = sqlite3.connect('database.db')
c = conn.cursor()

# Creación de la tabla 'usuarios'
c.execute('''CREATE TABLE IF NOT EXISTS usuarios
             (correo TEXT PRIMARY KEY, contraseña TEXT)''')

conn.commit()

class SplashScreen(Screen):
    def __init__(self, **kwargs):
        super(SplashScreen, self).__init__(**kwargs)
        self.layout = BoxLayout(orientation='vertical', spacing=10, padding=50)
        self.image = Image(source='Imágenes/mindmingle.png')
        self.layout.add_widget(self.image)
       # Llamar a la función para cambiar a HomeScreen después de 3 segundos
        self.add_widget(self.layout)
        Clock.schedule_once(self.ir_a_home, 3)

    def ir_a_home(self, dt):
        self.manager.current = 'home'

class HomeScreen(Screen):
    def __init__(self, **kwargs):
        super(HomeScreen, self).__init__(**kwargs)
        layout = BoxLayout(orientation='vertical', padding=50, spacing=10)
        button_register = Button(text='Registrarse', on_press=self.change_to_registro1,
                                 size_hint=(0.8, 0.2), pos_hint={'center_x': 0.5})
        button_login = Button(text='Log In', on_press=self.change_to_login,
                               size_hint=(0.8, 0.2), pos_hint={'center_x': 0.5})
        layout.add_widget(Label(text='Pantalla de inicio'))
        layout.add_widget(button_register)
        layout.add_widget(button_login)
        self.add_widget(layout)

    def change_to_registro1(self, *args):
        app = App.get_running_app()
        screen_manager = app.root
        screen_manager.transition = SlideTransition(direction='left')
        screen_manager.current = 'registro1'

    def change_to_login(self, *args):
        app = App.get_running_app()
        screen_manager = app.root
        screen_manager.transition = SlideTransition(direction='left')
        screen_manager.current = 'login'

class Registro1Screen(Screen):
    def __init__(self, **kwargs):
        super(Registro1Screen, self).__init__(**kwargs)
        layout = BoxLayout(orientation='vertical', padding=(25,50), spacing=10,)

        correo_input = TextInput(hint_text='Correo', size_hint=(None, None), size=(200, 40), multiline=False, pos_hint={'center_x':0.5, 'center_y':0.5})
        contraseña_input = TextInput(hint_text='Contraseña', password=False, size_hint=(None, None),
                                          size=(200, 40), multiline=False, pos_hint={'center_x':0.5, 'center_y':0.5})

        button_layout = BoxLayout(orientation='horizontal', size_hint=(None, None), spacing=40, pos_hint={'center_x':0.5, 'center_y':0.5})
        button_back = Button(text='S', on_press=self.change_to_home,
                             size_hint=(None, 0.5))
        registrar_button = Button(text='I', on_press=self.change_to_registro2,
                                size_hint=(None, 0.5), on_release=self.registrar)

        button_layout.add_widget(button_back)

        button_layout.add_widget(registrar_button)

        layout.add_widget(Label(text='Registro', halign='center'))
        layout.add_widget(correo_input)
        layout.add_widget(contraseña_input)

        layout.add_widget(button_layout)
        self.add_widget(layout)

    def registrar(self, instance):
        correo = self.correo_input.text
        contraseña = self.contraseña_input.text

        c.execute("INSERT INTO usuarios (correo, contraseña) VALUES (?, ?)", (correo, contraseña))
        conn.commit()

        self.correo_input.text = ''
        self.contraseña_input.text = ''
        
    def change_to_home(self, *args):
        app = App.get_running_app()
        screen_manager = app.root
        screen_manager.transition = SlideTransition(direction='right')
        screen_manager.current = 'home'

    def change_to_registro2(self, *args):
        app = App.get_running_app()
        screen_manager = app.root
        screen_manager.transition = SlideTransition(direction='left')
        screen_manager.current = 'registro2'
        
class Registro2Screen(Screen):
    def __init__(self, **kwargs):
        super(Registro2Screen, self).__init__(**kwargs)
        layout = BoxLayout(orientation='vertical', padding=50, spacing=10,)
        
        correo_input = TextInput(hint_text='Correo', size_hint=(None, None), size=(200, 40), multiline=False, pos_hint={'center_x':0.5, 'center_y':0.5})
        contraseña_input = TextInput(hint_text='Contraseña', password=False, size_hint=(None, None),
                                          size=(200, 40), multiline=False, pos_hint={'center_x':0.5, 'center_y':0.5})
        registrar_button = Button(text='Registrarse', size_hint=(None, None), size=(200, 40), on_press=self.change_to_home,	
                                       on_release=self.registrar, pos_hint={'center_x':0.5, 'center_y':0.5})
        button_layout = BoxLayout(orientation='horizontal', size_hint=(None, None), spacing=300)
        button_back = Button(text='Volver a la pantalla de inicio', on_press=self.change_to_home,
                             size_hint=(None, None), size=(200, 50))	
        button_forward = Button(text='Ir a la pantalla de registro 2', on_press=self.change_to_registro2,
                                size_hint=(None, None), size=(200, 50))

        button_layout.add_widget(button_back)
         
        button_layout.add_widget(button_forward)
      
        layout.add_widget(Label(text='Registro', halign='center'))
        layout.add_widget(correo_input)
        layout.add_widget(contraseña_input)
        layout.add_widget(registrar_button)

        layout.add_widget(button_layout)
        self.add_widget(layout)
        
    def registrar(self, instance):
        correo = self.correo_input.text
        contraseña = self.contraseña_input.text

        c.execute("INSERT INTO usuarios (correo, contraseña) VALUES (?, ?)", (correo, contraseña))
        conn.commit()

        self.correo_input.text = ''
        self.contraseña_input.text = ''
        
    def change_to_home(self, *args):
        app = App.get_running_app()
        screen_manager = app.root
        screen_manager.transition = SlideTransition(direction='right')
        screen_manager.current = 'home'

    def change_to_registro2(self, *args):
        app = App.get_running_app()
        screen_manager = app.root
        screen_manager.transition = SlideTransition(direction='left')
        screen_manager.current = 'registro2'


class LoginScreen(Screen):
    def __init__(self, **kwargs):
        super(LoginScreen, self).__init__(**kwargs)
        layout = BoxLayout(orientation='vertical', padding=50, spacing=10)
        button_back = Button(text='Volver a la pantalla de inicio', on_press=self.change_to_home,
                             size_hint=(None, None), size=(200, 50), pos_hint={'center_x': 0.5})
        layout.add_widget(Label(text='Log In'))
        layout.add_widget(button_back)
        self.add_widget(layout)

    def change_to_home(self, *args):
        app = App.get_running_app()
        screen_manager = app.root
        screen_manager.transition = SlideTransition(direction='right')
        screen_manager.current = 'home'

