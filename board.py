
class TicTacToeBoard:
   def __init__(self):
       #self.board = [['-' for i in range(3)] for i in range(3)]
       self.board = [['-', '-', '-'],
                       ['-', '-', '-'],
                       ['-', '-', '-']]
  
   def get(self, row: int, col: int) -> str:
       return self.board[row][col]
  
   def is_empty(self, row: int, col: int) -> bool:
       return self.board[row][col] == '-'
  
   def place(self, marker: str, row: int, col: int) -> bool:
       if marker in ['X', 'O'] and self.is_empty(row, col):
           self.board[row][col] = marker
           return True
       return False
  
   def is_full(self) -> bool:
       for row in self.board:
           if '-' in row:
               return False
       return True
  
   def is_winner(self, marker: str) -> bool:
       # Kolla rader
       for row in self.board:
           if all(cell == marker for cell in row):
               return True
      
       # Kolla kolumner
       for col in range(3):
           if all(self.board[row][col] == marker for row in range(3)):
               return True
      
       # Kolla diagonaler
       if all(self.board[i][i] == marker for i in range(3)):
           return True
       if all(self.board[i][2 - i] == marker for i in range(3)):
           return True
      
       return False
  
   def restart(self) -> None:
       self.board = [['-' for i in range(3)] for i in range(3)]
  
   def print_board(self) -> None:
       for row in self.board:
           print(" ".join(row))
           
