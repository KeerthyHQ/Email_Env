#calculate reward logic
def calculate_reward(scenario,reply):
    reply_lower=reply.lower()
    reward=0.0
    matches=0

     #match keywords expected with agent's reply
    expected_keywords=scenario.get("expected_keywords",[])
    for word in expected_keywords:
      if word in reply_lower:
        reward+=1.0
        matches+=1
    
    #check politeness for the reply 
    polite_words=["sorry","thank you","please"]
    for word in polite_words:
      if word in reply_lower:
        reward+=0.5
  
    #penalty for lazy reply 
    if len(reply.strip())<10 :
      reward-=1.0

    #penalty for rude tone
    rude_words = ["stupid","wait","can't help","not my problem"]
    for word in rude_words:
      if word in reply_lower:
        reward -=1.5

    #Bonus for strong responses
    if matches >=2:
      reward+=1.0

    #difficulty based scaling 
     reward += 0.1 * matches * scenario.get("difficulty_multiplier", 1)

    return reward,matches