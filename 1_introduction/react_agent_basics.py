from langchain_google_genai import GoogleGenerativeAI
from langchain_openai import ChatOpenAI
from langchain.agents import initialize_agent
from langchain_community.tools import DuckDuckGoSearchResults
from dotenv import load_dotenv

load_dotenv()

# llm = GoogleGenerativeAI(model="gemini-1.5-flash")
llm = ChatOpenAI(model="gpt-4o-mini")

searchTool = DuckDuckGoSearchResults()
tools = [searchTool]

agent = initialize_agent(
    tools=tools,
    llm=llm,
    agent="zero-shot-react-description",
    verbose=True,
)

agent.invoke("when was the last time india won cricket world cup and how many days ago was it from this instant")


