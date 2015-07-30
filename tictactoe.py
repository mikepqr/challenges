#!/usr/bin/env python
# -*- coding: utf-8 -*-
from __future__ import print_function
import itertools
import random
PLAYERS = ['❌', '😎']
TIE = 1


class Blackjack(object):
    '''
    TODO:
     - handle ties (equal scores, all bust)
     - cards should be a deck with state
     - handle situation when hand is five cards
     - test with > 2 players
    '''
    CARD_NAME = ['Ace', 'Two', 'Three', 'Four', 'Five', 'Six', 'Seven',
                 'Eight', 'Nine', 'Ten', 'Jack', 'Queen', 'King']
    CARD_VALUE = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 10, 10, 10]
    LIMIT = 21

    def __init__(self):
        self.hands = dict([(p, []) for p in PLAYERS])
        self.player_order = iter(PLAYERS)
        self.current_player = self.player_order.next()
        self.winner = None

    def _player_total(self, player=None):
        if not player:
            player = self.current_player
        return sum([v for n, v in self.hands[player]])

    def _player_hand_as_string(self, player=None):
        if not player:
            player = self.current_player
        return ' '.join([str(v) for n, v in self.hands[player]])

    def _determine_winner(self):
        best_hand = 0
        for p in self.hands:
            if best_hand < self._player_total(player=p) <= Blackjack.LIMIT:
                self.winner = p
                best_hand = self._player_total(player=p)

    def _player_busts(self):
        if self._player_total() >= Blackjack.LIMIT:
            print('{} busts.'.format(self.current_player))
            return True
        else:
            return False

    def turn(self):
        while not self._player_busts() and self._get_decision():
            self.hands[self.current_player].append(self._get_card())
            print(self._player_hand_as_string())
            print('= {}'.format(self._player_total()))

        try:
            self.current_player = self.player_order.next()
            return False
        except:
            self._determine_winner()
            return True

    def _get_card(self):
        card_id = random.choice(range(1, 13))
        card = (Blackjack.CARD_NAME[card_id], Blackjack.CARD_VALUE[card_id])
        return card

    def _get_decision(self):
        print('Your move, {}'.format(self.current_player))
        if raw_input('Another card?'):
            return True
        else:
            print('{} sticks on {}.'.format(self.current_player,
                                            self._player_total()))
            return False

    def __repr__(self):
        s = ''
        for p in self.hands:
            s += p
            s += ' '
            s += self._player_hand_as_string(p)
            s += '\n'

        return s


class TicTacToe(object):
    '''
    Tic tac toe class. To play, create an instance and repeatedly call its
    turn() method until it returns True, indicating the game is finished. The
    instance's winner attribute is then the winner. Print the instance at any
    time to render the current board.
    '''

    def __init__(self):
        self.board = self._create_board()
        self.player_order = itertools.cycle(PLAYERS)
        self.current_player = self.player_order.next()
        self.winner = None

    def _create_board(self):
        '''
        Board is represented as a dictionary with keys 1..9. Values are
        initially 1..9, but are changed to 'X' or 'O' by turn() as moves are
        made.
        '''
        return dict(zip(range(1, 10), range(1, 10)))

    def _is_finished(self):
        '''
        Returns True if game finished (by victory or stalemate), False
        otherwise.
        '''
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
            self.winner = TIE
            return True

        return False

    def turn(self):
        '''
        Gets and plays turn. Returns True if game is finished, False otherwise.
        '''
        move = self._get_move()
        self.board[move] = self.current_player
        self.current_player = self.player_order.next()
        return self._is_finished()

    def _check_move(self, move):
        '''
        Checks if input is an integer from 1..9, and that that location on
        board is empty.
        '''
        try:
            move = int(move)
            assert type(move) is int
            assert 1 <= move <= 9
            assert self.board[move] == move  # i.e. location is empty
            return True
        except:
            return False

    def _get_move(self):
        print('Your move, {}'.format(self.current_player))
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


def main(game=TicTacToe()):
    '''
    Plays a game that implements the following API (tic tac toe by default):

     - a turn() method that takes a turn, and returns True if the game is
       finished.
     - a winner attribute that contains the string value of the winner.

    Ideally game should implement __repr__ so print(game) returns something
    sensible.
    '''

    while not game.turn():
        pass

    if game.winner != TIE:
        print('Winner: {}'.format(game.winner))
    else:
        print('Game ended in tie')

    print(game)


if __name__ == '__main__':
    main()
