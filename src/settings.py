from os import getenv

MONGODB_HOST = getenv("MONGODB_HOST", "0.0.0.0:27017")
MONGODB_USER = getenv("MONGODB_USER", "root")
MONGODB_PASS = getenv("MONGODB_PASS", "pass12345")
MONGODB_NAME = getenv("MONGODB_NAME", "fastapi")

