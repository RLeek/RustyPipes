var streamList = {
    //Attributes
    htmlObject:document.getElementById("stream_list"),

    //Behaviour
    load: function(name, loaded) {
        streamArray = (storage.getStreams(name).slice());
        var i =0;
        while(i < streamArray.length) {
            streamArray[i] = JSON.parse(JSON.stringify(streamArray[i]));
            i++;
        }
        i = 0;
        while(i < streamArray.length) {
            this.createAndAddNoStore(streamArray[i]["name"], streamArray[i]["url"], streamArray[i]["type"]);
            i++;
        }
        if (loaded == "false") {
            streamArray.unshift({"name": name});
            serverRequest.addStreamsRequest(streamArray); 
        }
    },

    clear: function() {
        var child = this.htmlObject.firstChild;
        while(child) {
            this.htmlObject.removeChild(child);
            child = this.htmlObject.firstChild;
        }
    },

    createAndAdd: function(streamName, streamURL, streamType) {
        var streamObject = this.createStreamObject(streamName, streamURL, streamType);
        this.htmlObject.appendChild(streamObject);
        storage.addStream(feedList.currSelected.dataset.name, streamName, streamURL, streamType);
    },
    createAndAddNoStore: function(streamName, streamURL, streamType) {
        var streamObject = this.createStreamObject(streamName, streamURL, streamType);
        this.htmlObject.appendChild(streamObject);
    },
    addStream: function(streamObject) {
        this.htmlObject.appendChild(streamObject);
        storage.addStream(streamObject.dataset.name, streamObject.dataset.url, streamObject.dataset.type); 
    },
    deleteStream: function(streamObject) {
        this.htmlObject.removeChild(streamObject);
        storage.deleteStream(feedList.currSelected.dataset.name, streamObject.dataset.name); 
    },
    createStreamObject: function(streamName, streamURL, streamType) {
        var streamContainer = document.createElement("div"); 
        var feedText = document.createElement("div"); 
        var cross_div = document.createElement("div");
        var cross_text_div = document.createElement("div");
        var cross_text_text = document.createElement("div");
        cross_text_text.innerHTML = "&times;"
        cross_text_div.className = "cross_text";
        cross_text_div.appendChild(cross_text_text);
        cross_div.className = "cross";
        cross_div.style.left = "25px";
        cross_div.appendChild(cross_text_div);

        var newContent = document.createTextNode(streamName); 
        feedText.className = "button_text";
        feedText.style.left = "70px";
        feedText.appendChild(newContent);  
        streamContainer.className = "button button_margins";
        streamContainer.style.left = "10px";
        streamContainer.appendChild(feedText);
        streamContainer.appendChild(cross_div);
        cross_div.addEventListener("click", function() {
            event.stopPropagation();
            streamList.deleteStream(streamContainer);
            storage.deleteStream(feedList.currSelected.dataset.name, streamName);
            serverRequest.deleteStreamRequest(feedList.currSelected.dataset.name, streamName);
        });
        streamContainer.setAttribute("data-name", streamName);
        streamContainer.setAttribute("data-url", streamURL);
        streamContainer.setAttribute("data-type", streamType)
        return streamContainer;
    }
};