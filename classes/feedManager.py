from classes.feed import feed;
from classes.stream import stream;

class feedManager():
	def __init__ (self):
		self._feeds = [];

	def getFeeds(self):
		return self._feeds;

	def getFeedByName(self, name):
		for Feed in self.getFeeds():
			if (Feed.getName() == name):
				return Feed;
				
	def deleteFeedByName(self, name):
		for Feed in self.getFeeds():
			if (Feed.getName() == name):
				feeds.remove(Feed);

	def addFeed(self, name):
		self._feeds.append(feed(name));

	def fetchFeed(self, startDate, endDate, name):
		return self.getFeedByName(name).fetchStreams(startDate, endDate);

	def addFeedStream(self, name, stream_name, node):
		self.getFeedByName(name).addStream(stream(node,stream_name));

	def clearFeeds(self, code):
		for feed in self.getFeeds():
			if (feed.getName().endswith(code)):
				self.getFeeds().remove(feed);