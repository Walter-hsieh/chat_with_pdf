# import Anthropic's LLM as the brain of our app
from langchain_anthropic import ChatAnthropic
from langchain_community.document_loaders import PyPDFLoader

chat_model_Anthropic = ChatAnthropic(
  model="claude-3-sonnet-20240229",
  temperature=0,
  api_key="place_your_anthropic_api_key_here"
)

# External data
# file = open('source.txt', 'r', encoding='utf-8')
# SOURCE = file.read()

pdf_path = 'C:\\Users\\walte\\Desktop\\LangChainApp\\pdf_file\\5.pdf'
loader = PyPDFLoader(file_path=pdf_path)
pages = loader.load_and_split()
documents = loader.load()



# Instruction for LLM to generate the response
from langchain_core.prompts import ChatPromptTemplate
rag_prompt = ChatPromptTemplate.from_messages([
    ("system", 'You are a helpful assistant. Use the following context when responding:\n\n{context}.'),
    ("human", "{question}")
])

# Organize LLM's response into structured output
from langchain_core.output_parsers import StrOutputParser
output_parser = StrOutputParser()

rag_chain = rag_prompt | chat_model_Anthropic | StrOutputParser()


user_input = str(input("enter question: "))

# Initiat the App
response = rag_chain.invoke({
    "question": user_input,
    "context": documents
})

print(response)