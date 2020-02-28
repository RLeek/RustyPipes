from urllib.request import Request, urlopen
import json
from classes.node import node
from datetime import datetime
import time
import re
import sys

urls = re.compile(r"((https?):((//)|(\\\\))+[\w\d:#@%/;$()~_?\+-=\\\.&]*)", re.MULTILINE|re.UNICODE)

class ArtStationScraper(node):

    def __init__(self,name, url, project="unfinished"):
        if (project == "unfinished"):
            user = url[27:]
            user_link = "https://www.artstation.com/users/"+ user+"/projects.json?page="



            
            json_content = []
            page = 1
            url = Request(user_link + str(page), headers={'User-Agent': 'Mozilla/5.0'})
            data = json.loads(urlopen(url).read())
            content = data["data"]
            while(len(content) != 0):
                json_content = json_content + content
                page = page+1
                url = Request(user_link + str(page), headers={'User-Agent': 'Mozilla/5.0'})
                data = json.loads(urlopen(url).read())
                content = data["data"]
                time.sleep(1)






            self._project = (json_content)
        else:
            self._project = json.loads(project)
        self._url = url
        self._name = name

    
    def get_name(self):
        return self._name

    def get_url(self):
        return self._url

    def get_content(self):
        return json.dumps(self._project)
    
    def fetch(self, startDate, endDate):
        json_list =[]
        for i in self._project:
            date = datetime.strptime(i["published_at"][0:10], "%Y-%m-%d")
            if (date >= endDate):
                if (date <= startDate):
                    item = self.json_converter(i)
                    if (item != None):
                        json_list.append(item)
            else:
                return json_list
        return json_list

    def json_converter(self,i):
        json_podcast = {}
        try:
            json_podcast["title"] = i['title']
            json_podcast["date"] = (datetime.strptime(i['published_at'][0:10], "%Y-%m-%d")).strftime('%Y/%m/%d')
            json_podcast["description"] = self.urlify2(i['description']).replace('\n', '<br />')
            if (i['icons']['image'] == True):
                json_podcast["icon"] = i['permalink']
            elif (i['icons']['video'] == True):
                json_podcast["icon"] = i['permalink']
            elif (i['icons']['video_clip'] == True):
                json_podcast["icon"] = i['permalink']
            elif (i['icons']['model3d'] == True):
                json_podcast["icon"] = i['permalink']
            elif (i['icons']['marmoset'] == True):
                json_podcast["icon"] = i['permalink']
            elif (i['icons']['pano'] == True):
                json_podcast["icon"] = i['permalink']
            else:
                json_podcast["icon"] = "noNeed"
            source = [i['cover']['small_square_url']]
            source[0] = re.sub("\/[0-9]{14}\/small_square\/", "/large/",source[0])
            source[0] = source[0].replace("small_square","large")
            json_podcast["link"] = source
            json_podcast["type"] = "artstation"

        except:
            return
        return json_podcast        


    def urlify2(self,value):
        return urls.sub(r'<a href="\1" target="_blank">\1</a>', value)



