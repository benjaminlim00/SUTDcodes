from kivy.app import App 
from kivy.uix.gridlayout import GridLayout 
from kivy.uix.label import Label 
from kivy.uix.togglebutton import ToggleButton
from firebase import firebase

url = 'https://helloworld-8cf45.firebaseio.com/' # URL to Firebase database
token = 'YW3EBnf50kQ3dAbhsoeaIMy0poFDKe3R1TP6BWAm' # unique token used for authentication


firebase=firebase.FirebaseApplication(url,token)

class GuiKivy(App):
    
    def build(self):
        ls = firebase.get('/state_list')
        if ls != None:
            l2text = ls[0]
            l4text = ls[1]
            
        else:
            l2text = 'off'
            l4text = 'on'
            
        
        if l2text == 'on':
            l2state = 'down'
        else:
            l2state = 'normal'
            
        if l4text == 'on':
            l4state = 'down'
        else:
            l4state = 'normal'
            
        
        
        layout = GridLayout(cols=2)
        # add your widget to the layout
        l1=Label(text='Green LED')
        self.l2=ToggleButton(text=l2text)
        self.l2.state = l2state
        self.l2.bind(on_press=self.text_change1)
        
        l3=Label(text='Red LED')
        self.l4=ToggleButton(text=l4text)
        self.l4.state = l4state
        self.l4.bind(on_press=self.text_change2)
        
        
        layout.add_widget(l1)
        layout.add_widget(self.l2)
        layout.add_widget(l3)
        layout.add_widget(self.l4)
        

        return layout


    def text_change1(self, instance):
        
        greenstate = 'off'
        redstate = 'off'
        
        if self.l2.state == 'down':
            print('green state is down')
            self.l2.text = 'on'
        else:
            print('green state is normal')
            self.l2.text = 'off'
            

        ls = []
    
        if self.l2.text == 'on':
            greenstate = 'on'
            
        else:
            greenstate = 'off'
            
   
        # use this callback to update firebase

        if self.l4.text == 'on':
            redstate = 'on'
        else:
            redstate = 'off'
        ls.append(greenstate)
        ls.append(redstate)
        firebase.put('/', 'state_list', ls) # put the -- into node pie'''
        print("yay")
        return None
        
    def text_change2(self, instance):    
        greenstate = 'off'
        redstate = 'off'    
        if self.l4.state == 'down':
            print('red state is down')
            self.l4.text = 'on'
        else:
            print('red state is normal')
            self.l4.text = 'off'
            
            
        ls = []
     
        if self.l2.text == 'on':
            greenstate = 'on'
            
        else:
            greenstate = 'off'
            
   
        # use this callback to update firebase
       
        if self.l4.text == 'on':
            redstate = 'on'
        else:
            redstate = 'off'
        ls.append(greenstate)
        ls.append(redstate)
        print(ls)
        firebase.put('/', 'state_list', ls) # put the -- into node pie'''
        print("yay")
        return None
        
    
   

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
    GuiKivy().run()

