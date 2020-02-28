from flask import Flask, render_template,request
from classes.codeManager import codeManager
from classes.rssScraper import rssScraper
from classes.feed import feed
from datetime import datetime, timedelta
from classes.database import database
from classes.ArtStationScraper import ArtStationScraper
import json
app = Flask(__name__)

codeManager = codeManager()

#This will rarely break
#Should deal with this concurrency issue
#eventually
@app.route('/code')
def code():
	return str(codeManager.get_code())

#No change required
@app.route('/')
def index_page():
	return render_template('index.html')


#Can be considered fixed I think?
@app.route('/createStream', methods = ['GET'])
def createStream():
	addStream(request.args.get("feed_name"), request.args.get("name"),request.args.get("type"),request.args.get("url"))
	return "OK"

def addStream(feedName, streamName, types, url):
	infodb = database()
	if (types == "rss_podcast"):
		node = rssScraper(streamName, url)
		infodb.createStream(feedName, streamName,types,url, node.get_content())
	if (types == "artstation"):
		node = ArtStationScraper(streamName, url)
		infodb.createStream(feedName, streamName, types, url, node.get_content())
	infodb.close()



#Can be considered fixed I think?
@app.route('/fetch', methods = ['GET'])
def fetch():

	infodb = database()
	retrievedData = infodb.fetchFeedsInfo(request.args.get("name"))
	streamList = []
	if (len(retrievedData) == 0):
		return json.dumps([])

	for i in retrievedData:
		if (i[1] == "rss_podcast"):
			streamList.append(rssScraper(i[0], i[2], i[3]))
		elif (i[1] == "artstation"):
			streamList.append(ArtStationScraper(i[0], i[2], i[3]))
	requestedFeed = feed(streamList)
	curr_date = datetime(int(request.args.get("year")), int(request.args.get("month")), int(request.args.get("day")))
	day = 1
	posts = requestedFeed.fetch(curr_date, curr_date - timedelta(days=day))
	while(len(posts) < 10):
		day = day*2
		posts = requestedFeed.fetch(curr_date, curr_date - timedelta(days=day))

	posts = sorted(posts, key=lambda x: x['date'], reverse = True)
	curr_date=curr_date-timedelta(days = day+1)
	date = []
	json_date = {}
	json_date["year"] = curr_date.year
	json_date["month"] = curr_date.month
	json_date["day"] = curr_date.day
	date.append(json_date)

	posts.append(date)
	infodb.close()

	return json.dumps(posts)	

#This will rarely break
#Should deal with this concurrency issue
#eventually
@app.route('/unload', methods = ['POST'])
def unload():
	infodb =  database()
	code = request.get_data().decode('utf-8')
	codeManager.remove_code(code)
	infodb.deleteFeeds(code)
	infodb.close()
	return "Ok"


@app.route('/deleteFeed', methods = ['GET'])
def deleteFeed():
	infodb = database()
	name = request.args.get("name")
	code = request.args.get("code")
	infodb.deleteFeed(code, name)
	return "OK"


@app.route('/deleteStream', methods = ['GET'])
def deleteStream():
	infodb = database()
	name = request.args.get("name")
	code = request.args.get("code")
	streamName = request.args.get("streamName")
	infodb.deleteStream( name, code, streamName)
	return "OK"

@app.route('/addStreams', methods = ['POST'])
def addStreams():
	data = (request.json)
	name = data[0]["name"]
	i = 1
	while(i < len(data)):
		addStream(name, data[i]["name"], data[i]["type"], data[i]["url"])
		i+=1
	return "Ok"




	
