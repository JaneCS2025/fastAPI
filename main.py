from fastapi import FastAPI, Depends
from pydantic import BaseModel
from sqlmodel import Field, Session, SQLModel, create_engine, select

app = FastAPI()

class Item(BaseModel):
  name: str
  price: float
  is_offer: bool | None = None

class Hero(SQLModel, table=True):
  id: int | None = Field(default=None, primary_key = True)
  name: str = Field(index=True)
  age: int | None = Field(default=None, index=True)
  secret_name: str

sqlite_file_name = 'database.db'
sqlite_url = f'sqlite:///{sqlite_file_name}'

connect_args = {"check_same_thread": False}
engine = create_engine(sqlite_url, connect_args=connect_args)

def create_db_and_tables():
  SQLModel.metadata.create_all(engine)


# Dependency to provide a SQLModel Session
def get_session():
  with Session(engine) as session:
    yield session

##Add event - create the database tables when the application starts 
@app.on_event('startup')
def on_startup():
  create_db_and_tables()


@app.get('/') 
def read_root():
  return {"Hello": "World"}


@app.get('/items/{item_id}')
def read_item(item_id: int, q: str | None = None):
  return {"item_id": item_id, "q": q}

@app.put('/items/{item_id}')
def update_item(item_id:int, item: Item):
  return {"item_name": item.name, "item_id": item_id, "item_price": item.price}


#Add data to Hero table
@app.post('/heros/')
def create_hero(hero: Hero, session: Session = Depends(get_session)) -> Hero:
  session.add(hero)
  session.commit()
  session.refresh(hero)
  return hero
