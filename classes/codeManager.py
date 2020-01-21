from random import randint


class codeManager():
    
	def __init__ (self):
		self._maintained = [];


	def get_code(self):
		valid = False;
		code = 0;
		while(not (valid)):
			code = randint(1000,9999);
			collision = False;
			for i in self._maintained:
				if (code == i):
					collision = True;
			if (collision == True):
				valid = False;
			else:
				valid = True;
		self._maintained.append(str(code));
		return code;


	def remove_code(self, code):
		print(code);
		print("\n\n\n\n\n\n");
		for i in self._maintained:
			print(i);


		self._maintained.remove(code);

