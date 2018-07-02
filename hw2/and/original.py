
#-------------------------------------------------------------------------
# TacTical
# This program is designed to play Tac-Tical, using lookahead and board heuristics.
# It will allow the user to play a game against the machine, or allow the machine
# to play against itself for purposes of learning to improve its play.  All 'learning'
# code has been removed from this program.  
#
# Tac-Tical is a 2-player game played on a grid.  Each player has the same number 
# of tokens distributed on the grid in an initial configuration.  On each turn, a player 
# may move one of his/her tokens one unit either horizontally or vertically (not 
# diagonally) into an unoccupied square.  The object is to be the first player to get 
# three tokens in a row, either horizontally, vertically, or diagonally. 
#
# The board is represented by a matrix with extra rows and columns forming a 
# boundary to the playing grid.  Squares in the playing grid can be occupied by 
# either 'X', 'O', or 'Empty' spaces.  The extra elements are filled with 'Out of Bounds'
# squares, which makes some of the computations simpler.  
#-------------------------------------------------------------------------

from __future__ import print_function
import random
from random import randrange


def GetMoves (Player, Board): 
#-------------------------------------------------------------------------
# Determines all legal moves for Player with current Board, 
# and returns them in MoveList.  
#-------------------------------------------------------------------------

	MoveList = []
	for i in range(1,NumRows+1):
		for j in range(1,NumCols+1):
			if Board[i][j] == Player:
			#-------------------------------------------------------------
			#  Check move directions (m,n) = (-1,0), (0,-1), (0,1), (1,0)  
			#-------------------------------------------------------------
				for m in range(-1,2):
					for n in range(-1,2):
						if abs(m) != abs(n):
							if Board[i + m][j + n] == Empty:
								MoveList.append([i, j, i+m, j+n])

	return MoveList


def GetHumanMove (Player, Board):  
#-------------------------------------------------------------------------
# If the opponent is a human, the user is prompted to input a legal move.  
# Determine the set of all legal moves, then check input move against it. 
#-------------------------------------------------------------------------
	MoveList = GetMoves(Player, Board)
	Move = None

	while(True):
		FromRow, FromCol, ToRow, ToCol = map(int, \
			input('Input your move (FromRow, FromCol, ToRow, ToCol): ').split(' '))

		ValidMove = False
		if not ValidMove:
			for move in MoveList:
				if move == [FromRow, FromCol, ToRow, ToCol]:
					ValidMove = True
					Move = move

		if ValidMove:
			break

		print('Invalid move.  ')

	return Move


def ApplyMove (Board, Move): 
#-------------------------------------------------------------------------
# Perform the given move, and update Board. 
#-------------------------------------------------------------------------

	FromRow, FromCol, ToRow, ToCol = Move
	Board[ToRow][ToCol] = Board[FromRow][FromCol]
	Board[FromRow][FromCol] = Empty
	return Board


def InitBoard (Board):  
#-------------------------------------------------------------------------
# Initialize the game board. 
#-------------------------------------------------------------------------

	for i in range(0,BoardRows+1):
		for j in range(0,BoardCols+1):
			Board[i][j] = OutOfBounds
 
	for i in range(1,NumRows+1):
		for j in range(1,NumCols+1):
			Board[i][j] = Empty

	for j in range(1,NumCols+1):
		if odd(j):
			Board[1][j] = x
			Board[NumRows][j] = o
		else:
			Board[1][j] = o
			Board[NumRows][j] = x
 

def odd(n):  
	return n%2==1

def ShowBoard (Board):  
	print("")
	row_divider = "+" + "-"*(NumCols*4-1) + "+"
	print(row_divider)

	for i in range(1,NumRows+1):
		for j in range(1,NumCols+1):
			if Board[i][j] == x:
				print('| X ',end="")
			elif Board[i][j] == o:
				print('| O ',end="")
			elif Board[i][j] == Empty:
				print('|   ',end="")
		print('|')
		print(row_divider)

	print("")


def Win (Player, Board):
#-------------------------------------------------------------------------
# Determines if Player has won, by finding '3 in a row'. 
#-------------------------------------------------------------------------

	return False ;



def GetComputerMove (Player, Board): 
#-------------------------------------------------------------------------
# If the opponent is a computer, use artificial intelligence to select
# the best move. 
# For this demo, a move is chosen at random from the list of legal moves.
#-------------------------------------------------------------------------
	MoveList = GetMoves(Player, Board)
	k = randrange(0,len(MoveList))
	Move = MoveList[k]
	return Move


if __name__ == "__main__":


#-------------------------------------------------------------------------
# A move is represented by a list of 4 elements, representing 2 pairs of 
# coordinates, (FromRow, FromCol) and (ToRow, ToCol), which represent the 
# positions of the piece to be moved, before and after the move. 
#-------------------------------------------------------------------------
	x = -1
	o = 1
	Empty = 0
	OutOfBounds = 2
	NumRows = 5
	BoardRows = NumRows + 1 
	NumCols = 4
	BoardCols = NumCols + 1 
	MaxMoves = 4*NumCols 
	NumInPackedBoard = 4 * (BoardRows+1) *(BoardCols+1) 
	infinity = 10000  # Value of a winning board 
	MaxDepth = 4
	Board = [[0 for col in range(BoardCols+1)] for row in range(BoardRows+1)]

	print("\nThe squares of the board are numbered by row and column, with '1 1' ")
	print("in the upper left corner, '1 2' directly to the right of '1 1', etc.")
	print("")
	print("Moves are of the form 'i j m n', where (i,j) is a square occupied")
	print("by your piece, and (m,n) is the square to which you move it.")
	print("")
	print("You move the 'X' pieces.\n")

	InitBoard(Board) 
	ShowBoard(Board) 

	MoveList = GetMoves(x,Board)
	print(MoveList)
	MoveList = GetMoves(o,Board)
	print(MoveList)

	for n in range(5):
		Move = GetHumanMove(x,Board)
		Board = ApplyMove(Board,Move)
		ShowBoard(Board) 
		Move = GetComputerMove(o,Board)
		Board = ApplyMove(Board,Move)
		ShowBoard(Board) 