from pydantic import BaseModel
from typing import Dict, Any, List


class EmailAction(BaseModel):
    reply: str


class EmailObservation(BaseModel):
    email: str
    reward: float
    done: bool
    metadata: Dict[str, Any]


class EmailState(BaseModel):
    email: str
    step_count: int
    conversation_history: List[str]
    current_email: Dict
    current_task: Dict