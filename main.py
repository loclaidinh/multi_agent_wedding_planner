from prompts import WEDDING_PLANNER_AGENT_PROMPT, USER_PROMPT_FOR_MAIN_AGENT
from langchain.agents import create_agent
from models import deepseek_model
from agents import delegate_to_subagent1, delegate_to_subagent2
import logging
from langchain.messages import HumanMessage

#configure logging
logging.basicConfig(
    level=logging.INFO,
    format="%(asctime)s | %(levelname)s | %(message)s"
)

# asking user for their wedding requirements
logging.info("Asking user for their wedding requirements and preferences...")
requirements = input("Please enter your wedding requirements and preferences: \n")

# updating the prompt with user requirements
updated_prompt = WEDDING_PLANNER_AGENT_PROMPT.format(requirements=requirements)

# creating the main agent
logging.info("Creating the main agent...")
main_agent = create_agent(
    model=deepseek_model,
    tools=[delegate_to_subagent1, delegate_to_subagent2],
    name="WeddingPlannerAgent",
    system_prompt=updated_prompt
)
logging.info("Main agent created successfully.")

# invoking the main agent with user prompt
logging.info("Invoking the main agent with user prompt...")
try:
    response = main_agent.invoke({"messages": [HumanMessage(content=USER_PROMPT_FOR_MAIN_AGENT)]})
    print("\nWedding Planning Suggestions:\n")
    print(response["messages"][-1].content)
except Exception as e:
    logging.error(f"Error occurred while invoking the main agent: {e}")
    print("An error occurred while processing your request. Please try again later.")     

