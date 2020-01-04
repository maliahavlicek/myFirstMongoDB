import pymongo
import os

MONGODB_URI = os.getenv("MONGO_URI")
DBS_NAME = "myTestDB"
COLLECTION_NAME = "myFirstMDB"

def mongo_connect(url):
    try:
        conn = pymongo.MongoClient(url)
        print("Mongo is connected")
        return conn
    except pymongo.errors.ConnectionFailure as e:
        print("Could not connect to MongoDB: %s") % e


conn = mongo_connect(MONGODB_URI)

coll = conn[DBS_NAME][COLLECTION_NAME]

# inserting a single record
# new_doc = {'first': 'douglas', 'last': 'adams', 'dob': '11/03/1952', 'hair_colour': 'gray', 'occupation': 'writer',
#           'gender': 'm','nationality': 'english'}
# coll.insert(new_doc)

# insert many records
# new_docs = [{'first': 'terry', 'last': 'pratchett', 'dob': '28/04/1948', 'hair_colour': 'not much',
#              'gender': 'm', 'occupation': 'writer','nationality': 'english'},
#             {'first': 'george', 'last': 'rr martin', 'dob': '20/09/1948', 'hair_colour': 'white',
#              'gender': 'm', 'occupation': 'writer', 'nationality': 'american'}
#             ]
#
# coll.insert_many(new_docs)


# get all records in DB
# documents = coll.find()

# find all entries with first of douglas
# documents = coll.find({'first': 'douglas'})

# Remove an item
# coll.remove({'first': 'douglas'})
# documents = coll.find()

# update a single item
# coll.update_one({"nationality": 'american'}, {'$set': {'hair_colour': 'maroon'}})
# documents = coll.find({'nationality': 'american'})

# update many items
coll.update_many({"nationality": 'american'}, {'$set': {'hair_colour': 'maroon'}})
documents = coll.find({'nationality': 'american'})

# loop through all records
for doc in documents:
    print(doc)
