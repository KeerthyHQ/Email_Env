import requests
import os


# CONFIG (MANDATORY VARIABLES)

API_BASE_URL = os.getenv("API_BASE_URL", "http://127.0.0.1:8000")
MODEL_NAME = os.getenv("MODEL_NAME", "rule-based")

#agent_reply

def generate_reply(email: str) -> str:
    email = email.lower()

    # Follow-up handling
    if "weekend" in email:
        return "Yes, our support team is also available on weekends during limited hours."

    if "return" in email:
        return "You can return the item by initiating a return request. We will assist you with the replacement."

    if "when will i get" in email or "when will" in email:
        return "Your request is being processed and will be completed within a few days."

    if "still doesn't work" in email:
        return "Sorry for the inconvenience. We will investigate this issue further and resolve it as soon as possible."

    if "what's happening" in email or "no update" in email:
        return "We understand your concern. We are checking the status and will provide an update shortly."

    if "charged again" in email:
        return "No, you will not be charged again after cancellation. Your subscription has been successfully cancelled."

    if "confirmation" in email:
        return "We are confirming your payment status and will provide an update shortly."

    if "what are you doing" in email or "keeps happening" in email:
        return "We understand your concern. Our team is actively working to improve the service and prevent this issue."

    # Refund / Payment 
    if "refund" in email or "payment" in email:
        return "Sorry for the issue. We will process your refund as soon as possible."

    # Order / Delivery
    if "order" in email or "delivery" in email or "arrive" in email:
        return "Sorry for the delay. We will check your order status and update the delivery details shortly."

    # Wrong item
    if "wrong item" in email or "not what i purchased" in email:
        return "Sorry for the inconvenience. We will arrange a return and replace the wrong item quickly."

    # Complaint
    if "slow" in email or "not happy" in email:
        return "We apologize for the inconvenience. We are working to improve our support and resolve your issue."

    # Account issue
    if "account" in email or "login" in email or "password" in email:
        return "Please reset your password using the link provided. We will help you regain access to your account."

    # General query
    if "hours" in email or "time" in email:
        return "Our support team is available during working hours. Please let us know if you need further assistance."

    # Subscription cancel
    if "cancel" in email or "subscription" in email:
        return "Your subscription will be cancelled as requested. Please confirm if you need any further assistance."

    # Feature request
    if "feature" in email or "dark mode" in email:
        return "Thank you for your suggestion. We will consider this feature to improve the user experience."

    # Escalation (unknown)
    if not any(word in email for word in [
        "refund", "order", "delivery", "account",
        "payment", "cancel", "subscription",
        "feature", "hours", "time", "weekend",
        "login", "password", "wrong", "return"
    ]):
        return "Sorry for the inconvenience. I am unable to resolve this issue. I will connect you to customer support."

    # Default
    return "Sorry for the inconvenience. We will look into your issue and assist you shortly."

import os


# RUN ONE TASK EPISODE

def run_episode(task_name="email_support"):
    
    print(f"[START] task={task_name} env=email-support model={MODEL_NAME}")

    try:
        #reset env
        res=requests.post(f"{API_BASE_URL}/reset")
        data = res.json()

        done=False
        step=0
        rewards=[]

        while not done:
            step+=1

            email = data.get("email","")

            #generate reply 
            reply=generate_reply(email)

            #send action to server
            res=requests.post( f"{API_BASE_URL}/step",json={"reply":reply} )

            data = res.json()

            #extract reward ,done from reply
            reward= float(data.get("reward",0.0))
            done=data.get("done",False)

            rewards.append(reward)

            #print step results
            print(
                f"[STEP] step={step} action={reply} reward={reward:.2f} "
                f"done={str(done).lower()} error=null"
            )
        
        # compute score
        score = sum(rewards) / len(rewards) if rewards else 0.0
        rewards_str = ",".join([f"{r:.2f}" for r in rewards])

        print(
            f"[END] success=true steps={step} score={score:.2f} rewards={rewards_str}"
        )
    
    #error handling block
    except Exception as e:
        #still print END even if error
        print(
            f"[END] success=false steps=0 score=0.00 rewards= error={str(e)}"
        )



# MAIN

if __name__ == "__main__":
    run_episode()