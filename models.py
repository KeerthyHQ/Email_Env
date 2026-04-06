#In and Out of the System  


from typing import Dict,Any
from  pydantic import BaseModel


class EmailAction(BaseModel):  
    #agent's action is to reply to an email
     reply: str


class EmailObservation(BaseModel):
    #agent receives an email from environment response
    email:str
    reward :float
    done:bool
    metadata:Dict[str,Any] 


class EmailState(BaseModel):
    #internal state like current email thread
    email:str
    step_count:int 
    conversation_history: list[str]  
