var storage = {
    //Attributes
    data:  JSON.parse(localStorage.getItem('Data')) != null ?  JSON.parse(localStorage.getItem('Data')) : [],

    //Behaviors
    getFeeds: function() {
        feedArray=[];
        var i = 0;
        while(i < this.data.length) {
            feedArray.push(this.data[i]["name"]);
            i++;
        }
        return feedArray;
    },

    save: function() {
        localStorage.setItem('Data', JSON.stringify(this.data));
    },

    addFeed: function(feedName) {
        feed = {
            "name": feedName,
            "streams":[]
        };
        this.data.push(feed);
        this.save();
    },

    deleteFeed: function(feedName) {
        var i = 0;
        while(i < this.data.length) {
            if (this.data[i]["name"] == feedName) {
                this.data.splice(i, 1);
                break;
            }
            i++;
        }
        this.save();
    },
    hasFeed: function(feedName) {
        var i = 0;
        while(i < this.data.length) {
            if (this.data[i]["name"] == feedName) {
                return true;
            }
            i++;
        }    
        return false;
    },
    getStreams: function(feedName) {
        var i = 0;
        while(i < this.data.length) {            
            if (this.data[i]["name"] == feedName) {
                return this.data[i]["streams"];
            }
            i++;
        }
        return [];
    },
    addStream: function(feedName, streamName, streamURL, streamType) {
        stream = {
            "name": streamName,
            "type": streamType,
            "url": streamURL
        };

        var i = 0;
        while(i < this.data.length) {
            if (this.data[i]["name"] == feedName) {
                this.data[i]["streams"].push(stream);
            }
            i++;
        }
        this.save();
    },

    deleteStream: function(feedName, streamName) {
        var i = 0;
        while(i < this.data.length) {
            if (this.data[i]["name"] == feedName) {
                var i2 = 0;
                while(i2 < this.data[i]["streams"].length) {
                    if (this.data[i]["streams"][i2]["name"] == streamName) {
                        this.data[i]["streams"].splice(i2, 1);
                    }
                    i2++;
                }
            }
            i++;
        }
    },
    hasStream: function(feedName, streamName) {
        var i = 0;
        while(i < this.data.length) {
            if (this.data[i]["name"] == feedName) {
                var i2 = 0;
                while(i2 < this.data[i]["streams"].length) {
                    if (this.data[i]["streams"][i2]["name"] == streamName) {
                        return true;
                    }
                    i2++;
                }
            }
            i++;
        }
        return false;
    }
};
