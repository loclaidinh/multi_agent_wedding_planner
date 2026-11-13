from langchain.tools import tool
from tavily import TavilyClient
from dotenv import load_dotenv
import os
import logging

#configure logging
logging.basicConfig(
    level=logging.INFO,
    format="%(asctime)s | %(levelname)s | %(message)s"
)

load_dotenv()
tavily_client = TavilyClient(api_key=os.getenv("TAVILY_API_KEY"))

@tool
def search_web(query: str) -> str:
    """
    Searches the web for information based on the provided query and returns relevant results. This tool uses the Tavily API to perform the search.
    """
    logging.info(f"Searching the web for query: {query}")
    try:
        results = tavily_client.search(query)
        return results
    except Exception as e:
        logging.error(f"Error occurred while searching the web: {e}")
        return "An error occurred while searching the web. Please try again later."