from Sophia import MONGO_DB_URI
from pymongo import MongoClient
import io
import asyncio
import os
from Sophia import log
from Sophia.conf import get_int_key, get_str_key


client = MongoClient()
client = MongoClient(MONGO_DB_URI)
db = client["Sophia"]
approved_users = db.approve
