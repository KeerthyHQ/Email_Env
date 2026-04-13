#graders decide how good the agent actually did by evaluation scores

from typing import Dict,List

def clamp(score):
    # ensure score is strictly between (0,1)
    return max(0.01, min(score, 0.99))

#Easy 

def grade_easy(context, reply):
    reply = reply.lower()
    score = 0.1

    if any(word in reply for word in context["expected_keywords"]):
        score += 0.5

    if any(w in reply for w in ["sorry", "please", "thank you"]):
        score += 0.2

    return clamp(score)


def grade_medium(context, history):
    score = 0.2

    # consistency across conversation
    unique_replies = len(set(history))
    if unique_replies > 1:
        score += 0.3

    # politeness across conversation
    polite_count = sum(
        any(p in r for p in ["sorry", "please", "thank you"])
        for r in history
    )
    score += min(polite_count * 0.1, 0.3)

    return clamp(score)


def grade_hard(context, reply):
    reply = reply.lower()
    score = 0.2

    if any(word in reply for word in context["expected_keywords"]):
        score += 0.4

    if "refund" in reply or "resolved" in reply:
        score += 0.3

    return clamp(score)