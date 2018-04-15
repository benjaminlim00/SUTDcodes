from kivy.app import App
from kivy.uix.label import Label
from kivy.uix.textinput import TextInput
from kivy.uix.gridlayout import GridLayout
from kivy.uix.button import Button 

class MyLabel(Label):   #creates a class called MyLabel
    def __init__(self,**kwargs): #explaination??
        Label.__init__(self,**kwargs)
        self.bind(size=self.setter('text_size'))
        self.padding=(20,20)

class Investment(App):
    def build(self):
        layout = GridLayout(cols=2)     #creates a layout with 2 columns
        
        l1 = MyLabel(text="Investment Amount",font_size=24, halign='left', valign='middle')   #creates the label l1 with properties MyLabel
        layout.add_widget(l1)   #add the widget l1 to the layout

        self.txt_inv_amt = TextInput(text="0.0", font_size=24, multiline=False) #why need self?????
        layout.add_widget(self.txt_inv_amt)
        
        l2 = MyLabel(text="Years",font_size=24,halign='left',valign='middle')
        layout.add_widget(l2)
        
        self.txt_years = TextInput(text="0.0", font_size=24, multiline=False)
        layout.add_widget(self.txt_years)
        
        l3 = MyLabel(text="Annual Interest Rate", font_size=24, halign='left', valign='middle')
        layout.add_widget(l3)
        
        self.txt_ann_int_rate = TextInput(text="0.0", font_size=24, multiline=False)
        layout.add_widget(self.txt_ann_int_rate)
        
        l4 = MyLabel(text="Future Investment Value", font_size=24, halign='left', valign='middle')
        layout.add_widget(l4)
        
        self.l5 = MyLabel(text="0.0", font_size=24, halign='left',valign='middle')
        layout.add_widget(self.l5)
        
        btn = Button(text="Calculate", on_press=self.calculate, font_size=24)   #creates the widget called btn
        layout.add_widget(btn)  #add the widget btn to the layout
        return layout 

    def calculate(self, instance):
        inv_amt = float(self.txt_inv_amt.text)
        years = float(self.txt_years.text)
        mth_int_rate = float(self.txt_ann_int_rate.text) / 12.00 / 100
        ret_val = inv_amt * (1 + mth_int_rate)**(12*years)
        self.l5.text = str('%.2f'%ret_val)

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
    Investment().run()