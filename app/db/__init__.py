from pymongo import MongoClient

client = MongoClient("mongodb+srv://userReadOnly:7ZT817O8ejDfhnBM@minichallenge.q4nve1r.mongodb.net", 27017)
db = client['minichallenge']
