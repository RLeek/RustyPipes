from bs4 import BeautifulSoup, SoupStrainer

import urllib.request
import json
from classes.node import node

from datetime import datetime

class rssScraper(node):
	
	def __init__(self, url):
		web_page = urllib.request.urlopen(url);
		strainer = SoupStrainer("item");
		self._url = url;
		self._soup = BeautifulSoup(web_page, "xml", parse_only = strainer);

	def get_url(self):
		return self._url;

	def get_soup(self):
		return self._soup

	def set_soup(self, soup):
		self._soup = soup;

	def update(self):
		web_page = urllib.request(self.get_url());
		strainer = SoupStrainer("item");
		self.set_soup(BeautifulSoup(web_page, "xml", parse_only = strainer));

	def fetch(self, startDate, endDate):
		podcast = self.get_soup().find("item");
		date = datetime.strptime(podcast.find('pubDate').text[5:16], "%d %b %Y");
		json_list = []
		i = 0;
		while(date >= endDate):
			if (date <= startDate):
				item = self.json_converter(podcast);
				if (item != None):
					json_list.append(item);
			podcast = podcast.find_next("item");
			date = datetime.strptime(podcast.find('pubDate').text[5:16], "%d %b %Y");
			i = i + 1;
		return json_list;

	def json_converter(self, podcast):
		json_podcast = {};
		try:
			json_podcast["title"] = podcast.find('title').text;
			json_podcast["date"] = (datetime.strptime(podcast.find('pubDate').text[5:16], "%d %b %Y")).strftime('%m/%d/%Y');
			json_podcast["description"] = podcast.find('description').text;
			json_podcast["icon"] = podcast.find('itunes:image')['href'];
			json_podcast["link"] = podcast.find('enclosure')['url'];
		except:
			return;
		return json_podcast;