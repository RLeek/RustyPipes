from bs4 import BeautifulSoup, SoupStrainer
import urllib.request
import json
from classes.node import node

from datetime import datetime

class rssScraper(node):
	
	def __init__(self,name, url, soup="unfinished"):
		if (soup == "unfinished"):
			web_page = urllib.request.urlopen(url)
			strainer = SoupStrainer("item")
			self._soup = str(BeautifulSoup(web_page, "lxml", parse_only = strainer))
		else:
			self._soup = soup
		self._url = url
		self._name = name

	def get_name(self):
		return self._name

	def get_url(self):
		return self._url

	def get_content(self):
		return self._soup

	def set_content(self, soup):
		self._soup = str(soup)

	def fetch(self, startDate, endDate):
		podcast = BeautifulSoup(self.get_content(), "lxml").find("item")
		date = datetime.strptime(podcast.find('pubdate').text[5:16], "%d %b %Y")
		json_list = []
		i = 0
		while(date >= endDate):
			if (date <= startDate):
				item = self.json_converter(podcast)
				if (item != None):
					json_list.append(item)
			podcast = podcast.find_next("item")
			date = datetime.strptime(podcast.find('pubdate').text[5:16], "%d %b %Y")
			i = i + 1
		return json_list

	def json_converter(self, podcast):
		json_podcast = {}
		try:
			json_podcast["title"] = podcast.find('title').text
			json_podcast["date"] = (datetime.strptime(podcast.find('pubdate').text[5:16], "%d %b %Y")).strftime('%Y/%m/%d')
			json_podcast["description"] = str(podcast.find('description'))[13:-20]
			json_podcast["icon"] = podcast.find('itunes:image')['href']
			json_podcast["link"] = podcast.find('enclosure')['url']
			json_podcast["type"] = "rss_podcast"
		except:
			return
		return json_podcast