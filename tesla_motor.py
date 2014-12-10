from pymongo import MongoClient
import pprint

client = MongoClient('mongodb://localhost:27017/')

tesla_s = {
	"manufacturer" : "Maruti Motors",       
	"class":"luxary",
	"body style":"2-door liftback",
	"production":[2015,2016],
	"model year":[2014],
	"layout":["front-motor","rear-wheel drive"],
	"designer":{
		"first name":"tushar" ,
		"surname":"singh"
		},
	"assembly":[
		{
			"country" : "swiss",
			"city": "kanpur",
			"state":"UK"
		},
		{
			"country":"Neatherlands",
			"city":"Tilburg"

		}
	]


   }
db=client.examples
db.autos.insert(tesla_s)
for a in db.autos.find():
    pprint.pprint(a)

