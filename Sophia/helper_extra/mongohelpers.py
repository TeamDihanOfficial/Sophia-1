from Sophia import MONGO_DB_URI
from pymongo import MongoClient
import io
import asyncio
import os



client = MongoClient()
client = MongoClient(MONGO_DB_URI)
db = client["Sophia"]
approved_users = db.approve
