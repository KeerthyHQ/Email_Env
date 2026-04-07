#graders decide how good the agent actually did by evaluation scores

from typing import Dict,List

#Easy Grader >
"""
    Evaluates a single reply for:
    - keyword presence
    - politeness
    - minimum length
    """

def grade_easy(scenario:Dict ,reply:str) -> float:

    if not reply:
        return 0.0
    
    reply = reply.lower().strip();
    score= 0.0

    #atleast 1 keyword match
    for word in scenario.get("expected_keywords",[]):
        if word in reply:
            score+=0.4
            break

    #politeness
    if any(word in reply for word in ["sorry", "thank you", "please"]):
        score+=0.4

    #min length check
    if len(reply) > 20:
        score+=0.2
    
    return min(score,1.0)

#medium grader >
"""
    Evaluates multi-step conversation for:
    - handling multiple steps
    - keyword consistency across replies
    - polite tone maintenance
    """

def grade_medium(scenario:Dict,history:List[str]) ->float:

    if not history:
        return 0.0

    score=0.0

    #multistep handling
    if len(history) >=2:
        score+=0.4
    
    #atleast 1 keyword in each step of conversation
    keyword_hits=0
    for reply in history:
        reply=reply.lower()
        for word in scenario.get("expected_keywords",[]):
            if word in reply:
                keyword_hits+=1
                break

    if keyword_hits >=2 :
        score+=0.4

    #politeness across conversation
    polite_count=0
    for reply in history:
        reply=reply.lower()
        if any(word in reply for word in ["sorry", "thank you", "please"]):
            polite_count+=1
    
    if polite_count>=1:
        score+=0.2

    return min(score,1.0)

#hard grader
 """
    Evaluates strong resolution capability:
    - multiple keyword matches
    - resolution intent
    - politeness
    - penalizes lazy replies
    """
def grade_hard(scenario:Dict,reply:str)->float:

    if not reply:
        return 0.0
    
    reply=reply.lower().strip()
    score=0.0

    #strong keyword match
    matches=0
    for word in scenario.get("expected_keywords",[]):
        if word in reply:
            matches+=1

    if matches>=2:
        score+=0.5
    elif matches ==1:
        score+=0.2

    #resolution phrases check 
    if any(word in reply for word in ["resolve", "process", "check", "assist", "arrange"]):
        score+=0.2

    #politeness   
    if any(word in reply for word in ["sorry", "thank you", "please"]):
        score += 0.2

    # 4. Penalize lazy responses
    if len(reply) < 15:
        score -= 0.2

    # Final score (0 to 1)
    return max(0.0, min(score, 1.0))

