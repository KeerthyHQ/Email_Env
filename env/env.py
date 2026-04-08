from env.tasks import TASKS
from env.graders import grade_easy, grade_medium, grade_hard
from env.models import EmailAction, EmailObservation, EmailState
from env.rewards import calculate_reward
from env.scenarios import EMAIL_SCENARIOS
import random


class EmailEnvironment():
    def __init__(self, **kwargs):
        self._state = None

    def reset(self):
        current_email = random.choice(EMAIL_SCENARIOS)
        current_task = random.choice(TASKS)

        self._state = EmailState(
            email=current_email["email"],
            step_count=0,
            conversation_history=[],
            current_email=current_email,
            current_task=current_task
        )

        return EmailObservation(
            email=self._state.email,
            reward=0.0,
            done=False,
            metadata={"task": self._state.current_task["name"]}
        )

    def step(self, action: EmailAction):
        if self._state is None:
            self.reset()   
        state = self._state
        state.step_count += 1

        reply = (action.reply or "").lower()
        state.conversation_history.append(reply)

        context = {
            "email": state.email,
            "expected_keywords": state.current_email["expected_keywords"],
            "difficulty_multiplier": state.current_email["difficulty_multiplier"]
        }

        reward, matches = calculate_reward(context, reply)

        task_name = state.current_task["name"]

        if task_name == "easy_basic_response":
            task_score = grade_easy(context, reply)
        elif task_name == "medium_followup_handling":
            task_score = grade_medium(context, state.conversation_history)
        else:
            task_score = grade_hard(context, reply)

        done = state.step_count >= 3

        return EmailObservation(
            email=state.email,
            reward=reward,
            done=done,
            metadata={
                "task": task_name,
                "task_score": task_score,
                "keyword_matches": matches
            }
        )

    def state(self):
        return self._state.dict() if self._state else {}

    def load_state(self, state):
        if state:
            self._state = EmailState(**state)

    async def reset_async(self):
        return self.reset()

    async def step_async(self, action):
        return self.step(action)

    def close(self):
        return None