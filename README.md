# CSC-128 Assignment 3 - Intent Classifier

## About

For this assignment, I created an intent classifier for a CPCC help bot. The classifier uses TF-IDF and cosine similarity to identify five different intents:

- Password reset
- Printing help
- Tuition payment
- Parking
- Registration

## Stop Words and Negation

My normalize function converts the text to lowercase, removes punctuation, and removes common stop words.

I kept "not" and "no" out of my stop words because they can completely change what someone means. For example, "there is paper" and "there is no paper" are saying opposite things, so removing "no" could make the bot understand the message incorrectly.

## Testing and Threshold

I tested the classifier with 12 messages that should match an intent and 5 unrelated messages that should be rejected.

After adjusting my stop words and running the tests again, all 12 match tests and all 5 reject tests passed.

My test results showed:

- Lowest should-match confidence: 0.508
- Highest should-reject confidence: 0.000
- Chosen threshold: 0.25

I chose 0.25 because it is between the highest reject score and the lowest match score. This gives the classifier a gap between messages that should match and messages that should be rejected.

## Running the Program

Install the requirements:

python -m pip install -r requirements.txt

Run the tests:

python test_classifier.py

Run the Streamlit app:

python -m streamlit run app.py