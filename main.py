from elasticsearch import Elasticsearch
from fastapi.middleware.cors import CORSMiddleware
es=Elasticsearch('13.68.241.106:9200')
from fastapi import FastAPI
app = FastAPI()

origins = [
    "http://localhost:3000"
]

app.add_middleware(
    CORSMiddleware,
    allow_origins=origins,
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)
@app.get("/elasticsearch/{item}")
async def read_item(item: str):
    res = es.search(index='semantic', body={
        "query": {
            "match": {
                "text": {
                    "query": item
                }
            }
        }
    })

    response={}
    print(res['hits']['hits'])
    listRes=res['hits']['hits']
    for item in listRes:
        print(item['_source'])
        if item["_source"]['file_name']:
            response[item["_source"]['file_name']]=item["_source"]['doc_id']
        else:
            response[item["_source"]['url']] = item["_source"]['doc_id']

    return response
