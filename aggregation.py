from pymongo import MongoClient
import pprint

client=MongoClient("mongodb://localhost:27017")
db=client.twitter

def most_tweets():
	result = db.twitter.find()
	return result
if __name__ == '__main__':
     results = most_tweets()
     pprint.pprint(results)
