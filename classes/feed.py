

class feed():
	def __init__ (self, name):
		self._streams = [];
		self._name = name;

	def getName(self):
		return self._name;

	def fetchStreams(self, startDate,endDate): 
		jsonObjects = [];
		for stream in self.getStreams():
			jsonObjects.extend(stream.fetch(startDate, endDate));
		return jsonObjects;

	def getStreams(self):
		return self._streams

	def jsonGetStreams(self):
		json_streams = [];
		for i in self.getStreams():
			json_item = {}
			json_item['name'] = i.getName();
			json_streams.append(json_item);
		return json_streams;

	def getStreamByName(self, Name):
		for stream in self.getStreams():
			if (stream.getName() == Name):
				return stream;

	def deleteStreamById(self, Name):
		for stream in self.getStreams():
			if (stream.getName() == Name):
				getStreams().remove(stream);

	def addStream(self, stream):
		self.getStreams().append(stream);