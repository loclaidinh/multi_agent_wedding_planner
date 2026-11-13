from langchain.chat_models import init_chat_model
from dotenv import load_dotenv
import os

load_dotenv()

deepseek_model = init_chat_model(
    model="deepseek/deepseek-v4.1-flash-1017",
    model_provider="openai",
    api_key=os.getenv("OPENROUTER_API_KEY"),
    base_url="https://openrouter.ai/api/v1",
)

print(deepseek_model.invoke("what is the earth's diameter?").content)