from flask_pymongo import PyMongo
import os
from dotenv import load_dotenv
import base64

load_dotenv()


def insert_data(app, data):
    mongo = PyMongo(app=app, uri=os.getenv("MONGO_URI"))
    mongo.cx[os.getenv('MONGO_DB')][os.getenv('MONGO_COLLECTION')].insert_one(data)

def count_docs(app):
    mongo = PyMongo(app=app, uri=os.getenv("MONGO_URI"))
    db = mongo.cx[os.getenv('MONGO_DB')]
    collection = db[os.getenv('MONGO_COLLECTION')]
    count = collection.count_documents({})
    return count

def upload_image(images, stt):
    folder_name = os.path.abspath('../body_data/' + str(stt))
    if not os.path.exists(folder_name):
        os.makedirs(folder_name)

    for key, value in images.items():
        try:
            img = base64.b64decode(value)
            filename = os.path.join(folder_name, f'{key}.jpg')
            with open(filename, 'wb') as f:
                f.write(img)
        except Exception as e:
            print(f'Error with key={key}: {str(e)}')

