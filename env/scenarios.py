EMAIL_SCENARIOS = [
    {
        "email": "I want a refund",
        "expected_keywords": ["refund"],
        "difficulty_multiplier": 1.0
    },
    {
        "email": "My order is delayed",
        "expected_keywords": ["order", "delay"],
        "difficulty_multiplier": 1.0
    },
    {
        "email": "I received damaged product",
        "expected_keywords": ["refund", "replace"],
        "difficulty_multiplier": 1.2
    },
    {
        "email": "I can't login",
        "expected_keywords": ["reset", "password"], 
        "difficulty_multiplier": 1.0
    },
    {
        "email": "Payment failed", 
        "expected_keywords": ["payment", "retry"], 
        "difficulty_multiplier": 1.1
    },
]