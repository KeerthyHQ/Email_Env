EMAIL_SCENARIOS = [

    {
        "id": 1,
        "type": "order_issue",
        "email": "Hi, I ordered a phone last week but it hasn't arrived yet. Can you check the status?",
        "expected_keywords": ["order", "status", "delivery", "check"],
        "difficulty_multiplier": 1.5,
        "followups": [
            "Can you give me an exact delivery date?",
            "This delay is frustrating. Please resolve quickly."
        ]
    },

    {
        "id": 2,
        "type": "refund_request",
        "email": "I received a damaged product. I want a refund immediately.",
        "expected_keywords": ["refund", "return", "sorry"],
        "difficulty_multiplier": 2,
        "followups": [
            "When will I get my refund?",
            "I haven't received any update yet. What's happening?"
        ]
    },

    {
        "id": 3,
        "type": "complaint",
        "email": "Your service is very slow. I'm not happy with the support.",
        "expected_keywords": ["apologize", "improve", "support"],
        "difficulty_multiplier": 2,
        "followups": [
            "This keeps happening. What are you doing about it?",
            "I need a proper resolution, not just apologies."
        ]
    },

    {
        "id": 4,
        "type": "general_query",
        "email": "Can you tell me your working hours?",
        "expected_keywords": ["hours", "time", "available"],
        "difficulty_multiplier": 1,
        "followups": [
            "Are you available on weekends?",
            "What about customer support timings?"
        ]
    },

    {
        "id": 5,
        "type": "late_delivery",
        "email": "My package was supposed to arrive yesterday but it's still not here.",
        "expected_keywords": ["delay", "delivery", "check", "sorry"],
        "difficulty_multiplier": 1.5,
        "followups": [
            "Why is it delayed?",
            "I need this urgently. Can you speed it up?"
        ]
    },

    {
        "id": 6,
        "type": "wrong_item",
        "email": "I received the wrong item in my order. This is not what I purchased.",
        "expected_keywords": ["wrong", "replace", "return", "sorry"],
        "difficulty_multiplier": 2,
        "followups": [
            "How do I return this item?",
            "When will I get the correct product?"
        ]
    },

    {
        "id": 7,
        "type": "account_issue",
        "email": "I'm unable to log into my account. It says invalid credentials.",
        "expected_keywords": ["reset", "password", "account", "help"],
        "difficulty_multiplier": 1.5,
        "followups": [
            "I tried resetting but it still doesn't work.",
            "This is blocking my access. Fix this urgently."
        ]
    },

    {
        "id": 8,
        "type": "payment_issue",
        "email": "My payment was deducted but the order was not confirmed.",
        "expected_keywords": ["payment", "refund", "check", "issue"],
        "difficulty_multiplier": 2,
        "followups": [
            "When will the amount be refunded?",
            "I need confirmation of my payment status."
        ]
    },

    {
        "id": 9,
        "type": "subscription_cancel",
        "email": "I want to cancel my subscription immediately.",
        "expected_keywords": ["cancel", "subscription", "confirm"],
        "difficulty_multiplier": 1,
        "followups": [
            "Has my subscription been cancelled?",
            "Will I be charged again?"
        ]
    },

    {
        "id": 10,
        "type": "feature_request",
        "email": "It would be great if you add dark mode to your app.",
        "expected_keywords": ["feature", "improve", "consider"],
        "difficulty_multiplier": 1,
        "followups": [
            "Are there any plans to implement this?",
            "This feature would really improve usability."
        ]
    }

]