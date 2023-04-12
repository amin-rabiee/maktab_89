from pymongo import MongoClient

client = MongoClient('mongodb://admin:admin@127.0.0.1')
db = client['mflix']
movie_COLLECTION = db['movies']
print('hi')
result = movie_COLLECTION.aggregate([
    {'$project': {'title': 1, 'cast':1}},
    {'$unwind':'$cast'},
    {'$group':{
        '_id':'$cast',
        'count':{'$sum':1}}
    },
    {'$sort':{'count':pymongo.DESCENDING}},# چون تعداد ۱ ها زیاد هست ترمینال نمیتونه همه رو چاپ کنه لذا واضح نیستن اعداد بیشتر از ۱

])
for i in result:
    print(i)
