import kivy
from kivy.app import App
from kivy.uix.boxlayout import BoxLayout
from kivy.uix.label import Label
from kivy.uix.button import Button
from kivy.uix.textinput import TextInput
from kivy.uix.image import Image
from kivy.uix.relativelayout import RelativeLayout
from kivy.clock import Clock
from datetime import datetime, timedelta
import threading
import winsound  # Only works on Windows; replace with an appropriate sound library for other OS

class AlarmClockApp(App):
    def build(self):
        self.title = 'Alarm Clock'
        self.alarm_time = None
        self.is_alarm_set = False

        # Main layout to hold background image and content
        layout = RelativeLayout()

        # Add dark background image
        background = Image(source='th.jfif', allow_stretch=True, keep_ratio=False)
        layout.add_widget(background)

        # BoxLayout for UI elements with larger size
        ui_layout = BoxLayout(orientation='vertical', padding=20, spacing=20, size_hint=(None, None), width=400, height=400)
        ui_layout.pos_hint = {'center_x': 0.5, 'center_y': 0.5}

        self.title_label = Label(text='Alarm Clock', font_size='40sp', size_hint_y=None, height=60, color=(1,1,1,1))
        ui_layout.add_widget(self.title_label)

        self.time_input = TextInput(hint_text='Set Alarm Time (HH:MM:SS)', font_size='27sp', size_hint_y=None, height=60)
        ui_layout.add_widget(self.time_input)

        self.set_button = Button(text='Set Alarm', font_size='28sp', size_hint_y=None, height=60)
        self.set_button.bind(on_press=self.set_alarm)
        ui_layout.add_widget(self.set_button)

        self.status_label = Label(text='', font_size='22sp', size_hint_y=None, height=60, color=(1,1,1,1))
        ui_layout.add_widget(self.status_label)

        self.snooze_button = Button(text='Snooze', font_size='28sp', size_hint_y=None, height=60,background_color=(1, 1, 1, 2))
        self.snooze_button.bind(on_press=self.snooze_alarm)
        self.snooze_button.disabled = True
        ui_layout.add_widget(self.snooze_button)

        layout.add_widget(ui_layout)

        # Thread to check the alarm time
        self.check_alarm_thread = threading.Thread(target=self.check_alarm)
        self.check_alarm_thread.start()

        return layout

    def set_alarm(self, instance):
        alarm_time_input = self.time_input.text
        try:
            self.alarm_time = datetime.strptime(alarm_time_input, "%H:%M:%S").time()
            self.is_alarm_set = True
            self.status_label.text = f"Alarm set for {self.alarm_time}."
            self.time_input.text = ''
            self.snooze_button.disabled = False
        except ValueError:
            self.status_label.text = "Invalid time format! Use HH:MM:SS."

    def check_alarm(self):
        while True:
            if self.is_alarm_set:
                current_time = datetime.now().time()
                if current_time >= self.alarm_time:
                    self.trigger_alarm()
                    break
            threading.Event().wait(1)

    def trigger_alarm(self):
        self.is_alarm_set = False
        self.status_label.text = "Alarm ringing! Time to wake up!"
        self.snooze_button.disabled = False
        self.play_alarm_sound()

    def play_alarm_sound(self):
        duration = 10000  # milliseconds
        frequency = 440  # Hz
        winsound.Beep(frequency, duration)  # Use a different method on non-Windows systems

    def snooze_alarm(self, instance):
        snooze_time = timedelta(minutes=5)
        self.alarm_time = (datetime.combine(datetime.today(), self.alarm_time) + snooze_time).time()
        self.status_label.text = f"Snooze set for 5 minutes. New alarm time: {self.alarm_time}."
        self.snooze_button.disabled = True

if __name__ == '__main__':
    AlarmClockApp().run()
