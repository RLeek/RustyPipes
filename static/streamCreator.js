var streamCreator = {
    //Attributes
    htmlButtonObject: document.getElementById("stream_create"),
    htmlTypeObject: document.getElementById("stream_list_create"),
    htmlFormObject: document.getElementById("stream_list_form"),
    htmlFormNameObject: document.getElementById("create_stream_name"),
    htmlFormURLObject: document.getElementById("create_stream_url"),
    htmlFormCompleteObject: document.getElementById("create_stream"),
    formOpen: false,
    startOpen: false,
    invalidForm: false,
    currSelected: null,


    //Behavior
    selected: function(typeObject) {
        this.currSelected = typeObject;
    },
    getSelected: function() {
        return this.currSelected.dataset.type;
    },
    toggleButton: function() {
        this.htmlButtonObject.classList.toggle("unselectable");
    },

    toggleForm: function() {
        if (this.startOpen == false) {
            this.htmlTypeObject.classList.toggle("unhidden");
            this.startOpen = true;
        } else {
            this.toggleClose();
        }
    },

    toggleClose: function() {
        this.htmlFormNameObject.value="";
        this.htmlFormURLObject.value="";
        if (this.invalidForm == true) {
            this.htmlFormObject.removeChild(this.htmlFormObject.lastChild);
            this.invalidForm = false;
        }
        if (this.formOpen == false) {
            setTimeout(function(){
                streamCreator.htmlTypeObject.classList.toggle("unhidden");
                streamCreator.startOpen = false;
            }, 0);
        } else {
            setTimeout(function(){
                streamCreator.htmlTypeObject.classList.toggle("unhidden");
                streamCreator.htmlFormObject.classList.toggle("unhidden");
                this.formOpen = false;
                streamCreator.startOpen = false;
            }, 0);
        }
    },
    checkValid: function() {
        if (this.htmlFormNameObject.value == "") {
            return false;
        }
        if (storage.hasStream(feedList.getSelected(), this.htmlFormNameObject.value)) {
            return false;
        }

        return true;
    },

    inValidMessage: function() {
        if (this.invalidForm == false) {
            var error = document.createElement("div");
            error.className = "error_message";
            error.innerHTML = "Name chosen is invalid or already in use";
            this.htmlFormObject.appendChild(error);
            this.invalidForm = true;
        }
    },
    refreshForm: function() {
        this.htmlFormNameObject= document.getElementById("create_stream_name");
        this.htmlFormURLObject= document.getElementById("create_stream_url");
    },
    initialize: function() {
        this.htmlButtonObject.addEventListener("click", function() {
            streamCreator.toggleForm();
        });
        
        var i = 0;
        while(i < this.htmlTypeObject.children.length) {
            var child = this.htmlTypeObject.children[i];
            this.htmlTypeObject.children[i].addEventListener("click", function() {
                streamCreator.selected(this);
                streamCreator.formOpen = true;
                streamCreator.htmlFormObject.classList.toggle("unhidden");
            });
            i++;
        }

        this.htmlFormCompleteObject.addEventListener("click", function() {
            streamCreator.refreshForm();
            if (streamCreator.checkValid() == true) {
                streamList.createAndAdd(streamCreator.htmlFormNameObject.value, streamCreator.htmlFormURLObject.value, streamCreator.getSelected());
                serverRequest.addStreamRequest(streamCreator.htmlFormNameObject.value, streamCreator.htmlFormURLObject.value, streamCreator.getSelected(), feedList.getSelected());
                streamCreator.toggleForm();
            } else {
                streamCreator.inValidMessage();
            }

        });
    }
};
streamCreator.initialize();

