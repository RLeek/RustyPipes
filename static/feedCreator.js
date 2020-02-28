var feedCreator = {
    //Attributes dataset.loaded
    htmlButtonObject: document.getElementById("new_feed"),
    htmlFormPageObject: document.getElementById("feed_create"),
    htmlFormNameObject: document.getElementById("create_feed_name"),
    htmlFormCompleteObject: document.getElementById("create_feed"),
    invalidForm: false,

    //Behavior
    refreshForm: function() {
        this.htmlFormNameObject = document.getElementById("create_feed_name");
    },
    toggleForm: function() {
        setTimeout(function(){
                feedCreator.htmlFormPageObject.classList.toggle("unhidden");
                if (feedCreator.invalidForm == true) {
                    feedCreator.htmlFormPageObject.removeChild(feedCreator.htmlFormPageObject.lastChild);
                    feedCreator.invalidForm = false;
                }
                feedCreator.htmlFormNameObject.value = "";
        }, 0);
    },        
    checkValid: function() {
        if (this.htmlFormNameObject.value == "") {
            return false;
        }
        if (storage.hasFeed(this.htmlFormNameObject.value)) {
            return false;
        }
        return true;
    },
    inValidMessage: function() {
        if (this.invalidForm == false) {
            var error = document.createElement("div");
            error.className = "error_message";
            error.innerHTML = "Name chosen is invalid or already in use";
            this.htmlFormPageObject.appendChild(error);
            this.invalidForm = true;
        }
    },
    initialize: function() {
        this.htmlButtonObject.addEventListener("click", function() {
            feedCreator.toggleForm();
        });
        this.htmlFormCompleteObject.addEventListener("click", function() {
            feedCreator.refreshForm();
            if (feedCreator.checkValid() == true) {
                feedList.createAndAdd(feedCreator.htmlFormNameObject.value);
                feedCreator.toggleForm();
            } else {
                  feedCreator.inValidMessage();
            }
        });
    }
};

feedCreator.initialize();
