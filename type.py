from datetime import date
from datetime import datetime
from pydantic import BaseModel
from typing import Annotated

# JSON objects (dict).
# JSON array (list) defining item types, list[str]
# String (str) fields, defining min and max lengths.
# Numbers (int, float) with min and max values, etc.


def main(user_id: str):
  return user_id

# class User(BaseModel):
#   id: int
#   name: str
#   joined: date

# my_user = User(id=3, name="John", joined="2018-02-03")

# second_user_data = {
#   "id": 4,
#   "name": "Mary",
#   "joined": "2018-03-09"
# }

# my_second_user:User = User(**second_user_data)

def get_full_name(first_name: str, last_name: str):
  full_name = first_name.title() + " " + last_name.title()
  return full_name

# print(get_full_name('David', 'Liu'))

# list
def process_item(items: list[str]):
  for item in items:
    print(item)

# process_item(['A', 'B', 'C'])

#tuple/set
def process_tuple(items: tuple[int, int, str], names: set[bytes]):
  return items, names

# print('items', process_tuple(('Mike', 'Jimmy', 'Kelen'), {'A', 'B'}))

#dict
def process_items(prices: dict[str, float]):
    for item_name, item_price in prices.items():
        print(item_name)
        print(item_price)

# process_items({'cake': 65.0, 'banana': 32.0})

#union
def process_item(item: int | str):
    print(item)
  
# process_item('cake')

def say_hi(name: str | None = None):
    if name is not None:
        print(f"Hey {name}!")
    else:
        print("Hello World")


class Person:
    def __init__(self, name: str):
        self.name = name

#You can also declare a class as the type of a variable.
def get_person_name(one_person: Person):
    return one_person.name
  

class User(BaseModel):
    id: int
    name: str = "John Doe"
    signup_ts: datetime | None = None
    friends: list[int] = []


external_data = {
    "id": "123",
    "signup_ts": "2017-06-01 12:22",
    "friends": [1, "2", b"3"],
}
user = User(**external_data)
print(user)
print(user.id)

def say_hello(name: Annotated[str, "this is meta"]) -> str:
  print(f"Hello, I am {name}")
  
say_hello('Tina')