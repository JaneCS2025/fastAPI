from fastapi import FastAPI
from pydantic import BaseModel

app = FastAPI()

@app.get('/')
async def read_results():
  results = await some_library()
  return results


#Coroutine is just the very fancy term for the thing returned by an async def function. Python knows that it is something like a function, that it can start and that it will end at some point, but that it might be paused ⏸ internally too, whenever there is an await inside of it.
#concurrent
#Parallel 

# Concurrent
# Definition: Multiple tasks are in progress at the same time, but not necessarily running simultaneously.
# The system switches between tasks (context switching).
# Can happen on a single CPU/core.
# Goal: manage multiple tasks efficiently.

#Parallel
# Definition: Multiple tasks are literally running at the exact same time.
# Requires multiple CPUs/cores.
# Goal: speed up execution by doing things simultaneously.