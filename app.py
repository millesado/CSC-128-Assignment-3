import streamlit as st

from classifier import IntentClassifier


@st.cache_resource
def get_classifier():
    return IntentClassifier()


classifier = get_classifier()

st.title("CPCC Help Bot")
st.write("Ask me a question about password resets, printing, tuition payments, parking, or registration.")

user_message = st.chat_input("Type your question here")

if user_message:
    reply, intent, confidence = classifier.respond(user_message)

    with st.chat_message("user"):
        st.write(user_message)

    with st.chat_message("assistant"):
        st.write(reply)

        if intent is None:
            st.caption(f"Intent: None | Confidence: {confidence:.3f}")
        else:
            st.caption(f"Intent: {intent} | Confidence: {confidence:.3f}")