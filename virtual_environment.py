import os
from decouple import config
home = os.environ.get("home")
host = os.environ.get("REDIS_HOST")
port = os.environ.get("REDIS_PORT")
password = os.environ.get("REDIS_PASSWORD")
db = os.environ.get("REDIS_DB")
print(f"home: {home}, host: {host}, port: {port}, password: {password}, db: {db}")
#so decouple also get your environment variable
#decouple package will look for .env file in the project root directory and get environment variable
print("let try with decouple: ")
home = config("home")
host = config("REDIS_HOST")
port = config("REDIS_PORT")
password = config("REDIS_PASSWORD")
db = config("REDIS_DB")
print(f"home: {home}, host: {host}, port: {port}, password: {password}, db: {db}")