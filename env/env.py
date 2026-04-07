#logic for the server environment
from openenv.core.env import Environment
from env.tasks import TASKS
from env.graders import grade_easy, grade_medium, grade_hard
from env.models import EmailAction,EmailObservation,EmailState 
from env.rewards import calculate_reward
from env.scenarios import EMAIL_SCENARIOS
import random

class EmailEnvironment(Environment):
    def __init__(self):
          #internal state initialization => Nothing in memory at start
        self._state = None 
        self.current_email = None
        self.current_task = None

    #start a new email thread 
    def reset(self):
       
        #pick random scenario
        self.current_email = random.choice(EMAIL_SCENARIOS)

        #pick task 
        self.current_task = random.choice(TASKS)

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
                "task":self.current_task["name"],
                "email_type":self.current_email.get("type","unknown")
                }
        )
    
    #step
    def step(self,action:EmailAction):

        #check self._state is not empty before incrementing
        if self._state is None:
            raise ValueError("Call reset() before step()")

        #increment step count
        self._state.step_count+=1

        reply = action.reply

        #store reply in conversation history
        self._state.conversation_history.append(reply)

  
        #calculate reward for agent reply 
        reward,matches = calculate_reward(self.current_email,reply)

        #task grading
        task_name=self.current_task["name"]

        if task_name=="easy_basic_response":
            task_score=grade_easy(self.current_email,reply)

        elif task_name == "medium_followup_handling":
            task_score=grade_medium(self.current_email,self._state.conversation_history)
        
        else:
            task_score=grade_hard(self.current_email,reply)
     
        #episode ends after max_step fixed
        MAX_STEPS = 3
        done=self._state.step_count >= MAX_STEPS

        #escalation to Human support 
        if "customer support" in reply.lower():
            done = True

        #followup email (not done)
        if not done:
            followups=self.current_email.get("followups",[])

            if self._state.step_count - 1 < len(followups):
                self._state.email = followups[self._state.step_count -1 ]
            else:
                self._state.email = "Thank you for your response!"
            
           
        
        return EmailObservation(
                email = self._state.email,
                reward=reward,
                done=done,
                metadata={
                    "step_count":self._state.step_count,
                    "task": task_name,             
                    "task_score": task_score, 
                    "email_type":self.current_email.get("type","unknown"),
                    "keyword_matches":matches,
                    "reply_length":len(reply.strip()),
                    "conversation_history": self._state.conversation_history
                    }
            )


    #state        
  
    def state(self):
      return self._state
      