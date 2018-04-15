from kivy.app import App
from kivy.uix.label import Label 

class SlideDetectApp(App):
    def build(self):
        self.lblTouch = Label(text="Slide Me", font_size=72, \
                              on_touch_move=self.detect)
        return self.lblTouch

    def detect(self, instance, touch):
        if not instance.collide_point(touch.x, touch.y): #instance.collide_point??, touch.x/y and touch.dx/dy
            return False
        if touch.dx<-40:
            self.lblTouch.text="Slide Left"
        if touch.dx>40:
            self.lblTouch.text="Slide Right"
        if touch.dy<-40:
            self.lblTouch.text="Slide Down"
        if touch.dy>40:
            self.lblTouch.text="Slide Up"
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
            
if __name__=='__main__':
    reset()
    SlideDetectApp().run()