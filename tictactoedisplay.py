import time
from kivy.app import App
from tictactoe import Game
from kivy.uix.button import Button
from kivy.uix.label import Label
from kivy.uix.gridlayout import GridLayout
from kivy.uix.boxlayout import BoxLayout
from kivy.core.window import Window
from kivy.graphics import Line,Color
from kivy.uix.widget import Widget
from kivy.config import Config
from kivy.event import EventDispatcher
import tictactoe

class BoardBackground(Widget):
    def __init__(self, **kwargs):
        super(BoardBackground, self).__init__(**kwargs)
        self.add_widget(Widget())
        self.add_widget(BoardDisplay())

class BoardPiece(Button):
    def __init__(self):
        '''Import all attributes from Button class to board piece'''
        Button.__init__(self, text = '', font_size = 40, background_color = (1,1,1,.15))

    def on_touch_down(self, touch):
        '''Handle event of clicking on a button'''
        super(BoardPiece, self).on_touch_down(touch)
        if self.collide_point(*touch.pos):
            self.text = "X" if tictactoe.TRACKER%2==0 else "O"
            tictactoe.TRACKER += 1
            self.color = (1,0,0,1)
        '''make a game tracker on backend that can be used to keep track of games and turns'''

    def on_touch_up(self, touch):
        '''Handle event of clicking on a button'''
        super(BoardPiece, self).on_touch_up(touch)
        if self.collide_point(*touch.pos):
            print(tictactoe.TRACKER)
            self.color = (1,0,0,0.5)
        '''make a game tracker on backend that can be used to keep track of games and turns'''

class BoardDisplay(GridLayout, tictactoe.Board):
    def __init__(self, **kwargs):
        GridLayout.__init__(self, **kwargs)
        self.spots = [BoardPiece(), BoardPiece(), BoardPiece(),
                      BoardPiece(), BoardPiece(), BoardPiece(),
                      BoardPiece(), BoardPiece(), BoardPiece()]
        self.rows, self.cols = 3,3
        self.size_hint = (9/7,1)

        for spot in self.spots:
            self.add_widget(spot)
        self.pos_hint = {'center_x': .5}
        self.spacing = 2

        def place_mark(self, pressed_button):
            '''update matrix in backend'''
            user_pos = self.spots.index(pressed_button)
            #Update the raw board in tictactoe backend
            tictactoe.Board.place_mark(BoardDisplay, user_pos, pressed_button.symbol)

        

    
        

# class ButtonSection(BoxLayout):
#     def __init__(self, **kwargs):
#         super(ButtonSection, self).__init__(**kwargs)
#         self.orientation = 'vertical'
#         self.Restart = Button(text = "Restart", background_color = (0,0,0,1), color = (1,1,1,1), pos_hint = {'center_x': .5})
#         self.NewGame = Button(text = "New Game", background_color = (0,0,0,1), color = (1,1,1,1), pos_hint = {'center_x': .5})
#         self.add_widget(self.Restart)
#         self.add_widget(self.NewGame)
#         self.pos_hint = {'center_x': .5}

class BoardSection(BoxLayout):
    def __init__(self, **kwargs):
        super(BoardSection, self).__init__(**kwargs)
        self.orientation = 'vertical'
        
        self.title = Label(size_hint = (9/7,1/3), text = "TIC TAC TOE", pos_hint = {"center_x": 0.5}, color = (0,0,0,1), font_size = 30)
        self.board = BoardDisplay(size_hint = (9/7,1), pos_hint = {'center_x': .5})
        
        self.add_widget(self.title)
        self.add_widget(self.board)
        self.add_widget(Label(size_hint = (9/7,1/3), pos_hint = {"center_x": 0.5}, text = "O'S TURN", color = (1,0,0,1), font_size = 20))

class PlayerSection(BoxLayout):
    def __init__(self, player: str, my_turn: bool, justified: str, **kwargs):
        super().__init__(**kwargs)
        self.orientation = "vertical"
        self.label = Label(text = player, color = (0,0,0,.5) if not my_turn else (1,0,0,.5), font_size = 150) #player label
        self.score = 0
        self.score_label = Label(size_hint = (6/7, 1/3), text = str(self.score), color = (0,0,0,1), font_size = 30)
        self.score_label.pos_hint = {'x': 0 if justified == 'left' else 1/7}
        
        self._is_player_turn = my_turn
        # self.turn_display = Label(text = 'YOUR MOVE' if my_turn else '', color = (1,0,0,1))
        
        self.label.pos_hint = {'x': 0 if justified == 'left' else 1/7}
        self.label.size_hint = 6/7, 1
        # self.turn_display.size_hint = 6/7, 1/3
        # self.turn_display.pos_hint = {'x': 0 if justified == 'left' else 1/7}

        self.add_widget(self.score_label)
        self.add_widget(self.label)
        # self.add_widget(self.turn_display)
        self.add_widget(Label(size_hint = (6/7, 1/3)))
        
    def inc_score(self):
        self.score += 1
    
    def my_turn(self):
        # self.turn_display = Label(text = 'YOUR MOVE')
        # self.turn_display.text = 'YOUR MOVE'
        self.label.color = (1,0,0,.7)
        self._is_player_turn = True
        print(self.label.text)

    def not_my_turn(self):
        # self.turn_display = Label(text = '')
        # self.turn_display.text = ''
        self.label.color = (0,0,0,.2)
        self._is_player_turn = False

class OverallLayout(BoxLayout):
    def __init__(self, **kwargs):
        super().__init__(**kwargs)
        board_section = BoardSection(size_hint = (1,1))

        player1_display = PlayerSection("X", False, 'left')
        player2_display = PlayerSection("O", False, 'right')
        #!!!!need to tie these to events of buttons being clicked!!!!
        if tictactoe.TRACKER%2== 0:
            player1_display.my_turn()
            player2_display.not_my_turn()
        else:
            player2_display.my_turn()
            player1_display.not_my_turn()
        
        

        self.add_widget(player1_display)
        self.add_widget(board_section)
        self.add_widget(player2_display)
        




class GameApp(App, Game):
    def build(self):
        Window.clearcolor = (1, 1, 1, 1)
        Config.set('graphics', 'width', '1000')
        return OverallLayout()

if __name__ == '__main__':
    game = GameApp()
    game.run()