from pymongo import MongoClient
import pprint
import re

# client = MongoClient(host="localhost", port=27017)
client = MongoClient("mongodb://localhost:27017/")

# Get reference to 'Chinook' database
db = client["ChinookDB"]

# Get a reference to the 'customers' collection
customers_collection = db["Customer"]
# print(customers_collection)

# Print all documents
#doc1 = customers_collection.find_one()
#print(doc1)

for all_doc in customers_collection.find():
    print(all_doc)

for rec in customers_collection.find({},{"_id":0,"LastName":1,"FirstName":1}):
    print(rec)

rgx = re.compile('^Go.*?$', re.IGNORECASE) 
cursor = customers_collection.find({"LastName":rgx})
num_docs = 0
for document in cursor:
    num_docs += 1
    pprint.pprint(document)
    print()
print("# of documents found: "+ str(num_docs))

client.close()