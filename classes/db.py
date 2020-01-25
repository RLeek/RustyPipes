import sqlite3
from classes.feedManager import feedManager
import pickle 
class databaser():
    
	def __init__ (self):
		self._conn = sqlite3.connect(r"database");
		self._cursor = self._conn.cursor();
		self.start();

	def start(self):
		command = "CREATE TABLE IF NOT EXISTS feedManager (id integer PRIMARY KEY, data BLOB)"

		self._cursor.execute(command);


	def retrieve_manager(self):
		fetched = self._cursor.execute("SELECT data FROM feedManager").fetchone();


		if ((fetched) == None):
			print("This list is empty \n\n\n\n\n");
			return feedManager();
		else:
			print("This list has elements \n\n\n\n\n");
			return pickle.loads(fetched[0]);

	def update_manager(self, feedManager1):
		print("UPDATE MANAGER HAS BEEN CALLED:\n")
		for i in feedManager1.getFeeds():
			print(i.getName());
			print("RED WATER\n\n\n\n\n");

		self._cursor.execute("INSERT OR REPLACE INTO feedManager(id, data) VALUES(?,?)" , (1,sqlite3.Binary(pickle.dumps(feedManager1))));
		self._conn.commit();
		self._conn.close();







	def close(self):
		self._conn.close();
		self._conn = None;
		self._cursor = None;

