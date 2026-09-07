"""
CSC-128 Assignment 3 starter: Intent classifier
Michelle Salgado
"""
import re

from sklearn.feature_extraction.text import TfidfVectorizer
from sklearn.metrics.pairwise import cosine_similarity

# TODO 1: build a stop word list. Do not include "not" or "no".
STOP_WORDS = {
    "a", "an", "the", "is", "are",
    "i", "my", "me", "on", "how",
    "where", "can", "do", "does", "need", "to", "for"
}
# TODO 2: five intents, at least six example phrasings each
TRAINING = {
    "password_reset": [
        "reset my password",
        "forgot my login",
        "I cannot get into my account",
        "password help please",
        "I am locked out",
        "how do I change my password",
    ],
    "printing_help": [
        "printer stopped working",
        "printing issues",
        "I cannot print my document",
        "the printer is jammed",
        "how do I print on campus",
        "there is no paper",
    ],
    "tuition_payment": [
        "how to make payment",
        "payment help",
        "how do I pay my tuition",
        "where can I pay my school bill",
        "I need help paying for classes",
        "when is tuition due",
    ],
    "parking": [
        "how do I get a parking permit",
        "parking location",
        "where can I park",
        "is student parking available",
        "where is the parking deck",
        "do I need a parking pass",
    ],
    "registration": [
        "choosing classes",
        "searching for classes",
        "how do I register for classes",
        "I need to enroll in a course",
        "how can I add a class",
        "where do I register for next semester",
    ],
}

RESPONSES = {
    "password_reset": "Reset your password at password.cpcc.edu.",
    "printing_help": "Contact IT Help Desk at (123)456-7890",
    "tuition_payment": "Make payments at tuition.cpcc.edu",
    "parking": "For parking instructions and permits, contact Front Desk at (098)765-4321",
    "registration": "Search and register for classes at registration.cpcc.edu",
}

FALLBACK = "I'm not sure I understood your question. Please try rephrasing it."

# TODO 6: set this using the evidence your tests print out
DEFAULT_THRESHOLD = 0.25


def normalize(text):
    """TODO 3: lowercase, remove punctuation, drop stop words."""
    text = text.lower()
    text = re.sub(r"[^a-z0-9\s]", " ", text)
    words = text.split()
    words = [word for word in words if word not in STOP_WORDS]
    return " ".join(words)

class IntentClassifier:
    def __init__(self, training=None, threshold=DEFAULT_THRESHOLD):
        # TODO 4: flatten TRAINING into parallel phrases and labels lists,
        # then fit a TfidfVectorizer on the normalized phrases.
        self.training = training or TRAINING
        self.threshold = threshold
        self.phrases = []
        self.labels = []

        for intent, examples in self.training.items():
            for example in examples:
                self.phrases.append(normalize(example))
                self.labels.append(intent)

        self.vectorizer = TfidfVectorizer()
        self.training_vectors = self.vectorizer.fit_transform(self.phrases)

    def classify(self, text):
        """
        TODO 5: return (intent, confidence).

        Transform the text, take cosine similarity against every training
        phrase, find the best score, and return None for the intent when
        that score is below the threshold.
        """
        normalized = normalize(text)
        message_vector = self.vectorizer.transform([normalized])
        scores = cosine_similarity(message_vector, self.training_vectors)[0]

        best_index = scores.argmax()
        confidence = float(scores[best_index])
        intent = self.labels[best_index]

        if confidence < self.threshold:
            return None, confidence

        return intent, confidence


    def respond(self, text):
        """Return (reply, intent, confidence)."""
        intent, confidence = self.classify(text)

        if intent is None:
            return FALLBACK, None, confidence

        return RESPONSES[intent], intent, confidence
