from fastapi import FastAPI
import logging
import uvicorn

from hd2neo4j.routes import mapper_routes


logging.basicConfig(filename="logfile.log", level=logging.INFO)
logger = logging.getLogger(__name__)


app = FastAPI(title="UPR-K API", version="0.0.9")


app.include_router(mapper_routes.rt)



def start():
    """Launched with `poetry run start` at root level"""
    uvicorn.run("hd2neo4j.main:app", host="0.0.0.0", port=8000, reload=True)
