import pymongo
from pymongo import MongoClient

client = MongoClient('mongodb://admin:admin@127.0.0.1')
db = client['mflix']
movie_COLLECTION = db['movies']

result = movie_COLLECTION.aggregate([
    {'$project': {'title': 1, 'languages': 1}},
    {'$unwind': '$languages'},
    {'$group': {
        '_id': '$languages',
        'count': {'$sum': 1}
    }
    },
    {'$sort': {'count': pymongo.DESCENDING}}

])
for i in result:
    print(i)
