from pymongo import MongoClient

client = MongoClient('mongodb://admin:admin@127.0.0.1')
db = client['mflix']
movie_COLLECTION = db['movies']


result = movie_COLLECTION.aggregate([
    {'$project':{'cast':1, 'genres':1}},
    {'$unwind':'$cast'},
    {'$unwind':'$genres'},
    {'$group':{
        '_id':'$cast',
        'genres_each_player':{'$addToSet':'$genres'}
    }},
])

for i in result:
    print(i)