def calculate_reward(context, reply):
    reply = reply.lower()
    reward = 0.0
    matches = 0

    # keyword matching
    for word in context["expected_keywords"]:
        if word in reply:
            reward += 1.0
            matches += 1

    # politeness
    if any(w in reply for w in ["sorry", "thank you", "please"]):
        reward += 0.5

    # penalty for short reply
    if len(reply) < 10:
        reward -= 0.5

    # bonus for multiple keywords
    if matches >= 2:
        reward += 1.0

    # normalize 
    reward = min(reward / 3.0, 1.0)

    return reward, matches