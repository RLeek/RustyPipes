# RustyPipes
Currently deployed via heroku on: https://polar-citadel-94806.herokuapp.com/

## Motivation

This project was motivated by two main factors. The first factor is the increasing number of social media sites, requiring accounts across different sites and even multiple accounts per site to maintain separate feeds, making seeing desirable content unreasonably tedious. The second factor was the mass migration of artists and other accounts away from tumblr after it was bought by verizon. Many of these accounts spread across several websites such as twitter or instagram, sometimes exclusively only using one website. As a result, there was no easy way of creating content streams that previously existed on tumblr. The intent of this project then was to provide a simplified way of creating multiple feeds through providing links to relevant content. (Though this project was far from successful for several reasons, noted in limitations)

## Features/How-to-use

To start using the app, the "Add new Feed" button allows you to create a feed, which is designed to hold streams. Selecting this feed, then allows you to use the "Add new Stream" button. Currently there are two supported websites:<br/>
&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;- Artstation: For this stream, simply provide an artstation profile link and this app will scrape the relevant content.
&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;e.g.https://www.artstation.com/kuvshinov_ilya<br/>
&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;- rss_podcast: This is largely a placeholder stream for personal use and is designed to deal with rss links for audio 
&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;content. e.g. http://www.hellointernet.fm/podcast?format=rss<br/>
Multiple streams of each type can be added. The app will automatically load the content from these streams (note the first time loading this content for a website will take quite a while due to both processing and to avoid getting blocked from scraping). This content will be loaded into the centre. Scrolling to the bottom will automatically generate more content.

Multiple feeds can be added, each holding their own set of streams. This allows users to create feeds based on both content and website type. Furthermore, this website has persistence so once feeds are created, users will not have to add them again manually. 

Note: There is no validation for links provided for the stream and providing an incorrect stream link can cause the app to fail generating content. If this the case, the relevant stream/feed can be deleted by pressing the associated x and selecting the feed again, which will refresh the feed.

## Limitations

This app has several limitations. Its biggest issue is how long it takes to load content and how little content it supports. This is largely the result of underestimating the difficulty of doing this project (as this was my first project that used javascript, ajax, databases and scraping in general, all of which I had no previous experience with). It was also my first time deploying a website. The main issues were that scraping the majority of websites were largely infeasible due to difficulty in parsing content as well as the potential for getting blocked. For example, with the artstation stream it only provides the first image associated with a post and a link to the rest. This is because getting the rest of the information would require scraping the posts individually, making generating content incredibly slow and lead to getting blocked.

## Future Development

This website is still used for personal use and it is likely that as the need and possibility presents itself more websites will be supported. 
