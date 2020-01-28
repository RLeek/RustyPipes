from flask import Flask, render_template,request
from classes.codeManager import codeManager
from classes.rssScraper import rssScraper
from classes.feed import feed
from datetime import datetime, timedelta
from classes.database import database


import json;
app = Flask(__name__)

codeManager = codeManager();

#This will rarely break
#Should deal with this concurrency issue
#eventually;
@app.route('/code')
def code():
	return str(codeManager.get_code());

#No change required
@app.route('/')
def index_page():
	return render_template('index.html');


#getStreams Removed (This is stored locally)

#createFeed Removed (This is just a variable in the table)

#Can be considered fixed I think?
@app.route('/createStream', methods = ['GET'])
def createStream():
	infodb = database();
	rowid = None;
	if (request.args.get("type") == "rss_podcast"):
		node = rssScraper(request.args.get("name"), request.args.get("url"));
		rowid = infodb.createStream(request.args.get("feed_name"), request.args.get("name"),request.args.get("type"),request.args.get("url"), node.get_soup());
	infodb.close();
	return str(rowid);

#Can be considered fixed I think?
@app.route('/fetch', methods = ['GET'])
def fetch():

	infodb = database();
	retrievedData = infodb.fetchFeedsInfo(request.args.get("name"));
	streamList = [];
	for i in retrievedData:
		if (i[1] == "rss_podcast"):
			streamList.append(rssScraper(i[0], i[2], i[3]));
	requestedFeed = feed(streamList);

	curr_date = datetime(int(request.args.get("year")), int(request.args.get("month")), int(request.args.get("day")));
	day = 1;
	posts = requestedFeed.fetch(curr_date, curr_date - timedelta(days=day));
	while(len(posts) < 10):
		day = day*2;
		posts = requestedFeed.fetch(curr_date, curr_date - timedelta(days=day));
	

	posts = sorted(posts, key=lambda x: x['date'], reverse = True);
	curr_date=curr_date-timedelta(days = day);
	date = [];
	json_date = {};
	json_date["year"] = curr_date.year;
	json_date["month"] = curr_date.month;
	json_date["day"] = curr_date.day;
	date.append(json_date);

	posts.append(date);
	infodb.close();

	return json.dumps(posts);	

#This will rarely break
#Should deal with this concurrency issue
#eventually;
@app.route('/unload', methods = ['POST'])
def unload():

	infodb =  database();
	code = request.get_data().decode('utf-8');
	codeManager.remove_code(code);
	infodb.deleteFeed(code);
	infodb.close();
	return "Ok";
	
