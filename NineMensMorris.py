class NineMenMorris():
    def __init__(self):
        self.board = []
        self.pieces_to_place = {'P1': 9, 'P2': 9}
        self.pieces_on_board = {'P1': 0, 'P2': 0}
        self.current_player = 'P1'
        for i in range(0,24):
            self.board.append(i)

    def switch_player(self):
        self.current_player = 'P1' if self.current_player == 'P2' else 'P2'

    def print_board(self):
        b = self.board
        def p(i):
            return f"{str(b[i]).rjust(2)}"
        print(p(0) + f"█"*17 + p(1) + f"█"*17 + p(2))
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

        
    #def place_piece(self, pos):
        #self.board[pos] = 
def main():
    game = NineMenMorris();
    game.print_board()

main()
