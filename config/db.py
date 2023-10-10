from pymongo import MongoClient
import os

conn=MongoClient(f"mongodb+srv://{os.environ.get('USER_MONGO')}:{os.environ.get('MONGO_KEY')}@ufobrt.wyofdo3.mongodb.net/?retryWrites=true&w=majority")

