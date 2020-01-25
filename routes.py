from flask import Flask, render_template,request
from classes.feedManager import feedManager
from classes.codeManager import codeManager
from classes.rssScraper import rssScraper
from datetime import datetime, timedelta
from classes.db import databaser
import sys


import json;
app = Flask(__name__)

codeManager = codeManager();
sys.setrecursionlimit(8000);

@app.route('/code')
def code():
	return str(codeManager.get_code());


@app.route('/')
def index_page():
	return render_template('index.html');

@app.route('/getStreams', methods = ['GET'])
def getStreams():
	db =  databaser();
	feedMan = db.retrieve_manager();

	value = json.dumps(feedMan.getFeedByName(request.args.get("name")).jsonGetStreams());
	print(value);
	db.close();
	return value;

@app.route('/createFeed', methods = ['GET'])
def createFeed():

	db =  databaser();
	feedMan = db.retrieve_manager();
	feedMan.addFeed(request.args.get("name"));

	for i in feedMan.getFeeds():
		print(i.getName());

	db.update_manager(feedMan);
	return "Ok";


@app.route('/createStream', methods = ['GET'])
def createStream():
	if (request.args.get("type") == "rss_podcast"):

		db =  databaser();
		feedMan = db.retrieve_manager();
		print(len(feedMan.getFeeds()));


		for i in feedMan.getFeeds():
			print(i.getName());
			print("RED WATER\n\n\n\n\n");

		node = rssScraper(request.args.get("url"));
		feedMan.addFeedStream(request.args.get("feed_name"), request.args.get("name"), node);

	db.update_manager(feedMan);

	return "Ok";


@app.route('/fetch', methods = ['GET'])
def fetch():

	db =  databaser();
	feedMan = db.retrieve_manager();


	print("NAME: \n\n\n\n\n\n\n\n\n");
	print(request.args.get("name"));


	print(len(feedMan.getFeeds()));
	for i in feedMan.getFeeds():
		print(i.getName());
		print("RED WATERzzzzzzzz\n\n\n\n\n");

	curr_date = datetime(int(request.args.get("year")), int(request.args.get("month")), int(request.args.get("day")));
	day = 1;
	list1 = feedMan.fetchFeed(curr_date, curr_date - timedelta(days=day), request.args.get("name"));
	while(len(list1) < 10):
		day = day*2;
		list1 = feedMan.fetchFeed(curr_date, curr_date - timedelta(days=day), request.args.get("name"));
	

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
	db.close();

	return json.dumps(list1);	





@app.route('/unload', methods = ['POST'])
def unload():

	db =  databaser();
	feedMan = db.retrieve_manager();

	code = request.get_data().decode('utf-8');

	codeManager.remove_code(code);
	feedMan.clearFeeds(code);
	db.update_manager(feedMan);

	return "Ok";
	
