import streamlit as st
import requests

API_URL = "https://personalized-networking-assistant-j93r.onrender.com"

st.title("🤝 Personalized Networking Assistant")

event = st.text_input("Event Description")

interests = st.text_input("Your Interests")

if st.button("Generate Conversation Starters"):

    response = requests.post(
        f"{API_URL}/generate",
        json={
            "event": event,
            "interests": interests
        }
    )

    if response.status_code == 200:
        data = response.json()

        st.subheader("Conversation Starters")

        for starter in data["conversation_starters"]:
            st.write("•", starter)

st.divider()

topic = st.text_input("Topic for Wikipedia Fact Check")

if st.button("Get Fact"):

    response = requests.get(
        f"{API_URL}/fact/{topic}"
    )

    if response.status_code == 200:
        st.success(response.json()["fact"])

st.divider()

if st.button("View History"):

    response = requests.get(
        f"{API_URL}/history"
    )

    if response.status_code == 200:
        st.json(response.json())