# env/tasks.py
#agent should achieve these levels:easy,medium,hard

TASKS = [
    {
        "name": "easy_basic_response",
        "description": (
            "The agent must respond to a customer email politely and include "
            "at least one relevant keyword related to the issue."
        ),
        "difficulty": "easy",
        "success_criteria": [
            "Uses polite language (sorry, thank you, please)",
            "Includes at least one expected keyword",
            "Response is meaningful (not too short)"
        ]
    },

    {
        "name": "medium_followup_handling",
        "description": (
            "The agent must handle a multi-step email conversation, maintain context, "
            "and respond consistently across follow-ups."
        ),
        "difficulty": "medium",
        "success_criteria": [
            "Handles at least 2 steps",
            "Maintains conversation context",
            "Uses relevant keywords across steps",
            "Maintains polite tone"
        ]
    },

    {
        "name": "hard_complex_resolution",
        "description": (
            "The agent must resolve complex customer issues such as complaints, refunds, "
            "or wrong deliveries with a strong and complete response."
        ),
        "difficulty": "hard",
        "success_criteria": [
            "Includes multiple relevant keywords",
            "Provides clear resolution steps",
            "Maintains professional tone",
            "Avoids vague or lazy responses"
        ]
    }
]