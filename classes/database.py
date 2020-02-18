import sqlite3
import pickle 
class database():
    
	def __init__ (self):
		self._conn = sqlite3.connect(r"database");
		self._cursor = self._conn.cursor();
		self.start();

	def start(self):
		command = "CREATE TABLE IF NOT EXISTS feedManager (id INTEGER PRIMARY KEY, feedname TEXT, streamname TEXT, nodetype TEXT, url TEXT, content TEXT)"
		self._cursor.execute(command);

	def createStream(self, feedName, streamName,nodetype,  url, content):
		self._cursor.execute("INSERT INTO feedManager(feedname, streamname, nodetype, url, content) VALUES(?,?,?,?,?)", (feedName, streamName, nodetype, url, content));
		self._conn.commit();
		return self._cursor.lastrowid;

	def fetchFeedsInfo(self, name):
		self._cursor.execute("SELECT streamname, nodetype, url, content FROM feedManager WHERE feedname = ?",(name, ));
		rows = self._cursor.fetchall();
		return rows;

	def deleteStream(self, name, code, streamName):
		keyname = name + str(code);
		keystreamname = streamName + str(code);
		self._cursor.execute("DELETE FROM feedManager WHERE feedname = ? AND streamname = ?",(keyname, keystreamname));
		self._conn.commit();

	def deleteFeeds(self, code):
		self._cursor.execute("DELETE FROM feeedManager WHERE feedname LIKE '%{}'".format(code));
		self._conn.commit();


	def deleteFeed(self, code, name):
		keyname = name + str(code);
		self._cursor.execute("DELETE FROM feeedManager WHERE feedname = {}".format(keyname));
		self._conn.commit();


	def close(self):
		self._conn.close();

		self._conn = None;
		self._cursor = None;

