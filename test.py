# from dotenv import load_dotenv

# load_dotenv() 

# import streamlit as st
# import os
# import google.generativeai as genai
# import langchain
# from langchain.chains import LLMChain
# from langchain.chains import ConversationChain
# from langchain.prompts import PromptTemplate
# from langchain_google_genai import ChatGoogleGenerativeAI
# from langchain.agents import AgentType
# from langchain.agents import load_tools
# from langchain.agents import initialize_agent
# from langchain.memory import ConversationBufferMemory

# #### Direct access of Gemini pro model 

# genai.configure(api_key=os.getenv("GOOGLE_API_KEY"))

# model = genai.GenerativeModel("gemini-pro")

# response = model.generate_content("who is the first prime minister of india")

# print(response.text)

# #### Gemini pro model accessing from langchain
 
# prompt_template = PromptTemplate.from_template("what is the capital of {country}?")
# model = ChatGoogleGenerativeAI(model="gemini-pro",temperature=0.3)

# chain = ConversationChain(llm=model)

# print(chain.invoke("who won the recent mens ODI cricket world cup "))

# #### Connecting with agents,zero_shot_description
# model = ChatGoogleGenerativeAI(model="gemini-pro",temperature=0.3)
# tool = load_tools(['serpapi'],serpapi_api_key = os.getenv("serpapi_key"),llm=model)
# agent = initialize_agent(tool,model,agent = AgentType.ZERO_SHOT_REACT_DESCRIPTION)

# print(agent.run("who won the recent mens ODI cricket world cup"))

# #### Connecting with agents, conversational-react-description with ConversationBufferMemory

# model = ChatGoogleGenerativeAI(model="gemini-pro",temperature=0.3)
# tool = load_tools(['serpapi'],serpapi_api_key = os.getenv("serpapi_key"),llm=model)
# memory = ConversationBufferMemory(memory_key="chat_history")

# conversational_agent = initialize_agent(
#     agent="conversational-react-description", 
#     tools=tool, 
#     llm=model,
#     max_iterations=3,
#     memory=memory,)

# output_1=conversational_agent.run("")

# print(output_1)


file_path = "prompt.txt"  # Replace "example.txt" with your file's path

try:
    with open(file_path, 'r') as file:
        content = file.read().replace('\n', ' ')
        print(content)
except FileNotFoundError:
    print(f"The file '{file_path}' does not exist.")
except Exception as e:
    print(f"An error occurred: {e}")
