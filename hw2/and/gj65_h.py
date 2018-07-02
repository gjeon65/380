#CS380
#assignment 4

def CurrentStatus (Player, Board):
	get = []
	for i in range(1, NumRows + 1):
		for j in range(1, NumCols + 1):
			if(Board[i][j] == Player) :
				get.append((i,j))
	return get

def Win (Player, Board):
#-------------------------------------------------------------------------
#	Determines if Player has won, by finding '3 in a row'. 
#-------------------------------------------------------------------------
	getStatus = CurrentStatus(Player, Board)
	#setting possible winning
	#posWinRow = [(0,1,2),(1,2,3)]
	#posWinCol = [(0,1,2),(1,2,3)]
	posWin = [(0,1,2),(0,1,3),(1,2,3),(2,3,0)]
	for i in range(0,4):
		posA = posWin[i][0]
		posB = posWin[i][1]
		posC = posWin[i][2]
		CposA = getStatus[posA][0]
		CposB = getStatus[posA][1]
		CposC = getStatus[posB][0]
		CposD = getStatus[posB][1]
		CposE = getStatus[posC][0]
		CposF = getStatus[posC][1]
		
		if abs(CposA-CposC)==1 or CposA - CposC == 0:
			return True
		elif abs(CposB-CposD)==1 or CposB- CposD == 0:
			return True
		elif abs(CposC-CposE)==1 or CposC - CposE == 0:
			return True
		elif abs(CposD-CposF)== 1 or CposD-CposF == 0:
			return True
		else:
			return False
		
		mk = diagonal(CposA,CposC)#check dia pos
		if mk == False:
			cv = float(CposB-CposD)/float(CposA-CposC)*(CposE -CposA) + CposF
			if cv == CposF:
				if abs(CposA - CposC) == 1:
					return True
				elif abs(CposC -CposeE) == 1:
					return True
				elif abs(CposB-CposD) == 1:
					return True
				elif abs(CposD-CposF) == 1:
					return True
				else:
					return False
	
	return False ;
def diagonal (scA , scB):
	a = scA
	b = scB

	val = (a-b)
	if val == 0:
		return True
	else:
		return False


