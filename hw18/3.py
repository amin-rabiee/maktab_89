from pymongo import MongoClient

client = MongoClient('mongodb://admin:admin@127.0.0.1')
db = client['mflix']
movies_collection = db['movies']

for i in movies_collection.find({'year': {'$type': ['string', 'int'], '$gte': 1990}},
                                {'title': 1, 'imdb.rating': 1, 'year': 1}):
    print(i)
