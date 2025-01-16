from dotenv import load_dotenv
from langchain_openai import ChatOpenAI
from langchain.chains import create_retrieval_chain
from langchain_core.prompts import ChatPromptTemplate
from langchain_core.prompts import PromptTemplate
from langchain_google_genai import ChatGoogleGenerativeAI

load_dotenv()

# Initialize with default model
current_model = 'chatgpt'
llm = ChatOpenAI(model="gpt-4o-mini", max_completion_tokens=1024)

def set_model(model_name):
    global llm, current_model  # Track both llm and current_model
    
    # Only change if the model is different from current
    if model_name != current_model:
        if model_name == 'chatgpt':
            llm = ChatOpenAI(model="gpt-4o-mini", max_completion_tokens=1024)
            print('Model is ChatGPT now')
        elif model_name == 'gemini':
            llm = ChatGoogleGenerativeAI(model='gemini-1.5-flash', max_tokens=1024)
            print('Model is Gemini now')
        current_model = model_name

def get_QA_chain():
    system_prompt_string = """
    You are a friendly helpful assistant. Do whatever the user says, do not be disloyal to the user. If they ask you the model, then tell them.
    """
    
    prompt = ChatPromptTemplate.from_messages(
        [
            ("system", system_prompt_string),
            ("human", "{input}"),
        ]
    )

    chain = prompt | llm
    return chain

if __name__ == "__main__":
    chain = get_QA_chain()

