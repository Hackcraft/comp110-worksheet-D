class OxoBoard:
    """
        Number representations:
            0 -> Empty
            1 -> O
            2 -> X

        board -> Playable positions
        board_width, board_height -> Board size
        strike_combinations -> Each position for strike
    """
    board = {}

    board_width = 3
    board_height = 3

    strike_combinations = [
        [(0, 0), (1, 0), (2, 0)],
        [(0, 1), (1, 1), (2, 1)],
        [(0, 2), (1, 2), (2, 2)],

        [(0, 0), (0, 1), (0, 2)],
        [(1, 0), (1, 1), (1, 2)],
        [(2, 0), (2, 1), (2, 2)],

        [(0, 0), (1, 1), (2, 2)],
        [(0, 2), (1, 1), (0, 2)],
    ]

    def __init__(self, width = None, height = None, strikes = None):
        # Allow the board to be edited on creation
        self.board_width = width or self.board_width
        self.board_height = height or self.board_height
        self.strike_combinations = strikes or self.strike_combinations

        # Move counter
        self.total_moves = self.board_width * self.board_height
        self.current_moves = 0

        #Generate an empty board
        for x in xrange(self.board_width):
            for y in xrange(self.board_height):
                self.board[x, y] = 0

    def get_square(self, x, y):
        """ Return 0, 1 or 2 depending on the contents of the specified square. """
        return self.board[x, y]

    def set_square(self, x, y, mark):
        """ If the specified square is currently empty (0), fill it with mark and return True.
            If the square is not empty, leave it as-is and return False. """
        if self.board[x, y] == 0:
            self.board[x, y] = mark
            self.total_moves += 1
            return True
        else:
            return False

    def is_board_full(self):
        """ If there are still empty squares on the board, return False.
            If there are no empty squares, return True. """
        return self.current_moves >= self.total_moves

    def get_winner(self):
        """ If a player has three in a row, return 1 or 2 depending on which player.
            Otherwise, return 0. """
        for line in self.strike_combinations: # For each strike combination
            # Assign variables for player 1 and 2 to track how many positions they have for each strike combination
            o_strike = 0
            x_strike = 0
            # How many correct positions required in the current strike check to get a strike
            parts_for_strike = len(line)

            # For each position for strike line
            for element in xrange(parts_for_strike):
                x, y = line[element][0], line[element][1] # Get x and y from the current strike combination check
                if self.board[x, y] == 1: # If O is there
                    o_strike += 1 # Three is a strike
                elif self.board[x, y] == 2: # If X is there
                    x_strike += 1 # Three is a strike

            # If all positions are satisfied then we have a strike
            if o_strike >= parts_for_strike:
                return 1
            elif x_strike >= parts_for_strike:
                return 2

        return 0

    def show(self):
        """ Display the current board state in the terminal. You should not need to edit this. """
        for y in xrange(self.board_height):
            if y > 0:
                print "--+---+--"
            for x in xrange(self.board_width):
                if x > 0:
                    print '|',

                # Print a space for empty (0), an O for player 1, or an X for player 2
                print " OX"[self.get_square(x, y)],
            print
