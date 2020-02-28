var builder = {
    //Behavior
    titleBuilder: null,
    dateBuilder:null,
    contentBuilder:null,
    contentAppenderBuilder: null,
    descriptionBuilder: null,


    setTitleBuilder: function(desiredFunc) {
        this.titleBuilder = desiredFunc;
    },
    setDateBuilder: function(desiredFunc) {
        this.dateBuilder = desiredFunc;
    },
    setContentBuilder: function(desiredFunc) {
        this.contentBuilder = desiredFunc;
    },
    setContentApeenderBuilder: function(desiredFunc) {
        this.contentAppenderBuilder = desiredFunc;
    },
    setDescriptionBuilder: function(desiredFunc) {
        this.descriptionBuilder = desiredFunc;
    },



    build: function(title, date, creator, content, contentAppender, description) {
        



        //Creates container
        //Then calls relevant build types
        //Appends them and then returns
    },




};
