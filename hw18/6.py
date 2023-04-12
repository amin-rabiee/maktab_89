from pymongo import MongoClient
from bson.objectid import ObjectId

client = MongoClient('mongodb://admin:admin@127.0.0.1')
db = client['mflix']
movie_COLLECTION = db['movies']
comments_collection = db['comments']

for i in movie_COLLECTION.find({'title': "The Taking of Pelham 1 2 3"}):
    movie_id = i['_id']

for i in comments_collection.find({'movie_id': ObjectId(movie_id)}, {'name': 1}).distinct('name'):
    print(i)
