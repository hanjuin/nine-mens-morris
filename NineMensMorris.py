class NineMenMorris():
    def __init__(self):
        self.board = []
        self.pieces_to_place = {'P1': 9, 'P2': 9}
        self.pieces_on_board = {'P1': 0, 'P2': 0}
        self.current_player = 'P1'
        self.mills = self.define_mills()
        for i in range(0,24):
            self.board.append(i)

    def define_mills(self):
        return [
            [0, 1, 2], [3, 4, 5], [6, 7, 8], [15, 16, 17],
            [18, 19, 20], [21, 22, 23], [0, 9, 21], [3, 10, 18],
            [6, 11, 15], [1, 4, 7], [16, 19, 22], [8, 12, 17],
            [5, 13, 20], [2, 14, 23], [9, 10, 11], [12, 13, 14]
        ]
    
    def is_adjacent(self, a, b):
            adjacent_map = {
                0: [1, 9], 
                1: [0, 2, 4], 
                2: [1, 14], 
                3: [4, 10],
                4: [1, 3, 5, 7], 
                5: [4, 13], 
                6: [7, 11], 
                7: [4, 6, 8],
                8: [7, 12], 
                9: [0, 10, 21], 
                10: [3, 9, 11, 18],
                11: [6, 10, 15], 
                12: [8, 13, 17], 
                13: [5, 12, 14, 20],
                14: [2, 13, 23], 
                15: [11, 16], 
                16: [15, 17, 19],
                17: [12, 16], 
                18: [10, 19], 
                19: [16, 18, 20, 22],
                20: [13, 19], 
                21: [9, 22], 
                22: [19, 21, 23], 
                23: [14, 22]
            }
            return b in adjacent_map.get(a, [])

    def check_mill(self, pos):
        player = self.current_player
        for mill in self.mills:
            if pos in mill:
                if all(self.board[i] == player for i in mill):
                    return True
        return False
            
    def switch_player(self):
        self.current_player = 'P1' if self.current_player == 'P2' else 'P2'

    def print_board(self):
        b = self.board
        def p(i):
            return f"{str(b[i]).rjust(2)}"
        print(p(0) + f"█"*17 + p(1) + f"█"*17 + p(2) + " "*5 + str(self.pieces_to_place))
        print(f"██" + " "*36 + f"██")
        print(f"██" + " "*36 + f"██")
        print(f"██   " + p(3) + f"█"*12 + p(4) + f"█"*12 + p(5) + f"   ██")
        print(f"██" + " "*3 + f"██" + " "*26 + f"██" + " "*3 + f"██")
        print(f"██" + " "*3 + f"██" + " "*26 + f"██" + " "*3 + f"██")
        print(f"██   "*2 + p(6) + f"█"*7 + p(7) + f"█"*7 + p(8) + f"   ██"*2)
        print(f"██   "*3 +" "*10 + f"   ██"*3)
        print(f"██   "*3 +" "*10 + f"   ██"*3)
        print(p(9) + " "*3 + p(10) + " "*3 + p(11) + " "*16  + p(12) + " "*3 + p(13) + " "*3 + p(14))
        print(f"██   "*3 +" "*10 + f"   ██"*3)
        print(f"██   "*3 +" "*10 + f"   ██"*3)
        print(f"██   "*2 + p(15) + f"█"*7 + p(16) + f"█"*7 + p(17) + f"   ██"*2)
        print(f"██" + " "*3 + f"██" + " "*26 + f"██" + " "*3 + f"██")
        print(f"██" + " "*3 + f"██" + " "*26 + f"██" + " "*3 + f"██")
        print(f"██   " + p(18) + f"█"*12 + p(19) + f"█"*12 + p(20) + f"   ██")
        print(f"██" + " "*36 + f"██")
        print(f"██" + " "*36 + f"██")
        print(p(21) + f"█"*17 + p(22) + f"█"*17 + p(23))

    def place_piece(self, pos):
        self.board[pos] = self.current_player
        self.pieces_to_place[self.current_player] -= 1
        self.pieces_on_board[self.current_player] += 1

    def remove_piece(self, pos):
        self.board[pos] = pos  
            
def main():
    game = NineMenMorris()
    while(True):
        x = 0
        x = int(input(f"{game.current_player} turn:"))
        print(game.board[x])
        if (str(game.board[x]) != ("P1" or "P2")):
            game.place_piece(x)
            game.print_board()
        else:
            print(f"{x} position is occupied")
        if game.check_mill(x) == True:
            print("Mill formed")
            x = int(input(f"{game.current_player} choose piece to removed:"))
            game.remove_piece(x)
        else:
            print("No Mill formed")
        game.switch_player()
        
main()
