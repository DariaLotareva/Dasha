import json
from kivy.app import App
from kivy.uix.button import Button
from kivy.uix.gridlayout import GridLayout
from kivy.uix.label import Label
from kivy.uix.scrollview import ScrollView
from kivy.uix.textinput import TextInput
from kivy.core.window import Window
import random


# with open("text.txt", "rt") as file:
#     towns = file.read().split()
#     towns = {town.replace("-", "").replace("'", "").lower(): town for town in towns}
# with open("text.txt", "wt") as file:
#     json.dump(towns, file, indent=4)


class Widgets(GridLayout):
    def __init__(self):
        super().__init__(cols=1)
        # Window.size = (1000, 500)
        self.input = TextInput(multiline=False, font_size=50, halign='center')
        self.add_widget(self.input)

        self.town_label = Label()
        self.add_widget(self.town_label)

        self.error_label = Label()
        self.add_widget(self.error_label)

        self.check = Button(text='Check')
        self.check.bind(on_press=self.check_button)
        self.add_widget(self.check)

        self.restart = Button(text='Restart')
        self.restart.bind(on_press=self.start)
        self.add_widget(self.restart)

        with open('text.txt') as file:
            self.towns = json.load(file)

        self.used_towns = set()
        self.start()

    def start(self, instance=None):
        self.used_towns = set()
        self.town_label.text = ""

    def check_button(self, instance):
        town = self.input.text.replace("-", "").replace("'", "").lower()

        if town in self.used_towns:
            self.error_label.text = 'This town has been already used'
        elif town not in self.towns:
            self.error_label.text = 'This town does not exist'
        else:
            self.computer_step(town)

    def computer_step(self, town):
        self.used_towns.add(town)
        self.town_label.text += f"User: {self.towns[town]}\n"
        towns = [t for t in self.towns if t.startswith(town[-1])]
        town = random.choice(towns)
        self.town_label.text += f'Computer: {self.towns[town]}\n'
        self.input.text = ''


class MyApp(App):
    def build(self):
        return Widgets()


if __name__ == '__main__':
    MyApp().run()
