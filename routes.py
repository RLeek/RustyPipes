from flask import Flask, render_template,request
from classes.feedManager import feedManager
from classes.rssScraper import rssScraper
from datetime import datetime, timedelta
import json;
app = Flask(__name__)

FeedManager = feedManager();


@app.route('/')
def index_page():
	return render_template('index.html');

@app.route('/getStreams', methods = ['GET'])
def getStreams():
	print(json.dumps(FeedManager.getFeedByName(request.args.get("name")).jsonGetStreams()));
	return json.dumps(FeedManager.getFeedByName(request.args.get("name")).jsonGetStreams());

@app.route('/createFeed', methods = ['GET'])
def createFeed():
	print(request.args.get("name"));
	FeedManager.addFeed(request.args.get("name"));
	return "Ok";


@app.route('/createStream', methods = ['GET'])
def createStream():
	if (request.args.get("type") == "rss_podcast"):
		print("THIS WORKED");
		node = rssScraper(request.args.get("url"));
		FeedManager.addFeedStream(request.args.get("feed_name"), request.args.get("name"), node);
	return "Ok";


@app.route('/fetch', methods = ['GET'])
def fetch():
	curr_date = datetime(int(request.args.get("year")), int(request.args.get("month")), int(request.args.get("day")));
	day = 1;
	list1 = FeedManager.fetchFeed(curr_date, curr_date - timedelta(days=day), request.args.get("name"));
	while(len(list1) < 10):
		day = day*2;
		list1 = FeedManager.fetchFeed(curr_date, curr_date - timedelta(days=day), request.args.get("name"));
	

	list1 = sorted(list1, key=lambda x: x['date'], reverse = True);
	curr_date=curr_date-timedelta(days = day);
	date = [];
	json_date = {};
	json_date["year"] = curr_date.year;
	json_date["month"] = curr_date.month;
	json_date["day"] = curr_date.day;
	date.append(json_date);

	list1.append(date);
	print(list1);

	return json.dumps(list1);	
	
