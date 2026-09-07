from classifier import IntentClassifier

classifier = IntentClassifier()

MATCH_CASES = [
    ("I forgot my password again", "password_reset"),
    ("Can you help me change my login password", "password_reset"),
    ("I cannot print this assignment", "printing_help"),
    ("The campus printer will not work", "printing_help"),
    ("Where do I pay tuition", "tuition_payment"),
    ("I need to pay my school bill", "tuition_payment"),
    ("Where is student parking", "parking"),
    ("Do students need a parking permit", "parking"),
    ("I want to register for a course", "registration"),
    ("How can I enroll in classes", "registration"),
    ("I need help adding a class", "registration"),
    ("Where can I get a parking pass", "parking"),
]

REJECT_CASES = [
    "What is the weather today",
    "Where is the cafeteria",
    "What time does the library close",
    "Can I borrow a laptop",
    "Who is my instructor",
]

print("SHOULD MATCH")

for message, expected in MATCH_CASES:
    intent, confidence = classifier.classify(message)
    result = "PASS" if intent == expected else "FAIL"
    print(f"{result}: {message} -> {intent} ({confidence:.3f})")

print("\nSHOULD BE REJECTED")

for message in REJECT_CASES:
    intent, confidence = classifier.classify(message)
    result = "PASS" if intent is None else "FAIL"
    print(f"{result}: {message} -> {intent} ({confidence:.3f})")