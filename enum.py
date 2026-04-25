from enum import Enum

from fastapi import FastAPI

# define enum
# then create class attributes with fixed values, which will be the available valid values:
class ModelName(str, Enum):
  alexnet = 'alexnet'
  resnet = 'resnet'
  lenet = 'lenet'

app = FastAPI()

@app.get('/models/{model_name}')
async def get_model(model_name: ModelName):

  #Compare it with the enumeration member in your created enum ModelName:
  if model_name is ModelName.alexnet:
    return {"model_name": model_name, "message": "Deep Learning FTM"}
  
  #Get the actual value (a str in this case) using model_name.value, or in general, your_enum_member.value
  if model_name.value == 'lenet':
    return {"model_name": model_name, "message": "LeCNN all the images"}
  
  return {"model_name": model_name, "message": "Have some residuals"}


