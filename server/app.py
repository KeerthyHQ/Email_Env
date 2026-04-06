#api endpoints for the server
#manual method 

from models import EmailAction,EmailObservation
from server.environment import EmailEnvironment
from fastapi import FastAPI

app = FastAPI()
env = EmailEnvironment()

@app.post("/reset",response_model=EmailObservation)
def reset():
    return env.reset()

@app.post("/step",response_model=EmailObservation)
def step(action:EmailAction):
    return env.step(action)



#automatic method
'''from server.environment import EmailEnvironment
from openenv.core.env_server import create_fastapi_app 
from models import EmailAction,EmailObservation



app=create_fastapi_app(
    EmailEnvironment,
    action_cls=EmailAction,
    observation_cls=EmailObservation
)'''
