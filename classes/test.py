from rssScraper import rssScraper
from feedManager import feedManager
from feed import feed
from datetime import datetime

FeedManger = feedManager();
FeedManger.addFeed(feed("podcasts", "Gimmie Podcasts"));
FeedManger.addFeedStream("podcasts", rssScraper( "bestfriends", "http://superbestfriendcast.libsyn.com/rss"));
FeedManger.addFeedStream("podcasts", rssScraper( "hellointernet", "http://www.hellointernet.fm/podcast?format=rss"));
FeedManger.addFeedStream("podcasts", rssScraper( "supermega", "http://supermega.libsyn.com/rss"));
FeedManger.addFeedStream("podcasts", rssScraper( "jimquisition", "http://feeds.soundcloud.com/users/soundcloud:users:125332894/sounds.rss"));
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
	print(i["link"]);
	print("\n")