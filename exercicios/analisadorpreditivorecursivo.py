class Category(Enum):
	pt = 1 
	ptvg = 2
	eof = 3
	se = 4
	entao = 5
	senao = 6
	fim = 7
	para = 8
	ate = 9
	repita = 10
	id = 11
	atr = 12
	opl = 13
	nao = 14
	verd = 15
	falso = 16
	opa = 17
	opm = 18
	abpar = 19
	fepar = 20
	cten = 21

class Token(object):
	"""docstring for Token"""
	def __init__(self, lex, categ, position):
		self.lex = lex
		self.categ = categ
		self.position = position

	def self.tk.nextTokenToken():
		tk = Token()
	    #Implementação de self.tk.nextTokenTokem
	    return tk


class Sintatico(object):

	__init__(self, token):
	self.tk = token

	def error(self,token):
		print("ERROR:"+str(token.lex)+"|"str(token.position)+"|"+str(token.categ))	

	def main():


	def fpgm():
	     flsent()
	     if (self.tk.categ == Category.pt):
	     		self.tk.nextToken()
	        if(self.tk.categ == Category.eof):
	        	return
	        else:
	        	print("'EOF' ESPERADO")
	        	error(self.tk)
	     else:
	     	print("'.' ESPERADO")
	     	error(self.tk)

	def flsent():
		fsent()
		flsentr()  

	def flsentr():
		if(self.tk.categ == Category.ptvg):
			fsent()
			flsentr()

	def fsent():
		self.tk = self.tk.nextToken()
		if (self.tk.categ == Category.se):
			self.tk.nextToken()
			feb()
			if(self.tk.categ == Category.entao):
				self.tk.nextToken()
				flsent()
				fsenao()
			else
				print("'entao' esperado")
				error(self.tk)
		if (self.tk.categ == Category.para):
			self.tk.nextToken()
			fatr()
			if(self.tk.categ == Category.ate):
				self.tk.nextToken()
				fea()
				if(self.tk.categ == Category.repita):
					flsent()
					if(self.tk.categ == Category.fim):
						return
					else:
						print("'fim' esperado")
						error(self.tk)
				else:
					print("'repita' esperado")
					error(self.tk)
			else:
				print("'ate' esperado")
				error(self.tk)
		else:
			fatr()

	def fsenao():

		if(self.tk.categ == Category.fim):
			self.tk.nextToken()
			return
		else if(self.tk.categ == Category.senao):
			self.tk.nextToken()
			flsent()
			if(self.tk.categ == Category.fim):
				self.tk.nextToken()
				return
			else:
				print("'fim' esperado")
				error(self.tk)
		else:
			print("'fim' ou 'senao' esperado")
			error(self.tk)
		

	def fexpr():
		feb()

	def feb():
		ftb()
		febr()

	def febr():
		if(self.tk.categ == Category.opl):
	        self.tk.nextToken()
	        ftb()
	        febr()
		else:
			print("'opl' esperado")
			error(self.tk)

	def ftb():

		if(self.tk.categ == Category.nao):
			self.tk.nextToken()
			ftb()
		else if(self.tk.categ == Category.verd):
			self.tk.nextToken()
			return
		else if(self.tk.categ == Category.falso):
			self.tk.nextToken()
			return
		else:
			fea()

	def fea()
		fta()
		fear()


	def fear()
		if(self.tk.categ == Category.opa):
			self.tk.nextToken()
			fta()
			fear()
		else:
			print("'opa' esperado")
			error(self.tk)

	def fta()
		ffa()
		ftar()

	def ftar()
		if(self.tk.categ == Category.opm):
			self.tk.nextToken()
			ffa()
			ftar()	
		else:
			print("'opm' esperado")
			error(self.tk)

	def fatr()
		if(self.tk.categ == Category.id):
	         self.tk.nextToken()
	         if(self.tk.categ == Category.atr):
	         	self.tk.nextToken()
	         	fexpr()
	         else:
	         	print("'=' esperado")
	         	error(self.tk)	
		else:
			print("'id' esperado")
			error(self.tk)

	def ffa()
		if(self.tk.categ == Category.abpar):
			self.tk.nextToken()
			fexpr()
			if(self.tk.categ == Category.fepar):
				self.tk.nextToken()
				return
			else:
				print("'fepar' esperado")
				error(self.tk)
		else if(self.tk.categ == Category.id):
			self.tk.nextToken()
			return
		
		else if(self.tk.categ == Category.cten):
			self.tk.nextToken()
			return
	
    























