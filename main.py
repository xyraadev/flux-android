<<<<<<< HEAD
# main.py - упрощенная версия для первого APK
import socket
import threading
from kivy.app import App
from kivy.uix.boxlayout import BoxLayout
from kivy.uix.scrollview import ScrollView
from kivy.uix.label import Label
from kivy.uix.textinput import TextInput
from kivy.uix.button import Button
from kivy.core.window import Window
from kivy.clock import Clock

class SimpleMobileClient(BoxLayout):
    def __init__(self, **kwargs):
        super().__init__(**kwargs)
        self.orientation = 'vertical'
        self.padding = 10
        self.spacing = 10
        
        # Настройки сервера (ЗАМЕНИ НА СВОЙ IP!)
        self.server_host = '192.168.1.XXX'  # ТВОЙ IP АДРЕС
        self.server_port = 5555
        self.client_socket = None
        self.connected = False
        
        self.create_ui()
        self.connect_to_server()
    
    def create_ui(self):
        # Заголовок
        title = Label(
            text='FLUX Mobile 📱',
            size_hint=(1, 0.1),
            font_size='20sp',
            bold=True
        )
        self.add_widget(title)
        
        # Статус подключения
        self.status_label = Label(
            text='Подключаемся...',
            size_hint=(1, 0.05),
            font_size='14sp'
        )
        self.add_widget(self.status_label)
        
        # Поле чата с прокруткой
        scroll = ScrollView(size_hint=(1, 0.6))
        self.chat_history = Label(
            text='Чат:\n',
            size_hint_y=None,
            text_size=(Window.width - 20, None),
            markup=True
        )
        self.chat_history.bind(texture_size=self.chat_history.setter('size'))
        scroll.add_widget(self.chat_history)
        self.add_widget(scroll)
        
        # Поле ввода сообщения
        self.message_input = TextInput(
            hint_text='Введите сообщение...',
            size_hint=(1, 0.1),
            multiline=False
        )
        self.message_input.bind(on_text_validate=self.send_message)
        self.add_widget(self.message_input)
        
        # Кнопка отправки
        send_btn = Button(
            text='Отправить сообщение',
            size_hint=(1, 0.1),
            background_color=(0.2, 0.6, 1, 1)
        )
        send_btn.bind(on_press=self.send_message)
        self.add_widget(send_btn)
    
    def connect_to_server(self):
        """Подключение к серверу в отдельном потоке"""
        def connect_thread():
            try:
                self.client_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
                self.client_socket.connect((self.server_host, self.server_port))
                self.connected = True
                
                Clock.schedule_once(lambda dt: self.update_status('[color=00FF00]✅ Подключено![/color]'))
                Clock.schedule_once(lambda dt: self.update_chat('Подключен к серверу!\n'))
                
                # Запускаем прием сообщений
                receive_thread = threading.Thread(target=self.receive_messages)
                receive_thread.daemon = True
                receive_thread.start()
                
            except Exception as e:
                error_msg = f'[color=FF0000]❌ Ошибка: {str(e)}[/color]'
                Clock.schedule_once(lambda dt: self.update_status(error_msg))
                Clock.schedule_once(lambda dt: self.update_chat(f'Не удалось подключиться: {str(e)}\n'))
        
        thread = threading.Thread(target=connect_thread)
        thread.daemon = True
        thread.start()
    
    def send_message(self, instance):
        """Отправка сообщения"""
        if not self.connected:
            self.update_chat('Сначала подключитесь к серверу!\n')
            return
            
        message = self.message_input.text.strip()
        if message:
            try:
                # Простая отправка текста
                self.client_socket.send(message.encode('utf-8'))
                self.update_chat(f'[color=0000FF]Я:[/color] {message}\n')
                self.message_input.text = ''
            except Exception as e:
                self.update_chat(f'[color=FF0000]Ошибка отправки: {str(e)}[/color]\n')
                self.connected = False
    
    def receive_messages(self):
        """Получение сообщений от сервера"""
        while self.connected:
            try:
                message = self.client_socket.recv(1024).decode('utf-8')
                if message:
                    Clock.schedule_once(lambda dt: self.update_chat(f'[color=00AA00]Сервер:[/color] {message}\n'))
            except:
                Clock.schedule_once(lambda dt: self.update_status('[color=FF0000]❌ Отключен от сервера[/color]'))
                self.connected = False
                break
    
    def update_status(self, new_text):
        """Обновление статуса"""
        self.status_label.text = new_text
    
    def update_chat(self, new_text):
        """Обновление чата"""
        self.chat_history.text += new_text

class FluxMobileApp(App):
    def build(self):
        self.title = 'FLUX Mobile'
        return SimpleMobileClient()

if __name__ == '__main__':
=======
# main.py - упрощенная версия для первого APK
import socket
import threading
from kivy.app import App
from kivy.uix.boxlayout import BoxLayout
from kivy.uix.scrollview import ScrollView
from kivy.uix.label import Label
from kivy.uix.textinput import TextInput
from kivy.uix.button import Button
from kivy.core.window import Window
from kivy.clock import Clock

class SimpleMobileClient(BoxLayout):
    def __init__(self, **kwargs):
        super().__init__(**kwargs)
        self.orientation = 'vertical'
        self.padding = 10
        self.spacing = 10
        
        # Настройки сервера (ЗАМЕНИ НА СВОЙ IP!)
        self.server_host = '192.168.1.XXX'  # ТВОЙ IP АДРЕС
        self.server_port = 5555
        self.client_socket = None
        self.connected = False
        
        self.create_ui()
        self.connect_to_server()
    
    def create_ui(self):
        # Заголовок
        title = Label(
            text='FLUX Mobile 📱',
            size_hint=(1, 0.1),
            font_size='20sp',
            bold=True
        )
        self.add_widget(title)
        
        # Статус подключения
        self.status_label = Label(
            text='Подключаемся...',
            size_hint=(1, 0.05),
            font_size='14sp'
        )
        self.add_widget(self.status_label)
        
        # Поле чата с прокруткой
        scroll = ScrollView(size_hint=(1, 0.6))
        self.chat_history = Label(
            text='Чат:\n',
            size_hint_y=None,
            text_size=(Window.width - 20, None),
            markup=True
        )
        self.chat_history.bind(texture_size=self.chat_history.setter('size'))
        scroll.add_widget(self.chat_history)
        self.add_widget(scroll)
        
        # Поле ввода сообщения
        self.message_input = TextInput(
            hint_text='Введите сообщение...',
            size_hint=(1, 0.1),
            multiline=False
        )
        self.message_input.bind(on_text_validate=self.send_message)
        self.add_widget(self.message_input)
        
        # Кнопка отправки
        send_btn = Button(
            text='Отправить сообщение',
            size_hint=(1, 0.1),
            background_color=(0.2, 0.6, 1, 1)
        )
        send_btn.bind(on_press=self.send_message)
        self.add_widget(send_btn)
    
    def connect_to_server(self):
        """Подключение к серверу в отдельном потоке"""
        def connect_thread():
            try:
                self.client_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
                self.client_socket.connect((self.server_host, self.server_port))
                self.connected = True
                
                Clock.schedule_once(lambda dt: self.update_status('[color=00FF00]✅ Подключено![/color]'))
                Clock.schedule_once(lambda dt: self.update_chat('Подключен к серверу!\n'))
                
                # Запускаем прием сообщений
                receive_thread = threading.Thread(target=self.receive_messages)
                receive_thread.daemon = True
                receive_thread.start()
                
            except Exception as e:
                error_msg = f'[color=FF0000]❌ Ошибка: {str(e)}[/color]'
                Clock.schedule_once(lambda dt: self.update_status(error_msg))
                Clock.schedule_once(lambda dt: self.update_chat(f'Не удалось подключиться: {str(e)}\n'))
        
        thread = threading.Thread(target=connect_thread)
        thread.daemon = True
        thread.start()
    
    def send_message(self, instance):
        """Отправка сообщения"""
        if not self.connected:
            self.update_chat('Сначала подключитесь к серверу!\n')
            return
            
        message = self.message_input.text.strip()
        if message:
            try:
                # Простая отправка текста
                self.client_socket.send(message.encode('utf-8'))
                self.update_chat(f'[color=0000FF]Я:[/color] {message}\n')
                self.message_input.text = ''
            except Exception as e:
                self.update_chat(f'[color=FF0000]Ошибка отправки: {str(e)}[/color]\n')
                self.connected = False
    
    def receive_messages(self):
        """Получение сообщений от сервера"""
        while self.connected:
            try:
                message = self.client_socket.recv(1024).decode('utf-8')
                if message:
                    Clock.schedule_once(lambda dt: self.update_chat(f'[color=00AA00]Сервер:[/color] {message}\n'))
            except:
                Clock.schedule_once(lambda dt: self.update_status('[color=FF0000]❌ Отключен от сервера[/color]'))
                self.connected = False
                break
    
    def update_status(self, new_text):
        """Обновление статуса"""
        self.status_label.text = new_text
    
    def update_chat(self, new_text):
        """Обновление чата"""
        self.chat_history.text += new_text

class FluxMobileApp(App):
    def build(self):
        self.title = 'FLUX Mobile'
        return SimpleMobileClient()

if __name__ == '__main__':
>>>>>>> a008b8df93bcf1c0d554764ed418ce90d94723a9
    FluxMobileApp().run()