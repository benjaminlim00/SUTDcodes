from kivy.app import App 
from kivy.uix.label import Label  

class AlternateApp(App):
    c = 0
    def build(self):
        self.myLabel = Label(text = 'Programming is fun', font_size = 72)
        self.myLabel.bind(on_touch_down=self.alternate)
        return self.myLabel
    def alternate(self,instance, touch):
        print(self.c)
        if self.c == 0:
            self.myLabel.text = 'It is fun to program'
        else:
            self.myLabel.text = 'Programming is fun'
        self.c = 1 - self.c
        return True
		

def reset():
    import kivy.core.window as window
    from kivy.base import EventLoop
    if not EventLoop.event_listeners:
        from kivy.cache import Cache
        window.Window = window.core_select_lib('window', \
                                               window.window_impl, True)
        Cache.print_usage()
        for cat in Cache._categories:
            Cache._objects[cat] = {}
    
if __name__ == '__main__':
    reset()
    AlternateApp().run()