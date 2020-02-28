var serverRequest = {
	code: null,
	loadedStreams: 0,
	totalStreams:0,
	currFetching: false,

	addStreamRequest: function(streamName, url, type, feedName) {
		var request = new XMLHttpRequest();
		request.open("GET", "/createStream?type="+type+"&url="+url+"&name="+streamName+serverRequest.code+"&feed_name="+feedName+serverRequest.code);
		request.onreadystatechange = function() {
			if (request.readyState == 4) {
				centre.clear();
				centre.update();
			}
		}
		request.send();
	},
	
	addStreamsRequest: function(streamArray) {
		//Add code for stream array
		var i = 0;
		while(i < streamArray.length) {
			streamArray[i]["name"] = streamArray[i]["name"] + serverRequest.code
			i++;
		}
		var request = new XMLHttpRequest();
		request.open("POST", "/addStreams");
		request.setRequestHeader("Content-Type", "application/json");
		request.onreadystatechange = function() {
			if (request.readyState == 4) {
				centre.clear();
				centre.update();
			}
		}
		request.send(JSON.stringify(streamArray));
	}, 

	deleteFeedRequest: function(feedName) {
		var request = new XMLHttpRequest();
		request.open("GET", "/deleteFeed?name="+feedName+"&code="+serverRequest.code);
		request.onreadystatechange = function() {
			if (request.readyState == 4) {
				//nothing
			}
		}
		request.send();
	},

	deleteStreamRequest: function(name, streamName) {
		var request = new XMLHttpRequest();
		request.open("GET", "/deleteStream?name="+name+"&code="+serverRequest.code +"&streamName=" + streamName);
		request.onreadystatechange = function() {
			if (request.readyState == 4) {
				//nothing
			}
		}
		request.send();
	},

	fetchContent: function(name) {
		this.currFetching = true;
		var request = new XMLHttpRequest();
		request.open("GET", "/fetch?name=" + name+serverRequest.code+"&day="+ centre.day+"&month="+centre.month+"&year="+centre.year);
		request.onreadystatechange = function() {
			if (request.readyState == 4) {
				centre.removeLoad();
				if (feedList.getSelected() == name) {
					serverRequest.currFetching = false;
					var requestText = JSON.parse(request.responseText);
					var i = 0;
					while(i < requestText.length-1) {
						centre.add(requestText[i].type, requestText[i].date, requestText[i].title, requestText[i].link, requestText[i].icon, requestText[i].description);
						i = i + 1;
					}
					if (requestText.length != 0) {
						centre.year = requestText[i][0].year;
						centre.month = requestText[i][0].month;
						centre.day = requestText[i][0].day;
					}
				}
			}
		}					
		request.send();
	},

	initialize: function() {
		var request = new XMLHttpRequest();
		request.open("GET", "/code");
		request.onreadystatechange = function() {
			if (request.readyState == 4) {
				serverRequest.code = request.responseText;
			}
		}
		request.send();
	}
};
serverRequest.initialize();		

window.addEventListener("unload", function logData() {
	navigator.sendBeacon("/unload", serverRequest.code);
  });