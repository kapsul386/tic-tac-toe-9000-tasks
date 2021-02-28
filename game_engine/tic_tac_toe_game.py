from copy import deepcopy
from typing import Callable, List, Optional
from tic_tac_toe_common_lib import TicTacToeTurn, TicTacToeGameInfo, AbstractTicTacToeGame


class TicTacToeGame(AbstractTicTacToeGame):
    def __init__(self,game_id,first_player_id,second_player_id):
        self._player_id = first_player_id
        self.TicTacToeGameInfo = TicTacToeGameInfo(
            game_id=game_id,
            field=[
                [" ", " ", " "],
                [" ", " ", " "],
                [" ", " ", " "]
            ],
            sequence_of_turns=[],
            first_player_id=first_player_id,
            second_player_id=second_player_id,
            winner_id=""
        )

    def is_turn_correct(self, TicTacToeTurn):
        X = TicTacToeTurn.x_coordinate
        Y = TicTacToeTurn.y_coordinate

        if self.TicTacToeGameInfo.winner_id != "":
            return False

        if self._player_id == TicTacToeTurn.player_id:
            return False

        if not (X >= 0 and X < 3) and (Y >= 0 and Y < 3):
            return False

        if self.TicTacToeGameInfo.field[X][Y] != " ":
            return False

    def do_turn(self, TicTacToeTurn):
        X = TicTacToeTurn.x_coordinate
        Y = TicTacToeTurn.y_coordinate

        if self.is_turn_correct(TicTacToeTurn):
            if TicTacToeTurn.player_id == self.TicTacToeGameInfo.first_player_id:
                self.TicTacToeGameInfo.field[X][Y] = "X"
                self._player_id = self.TicTacToeGameInfo.second_player_id

            elif TicTacToeTurn.player_id == self.TicTacToeGameInfo.second_player_id:
                self.TicTacToeGameInfo.field[X][Y] = "O"
                self._player_id = self.TicTacToeGameInfo.first_player_id

            self.TicTacToeGameInfo.sequence_of_turns.append(TicTacToeTurn)

            self.Winners()

            return self.TicTacToeGameInfo
        else:
            return self.TicTacToeGameInfo

    def get_game_info(self):
        return deepcopy(self.TicTacToeGameInfo)

    def AreThereWinners(self):
        for elem in self.TicTacToeGameInfo.field:
            if elem == ["X", "X", "X"]:
                self.TicTacToeGameInfo.winner_id = self.TicTacToeGameInfo.first_player_id
            elif elem == ["O", "O", "O"]:
                self.TicTacToeGameInfo.winner_id = self.TicTacToeGameInfo.second_player_id