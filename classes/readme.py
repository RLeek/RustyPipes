from random import randrange


class codeManager(ABC):
    
	def __init__ (self):
		self._maintained = [];


	def get_code():
		valid = False;
		code = 0;
		while(!valid):
			code = random.randint(1000,9999);
			collision = False;
			for i in maintained:
				if (code == i):
					collision = True;
			if (collision == True):
				valid = False;
			else:
				valid = True;
		maintained.append(code);
		return code;

	def remove_code(code):
		maintained.remove(code);



