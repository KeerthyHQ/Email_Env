#graders decide how good the agent actually did by evaluation scores

from typing import Dict,List

#Easy 

def grade_easy(context, reply):
    reply = reply.lower()

    score = 0.0

    if any(word in reply for word in context["expected_keywords"]):
        score += 0.5

    if any(w in reply for w in ["sorry", "thank you", "please"]):
        score += 0.5

    return min(score, 1.0)

#medium

def grade_medium(context, history):
    if not history:
        return 0.0

    score = 0.0

    if len(history) >= 2:
        score += 0.4

    keyword_hits = sum(
        any(word in r.lower() for word in context["expected_keywords"])
        for r in history
    )

    if keyword_hits >= 2:
        score += 0.4

    if any("sorry" in r.lower() for r in history):
        score += 0.2

    return min(score, 1.0)

# Hard

def grade_hard(context, reply):
    reply = reply.lower()
    score = 0.0

    matches = sum(
        word in reply for word in context["expected_keywords"]
    )

    if matches >= 2:
        score += 0.6
    elif matches == 1:
        score += 0.3

    if any(w in reply for w in ["resolve", "process", "check"]):
        score += 0.2

    if any(w in reply for w in ["sorry", "thank you", "please"]):
        score += 0.2

    return min(score, 1.0)






