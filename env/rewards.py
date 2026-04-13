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
        reward += 1.5

    # repetition penalty
    history = context.get("conversation_history", []) 
    if history.count(reply) > 1: 
        reward -= 0.5

    # resolution bonus
    if any(word in reply for word in ["refund processed", "issue resolved", "we will resolve this"]):
        reward += 1.0
    elif any(word in reply for word in ["refund", "resolve", "assist"]):
        reward += 0.5

    # normalize 
    reward = max(0.01, min(reward / 3.0, 0.99))
        

    return reward, matches