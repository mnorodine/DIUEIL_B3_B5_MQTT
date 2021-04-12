#=============================================================================================================
# Dans ce scrit, l'objectif est d'observer ce qu'il fait et non comment il le fait ni comment créer le script 
#=============================================================================================================
import tkinter
import random



Clrs = ['Red','Green','Blue']



class Recherche:
	def __init__(self, Root, yPos, DataSize, MotifSize, iSize):
		self.Root		= Root
		self.yPos		= yPos
		self.DataSize	= DataSize
		self.MotifSize 	= MotifSize
		self.iSize		= iSize
		self.mp         = 1
		self.cList		= list()
		self.tList 		= list()
		self.mList		= list()
		self.Check 		= tkinter.Frame(self.Root, width=self.DataSize * self.iSize, height=self.iSize)
		self.Data 		= tkinter.Frame(self.Root, width=self.DataSize * self.iSize, height=self.iSize)
		self.Motif 		= tkinter.Frame(self.Root, width=self.MotifSize * self.iSize, height=self.iSize)


	def Rectangle(self, Parent, posx, posy, clr):
		Canvas = tkinter.Canvas(Parent, width= self.iSize, height= self.iSize)
		Canvas.create_rectangle(0, 0, self.iSize, self.iSize, fill=clr)
		Canvas.place(x= posx * self.iSize, y=posy)


	def Sequence(self, Parent, sList, cnt, Color = True):
		K = len(Clrs)
		sList.clear()
		for I in range (cnt):
			J = random.randrange(K)
			sList.append(J)
			if( Color ): 
				self.Rectangle(Parent, I, 0, Clrs[J])
			else:
				self.Rectangle(Parent, I, 0,'White')

	def MotifReplace(self):
		p = self.mp-1

		Finder.Motif.place(x=self.iSize*self.mp, y=self.yPos + 2*self.iSize)
		print("{", self.tList[p] -self.mList[0], "}", "{", self.tList[p+1] -self.mList[1], "}","{", self.tList[p+2] -self.mList[2], "}")


	def CreateData(self):
		
		self.Sequence(self.Data, self.tList, self.DataSize)
		self.Sequence(self.Check, self.cList, self.DataSize, False)
		self.Check.place(x=self.iSize, y=self.yPos)
		self.Data.place(x=self.iSize, y=self.yPos + self.iSize)

		self.Sequence(self.Motif, self.mList, self.MotifSize)
		self.MotifReplace()


global Finder



def Next(event):
	Finder.mp +=1
	Finder.MotifReplace()


def Previous(event):
	Finder.mp -=1
	Finder.MotifReplace()

		
Root = tkinter.Tk()
Root.title("RECHERCHE TEXTUELLE NAIVE")
screen_x 	= int (Root.winfo_screenwidth())
screen_y 	= int (Root.winfo_screenheight())
win_x		= int(0.99*screen_x)
win_y		= 200
geometry = "{}x{}+{}+{}".format(win_x, win_y, (screen_x - win_x)//2, (screen_y-win_y)//2)
Root.geometry(geometry)
Root.resizable(width=False, height= False)


Finder = Recherche(Root, 50, 150, 4, 10)
Finder.CreateData()


Root.bind("n", Next)
Root.bind("N", Next)
Root.bind("p", Previous)
Root.bind("P", Previous)


Root.mainloop()
