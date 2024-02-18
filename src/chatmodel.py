import os,sys
from dotenv import load_dotenv
from src.logger import logging
from src.exception import CustException

import google.generativeai as genai
import langchain
from langchain.chains import LLMChain
from langchain.chains import ConversationChain
from langchain.prompts import PromptTemplate
from langchain_google_genai import ChatGoogleGenerativeAI
from langchain.agents import AgentType
from langchain.agents import load_tools
from langchain.agents import initialize_agent
from langchain.memory import ConversationBufferMemory

load_dotenv()

class Model:
    
    def get_the_agent(self):
        try:
            logging.info("Inside get_the_agent method it will return the agent")

            genai.configure(api_key=os.getenv("GOOGLE_API_KEY"))
            logging.info("gemini api key is configured")

            model = ChatGoogleGenerativeAI(model="gemini-pro",temperature=0.3)
            logging.info("gemini chat model loaded from langchain")

            tool = load_tools(['serpapi'],serpapi_api_key = os.getenv("serpapi_key"),llm=model)
            logging.info("tool created using serpapi and the gemini model")

            memory = ConversationBufferMemory(memory_key="chat_history")
            logging.info("conversation memory created")
            
            conversational_agent = initialize_agent(
                agent="conversational-react-description", 
                tools=tool, 
                llm=model,
                max_iterations=3,
                memory=memory)
            logging.info("agent is ready")
            return conversational_agent
        except Exception as e:
            raise CustException(e,sys)