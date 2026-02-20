from langchain_google_genai import ChatGoogleGenerativeAI
from langchain_huggingface import ChatHuggingFace,HuggingFaceEndpoint
from dotenv import load_dotenv
load_dotenv()


# from langchain.schema import HumanMessage, SystemMessage

# chatmodel=ChatGoogleGenerativeAI(model="gemini-2.5-flash",temperature=0.9)

# messages = [
#     SystemMessage(content="You are a helpful assistant."),
#     HumanMessage(content="Explain Docker simply")
# ]

# response = chatmodel.generate(messages)
# print(response.generations[0][0].text)

llm=HuggingFaceEndpoint(repo_id="deepseek-ai/DeepSeek-V3.2",task="text-generation")

chat=ChatHuggingFace(llm=llm,)
print(chat.invoke("What is the capital of France?"))