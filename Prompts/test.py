from langchain_groq import ChatGroq
from dotenv import load_dotenv

load_dotenv()
# Initialize the LLaMA 3.1 model
model = ChatGroq(
    temperature=0,
    #groq_api_key='your_groq_api_key_here', 
    model_name="llama-3.3-70b-versatile"
)

result = model.invoke("Write a 5 line poem on cricket")

print(result.content)