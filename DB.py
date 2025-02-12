import pymongo
from email_retriever import retrieve_n_emails, get_emails
import os

client = pymongo.MongoClient("localhost", 27017)
db = client.job_sorter
collection = db.jobs

emails = get_emails()
length = len(emails)
query = {"sender": "admin"}
doc = collection.find_one(query)
prev = int(doc['body'])
print(prev, length, length-prev)
if prev >= length:
    print("DONE!")
else:
    ans = retrieve_n_emails(length-prev, emails)
    collection.insert_many(ans)
    collection.find_one_and_update(query, {"$set": {'sender':'admin', 'subject':'LAST', 'body':str(length)}})
    print("DONE!")