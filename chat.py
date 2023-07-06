from kivy.app import App
from kivy.uix.boxlayout import BoxLayout
from kivy.uix.button import Button
from kivy.uix.label import Label
from kivy.uix.textinput import TextInput
from kivy.uix.screenmanager import ScreenManager, Screen, SlideTransition
from kivy.clock import Clock

class ChatScreen(Screen):
    def __init__(self, **kwargs):
        super(ChatScreen, self).__init__(**kwargs)
        layout = BoxLayout(orientation='vertical')

        # Título
        title_label = Label(text='Chat de preguntas', size_hint=(1, 0.1))
        layout.add_widget(title_label)

        # Globo de diálogo
        self.dialog_label = Label(text='', size_hint=(1, 0.6))
        layout.add_widget(self.dialog_label)

        # Casilla de entrada y botón de enviar
        input_layout = BoxLayout(size_hint=(1, 0.1))
        self.input_text = TextInput(hint_text='Haz una pregunta', multiline=False, size_hint=(0.8, 1))
        send_button = Button(text='Enviar', size_hint=(0.2, 1))
        send_button.bind(on_press=self.send_question)
        input_layout.add_widget(self.input_text)
        input_layout.add_widget(send_button)
        layout.add_widget(input_layout)

        # Botones de cambio de interfaz
        button_layout = BoxLayout(size_hint=(1, 0.2), spacing=0.5)
        button1 = Button(text='Interfaz 1', size_hint=(0.25, 1))
        button2 = Button(text='Interfaz 2', size_hint=(0.25, 1))
        button3 = Button(text='Interfaz 3', size_hint=(0.25, 1))
        button4 = Button(text='Interfaz 4', size_hint=(0.25, 1))
        button_layout.add_widget(button1)
        button_layout.add_widget(button2)
        button_layout.add_widget(button3)
        button_layout.add_widget(button4)
        layout.add_widget(button_layout)

        # Asociar eventos a los botones
        button1.bind(on_press=self.change_to_interface1)
        button2.bind(on_press=self.change_to_interface2)
        button3.bind(on_press=self.change_to_interface3)
        button4.bind(on_press=self.change_to_interface4)

        self.add_widget(layout)

    def change_to_interface1(self, instance):
        # Lógica para cambiar a interfaz 1 con una transición deslizante hacia la derecha en 0.2 segundos
        app = App.get_running_app()
        app.root.transition = SlideTransition(direction='right', duration=0.2)
        app.root.current = 'chat'

    def change_to_interface2(self, instance):
        # Lógica para cambiar a interfaz 2 después de 0.2 segundos
        Clock.schedule_once(lambda dt: self.switch_screen('interface2'), 0.2)

    def change_to_interface3(self, instance):
        # Lógica para cambiar a interfaz 3 después de 0.2 segundos
        Clock.schedule_once(lambda dt: self.switch_screen('interface3'), 0.2)

    def change_to_interface4(self, instance):
        # Lógica para cambiar a interfaz 4 después de 0.2 segundos
        Clock.schedule_once(lambda dt: self.switch_screen('interface4'), 0.2)

    def switch_screen(self, screen_name):
        app = App.get_running_app()
        app.root.current = screen_name

    def send_question(self, instance):
        question = self.input_text.text
        self.input_text.text = ''
        self.dialog_label.text += f'\n[Pregunta]: {question}'

    def on_enter(self):
        self.input_text.focus = True


class Interface2Screen(Screen):
    def __init__(self, **kwargs):
        super(Interface2Screen, self).__init__(**kwargs)
        layout = BoxLayout(orientation='vertical')

        # Buscador
        search_layout = BoxLayout(size_hint=(1, 0.1))
        search_input = TextInput(hint_text='Buscar', multiline=False, size_hint=(0.7, 1))
        send_button = Button(text='Enviar', size_hint=(0.3, 1))
        search_layout.add_widget(search_input)
        search_layout.add_widget(send_button)
        layout.add_widget(search_layout)

        # Espacio para mostrar resultados de búsqueda
        search_results_label = Label(text='Resultados de búsqueda', size_hint=(1, 0.4))
        layout.add_widget(search_results_label)

        # Botones de cambio de interfaz
        button_layout = BoxLayout(size_hint=(1, 0.2), spacing=0.5)
        button1 = Button(text='Interfaz 1', size_hint=(0.25, 1))
        button2 = Button(text='Interfaz 2', size_hint=(0.25, 1))
        button3 = Button(text='Interfaz 3', size_hint=(0.25, 1))
        button4 = Button(text='Interfaz 4', size_hint=(0.25, 1))
        button_layout.add_widget(button1)
        button_layout.add_widget(button2)
        button_layout.add_widget(button3)
        button_layout.add_widget(button4)
        layout.add_widget(button_layout)

        # Asociar eventos a los botones
        button1.bind(on_press=self.change_to_interface1)
        button2.bind(on_press=self.change_to_interface2)
        button3.bind(on_press=self.change_to_interface3)
        button4.bind(on_press=self.change_to_interface4)

        self.add_widget(layout)

    def change_to_interface1(self, instance):
        # Lógica para cambiar a interfaz 1 después de 0.2 segundos
        Clock.schedule_once(lambda dt: self.switch_screen('chat'), 0.2)

    def change_to_interface2(self, instance):
        # Lógica para cambiar a interfaz 2 después de 0.2 segundos
        Clock.schedule_once(lambda dt: self.switch_screen('interface2'), 0.2)

    def change_to_interface3(self, instance):
        # Lógica para cambiar a interfaz 3 después de 0.2 segundos
        Clock.schedule_once(lambda dt: self.switch_screen('interface3'), 0.2)

    def change_to_interface4(self, instance):
        # Lógica para cambiar a interfaz 4 después de 0.2 segundos
        Clock.schedule_once(lambda dt: self.switch_screen('interface4'), 0.2)

    def switch_screen(self, screen_name):
        app = App.get_running_app()
        app.root.current = screen_name


class Interface3Screen(Screen):
    def __init__(self, **kwargs):
        super(Interface3Screen, self).__init__(**kwargs)
        layout = BoxLayout(orientation='vertical')

        # Conversación
        conversation_layout = BoxLayout(size_hint=(1, 0.6))
        self.conversation_label = Label(text='', size_hint=(1, 1))
        conversation_layout.add_widget(self.conversation_label)
        layout.add_widget(conversation_layout)

        # Casilla de entrada y botón de enviar
        input_layout = BoxLayout(size_hint=(1, 0.1))
        self.input_text = TextInput(hint_text='Escribe un mensaje', multiline=False, size_hint=(0.8, 1))
        send_button = Button(text='Enviar', size_hint=(0.2, 1))
        send_button.bind(on_press=self.send_message)
        input_layout.add_widget(self.input_text)
        input_layout.add_widget(send_button)
        layout.add_widget(input_layout)

        # Botones de cambio de interfaz
        button_layout = BoxLayout(size_hint=(1, 0.2), spacing=0.5)
        button1 = Button(text='Interfaz 1', size_hint=(0.25, 1))
        button2 = Button(text='Interfaz 2', size_hint=(0.25, 1))
        button3 = Button(text='Interfaz 3', size_hint=(0.25, 1))
        button4 = Button(text='Interfaz 4', size_hint=(0.25, 1))
        button_layout.add_widget(button1)
        button_layout.add_widget(button2)
        button_layout.add_widget(button3)
        button_layout.add_widget(button4)
        layout.add_widget(button_layout)

        # Asociar eventos a los botones
        button1.bind(on_press=self.change_to_interface1)
        button2.bind(on_press=self.change_to_interface2)
        button3.bind(on_press=self.change_to_interface3)
        button4.bind(on_press=self.change_to_interface4)

        self.add_widget(layout)

    def change_to_interface1(self, instance):
        # Lógica para cambiar a interfaz 1 después de 0.2 segundos
        Clock.schedule_once(lambda dt: self.switch_screen('chat'), 0.2)

    def change_to_interface2(self, instance):
        # Lógica para cambiar a interfaz 2 después de 0.2 segundos
        Clock.schedule_once(lambda dt: self.switch_screen('interface2'), 0.2)

    def change_to_interface3(self, instance):
        # Lógica para cambiar a interfaz 3 después de 0.2 segundos
        Clock.schedule_once(lambda dt: self.switch_screen('interface3'), 0.2)

    def change_to_interface4(self, instance):
        # Lógica para cambiar a interfaz 4 después de 0.2 segundos
        Clock.schedule_once(lambda dt: self.switch_screen('interface4'), 0.2)

    def switch_screen(self, screen_name):
        app = App.get_running_app()
        app.root.current = screen_name

    def send_message(self, instance):
        message = self.input_text.text
        self.input_text.text = ''
        self.conversation_label.text += f'\n[Tú]: {message}'

    def on_enter(self):
        self.input_text.focus = True


class Interface4Screen(Screen):
    def __init__(self, **kwargs):
        super(Interface4Screen, self).__init__(**kwargs)
        layout = BoxLayout(orientation='vertical')

        # Etiqueta de datos personales
        data_label = Label(text='Datos personales', size_hint=(1, 0.1))
        layout.add_widget(data_label)

        # Casilla de imagen
        image_layout = BoxLayout(size_hint=(1, 0.1))
        image_label = Label(text='Imagen:', size_hint=(0.35, 1))
        image_input = TextInput(hint_text='URL de la imagen', multiline=False, size_hint=(0.65, 1))
        image_layout.add_widget(image_label)
        image_layout.add_widget(image_input)
        layout.add_widget(image_layout)

        # Casilla de nombre y apellido
        name_layout = BoxLayout(size_hint=(1, 0.1))
        name_label = Label(text='Nombre y apellido:', size_hint=(0.35, 1))
        name_input = TextInput(hint_text='Escribe tu nombre y apellido', multiline=False, size_hint=(0.65, 1))
        name_layout.add_widget(name_label)
        name_layout.add_widget(name_input)
        layout.add_widget(name_layout)

        # Casilla de fecha de nacimiento
        dob_layout = BoxLayout(size_hint=(1, 0.1))
        dob_label = Label(text='Fecha de nacimiento:', size_hint=(0.35, 1))
        dob_input = TextInput(hint_text='dd/mm/yyyy', multiline=False, size_hint=(0.65, 1))
        dob_layout.add_widget(dob_label)
        dob_layout.add_widget(dob_input)
        layout.add_widget(dob_layout)

        # Casilla de usuario
        username_layout = BoxLayout(size_hint=(1, 0.1))
        username_label = Label(text='Usuario:', size_hint=(0.35, 1))
        username_input = TextInput(hint_text='Escribe tu usuario', multiline=False, size_hint=(0.65, 1))
        username_layout.add_widget(username_label)
        username_layout.add_widget(username_input)
        layout.add_widget(username_layout)

        # Casilla de correo electrónico
        email_layout = BoxLayout(size_hint=(1, 0.1))
        email_label = Label(text='Correo electrónico:', size_hint=(0.35, 1))
        email_input = TextInput(hint_text='Escribe tu correo electrónico', multiline=False, size_hint=(0.65, 1))
        email_layout.add_widget(email_label)
        email_layout.add_widget(email_input)
        layout.add_widget(email_layout)

        # Botones de cambio de interfaz
        button_layout = BoxLayout(size_hint=(1, 0.2), spacing=0.5)
        button1 = Button(text='Interfaz 1', size_hint=(0.25, 1))
        button2 = Button(text='Interfaz 2', size_hint=(0.25, 1))
        button3 = Button(text='Interfaz 3', size_hint=(0.25, 1))
        button4 = Button(text='Interfaz 4', size_hint=(0.25, 1))
        button_layout.add_widget(button1)
        button_layout.add_widget(button2)
        button_layout.add_widget(button3)
        button_layout.add_widget(button4)
        layout.add_widget(button_layout)

        # Asociar eventos a los botones
        button1.bind(on_press=self.change_to_interface1)
        button2.bind(on_press=self.change_to_interface2)
        button3.bind(on_press=self.change_to_interface3)
        button4.bind(on_press=self.change_to_interface4)

        self.add_widget(layout)

    def change_to_interface1(self, instance):
        # Lógica para cambiar a interfaz 1 después de 0.2 segundos
        Clock.schedule_once(lambda dt: self.switch_screen('chat'), 0.2)

    def change_to_interface2(self, instance):
        # Lógica para cambiar a interfaz 2 después de 0.2 segundos
        Clock.schedule_once(lambda dt: self.switch_screen('interface2'), 0.2)

    def change_to_interface3(self, instance):
        # Lógica para cambiar a interfaz 3 después de 0.2 segundos
        Clock.schedule_once(lambda dt: self.switch_screen('interface3'), 0.2)

    def change_to_interface4(self, instance):
        # Lógica para cambiar a interfaz 4 después de 0.2 segundos
        Clock.schedule_once(lambda dt: self.switch_screen('interface4'), 0.2)

    def switch_screen(self, screen_name):
        app = App.get_running_app()
        app.root.current = screen_name


class MyScreenManager(ScreenManager):
    pass


class MyApp(App):
    def build(self):
        sm = MyScreenManager()
        sm.add_widget(ChatScreen(name='chat'))
        sm.add_widget(Interface2Screen(name='interface2'))
        sm.add_widget(Interface3Screen(name='interface3'))
        sm.add_widget(Interface4Screen(name='interface4'))
        return sm


if __name__ == '__main__':
    MyApp().run()
