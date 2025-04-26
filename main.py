from fastapi import FastAPI,Depends, HTTPException
from typing import List
from .database import get_db
from .models import Item
from sqlmodel import Session,select


from pydantic import BaseModel

class Message(BaseModel):
    message: str

    
app =FastAPI()


@app.post("/items", response_model=Item)
def create_item(item:Item, db:Session = Depends(get_db)):
    db.add(item)
    db.commit()
    db.refresh(item)
    return item

@app.get("/items/{item_id}", response_model=Item)
def read_item(item_id:int, db:Session = Depends(get_db)):
    db_item = db.get(Item,item_id)
    if db_item is None:
        raise HTTPException(status_code=404, detail="Item not found")
    return db_item

@app.get("/items", response_model=List[Item])
def read_items(skip:int=0,limit:int=10,db:Session = Depends(get_db)):
    db_item = db.exec(select(Item).offset(skip).limit(limit)).all()
    return db_item

@app.put("/items/{item_id}", response_model=Item)
def update_item(item_id:int,item:Item,db:Session = Depends(get_db)):
    db_item = db.get(Item,item_id)
    if db_item is None:
        raise HTTPException(status_code=404, detail="Item not found")
    for key, value in item.dict(exclude_unset=True).items():
        setattr(db_item, key, value)
    db.commit()
    db.refresh(db_item)
    return db_item


@app.delete("/items/{item_id}")
def delete_item(item_id:int,db:Session = Depends(get_db)):
    db_item = db.get(Item,item_id)
    if db_item is None:
        raise HTTPException(status_code=404, detail="Item not found")
    db.delete(db_item)
    db.commit()
    return {"message":"Item deleted"}