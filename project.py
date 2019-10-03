# from tkinter import *
#
# root=Tk()
# theLabel=Label(root,text='This is too easy')
# theLabel.pack()
# root.mainloop()

# from kivy.app import App
# from kivy.uix.button import Button
# from kivy.uix.boxlayout import BoxLayout
#
# class MyApp(App):
#     def build(self):
#         return Button(text='this is my first button',
#                       font_size=30,
#                       on_press=self.btn_press,
#                       background_color=[1,0,0,1],
#                       background_normal='')
#
#     def btn_press(self,instance):
#         print('the button is pressed')
#         instance.text='I am pressed'
# if __name__=='__main__':
#     MyApp().run()

from kivy.app import App
from kivy.uix.button import Button
from kivy.uix.boxlayout import BoxLayout
from kivy.uix.gridlayout import GridLayout
from kivy.uix.textinput import TextInput
from kivy.uix.label import Label
from kivy.core.window import Window
import re
import random

towns = []


class Widgets(GridLayout):
    def __init__(self, **kwargs):
        super().__init__(**kwargs)
        self.cols = 1
        Window.size = (1000, 500)
        self.permission = ''
        self.towns = ''
        self.w = TextInput(multiline=False, font_size=50, halign='center')
        self.add_widget(self.w)

        self.l = Label()
        self.add_widget(self.l)

        self.l1 = Label()
        self.add_widget(self.l1)

        self.check = Button(text='Check')
        self.check.bind(on_press=self.check_button)
        self.add_widget(self.check)

    def check_button(self, instance):
        w = self.w.text
        self.towns += str(instance.text)
        self.permission = str(instance.text)
        words = []
        used_words = []
        if self.l.text == '':
            with open('text.txt') as file:
                for line in file:
                    if w in line:
                        self.l.text = w
                        self.l1.text = ''
                        s = w[-1]
                        s1 = s.upper()
                        for line in open('text.txt'):
                            words += [w for w in line.split() if w.startswith(s1)]
                            w1 = random.choice(words)
                            used_words += [w1]
                            print(used_words)
                            self.l.text += '=>'
                            self.l.text += w1
                            self.w.text = ''

                    else:
                        self.l1.text = 'This town does not exist'
        else:
            q = self.l.text
            q1 = q[-1].upper()
            words1 = []
            used_words1 = []
            used_words1 += [w for w in used_words if w.startswith(q1)]
            with open('text.txt') as file:
                for line in file:
                    for line in open('text.txt'):
                        words1 += [w for w in line.split() if w.startswith(q1)]
                    if used_words1 in words1:
                        self.l.text = ''
                        self.l1.text = 'You lose'
                    elif w in used_words:
                        self.l1.text = 'This town has been already used'
                    elif w[0] != q1:
                        self.l1.text = 'The first letter is not correct'
                    elif w in line and w != used_words and w[0] == q1:
                        self.l.text += '=>'
                        self.l.text += w
                        self.l1.text = ''
                        s = w[-1]
                        s1 = s.upper()
                        used_words += [w]
                        for line in open('text.txt'):
                            words += [w for w in line.split() if w.startswith(s1)]
                            w1 = random.choice(words)
                            if w1 == used_words:
                                while w1 == used_words:
                                    try:
                                        w1 = random.choice(words)
                                    except:
                                        self.l.text = ''
                                        self.l1.text = 'You won'
                            used_words += [w1]
                            self.l.text += '=>'
                            self.l.text += w1
                            self.w.text = ''
                    else:
                        self.l1.text = 'This town does not exist'

        #     w2=w1[-1]
        #     w3=w2.upper()
        #     with open('text.txt') as file:
        #         for line in file:
        #             if w in line and w!=used_words and w[0]==w3:
        #                 self.l.text += '=>'
        #                 self.l.text += w
        #                 self.l1.text = ''
        #                 s = w[-1]
        #                 s1 = s.upper()
        #                 used_words += [w]
        #                 for line in open('text.txt'):
        #                     words += [w for w in line.split() if w.startswith(s1)]
        #                     w1 = random.choice(words)
        #                     if w1==used_words:
        #                         while w1==used_words:
        #                             w1 = random.choice(words)
        #                     used_words += [w1]
        #                     self.l.text += '=>'
        #                     self.l.text += w1
        #                     self.w.text = ''
        #             else:
        #                 self.l1.text = 'This town does not exist'


class MyApp(App):
    def build(self):
        return Widgets()


if __name__ == '__main__':
    MyApp().run()
