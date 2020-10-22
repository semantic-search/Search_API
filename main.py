from elasticsearch import Elasticsearch
es=Elasticsearch('localhost:9200')
from fastapi import FastAPI
app = FastAPI()
@app.get("/typesense/{item}")
async def read_item(item: str):


    return


@app.get("/elasticsearch/{item}")
async def read_item(item: str):
    res = es.search(index='semantic', body={
        "query": {
            "match": {
                "text": {
                    "query": "item"
                }
            }
        }
    })
    response={}
    print(res['hits']['hits'])
    listRes=res['hits']['hits']
    for item in listRes:
        print(item['_source'])
        response[item["_source"]['file_name']]=item["_source"]['doc_id']

    return response

