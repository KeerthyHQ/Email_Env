EMAIL_SCENARIOS = [
    {
        "email": "I received a damaged product. I want a refund.",
        "expected_keywords": ["refund", "return", "sorry"],
        "difficulty_multiplier": 2
    },
    {
        "email": "My order hasn’t arrived yet. What’s the status?",
        "expected_keywords": ["order", "status", "delivery", "check"],
        "difficulty_multiplier": 1.5
    },
    {
        "email": "I can’t log into my account.",
        "expected_keywords": ["account", "password", "reset"],
        "difficulty_multiplier": 1.5
    }
]