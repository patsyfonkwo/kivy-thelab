
from kivy.app import App
from kivy.uix.widget import Widget
from kivy.uix.boxlayout import BoxLayout
from kivy.uix.button import Button
from kivy.uix.label import Label
from kivy.uix.anchorlayout import AnchorLayout

class AnchorLayoutExample(AnchorLayout):
    pass

class BoxLayoutExample(BoxLayout):
    # pass
    def __init__(self, **kwargs):
        super().__init__(**kwargs)
        self.orientation = 'horizontal'
        b1 = Button(text = "A")
        b2 = BoxLayout()
        b2.spacing = "10dp"
        b2.orientation = "vertical"
        b2.add_widget(Button(text="hey", background_color = (1,1,1,1), color = (0,0,0,1)))
        b2.add_widget(Button(text="yer"))
        b2.add_widget(Button(text = "good things come in threes"))
        self.add_widget(b1)
        self.add_widget(b2)
        l1 = Label(text = "UR MOM")
        self.add_widget(l1)

class MainWidget(Widget):
    pass

class TheLabApp(App):
    pass
    # def build(self):
    #     return BoxLayoutExample()

TheLabApp().run()