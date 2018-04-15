from kivy.app import App
from kivy.uix.button import Button

class TestApp(App):
    def build(self):
        self.myButton = Button(text = 'hello', font_size = 36, color = (0,1,0,1))
        return self.myButton
    
    
    
    
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
    TestApp().run()
    

#reset()
#TestApp().run()
#reset()
#TestApp().run()
#reset()
#TestApp().run()