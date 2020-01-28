from bs4 import BeautifulSoup, SoupStrainer

import urllib.request
import json
from classes.node import node

from datetime import datetime

class feed():
	
	def __init__(self, streamList):
		self._streamList = streamList;



	def fetch(self, startDate, endDate):
		jsonObjects = [];
		for i in self._streamList:
			jsonObjects.extend(i.fetch(startDate, endDate));
		return jsonObjects;







