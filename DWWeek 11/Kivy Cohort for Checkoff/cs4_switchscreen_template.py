### PSET 11 ###
#Cohort
"""
Q4
"""
from kivy.uix.screenmanager import ScreenManager, Screen
from kivy.lang import Builder
from kivy.uix.boxlayout import BoxLayout
from kivy.uix.button import Button
from kivy.uix.label import Label
from kivy.app import App

class MenuScreen(Screen):
    def __init__(self, **kwargs):
        super().__init__(**kwargs)
        self.layout=BoxLayout()
        # Add your code below to add the two Buttons
        button1 = Button(text = 'Settings', on_press = self.change_to_setting, font_size = 24)
        self.layout.add_widget(button1)
        button2 = Button(text = 'Quit', on_press = self.quit_app, font_size = 24)
        self.layout.add_widget(button2)

        self.add_widget(self.layout)

    def change_to_setting(self, value):
        self.manager.transition.direction = 'left'
        # modify the current screen to a different "name"
        self.manager.current = 'settings'

    def quit_app(self, value):
        App.get_running_app().stop()


class SettingsScreen(Screen):
    def __init__(self, **kwargs):
        super().__init__( **kwargs)
        self.layout=BoxLayout()
        # Add your code below to add the label and the button
        button3 = Button(text = 'Settings Screen', font_size = 24)
        self.layout.add_widget(button3)
        button4 = Button(text = 'Return to Menu', on_press = self.change_to_menu, font_size = 24)
        self.layout.add_widget(button4)

        self.add_widget(self.layout)

    def change_to_menu(self,value):
        self.manager.transition.direction = 'right'
        # modify the current screen to a different "name"
        self.manager.current = "menu"


class SwitchScreenApp(App):
	def build(self):
            sm=ScreenManager()
            ms=MenuScreen(name='menu')
            st=SettingsScreen(name='settings')
            sm.add_widget(ms)
            sm.add_widget(st)
            sm.current='menu'
            return sm

def reset():
    import kivy.core.window as window
    from kivy.base import EventLoop
    if not EventLoop.event_listeners:
        from kivy.cache import Cache
        window.Window = window.core_select_lib('window', window.window_impl, True)
        Cache.print_usage()
        for cat in Cache._categories:
            Cache._objects[cat] = {}
reset()

if __name__=='__main__':
	SwitchScreenApp().run()
