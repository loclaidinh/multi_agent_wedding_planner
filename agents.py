from langchain.agents import create_agent
from langchain.tools import tool
from langchain.messages import HumanMessage
from models import deepseek_model
from tools import search_web
import logging

#configure logging
logging.basicConfig(
    level=logging.INFO,
    format="%(asctime)s | %(levelname)s | %(message)s"
)

#creating subagents
logging.info("Creating SubAgent1 ...")
subagent1 = create_agent(
    model=deepseek_model,
    tools=[search_web],
    name="SubAgent1"
)
logging.info("SubAgent1 created successfully.")

logging.info("Creating SubAgent2 ...")
subagent2 = create_agent(
    model=deepseek_model,
    tools=[search_web],
    name="SubAgent2"
)
logging.info("SubAgent2 created successfully.")

@tool
def delegate_to_subagent1(query: str) -> str:
    """
    Delegates the query to SubAgent1 and returns the response.
    """
    logging.info(f"Delegating query to SubAgent1: {query}")
    try:
        response = subagent1.invoke({"messages": [HumanMessage(content=query)]})
        return response["messages"][-1].content
    except Exception as e:
        logging.error(f"Error occurred while delegating to SubAgent1: {e}")
        return "An error occurred while processing your request. Please try again later."

@tool
def delegate_to_subagent2(query: str) -> str:
    """
    Delegates the query to SubAgent2 and returns the response.
    """
    logging.info(f"Delegating query to SubAgent2: {query}")
    try:
        response = subagent2.invoke({"messages": [HumanMessage(content=query)]})
        return response["messages"][-1].content
    except Exception as e:
        logging.error(f"Error occurred while delegating to SubAgent2: {e}")
        return "An error occurred while processing your request. Please try again later."
