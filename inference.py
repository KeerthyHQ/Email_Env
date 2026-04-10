import requests
import os

API_BASE_URL = os.getenv("API_BASE_URL", "http://127.0.0.1:8000")
MODEL_NAME = os.getenv("MODEL_NAME", "rule-based")


def log_start():
    print(f"[START] task=email_support env=email-support model={MODEL_NAME}",flush=True)


def log_step(step, action, reward, done):
    print(f"[STEP] step={step} action={action} reward={reward:.2f} done={str(done).lower()} error=null",flush=True)


def log_end(success, steps, score, rewards):
    rewards_str = ",".join([f"{r:.2f}" for r in rewards])
    print(f"[END] success={str(success).lower()} steps={steps} score={score:.2f} rewards={rewards_str}",flush=True)


def get_reply(email):
    email = email.lower()

    if "refund" in email:
        return "Sorry for the issue. We will process your refund and assist with return."

    if "order" in email or "delivery" in email:
        return "Sorry for the delay. We will check your order status and update delivery."

    if "account" in email:
        return "Please reset your password. We will help you access your account."

    return "Sorry for the inconvenience. We will resolve your issue."


def run():
    log_start()

    rewards = []
    steps = 0
    score=0.0
    success = False

    try:
        # RESET
        res = requests.post(f"{API_BASE_URL}/reset")
        res.raise_for_status()  #catch HTTP errors
        data = res.json()

        email = data["observation"]["email"]
        done = False

       
        while not done and steps < 3:
            steps += 1

            reply = get_reply(email)

            res = requests.post(
                f"{API_BASE_URL}/step",
                json={"action": {"reply": reply}}   
            )

            data = res.json()

            reward = float(data.get("reward", 0.0))
            done = data.get("done", False)
            email = data["observation"]["email"]

            rewards.append(reward)

            log_step(steps, reply, reward, done)

        if rewards:
            score = min(sum(rewards) / len(rewards), 1.0) 
            
        else :
            score=0.0

        success = score > 0.1

    except Exception as e:
        print(f"[ERROR] {e}")
        success = False

    log_end(success, steps, score, rewards)


if __name__ == "__main__":
    run()