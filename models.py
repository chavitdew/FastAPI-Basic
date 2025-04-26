from typing import Optional
from sqlmodel import SQLModel,Field,Relationship


#Step 2 Model Class

class Item(SQLModel,table=True):
    id: Optional[int] = Field(primary_key=True,index=True)
    name: str
    description: str
    price: Optional[int]= None
