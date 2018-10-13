from mshackman_bot.constants import MoveType
from mshackman_bot.field import Field
from mshackman_bot.pathfinding import a_star_search, heuristic_distance


class Bot:
    def __init__(self):
        self.data = {}
        self.field = None
        self.my_bot_id = None
        self.round = 0
        self._current_goal = None
        self._current_path = None

    def settings(self, args):
        """
        args - list(str). Command split by spaces

        Saves all settings to self.data
        self.players - dict(Player.name : Player)
        Also link to your player in self.me
        """
        self.data[args[0]] = args[1]
        if args[0] == "your_botid":
            self.my_bot_id = args[1]

        elif args[0] == "field_height":
            self.field = Field(int(self.data["field_width"]),
                               int(self.data['field_height']))

    def update(self, args):
        """
        args - list(str). Command split by spaces
        """
        if args[0] == "game":
            if args[1] == "field":
                '''
                update game field [c,…]
                CellType c (String)
                The current field, each coordinate separated by commas, from 
                top left to bottom right
                '''
                self.field.update(args[2])
            else:
                '''
                update game round i
                Number i (Integer)
                The current round (step).
                '''
                self.round = int(args[2])

    def action(self, args):
        """
        args - list(str). Command split by spaces
        """
        if args[0] == "move":
            '''
            action move t
            Time t (Integer)
            Request for a direction to move. Should be answered within 
            t milliseconds.
            '''
            # On each turn locate nearest code snippet and move to it
            my_pos = self.field.get_cell_at_xy(*self.field.get_player_position(self.my_bot_id))
            nearest_snippets = sorted(self.field.code_snippets, key=lambda x: heuristic_distance(my_pos, self.field.get_cell_at_xy(*x)))
            if nearest_snippets:
                nearest_snippet = nearest_snippets[0]
                if nearest_snippet != self._current_goal:
                    self._current_goal = nearest_snippet
                    self._current_path = a_star_search(self.field, my_pos, self.field.get_cell_at_xy(*nearest_snippet))
                if self._current_path:
                    next_move = self._current_path.pop(0)
                    print(next_move[1].value)
                else:
                    print(MoveType.PASS.value)
            else:
                # TODO: Maybe do something more smart then just standing still when there are no snippets available
                print(MoveType.PASS.value)
        else:
            '''
            action character t
            Time t (Integer)
            Request for which character your bot would like to play as, only 
            asked at the start of the game. Should be answered within 
            t milliseconds.
            '''
            print("bixiette")

    def run(self):

        while 1:
            line = input()
            if len(line) == 0:
                continue
            parts = line.split(" ")
            controller = {
                "settings": self.settings,
                "update": self.update,
                "action": self.action
            }
            controller[parts[0]](parts[1:])
