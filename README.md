# Fist FastAPI project using MongoDB

## Docker compose file

```yaml
version: "3.8"
services:
  fast-api:
    image: "babynghe2003/fastapiimage"
    container_name: fastapi
    build:
      dockerfile: Dockerfile
    environment:
      - MONGODB_HOST=mongodb
      - MONGODB_PORT=27017
      - MONGODB_USER=root
      - MONGODB_PASS=pass12345
    ports:
      - 5000:5000
```

## Installation

```
python -m venv venv
source venv/bin/activate

pip install -r requirements.txt

uvicorn src.main:app --reload
```
