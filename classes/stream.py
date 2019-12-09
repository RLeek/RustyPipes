

class stream():
	def __init__ (self, node, name):
		self._node = node;
		self._name = name;

	def getNode(self):
		return self._node;

	def getName(self):
		return self._name;

	def getId(self):
		return self._id;

	def updateNode(self):
		self.getNode().update();

	def fetch(self,startDate, endDate):
		return self.getNode().fetch(startDate, endDate)
