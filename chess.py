#pygame class
#chess board class
#pieces class
#individual pieces class (inherited from pieces class)
import numpy as np
import pygame

#common problems:
#Boards sideways instead of up and down
#Black and white are on the wrong side of the board
#The white king and queen are in the wrong positions
#It doesn't recognize checkmate
#It lets you take into check
#Pawns only move one square
#No en passant
#No castling
#Crashes when you capture king
#Not proper notation


class chesspygame:
	#every function manipulates the pygame window and input in some way
	def __init__:
		#get instance of ChessBoard class
	def showboard():
		#takes as input, a Board and displays the current state of the board
	def checkforinput():
		#takes input from a window and applies the corresponding changes to Board

class ChessBoard:
	#every function manipulates self.Board and its objects in some way
	def __init__(self):
		#make an 8 by 8 array, which will be called self.board
		self.board = [[Square("white") for _ in range(8)]for _ in range(8)]

		#set starting player, which restrains how self.move() can be called
		self.currentPlayer = "white"
		self.whitetaken = []
		self.blacktaken = []

		self.currentmove = 0
	def place(self,pieceType,side,index):
		#getting all the paramaters in Square() to call for the super().__init() method in the pieces class

		#account for when we try to replace a piece that already exists
		self.board[index] = pieceType(self.board[index],side)
	################################
	def selected(self,index1):
		#selects an index in which to be index1
		self.index1 = np.array(index1)
	def checkMoves(self):
		#check an index on self.Board and gets the object in that index
		#then, checks every possible index that that object can move to (relates properties of objects)
		#returns list
		
		#checkwhat side this object is on
		self.selectedSide = self.board[self.index1].side
		self.avaliableMoves = []
		self.selectedType = type(self.board[self.index1])
		#############################################
		if self.selectedType == Pawn:
			self.pawnIncrementValue = None


			if self.board[self.index1].directionFacing == "North":
				self.pawnIncrementValue = np.array((1,0))
			if self.board[self.index1].directionFacing == "South":
				self.pawnIncrementValue = np.array((-1,0))
			#promotion


			#Check indicies of position index1+1 and index1-1 to see if any of them are of class Pawn
			#The ones that have the quality Pawn.tookJumpMove as True and Pawn.moveJumpMoveWasTaken as self.currentmove(+ or - 1 depending on side) 
			#are eligble to take by en passant

			#If Pawn.isEligbleForJumpMove is True, append the position of index + or - (0,2) to available moves
			try:
				if self.board[self.index1 + (0,1)].side != self.selectedSide and type(self.board[self.index1 + (0,1)]) == Pawn and self.board[self.index1 + (0,1)].moveJumpMoveWasTaken+1 == self.currentmove:
					self.availableMoves.append(self.pawnIncrementValue + (0,1))
			except:
				pass

			try:
				if self.board[self.index1 + (0,-1)].side != self.selectedSide and type(self.board[self.index1 + (0,-1)]) == Pawn and self.board[self.index1 + (0,-1)].moveJumpMoveWasTaken+1 == self.currentmove:
					self.availableMoves.append(self.pawnIncrementValue + (0,-1))
			except:
				pass

			try:
				if self.board[self.index1 + self.pawnIncrementValue] == Square:
					self.availableMoves.append(self.index1 + self.pawnIncrementValue)
			except:
				pass

			try:
				if self.board[self.index1].eligibleForJumpMove and self.board[self.index1 + self.pawnIncrementValue] == Square and self.board[self.index1 + (2*self.pawnIncrementValue)] == Square:
					self.availableMoves.append(self.index1 + (2*self.pawnIncrementValue))
			except:
				pass
		#############################################
		if self.SelectedType == King:
			#castling
		#############################################
		if self.SelectedType == Knight:
			try:
				if self.board[np.array(self.index1) + (2,1)].side != self.selectedSide:
					self.availableMoves.append(np.array(self.index1) + (2,1))
			except:
				pass

			try:
				if self.board[np.array(self.index1) + (2,-1)].side != self.selectedSide:
					self.availableMoves.append(np.array(self.index1) + (2,-1))
			except:
				pass

			try:
				if self.board[np.array(self.index1) + (1,2)].side != self.selectedSide:
					self.availableMoves.append(np.array(self.index1) + (1,2))
			except:
				pass

			try:
				if self.board[np.array(self.index1) + (1,-2)].side != self.selectedSide:
					self.availableMoves.append(np.array(self.index1) + (1,-2))
			except:
				pass
			
			try:
				if self.board[np.array(self.index1) + (-2,1)].side != self.selectedSide:
					self.availableMoves.append(np.array(self.index1) + (-2,1))
			except:
				pass
			
			try:
				if self.board[np.array(self.index1) + (-2,-1)].side != self.selectedSide:
					self.availableMoves.append(np.array(self.index1) + (-2,-1))
			except:
				pass
			
			try:
				if self.board[np.array(self.index1) + (-1,2)].side != self.selectedSide:
					self.availableMoves.append(np.array(self.index1) + (-1,2))
			except:
				pass
			
			try:
				if self.board[np.array(self.index1) + (-1,-2)].side != self.selectedSide:
					self.availableMoves.append(np.array(self.index1) + (-1,-2))
			except:
				pass
		
		#############################################
		if self.SelectedType == Bishop:
			loopedindex = np.array(index1)
			while True:
				try:
					if type(self.Board[loopedindex]) == Square:
						self.availableMoves.append(loopedindex)
					elif self.selectedSide == self.Board[loopedindex].side:
						break
					elif self.selectedSide != self.Board[loopedindex.side]:
						self.availableMoves.append(loopedindex)
						break
					else:
						pass
				except:
					break
				loopedindex = loopedindex + (1,1)
			while True:
				try:
					if type(self.Board[loopedindex]) == Square:
						self.availableMoves.append(loopedindex)
					elif self.selectedSide == self.Board[loopedindex].side:
						break
					elif self.selectedSide != self.Board[loopedindex.side]:
						self.availableMoves.append(loopedindex)
						break
					else:
						pass
				except:
					break
				loopedindex = loopedindex + (1,-1)
			while True:
				try:
					if type(self.Board[loopedindex]) == Square:
						self.availableMoves.append(loopedindex)
					elif self.selectedSide == self.Board[loopedindex].side:
						break
					elif self.selectedSide != self.Board[loopedindex.side]:
						self.availableMoves.append(loopedindex)
						break
					else:
						pass
				except:
					break
				loopedindex = loopedindex + (-1,-1)
			while True:
				try:
					if type(self.Board[loopedindex]) == Square:
						self.availableMoves.append(loopedindex)
					elif self.selectedSide == self.Board[loopedindex].side:
						break
					elif self.selectedSide != self.Board[loopedindex.side]:
						self.availableMoves.append(loopedindex)
						break
					else:
						pass
				except:
					break
				loopedindex = loopedindex + (-1,1)
		#############################################
		if self.SelectedType == Rook:
			#run 4 while loops. Each for loop goes in one direction, checking the object at each index. 
			#If it gets to an index in which type(self.Board[loopedindex]) == Square(), append loopedindex to self.available Moves
			#Else, If it gets to an index in which self.selectedSide == self.Board[loopedindex].side, terminate loop
			#Else, If it gets to an index in which self.selectedSide != self.Board[loopedindex].side, append loopedindex to self.availableMoves, then break
			loopedindex = np.array(index1)
			while True:
				try:
					if type(self.Board[loopedindex]) == Square:
						self.availableMoves.append(loopedindex)
					elif self.selectedSide == self.Board[loopedindex].side:
						break
					elif self.selectedSide != self.Board[loopedindex.side]:
						self.availableMoves.append(loopedindex)
						break
					else:
						pass
				except:
					break
				loopedindex = loopedindex + (1,0)
			while True:
				try:
					if type(self.Board[loopedindex]) == Square:
						self.availableMoves.append(loopedindex)
					elif self.selectedSide == self.Board[loopedindex].side:
						break
					elif self.selectedSide != self.Board[loopedindex.side]:
						self.availableMoves.append(loopedindex)
						break
					else:
						pass
				except:
					break
				loopedindex = loopedindex + (0,1)
			while True:
				try:
					if type(self.Board[loopedindex]) == Square:
						self.availableMoves.append(loopedindex)
					elif self.selectedSide == self.Board[loopedindex].side:
						break
					elif self.selectedSide != self.Board[loopedindex.side]:
						self.availableMoves.append(loopedindex)
						break
					else:
						pass
				except:
					break
				loopedindex = loopedindex - (1,0)
			while True:
				try:
					if type(self.Board[loopedindex]) == Square:
						self.availableMoves.append(loopedindex)
					elif self.selectedSide == self.Board[loopedindex].side:
						break
					elif self.selectedSide != self.Board[loopedindex.side]:
						self.availableMoves.append(loopedindex)
						break
					else:
						pass
				except:
					break
				loopedindex = loopedindex - (0,1)

		#############################################
		if self.SelectedType == Queen:
			loopedindex = np.array(index1)
			while True:
				try:
					if type(self.Board[loopedindex]) == Square:
						self.availableMoves.append(loopedindex)
					elif self.selectedSide == self.Board[loopedindex].side:
						break
					elif self.selectedSide != self.Board[loopedindex.side]:
						self.availableMoves.append(loopedindex)
						break
					else:
						pass
				except:
					break
				loopedindex = loopedindex + (0,1)
			while True:
				try:
					if type(self.Board[loopedindex]) == Square:
						self.availableMoves.append(loopedindex)
					elif self.selectedSide == self.Board[loopedindex].side:
						break
					elif self.selectedSide != self.Board[loopedindex.side]:
						self.availableMoves.append(loopedindex)
						break
					else:
						pass
				except:
					break
				loopedindex = loopedindex + (1,1)
			while True:
				try:
					if type(self.Board[loopedindex]) == Square:
						self.availableMoves.append(loopedindex)
					elif self.selectedSide == self.Board[loopedindex].side:
						break
					elif self.selectedSide != self.Board[loopedindex.side]:
						self.availableMoves.append(loopedindex)
						break
					else:
						pass
				except:
					break
				loopedindex = loopedindex + (1,0)
			while True:
				try:
					if type(self.Board[loopedindex]) == Square:
						self.availableMoves.append(loopedindex)
					elif self.selectedSide == self.Board[loopedindex].side:
						break
					elif self.selectedSide != self.Board[loopedindex.side]:
						self.availableMoves.append(loopedindex)
						break
					else:
						pass
				except:
					break
				loopedindex = loopedindex + (1,-1)
			while True:
				try:
					if type(self.Board[loopedindex]) == Square:
						self.availableMoves.append(loopedindex)
					elif self.selectedSide == self.Board[loopedindex].side:
						break
					elif self.selectedSide != self.Board[loopedindex.side]:
						self.availableMoves.append(loopedindex)
						break
					else:
						pass
				except:
					break
				loopedindex = loopedindex + (0,-1)
			while True:
				try:
					if type(self.Board[loopedindex]) == Square:
						self.availableMoves.append(loopedindex)
					elif self.selectedSide == self.Board[loopedindex].side:
						break
					elif self.selectedSide != self.Board[loopedindex.side]:
						self.availableMoves.append(loopedindex)
						break
					else:
						pass
				except:
					break
				loopedindex = loopedindex + (-1,-1)
			while True:
				try:
					if type(self.Board[loopedindex]) == Square:
						self.availableMoves.append(loopedindex)
					elif self.selectedSide == self.Board[loopedindex].side:
						break
					elif self.selectedSide != self.Board[loopedindex.side]:
						self.availableMoves.append(loopedindex)
						break
					else:
						pass
				except:
					break
				loopedindex = loopedindex + (-1,0)
			while True:
				try:
					if type(self.Board[loopedindex]) == Square:
						self.availableMoves.append(loopedindex)
					elif self.selectedSide == self.Board[loopedindex].side:
						break
					elif self.selectedSide != self.Board[loopedindex.side]:
						self.availableMoves.append(loopedindex)
						break
					else:
						pass
				except:
					break
				loopedindex = loopedindex + (-1,)
		

	def move(self,index1,index2):
		#takes as input, index1 and index2, and attempts to move the object at index1 to index2
		#index2 has to be under self.checkMoves() of self.index1
		#otherwise, do nothing
	################################
	def checkOccupiedWhite():
		#for every object with piece.side opposite that of piece.currentplayer, run the checkmoves function and set Squares to occupied accordingly
		#does not return anything
	def checkOccupiedBlack():
		#same thing as above
		#does not return anything
	################################
	def checkIfCheck(,side):
		#sets King.isInCheck accordingly
		#does not return anything
	def checkIfPawnIsOnPromotionSquare(self):
		#if pawn is has property Square in which self.promotionSquare returns True,
		#then set that pawn to an option of class Rook, Bishop, Knight, or Queen



#Some rules of moving pieces in chess:
#Castling
#En passant
#Promotion

class Square:
	def __init__(self, color, promotionsquare = False):
		self.occupiedByWhite = False #depends on other piece inherited objects
		self.occupiedByBlack = False #^
		self.color = color #set up for loop later

		self.promotionSquare = promotionsquare #a bool value

class Piece:
	def __init__(self, squareClass, side):
		#all the properities of a chess piece
		self.squareClass = squareClass

		self.occupiedByWhite = self.square.occupiedByWhite
		self.occupiedByBlack = self.square.occupiedByBlack
		self.color = self.square.color
		self.promotionSquare = promotionSquare

		###################################
		self.isKing = False

		self.side = side
		self.directionFacing = None

		if self.side == "white":
			self.directionFacing = "North"
		elif self.side == "black":
			self.directionFacing = "South"
		else:
			pass

		self.lastMoveMoved = None # decided by move function in class ChessBoard
	def setOccupiedValue(self, side):
		if side == white:
			self.occupiedByWhite = True
		if side == Black:
			self.occupiedByBlack = True
		else:
			pass

class Pawn(Piece):
	def __init__(self, squareClass, side):
		super().__init__(squareClass, side)
		self.eligibleForJumpMove = True#Depends on move function in class ChessBoard

		self.moveJumpMoveWasTaken = None #Depends on move function in class ChessBoard



class King(Piece):
	def __init__(self, squareClass, side):
		super().__init__(squareClass, side)
		self.isKing = True
		#self.isInCheck
		#self.hasBeenChecked

class Rook(Piece):
	def __init__():
		#self.hasBeenMoved

class Bishop(Piece):
	def __init__(self, squareClass, side):
		super().__init__(squareClass, side)

class Knight(Piece):
	def __init__(self, squareClass, side):
		super().__init__(squareClass, side)

class Queen(Piece):
	def __init__(self, squareClass, side):
		super().__init__(squareClass, side)

