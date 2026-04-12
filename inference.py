import os
import requests


def log_start():
    print(f"[START] task=email_support env=email-support model={os.getenv('MODEL_NAME','gpt-3.5-turbo')}", flush=True)


def log_step(step, action, reward, done):
    print(
        f"[STEP] step={step} action={action} reward={reward:.2f} done={str(done).lower()} error=null",
        flush=True,
    )


def log_end(success, steps, score, rewards):
    rewards_str = ",".join([f"{r:.2f}" for r in rewards])
    print(
        f"[END] success={str(success).lower()} steps={steps} score={score:.2f} rewards={rewards_str}",
        flush=True,
    )

def get_llm_reply(email):
    try:
        from openai import OpenAI

        client = OpenAI(
            base_url=os.environ["API_BASE_URL"],
            api_key=os.environ["API_KEY"],
        )

        response = client.chat.completions.create(
            model=os.environ.get("MODEL_NAME", "gpt-3.5-turbo"),
            messages=[
                {"role": "system", "content": "You are a helpful customer support agent."},
                {"role": "user", "content": f"Customer email: {email}\nWrite a helpful reply."},
            ],
            temperature=0.7,
            max_tokens=100,
        )

        return response.choices[0].message.content.strip()

    except Exception as e:
        print(f"[ERROR] LLM call failed: {e}", flush=True)
        return "Sorry for the inconvenience. We will resolve your issue."


def run():
    log_start()

    rewards = []
    steps = 0
    score = 0.0
    success = False

    try:
        # RESET
        res = requests.post("http://127.0.0.1:8000/reset")
        res.raise_for_status()
        data = res.json()

        email = data["observation"]["email"]
        done = False

        # STEP LOOP
        while not done and steps < 3:
            steps += 1

            #  CALL LLM PROXY
            reply = get_llm_reply(email)

            res = requests.post(
                "http://127.0.0.1:8000/step",
                json={"action": {"reply": reply}},
            )
            res.raise_for_status()

            data = res.json()

            reward = float(data.get("reward", 0.0))
            done = data.get("done", False)
            email = data["observation"]["email"]

            rewards.append(reward)

            log_step(steps, reply, reward, done)

        # SCORE
        if rewards:
            score = min(sum(rewards) / len(rewards), 1.0)

        success = score > 0.1

    except Exception as e:
        print(f"[ERROR] {e}", flush=True)
        success = False

    log_end(success, steps, score, rewards)


if __name__ == "__main__":
    run()