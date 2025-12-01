import random
import os
import time
import sys

class SimpleSudoku:
    def _init_(self):
        self.board = [[0]*9 for _ in range(9)]
        self.original = [[0]*9 for _ in range(9)]
        self.current_pos = [0, 0]
        
    def generate_puzzle(self, difficulty='easy'):
        self.solve_empty_board()
        
        cells_to_remove = {'easy': 30, 'medium': 40, 'hard': 50}
        remove_count = cells_to_remove.get(difficulty, 30)
        cells = [(i, j) for i in range(9) for j in range(9)]
        random.shuffle(cells)
        
        for i in range(remove_count):
            row, col = cells[i]
            self.board[row][col] = 0
            
        self.original = [row[:] for row in self.board]
    
    def solve_empty_board(self):
        self.board = [[0]*9 for _ in range(9)]
        for i in range(0, 9, 3):
            numbers = list(range(1, 10))
            random.shuffle(numbers)
            for j in range(3):
                for k in range(3):
                    self.board[i + j][i + k] = numbers.pop()
        self._solve_backtrack()
    
    def _solve_backtrack(self):
        empty = self._find_empty()
        if not empty:
            return True
        row, col = empty
        for num in range(1, 10):
            if self._is_valid(row, col, num):
                self.board[row][col] = num
                if self._solve_backtrack():
                    return True
                self.board[row][col] = 0
        return False
    
    def _find_empty(self):
        for i in range(9):
            for j in range(9):
                if self.board[i][j] == 0:
                    return (i, j)
        return None
    
    def _is_valid(self, row, col, num):
        # Check row
        if num in self.board[row]:
            return False
        # Check column
        for i in range(9):
            if self.board[i][col] == num:
                return False
        # Check 3x3 box
        box_row = row // 3 * 3
        box_col = col // 3 * 3
        for i in range(3):
            for j in range(3):
                if self.board[box_row + i][box_col + j] == num:
                    return False
        return True

def print_board(game):
    os.system('cls' if os.name == 'nt' else 'clear')
    print("\n" + "="*40)
    print("SUDOKU GAME".center(40))
    print("="*40)
    print("\n    1 2 3   4 5 6   7 8 9")
    print("  " + "+" + "-"*21 + "+")
    
    for i in range(9):
        if i % 3 == 0 and i != 0:
            print("  " + "+" + "-"*7 + "+" + "-"*7 + "+" + "-"*7 + "+")
        
        row_str = f"{i+1} |"
        for j in range(9):
            if j % 3 == 0 and j != 0:
                row_str += " |"
            
            if game.current_pos == [i, j]:
                row_str += "[" + (str(game.board[i][j]) if game.board[i][j] != 0 else " ") + "]"
            else:
                row_str += " " + (str(game.board[i][j]) if game.board[i][j] != 0 else " ") + " "
        
        row_str += " |"
        print(row_str)
    
    print("  " + "+" + "-"*21 + "+")
    print("\nControls: WASD to move, 1-9 to input, 0 to clear, Q to quit")
    print("="*40)

def main_simple():
    game = SimpleSudoku()
    game.generate_puzzle('easy')
    
    while True:
        print_board(game)
        
        print(f"\nCurrent position: ({game.current_pos[0]+1}, {game.current_pos[1]+1})")
        print(f"Current value: {game.board[game.current_pos[0]][game.current_pos[1]] or 'Empty'}")
        
        cmd = input("\nEnter command (WASD/1-9/0/Q): ").upper()
        
        if cmd == 'Q':
            print("Thanks for playing!")
            break
        elif cmd == 'W':
            game.current_pos[0] = max(0, game.current_pos[0] - 1)
        elif cmd == 'S':
            game.current_pos[0] = min(8, game.current_pos[0] + 1)
        elif cmd == 'A':
            game.current_pos[1] = max(0, game.current_pos[1] - 1)
        elif cmd == 'D':
            game.current_pos[1] = min(8, game.current_pos[1] + 1)
        elif cmd in '123456789':
            num = int(cmd)
            if game.original[game.current_pos[0]][game.current_pos[1]] == 0:
                game.board[game.current_pos[0]][game.current_pos[1]] = num
        elif cmd == '0':
            if game.original[game.current_pos[0]][game.current_pos[1]] == 0:
                game.board[game.current_pos[0]][game.current_pos[1]] = 0

if __name__ == "_main_":
    # Pilih versi yang diinginkan
    # main()  # Versi dengan dependencies
    main_simple()  # Versi sederhana tanpa dependencies