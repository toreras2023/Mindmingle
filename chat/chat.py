from kivy.app import App
from kivy.uix.boxlayout import BoxLayout
from kivy.uix.button import Button
from kivy.uix.label import Label
from kivy.uix.textinput import TextInput


class ChatScreen(BoxLayout):
    def __init__(self, **kwargs):
        super(ChatScreen, self).__init__(**kwargs)
        self.orientation = 'vertical'

        # Título
        title_label = Label(text='Chat de preguntas', size_hint=(1, 0.1))
        self.add_widget(title_label)

        # Globo de diálogo
        self.dialog_label = Label(text='', size_hint=(1, 0.6))
        self.add_widget(self.dialog_label)

        # Casilla de entrada y botón de enviar
        input_layout = BoxLayout(size_hint=(1, 0.1))
        self.input_text = TextInput(hint_text='Haz una pregunta', multiline=False,
                                    size_hint=(0.8, 1))
        send_button = Button(text='Enviar', size_hint=(0.2, 1))
        send_button.bind(on_press=self.send_question)
        input_layout.add_widget(self.input_text)
        input_layout.add_widget(send_button)
        self.add_widget(input_layout)

        # Botones de cambio de interfaz
        button_layout = BoxLayout(size_hint=(1, 0.2))
        button1 = Button(text='Interfaz 1', size_hint=(0.25, 1))
        button2 = Button(text='Interfaz 2', size_hint=(0.25, 1))
        button3 = Button(text='Interfaz 3', size_hint=(0.25, 1))
        button4 = Button(text='Interfaz 4', size_hint=(0.25, 1))
        button_layout.add_widget(button1)
        button_layout.add_widget(button2)
        button_layout.add_widget(button3)
        button_layout.add_widget(button4)
        self.add_widget(button_layout)

        # Asociar eventos a los botones
        button1.bind(on_press=self.change_to_interface1)
        button2.bind(on_press=self.change_to_interface2)
        button3.bind(on_press=self.change_to_interface3)
        button4.bind(on_press=self.change_to_interface4)

    def change_to_interface1(self, instance):
        # Lógica para cambiar a interfaz 1
        print('Cambiando a interfaz 1')

    def change_to_interface2(self, instance):
        # Lógica para cambiar a interfaz 2
        print('Cambiando a interfaz 2')

    def change_to_interface3(self, instance):
        # Lógica para cambiar a interfaz 3
        print('Cambiando a interfaz 3')

    def change_to_interface4(self, instance):
        # Lógica para cambiar a interfaz 4
        print('Cambiando a interfaz 4')

    def send_question(self, instance):
        question = self.input_text.text
        self.input_text.text = ''
        self.dialog_label.text += f'\n[Pregunta]: {question}'

    def on_enter(self):
        self.input_text.focus = True


class MyApp(App):
    def build(self):
        return ChatScreen()

if __name__ == '__main__':
    MyApp().run()
