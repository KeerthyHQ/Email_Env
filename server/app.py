from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware

from openenv.core.env_server import create_fastapi_app
from env.env import EmailEnvironment
from env.models import EmailAction, EmailObservation


#Create OpenEnv API
app = create_fastapi_app(
    EmailEnvironment,
    action_cls=EmailAction,
    observation_cls=EmailObservation
)


# Enable CORS for UI
app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"], 
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)


#home route
@app.get("/")
def home():
    return {
        "message": "Email Support RL Environment is running 🚀",
        "endpoints": {
            "reset": "/reset",
            "step": "/step"
        }
    }

 


