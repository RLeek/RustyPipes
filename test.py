from classes.rssScraper import rssScraper
from classes.feedManager import feedManager
from classes.feed import feed
from datetime import datetime
from classes.stream import stream;

FeedManger = feedManager();
FeedManger.addFeed("podcasts");
FeedManger.addFeedStream("podcasts", "Bestfriends", rssScraper("http://superbestfriendcast.libsyn.com/rss"));
FeedManger.addFeedStream("podcasts", "hellointernet",rssScraper("http://www.hellointernet.fm/podcast?format=rss"));
FeedManger.addFeedStream("podcasts", "matticacacaus",rssScraper("http://supermega.libsyn.com/rss"));
FeedManger.addFeedStream("podcasts", "fishes", rssScraper("http://feeds.soundcloud.com/users/soundcloud:users:125332894/sounds.rss"));
'''
for i in (FeedManger.fetchFeed(datetime(2018, 12,5), datetime(2017, 8,6), "podcasts")).sort(key=lambda s: s['date']):
	print(i["title"]);
	print(i["date"]);
	print(i["description"]);
	print(i["link"]);
	print("\n")

'''
for i in (sorted((FeedManger.fetchFeed(datetime(2019, 12,5), datetime(2017, 8,6), "podcasts")), key=lambda x: x['date'])):
	print(i["title"]);
	print(i["date"]);
	print(i["description"]);
	print(i["icon"]);
	print(i["link"]);
	print("\n")