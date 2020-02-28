centre = {
    //Attributes
    day: 0,
    month:0,
    year:0,
    htmlObject:document.getElementById("center"),

    //Behaviors
    clear: function() {
        if (this.htmlObject.children.length != 0) {
            var child = this.htmlObject.firstChild;
            while(child) {
                this.htmlObject.removeChild(child);
                child = this.htmlObject.firstChild;
            }
        }
        this.set();
    },
    set: function() {
        var currentTime = new Date();
        this.day = currentTime.getDate();
        this.month = currentTime.getMonth() + 1;
        this.year = currentTime.getFullYear();
    },
    update: function() {
        this.load();
        serverRequest.fetchContent(feedList.getSelected());
    },
    removeLoad: function () {
        this.htmlObject.removeChild(this.htmlObject.lastChild);
    },
    load: function() {
        this.htmlObject.appendChild(this.create_load_object());
    },
    create_load_object: function() {
        var loader = document.createElement("div");
        loader.className = "loader";
        loader.style.left = "calc(50% - 40px)";
        var text_div = document.createElement("div");
        text_div.className = "centre_mid_text";
        text_div.innerHTML = "Loading...&ensp;&ensp;&ensp;"
        var storage = document.createElement('div');
        storage.appendChild(loader);
        storage.appendChild(text_div);
        return storage;
    },
    add: function(type, date, title, link, icon, description) {
        if (type == "rss_podcast") {
            node = this.createRSSPodcastNode(date, title, link, icon, description);
            this.htmlObject.appendChild(node);
        } else if (type == "artstation") {
            node = this.createArtStationNode(date, title, link, icon, description);
            this.htmlObject.appendChild(node);
        }
    },
    createArtStationNode: function(date, title, link, icon, description) {
        var descrip = document.createElement("div");
        descrip.className = "centre_description";
        descrip.innerHTML = description;

        var tite = document.createElement("div");
        tite.className = "centre_title";
        tite.appendChild(document.createTextNode(title));

        var dae = document.createElement("div");
        dae.className = "centre_date";
        dae.appendChild(document.createTextNode(date));

        var img = document.createElement("img");
        img.setAttribute('src', link);
        img.className = "centre_img";
        imgContent = document.createElement("div");
        imgContent.className = "centre_img";
        imgContent.appendChild(img);


        var content = document.createElement("div");
        content.className = "centre_content";
        content.appendChild(dae);
        content.appendChild(tite);

        content.appendChild(imgContent);

        if (icon != "noNeed") {
            test = document.createElement('a');
            test.appendChild(document.createTextNode("There is more to this project"));
            test.href = icon;
            contentStuff = document.createElement('div');
            contentStuff.appendChild(test);
            contentStuff.className = "centre_content_appended"
            content.appendChild(contentStuff)
        } else {
            contentStuff = document.createElement('div');
            contentStuff.className = "centre_content_appended"
            content.appendChild(contentStuff)
        }
        content.appendChild(descrip);
        var enc = document.createElement("div");
        enc.className = "centre_enclosure";
        enc.appendChild(content);
        return enc;
    },

    createRSSPodcastNode: function(date, title, audio, icon, description) {
        var descrip = document.createElement("div");
        descrip.className = "centre_description";
        descrip.innerHTML = description;

        var audA = document.createElement("div");
        audA.className = "centre_audio_content";

        var aud = document.createElement("audio");
        aud.controls = "controls";

        var img = document.createElement("img");
        img.src = icon;
        img.className = "icon";
        var sour1 = document.createElement("source");
        sour1.src = audio;
        sour1.type = 'audio/ogg';
        var sour2 = document.createElement("source");
        sour2.src = audio;
        sour2.type ='audio/mpeg';
        aud.appendChild(sour1);
        aud.appendChild(sour2);
        audA.appendChild(img);
        audA.appendChild(aud);

        var tite = document.createElement("div");
        tite.className = "centre_title";
        tite.appendChild(document.createTextNode(title));

        var dae = document.createElement("div");
        dae.className = "centre_date";
        dae.appendChild(document.createTextNode(date));

        var content = document.createElement("div");
        content.className = "centre_content";
        content.appendChild(dae);
        content.appendChild(tite);
        content.appendChild(audA);
        content.appendChild(descrip);

        var enc = document.createElement("div");
        enc.className = "centre_enclosure";
        enc.appendChild(content);
        
        return enc;
    },
    initialize: function() {
        centre.htmlObject.addEventListener("scroll",  function() {  
            if (centre.htmlObject.scrollHeight-centre.htmlObject.scrollTop-centre.htmlObject.clientHeight < 1) {
                if (serverRequest.currFetching == false) {
                    serverRequest.currFetching = true;
                    centre.update();
                }

            }
        });
    }
}
centre.initialize();