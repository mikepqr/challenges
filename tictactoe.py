from __future__ import print_function
PLAYERS = ['X', 'O']
STALEMATE = 1


class TicTacToe(object):

    def __init__(self):
        self.board = self._create_board()
        self.next_player = PLAYERS[0]
        self.winner = None

    def _create_board(self):
        return dict(zip(range(1, 10), range(1, 10)))

    def is_finished(self):
        lines = ((1, 2, 3), (4, 5, 6), (7, 8, 9),
                 (1, 4, 7), (2, 5, 8), (3, 6, 9),
                 (1, 5, 9), (3, 5, 7))

        # Check for winner
        for line in lines:
            tiles = [self.board[i] for i in line]
            if all(tile == tiles[0] for tile in tiles):
                self.winner = tiles[0]
                return True

        # Check for stalemate
        if all(v in PLAYERS for v in self.board.values()):
            self.winner = STALEMATE
            return True

        return False

    def add_move(self):
        move = self.get_move()
        self.board[move] = self.next_player
        self.next_player = (PLAYERS[0] if self.next_player == PLAYERS[1]
                            else PLAYERS[1])

    def _check_move(self, move):
        try:
            move = int(move)
            assert type(move) is int
            assert 1 <= move <= 9
            assert self.board[move] not in PLAYERS
            return True
        except:
            return False

    def get_move(self):
        print('Your move, {}'.format(self.next_player))
        print(self)
        move = None
        while not self._check_move(move):
            move = raw_input('Enter move: ')
        return int(move)

    def __repr__(self):
        s = ''
        for k, v in self.board.items():
            s += ' {} '.format(v)
            if k % 3 == 0 and k != 9:
                s += '\n'
        return s


def main():
    game = TicTacToe()

    while not game.is_finished():
        game.add_move()

    if game.winner != STALEMATE:
        print('Winner: {}'.format(game.winner))
    else:
        print('Game ended in stalemate')

    print(game)


if __name__ == '__main__':
    main()
