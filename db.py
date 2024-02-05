from flask_pymongo import PyMongo
import os
from dotenv import load_dotenv
load_dotenv()

def insert_data(app, data):
    mongo = PyMongo(app=app, uri=os.getenv("MONGO_URI"))
    mongo.cx[os.getenv('MONGO_DB')][os.getenv('MONGO_COLLECTION')].insert_one(data)