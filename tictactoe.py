TRACKER = 0

class Game:
    def __init__(self):
        self.board = Board()
        self.winner_marker = None
        self.running = True
        self.winner = None # will be the winner of the game
        #self.mode = None # Options to play: keyboard or mouse
        
        self.player1 = Player('X', 1) # player 1 is x
        self.player2 = Player('O', 2) # player 2 is o
        self._display = False
        
    def console_run(self):
        while self.running:
            # actually I just decided that I will ask the users if they want to play with mouse or keyboard arrows
            self._reset()
            turns = 0
            while not self.winner:
                self.board.print_raw()
                print()
                active_player = self.player1 if turns%2 == 0 else self.player2
                print('Turn: ', active_player)
                
                user_y = int(input('What row would you like to place your marker in?: '))
                user_x = int(input('What spot would you like to place your marker in?: '))
                user_pos = (user_y-1) * 3 + (user_x-1)
                
                while not self.board.place_mark(user_pos, active_player.getsymbol()):
                    #either grey out spots already taken or make that spot turn red when user tries to place there
                    self.board.print_raw()
                    user_y = int(input('What row would you like to place your marker in?: '))
                    user_x = int(input('What spot would you like to place your marker in?: '))
                    user_pos = (user_y-1) * 3 + (user_x-1)
                
                turns += 1
                
                
                if self._check_winner(): #AnnounceWinner
                    self.board.print_raw()
                    print('\nThe winner is', self.winner, '!\n')
                    

                if self._check_tie(turns): #AnnounceTie
                    self.board.print_raw()
                    print('\n IT\'S A TIE\n')
                    self.winner = "TIE"
            play_again = input("Play again? (Y/N)")
            if play_again == 'N':   break
    
    def kivy_run(self):
        self.display()
        while self.running:
            pass
                    
    def is_running(self):
        return self.running              
    
    def _check_winner(self):
        '''check to see which marker will be that of the winner; returns that marker'''
        for index, spot in enumerate(self.board.rawboard):
            if spot != 0:
                if index == 0:
                    if spot == self.board.rawboard[1] and spot == self.board.rawboard[2]: self.winner_marker = self.board.rawboard[0]
                    elif spot == self.board.rawboard[4] and spot == self.board.rawboard[8]: self.winner_marker = self.board.rawboard[0]
                    elif spot == self.board.rawboard[3] and spot == self.board.rawboard[6]: self.winner_marker = self.board.rawboard[0]
                elif index == 1:
                    if spot == self.board.rawboard[4] and spot == self.board.rawboard[7]: self.winner_marker = self.board.rawboard[1]
                elif index == 2:
                    if spot == self.board.rawboard[4] and spot == self.board.rawboard[6]: self.winner_marker = self.board.rawboard[2]
                    elif spot == self.board.rawboard[5] and spot == self.board.rawboard[8]: self.winner_marker = self.board.rawboard[2]
                elif index == 3:
                    if spot == self.board.rawboard[4] and spot == self.board.rawboard[5]: self.winner_marker = self.board.rawboard[3]
                elif index == 6:
                    if spot == self.board.rawboard[7] and spot == self.board.rawboard[8]: self.winner_marker = self.board.rawboard[6]
        return self._is_winner()
    
    def _is_winner(self):
        if self.winner_marker == self.player1.getsymbol():
            self.winner = self.player1
            return True
        elif self.winner_marker == self.player2.getsymbol():
            self.winner = self.player2
            return True
        return False
    
    def _check_tie(self, turns):
        if turns == 9:  return True
        return False
    
    def _reset(self):
        if not self.display:
            print('NEW GAME\n')
        self.board.reset()
        self.winner = None
    
    def display(self):
        self._display = True
                        
        
class Player:
    def __init__(self, symbol, num):
        self._symbol= symbol
        self.player_num = num
    
    def getsymbol(self):
        return self._symbol
    
    def __str__(self):
        return 'Player ' + str(self.player_num)

        
class Board:
    def __init__(self):
        self.rawboard = [0,0,0,0,0,0,0,0,0]
    
    def print_raw(self):
        '''will print board onto the console'''
        print()
        def new_line_and_inc_j(j):
            j[0] += 1
            return '\n'
        i = 1
        j = [1]
        for spot in self.rawboard:
            print (j[0] if i%3 == 1 else '', end='   ' if i%3 == 1 else '')
            print('*' if spot == 0 else spot, end=(new_line_and_inc_j(j) if (i%3 == 0) else '  '))
            i += 1
        print('\n  ',1,2,3, sep='  ')
            
    
    def display(self):
        '''Will display the board on the screen with pygame'''
        
    
    def place_mark(self, user_pos, symbol):
        '''position will be a tuple that has the row and column where the program will place the symbol
           x(left to right) and y(top to bottom); also returns whether spot is taken or not before placing'''
        while True:
            try:
                if self.rawboard[user_pos] == 0:
                    self.rawboard[user_pos] = symbol
                    return True
                else:   
                    print('That spot is already taken :(\n')
                    return False
            except IndexError:
                print('Invalid position :(\n')
                return False
    
    def reset(self):
        self.rawboard = [0,0,0,0,0,0,0,0,0]
        

if __name__ == '__main__':
    Game().console_run()
        