var feedList = {
    //Attributes
    htmlObject: document.getElementById("feed_list"),
    currSelected: null,

    //Behaviors
    getSelected: function() {
        return this.currSelected.dataset.name;
    },
    select: function(selectedFeed) {
        if (this.currSelected != null) {
            this.currSelected.classList.toggle("selected");
        } else {
            streamCreator.toggleButton();
        }
        selectedFeed.classList.toggle("selected");
        this.currSelected = selectedFeed;
    },
    createAndAdd: function(feedName) {
        var feedObject = this.createFeedObject(feedName);
        this.htmlObject.appendChild(feedObject);
        storage.addFeed(feedName);
    },
    createAndAddNoStore: function(feedName) {
        var feedObject = this.createFeedObject(feedName);
        this.htmlObject.appendChild(feedObject);
    },
    addFeed: function(feedObject) {
        this.htmlObject.appendChild(feedObject);
        storage.addFeed(feedObject.dataset.name); 
    },
    deleteFeed: function(feedObject) {
        this.htmlObject.removeChild(feedObject);
        storage.deleteFeed(feedObject.dataset.name); 
    },
    createFeedObject: function(feedName) {
        var feedContainer = document.createElement("div"); 
        var FeedText = document.createElement("div"); 
        var cross_div = document.createElement("div");
        var cross_text_div = document.createElement("div");
        var cross_text_text = document.createElement("div");
        cross_text_text.innerHTML = "&times;"
        cross_text_div.className = "cross_text";
        cross_text_div.appendChild(cross_text_text);
        cross_div.className = "cross";
        cross_div.style.left = "25px";
        cross_div.appendChild(cross_text_div);
        var newContent = document.createTextNode(feedName); 
        FeedText.className = "button_text";
        FeedText.style.left = "70px";
        FeedText.appendChild(newContent);  
        feedContainer.className = "button button_margins";
        feedContainer.style.left = "10px";
        feedContainer.appendChild(cross_div);
        feedContainer.appendChild(FeedText);

        feedContainer.setAttribute("data-name", feedName);
        feedContainer.setAttribute("data-loaded", "false");

        cross_div.addEventListener("click", function() {
            event.stopPropagation();
            feedList.deleteFeed(feedContainer);
            serverRequest.deleteFeedRequest(feedContainer.dataset.name);  
            if (feedList.currSelected == feedContainer) {
                feedList.currSelected = null;
                streamCreator.toggleButton();
            }
        });
        feedContainer.addEventListener("click", function() {
            feedList.select(feedContainer);
            if (feedContainer.dataset.loaded == "true") {
                centre.clear(); 
                centre.update();
            }
            streamList.clear();
            streamList.load(feedName, feedContainer.dataset.loaded);
            feedContainer.setAttribute("data-loaded", "true");
        });
        return feedContainer;
    },

    initialize: function() {
        feedArray = storage.getFeeds();
        var i = 0;
        while(i < feedArray.length) {
            this.createAndAddNoStore(feedArray[i]);
            i++;
        }
    }
};
feedList.initialize();
