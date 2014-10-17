def board(input_board):
    return Board(input_board).printout()

class Board:
    def __init__(self, input_board):
        self.rows = input_board

    def printout(self):
        return self._print_hints()
        return ["+------+", "|1*22*1|", "|12*322|", "| 123*2|", "|112*4*|",
               "|1*22*2|", "|111111|", "+------+"]

    def _print_hints(self):
        for i, row in enumerate(self.rows):
            for j, space in enumerate(row):
                count = self._count_contacts(i, j)
                self.rows[i][j] = count
        return self.rows

    def _count_contacts(self, row_num, space_num):
        count = 0
        neighbors = [self.rows[row_num][space_num - 1], self.rows[row_num][space_num + 1]]
        for space in neighbors:
            if self._is_mined(space):
                count += 1
        final_count = count or self.rows[row_num][space_num]
        return final_count

    def _is_mined(self, string):
        if string is '*':
            return True

