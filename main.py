from elasticsearch import Elasticsearch
es=Elasticsearch([{'host':'13.68.236.211','port':9200}])
from fastapi import FastAPI
app = FastAPI()
@app.get("/typesense/{item}")
async def read_item(item: str):


    return


@app.get("/elasticsearch/{item}")
async def read_item(item: str):
    res = es.search(index='store', body={
        "query": {
            "match": {
                "text": {
                    "query": "item"
                }
            }
        }
    })
    print(res['hits']['hits'])
    return res['hits']['hits']

