from pymongo import MongoClient

client = MongoClient('mongodb://admin:admin@127.0.0.1')
db = client['mflix']
movie_COLLECTION = db['movies']


for i in movie_COLLECTION.find({'genres':'History'}, {'title':1}):
    print(i)