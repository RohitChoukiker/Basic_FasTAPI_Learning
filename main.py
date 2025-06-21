from fastapi import FastAPI
from pydantic import BaseModel
import uvicorn
app = FastAPI()

class Item(BaseModel):
    name: str
    price: float
    
@app.post("/items/")
def create_item(item: Item):
     return item


@app.get("/items/{item_id}")
def read_item(item_id: int):
    return {"item_id": item_id}


@app.get("/items/{item_id}/details")
def read_item_details(item_id: int):
    return {"item_id": item_id, "details": "This is a detailed view of the item."}


# Blog endpoint with a query parameter
# @app.get("/blog")
# def read_blog(limit)
















if __name__ == "__main__":

    uvicorn.run(app, host="127.0`0.1", port=8000, log_level="info")