import streamlit as st
from langchain_helper import get_QA_chain, set_model

st.title("Langhain Demo Chatbot ")
st.caption("Developed by [Muhammad Danish](https://linkedin.com/danisaysskol)")
st.caption("[GitHub Repo](https://github.com/danisaysskol/LANGCHAIN_DEMO)")

with st.sidebar:
    choice = st.radio(
        "Select a service to use:",
        ("OpenAI", "Google"),
        index=0,
        key="service_choice"
    )

# Update model based on selection
if choice == "Google":
    set_model('gemini')
else:
    set_model('chatgpt')

def get_response(question):
    chain = get_QA_chain()
    ans = chain.invoke({"input": question})
    print(ans)
    return ans

# Text input that triggers on enter or button press
question = st.text_input("Question: ", key="user_question", on_change=None)

# Respond when there's input (through Enter)
if question:
    response = get_response(question)
    st.header("Answer")
    st.write(response.content)
