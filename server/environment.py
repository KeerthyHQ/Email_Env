#logic for the server environment

from models import EmailAction,EmailObservation,EmailState 
from rewards import calculate_reward
from scenarios import EMAIL_SCENARIOS
import random

class EmailEnvironment:
    def __init__(self):
          #internal state initialization => Nothing in memory at start
        self._state = None 
        self.current_email = None

    def reset(self):
        #start a new email thread 

        #pick random scenario
        self.current_email = random.choice(EMAIL_SCENARIOS)

        if not self.current_email or "email" not in self.current_email:
            raise ValueError("Invalid scenario format")

        self._state = EmailState(
            email = self.current_email["email"],
            step_count=0,
            conversation_history=[]
        )

        return EmailObservation(
            email = self._state.email,
            reward=0.0,
            done=False,
            metadata={
                "step_count":self._state.step_count,
                "email_type":self.current_email.get("type","unknown")
                }
        )
    
    def step(self,action:EmailAction):
        #check self._state is not empty before incrementing
        if self._state is None:
            return EmailObservation(
                email = "Please call reset() function to proceed",
                reward=0.0,
                done=True,
                metadata={"error":"environment not initialised"}
            )
        #increment step count
        self._state.step_count+=1

        reply = action.reply

        #store reply in conversation history
        self._state.conversation_history.append(reply)

  
        #calculate reward for agent reply 
        reward,matches = calculate_reward(self.current_email,reply)
     
        #episode ends after max_step fixed
        MAX_STEPS = 3
        done=self._state.step_count >= MAX_STEPS

        #if done not true , then mail chain still continues
        if not done:
            followups=self.current_email.get("followups",[])

            if self._state.step_count - 1 < len(followups):
                next_email = followups[self._state.step_count -1 ]
            else:
                next_email = "Thank you for your response!"
            
            self._state.email= next_email
              
       print("STEP:", self._state.step_count)
       print("EMAIL:", self._state.email)

        return EmailObservation(
                email = self._state.email,
                reward=reward,
                done=done,
                metadata={
                    "step_count":self._state.step_count,
                    "email_type":self.current_email.get("type","unknown"),
                    "keyword_matches":matches,
                    "reply_length":len(reply.strip()),
                     "conversation_history": self._state.conversation_history
                    }
            )
    @property
    def state(self):
      return self._state
      